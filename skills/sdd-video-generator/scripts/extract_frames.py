#!/usr/bin/env python3
"""
SDD Video Generator — Frame Extractor

Extracts a video into a numbered WebP frame sequence, for the canvas-based
approach in the companion module `_shared/viewers/scroll-scrubbing-video.md`.
Requires ffmpeg installed and available on PATH.

Usage:
    python extract_frames.py --input hero.mp4 --output ./public/assets/video/hero-frames/ --fps 12
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def check_ffmpeg() -> bool:
    if shutil.which("ffmpeg") is None:
        print("[ERROR] ffmpeg not found on PATH.")
        print("Install: https://ffmpeg.org/download.html (or `brew install ffmpeg` / `apt install ffmpeg`)")
        return False
    return True


def extract_frames(input_path: Path, output_dir: Path, fps: int, quality: int = 82) -> int:
    """Extract frames as WebP. Returns the frame count, or -1 on failure."""
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_path),
        "-vf", f"fps={fps}",
        "-c:v", "libwebp",
        "-quality", str(quality),
        str(output_dir / "frame-%04d.webp"),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("[FAIL] ffmpeg failed:")
        print(result.stderr[-2000:])
        return -1

    frame_count = len(sorted(output_dir.glob("frame-*.webp")))
    return frame_count


def main():
    parser = argparse.ArgumentParser(description="Extract a video into a WebP frame sequence.")
    parser.add_argument("--input", "-i", type=Path, required=True)
    parser.add_argument("--output", "-o", type=Path, required=True)
    parser.add_argument(
        "--fps", type=int, default=12,
        help="Frames per second to extract (default: 12 — smooth enough for scroll-scrub "
             "without an excessive frame count; an 8s clip at fps=12 yields ~96 frames).",
    )
    parser.add_argument("--quality", type=int, default=82, help="WebP quality (0-100, default 82).")

    args = parser.parse_args()

    if not args.input.exists():
        print(f"[ERROR] Input file not found: {args.input}")
        sys.exit(1)

    if not check_ffmpeg():
        sys.exit(1)

    frame_count = extract_frames(args.input, args.output, args.fps, args.quality)
    if frame_count <= 0:
        sys.exit(1)

    print(f"[OK] Extracted {frame_count} frames to {args.output}")
    print(f"     Pass frameCount={frame_count} to the scroll-scrubbing-video component.")


if __name__ == "__main__":
    main()
