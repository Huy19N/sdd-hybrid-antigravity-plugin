#!/usr/bin/env python3
"""
Multi-Tier Image Generation Fallback Script (SDD-Asset-Generator)
-----------------------------------------------------------------
Provides a bulletproof, zero-crash image generation pipeline:
  Tier 1: Google GenAI Imagen 3 API (if GEMINI_API_KEY is available)
  Tier 2: Pollinations.ai FLUX/SDXL (Free, zero-setup, unlimited quota, no API key needed)
  Tier 3: OpenAI DALL-E 3 (if OPENAI_API_KEY is available)

Usage:
  python generate_image_fallback.py --prompt "Artisanal matcha tea..." --output public/assets/generated/matcha.webp --aspect-ratio 16:9
  python generate_image_fallback.py --manifest public/assets/generated/manifest.json
"""

import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ASPECT_RATIO_DIMS = {
    "1:1": (1024, 1024),
    "16:9": (1280, 720),
    "9:16": (720, 1280),
    "4:3": (1024, 768),
    "3:4": (768, 1024),
    "4:5": (800, 1000),
    "3:2": (1200, 800),
    "2:3": (800, 1200),
}


def generate_with_gemini(prompt: str, output_path: Path, aspect_ratio: str = "1:1") -> bool:
    """Tier 1: Generate image using Google GenAI API (Imagen 3)."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[Gemini Imagen 3] Skipped: GEMINI_API_KEY environment variable not found.")
        return False

    try:
        from google import genai
        from google.genai import types

        print("[Gemini Imagen 3] Attempting generation with Imagen 3...")
        client = genai.Client(api_key=api_key)

        # Normalize aspect ratio for Imagen 3
        ar_mapping = {
            "1:1": "1:1",
            "16:9": "16:9",
            "9:16": "9:16",
            "4:3": "4:3",
            "3:4": "3:4",
        }
        target_ar = ar_mapping.get(aspect_ratio, "1:1")

        result = client.models.generate_images(
            model="imagen-3.0-generate-002",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                output_mime_type="image/jpeg",
                aspect_ratio=target_ar,
                person_generation="ALLOW_ADULT",
            ),
        )

        for generated_image in result.generated_images:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(generated_image.image.image_bytes)
            print(f"[Gemini Imagen 3] [OK] Success: Saved to {output_path}")
            return True

    except Exception as e:
        print(f"[Gemini Imagen 3] [WARN] Failed/Quota Exhausted: {e}")
        return False

    return False


def generate_with_pollinations(prompt: str, output_path: Path, aspect_ratio: str = "1:1") -> bool:
    """Tier 2: Generate image using Pollinations.ai FLUX.1 (Free, no API key, unlimited)."""
    width, height = ASPECT_RATIO_DIMS.get(aspect_ratio, (1024, 1024))
    encoded_prompt = urllib.parse.quote(prompt)
    seed = int(time.time() * 1000) % 1000000

    url = (
        f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        f"?width={width}&height={height}&seed={seed}&nologo=true&model=flux"
    )

    print(f"[Pollinations FLUX] Attempting zero-quota generation ({width}x{height})...")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) SDD-Hybrid-Asset-Generator/1.0"
    }

    req = urllib.request.Request(url, headers=headers)
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                if response.status == 200:
                    image_data = response.read()
                    if len(image_data) > 1000:  # Valid image byte threshold
                        with open(output_path, "wb") as f:
                            f.write(image_data)
                        print(f"[Pollinations FLUX] [OK] Success: Saved to {output_path} ({len(image_data)//1024} KB)")
                        return True
        except Exception as e:
            print(f"[Pollinations FLUX] Attempt {attempt} failed: {e}. Retrying...")
            time.sleep(2)

    print("[Pollinations FLUX] [FAIL] Failed after 3 attempts.")
    return False


def generate_with_openai(prompt: str, output_path: Path, aspect_ratio: str = "1:1") -> bool:
    """Tier 3: Generate image using OpenAI DALL-E 3 (if OPENAI_API_KEY exists)."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return False

    try:
        import urllib.request
        print("[OpenAI DALL-E 3] Attempting generation...")

        size = "1024x1024"
        if aspect_ratio == "16:9" or aspect_ratio == "3:2":
            size = "1792x1024"
        elif aspect_ratio == "9:16" or aspect_ratio == "2:3":
            size = "1024x1792"

        data = json.dumps({
            "model": "dall-e-3",
            "prompt": prompt,
            "n": 1,
            "size": size,
            "response_format": "url"
        }).encode("utf-8")

        req = urllib.request.Request(
            "https://api.openai.com/v1/images/generations",
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
                "User-Agent": "SDD-Hybrid/1.0"
            }
        )

        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))
            img_url = result["data"][0]["url"]

            with urllib.request.urlopen(img_url, timeout=30) as img_resp:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, "wb") as f:
                    f.write(img_resp.read())
            print(f"[OpenAI DALL-E 3] ✅ Success: Saved to {output_path}")
            return True
    except Exception as e:
        print(f"[OpenAI DALL-E 3] Failed: {e}")
        return False


def generate_image_cascade(prompt: str, output_path: str, aspect_ratio: str = "1:1", provider: str = "auto") -> bool:
    """
    Executes multi-tier cascade fallback:
      1. Gemini Imagen 3 (if provider is auto or gemini)
      2. Pollinations FLUX.1 (Free, zero-quota fallback)
      3. OpenAI DALL-E 3 (if key available)
    """
    path = Path(output_path)

    if provider == "gemini":
        return generate_with_gemini(prompt, path, aspect_ratio)
    elif provider == "pollinations":
        return generate_with_pollinations(prompt, path, aspect_ratio)
    elif provider == "openai":
        return generate_with_openai(prompt, path, aspect_ratio)

    # Cascade auto mode:
    # 1. Try Gemini Imagen 3 if key exists
    if os.environ.get("GEMINI_API_KEY"):
        if generate_with_gemini(prompt, path, aspect_ratio):
            return True

    # 2. Try Pollinations FLUX (bulletproof zero-quota fallback)
    if generate_with_pollinations(prompt, path, aspect_ratio):
        return True

    # 3. Try OpenAI DALL-E 3
    if os.environ.get("OPENAI_API_KEY"):
        if generate_with_openai(prompt, path, aspect_ratio):
            return True

    return False


def main():
    parser = argparse.ArgumentParser(description="Multi-Tier Image Generation Fallback Script")
    parser.add_argument("--prompt", type=str, help="Text prompt for image generation")
    parser.add_argument("--output", type=str, help="Output image file path (e.g. public/assets/generated/hero.webp)")
    parser.add_argument("--aspect-ratio", type=str, default="1:1", choices=list(ASPECT_RATIO_DIMS.keys()), help="Aspect ratio")
    parser.add_argument("--provider", type=str, default="auto", choices=["auto", "gemini", "pollinations", "openai"], help="Generation provider")
    parser.add_argument("--manifest", type=str, help="JSON manifest file with list of image jobs")

    args = parser.parse_args()

    if args.manifest:
        manifest_path = Path(args.manifest)
        if not manifest_path.exists():
            print(f"Error: Manifest file '{args.manifest}' not found.", file=sys.stderr)
            sys.exit(1)

        with open(manifest_path, "r", encoding="utf-8") as f:
            jobs = json.load(f)

        success_count = 0
        for job in jobs:
            prompt = job.get("prompt")
            output = job.get("output")
            ar = job.get("aspect_ratio", "1:1")
            prov = job.get("provider", args.provider)

            if not prompt or not output:
                continue

            print(f"\n--- Processing: {output} ---")
            if generate_image_cascade(prompt, output, ar, prov):
                success_count += 1

        print(f"\nCompleted: {success_count}/{len(jobs)} assets generated.")
        sys.exit(0 if success_count == len(jobs) else 1)

    if not args.prompt or not args.output:
        parser.print_help()
        sys.exit(1)

    success = generate_image_cascade(args.prompt, args.output, args.aspect_ratio, args.provider)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
