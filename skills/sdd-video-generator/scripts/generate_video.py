#!/usr/bin/env python3
"""
SDD Video Generator — Generate video using Google's Veo 3.1 model via the
Gemini API (NOT via the Google Flow web app, which has no public API —
see SKILL.md "Flow vs. API").

Usage:
    python generate_video.py --prompt "..." --output ./assets/video/hero.mp4 \
        --tier fast --aspect-ratio 16:9 --resolution 720p --duration 8

Requirements:
    pip install google-genai
    export GEMINI_API_KEY=your_key_here   # https://aistudio.google.com/apikey

Note: Veo 3.1 models are in Preview status as of this writing — model IDs and
config field names may change. If this script errors on a config parameter,
check https://ai.google.dev/gemini-api/docs/veo for the current API shape
before assuming the script logic itself is wrong.
"""

import argparse
import os
import sys
import time
from pathlib import Path

MODEL_TIERS = {
    "lite": "veo-3.1-lite-generate-preview",
    "fast": "veo-3.1-fast-generate-preview",
    "standard": "veo-3.1-generate-preview",
}

# Tiers that support video extension / reference images (lite does not)
ADVANCED_FEATURE_TIERS = {"fast", "standard"}


def check_dependencies() -> bool:
    try:
        from google import genai  # noqa: F401
        return True
    except ImportError:
        print("[ERROR] Missing dependency: google-genai")
        print("Install with: pip install google-genai")
        return False


def check_api_key() -> bool:
    if not os.environ.get("GEMINI_API_KEY"):
        print("[ERROR] GEMINI_API_KEY environment variable not set.")
        print("Get a key at: https://aistudio.google.com/apikey")
        return False
    return True


def validate_params(tier: str, resolution: str, duration: str) -> list[str]:
    """Return a list of validation error messages (empty list = valid)."""
    errors = []
    if resolution == "4k" and tier == "lite":
        errors.append("4k resolution is not supported on the 'lite' tier. Use --tier fast or standard.")
    if resolution in ("1080p", "4k") and duration != "8":
        errors.append(f"Resolution '{resolution}' requires --duration 8.")
    return errors


def generate_video(
    prompt: str,
    output_path: Path,
    tier: str = "fast",
    aspect_ratio: str = "16:9",
    resolution: str = "720p",
    duration_seconds: str = "8",
    poll_interval: int = 10,
    max_wait: int = 360,
) -> bool:
    from google import genai
    from google.genai import types

    client = genai.Client()
    model_name = MODEL_TIERS[tier]

    print(f"[INFO] Requesting video generation (model={model_name})...")
    print(f"[INFO] Prompt: {prompt[:120]}{'...' if len(prompt) > 120 else ''}")

    operation = client.models.generate_videos(
        model=model_name,
        prompt=prompt,
        config=types.GenerateVideosConfig(
            aspect_ratio=aspect_ratio,
            resolution=resolution,
            duration_seconds=duration_seconds,
        ),
    )

    elapsed = 0
    while not operation.done:
        if elapsed >= max_wait:
            print(f"[ERROR] Timed out after {max_wait}s waiting for video generation.")
            print("        (Documented latency range: 11s min, up to 6 min at peak hours.)")
            return False
        print(f"[INFO] Waiting for video generation... ({elapsed}s elapsed)")
        time.sleep(poll_interval)
        elapsed += poll_interval
        operation = client.operations.get(operation)

    try:
        generated_video = operation.response.generated_videos[0]
    except (AttributeError, IndexError, TypeError):
        print("[FAIL] No video was generated.")
        print("       Most likely cause: blocked by safety filters (not charged in this case),")
        print("       or an audio-related processing error. Review the prompt and retry.")
        return False

    output_path.parent.mkdir(parents=True, exist_ok=True)
    client.files.download(file=generated_video.video)
    generated_video.video.save(str(output_path))

    print(f"[OK] Video saved to {output_path}")
    print("[WARN] Google stores generated videos server-side for only 2 days —")
    print("       the local file just saved is now your only persistent copy.")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Generate video via Veo 3.1 through the Gemini API."
    )
    parser.add_argument("--prompt", "-p", required=True, help="Video generation prompt.")
    parser.add_argument("--output", "-o", type=Path, required=True, help="Output .mp4 path.")
    parser.add_argument("--tier", choices=list(MODEL_TIERS.keys()), default="fast")
    parser.add_argument("--aspect-ratio", choices=["16:9", "9:16"], default="16:9")
    parser.add_argument("--resolution", choices=["720p", "1080p", "4k"], default="720p")
    parser.add_argument("--duration", choices=["4", "6", "8"], default="8")

    args = parser.parse_args()

    errors = validate_params(args.tier, args.resolution, args.duration)
    if errors:
        for e in errors:
            print(f"[ERROR] {e}")
        sys.exit(1)

    if not check_dependencies() or not check_api_key():
        sys.exit(1)

    success = generate_video(
        prompt=args.prompt,
        output_path=args.output,
        tier=args.tier,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution,
        duration_seconds=args.duration,
    )
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
