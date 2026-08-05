#!/usr/bin/env python3
"""
SDD Background Remover — Batch background removal for product images.

Uses the `rembg` library to remove backgrounds from images, producing
transparent PNGs suitable for overlay-style web layouts.

Usage:
    # Process specific files:
    python remove_bg.py --input ./assets/generated/ --output ./assets/no-bg/ \
        --files product-01.webp product-02.webp

    # Process all images in input directory:
    python remove_bg.py --input ./assets/generated/ --output ./assets/no-bg/ --all

Requirements:
    pip install rembg Pillow
"""

import argparse
import sys
from pathlib import Path

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff", ".tif"}


def check_dependencies():
    """Verify rembg and Pillow are installed."""
    try:
        import rembg  # noqa: F401
        from PIL import Image  # noqa: F401
        return True
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e}")
        print("Install with: pip install rembg Pillow")
        print("For GPU support: pip install rembg[gpu] Pillow")
        return False


def remove_background(input_path: Path, output_path: Path) -> bool:
    """Remove background from a single image file.

    Args:
        input_path: Path to the source image.
        output_path: Path where the transparent PNG will be saved.

    Returns:
        True if successful, False otherwise.
    """
    from rembg import remove
    from PIL import Image

    try:
        with Image.open(input_path) as img:
            # Convert to RGBA if needed
            if img.mode != "RGBA":
                img = img.convert("RGBA")

            # Remove background
            result = remove(img)

            # Ensure output directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Save as PNG to preserve transparency
            output_file = output_path.with_suffix(".png")
            result.save(output_file, "PNG")

            # Verify output
            if output_file.stat().st_size == 0:
                print(f"  [WARN] Output file is empty: {output_file}")
                return False

            print(f"  [OK] {input_path.name} → {output_file.name}")
            return True

    except Exception as e:
        print(f"  [FAIL] {input_path.name}: {e}")
        return False


def get_image_files(input_dir: Path, file_names: list[str] | None = None) -> list[Path]:
    """Get list of image files to process.

    Args:
        input_dir: Directory containing source images.
        file_names: Specific file names to process, or None for all images.

    Returns:
        List of Path objects for files to process.
    """
    if file_names:
        files = []
        for name in file_names:
            path = input_dir / name
            if path.exists() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
                files.append(path)
            else:
                print(f"  [SKIP] {name}: not found or unsupported format")
        return files
    else:
        return sorted(
            p for p in input_dir.iterdir()
            if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
        )


def main():
    parser = argparse.ArgumentParser(
        description="Remove backgrounds from product images using rembg."
    )
    parser.add_argument(
        "--input", "-i",
        type=Path,
        required=True,
        help="Input directory containing source images.",
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        required=True,
        help="Output directory for transparent PNGs.",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--files", "-f",
        nargs="+",
        help="Specific file names to process (relative to input dir).",
    )
    group.add_argument(
        "--all", "-a",
        action="store_true",
        help="Process all supported image files in input directory.",
    )

    args = parser.parse_args()

    # Validate input directory
    if not args.input.is_dir():
        print(f"[ERROR] Input directory does not exist: {args.input}")
        sys.exit(1)

    # Check dependencies
    if not check_dependencies():
        sys.exit(1)

    # Get files to process
    files = get_image_files(args.input, args.files if not args.all else None)

    if not files:
        print("[WARN] No image files found to process.")
        sys.exit(0)

    print(f"\n{'='*50}")
    print(f"SDD Background Remover")
    print(f"Input:  {args.input.resolve()}")
    print(f"Output: {args.output.resolve()}")
    print(f"Files:  {len(files)}")
    print(f"{'='*50}\n")

    # Process each file
    success = 0
    failed = 0

    for file_path in files:
        output_path = args.output / file_path.name
        if remove_background(file_path, output_path):
            success += 1
        else:
            failed += 1

    # Summary
    print(f"\n{'='*50}")
    print(f"Done: {success} succeeded, {failed} failed out of {len(files)} total")
    print(f"{'='*50}")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
