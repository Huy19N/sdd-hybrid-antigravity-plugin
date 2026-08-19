#!/usr/bin/env python3
"""
SDD Asset Generator — Tileable Texture Post-Processor

Image-gen models rarely produce perfectly seamless tileable textures on the
first try. This applies the standard "offset + heal seam" technique used in
image editors (Photoshop's Offset filter + retouch, GIMP's Make Seamless):

  1. Roll the image by half its width/height — this moves the original outer
     edges (which must match for tiling) to the CENTER of the image, and
     hides them from view; the visible seam is now a "+" cross through the
     middle instead of split across 4 edges.
  2. Feather-blur ONLY a narrow band around that center cross, leaving the
     rest of the texture sharp — this smooths the discontinuity without
     softening the whole image.

This is an automated APPROXIMATION of manual seam healing, not true
content-aware inpainting — it works well for low-detail/noisy textures
(grass, dirt, stone, fabric) and less well for textures with large, distinct
shapes near the edges (those may show a faint soft patch at the seam). For a
hero/close-up texture, do a manual retouch pass after this script.

Usage:
    python make_tileable.py --input ground-raw.webp --output ground-tile.png --blend-width 48
"""

import argparse
from pathlib import Path


def make_tileable(image, blend_width: int = 48):
    from PIL import Image, ImageFilter
    import numpy as np

    img = image.convert("RGBA")
    w, h = img.size

    arr = np.array(img)
    offset_arr = np.roll(arr, shift=(h // 2, w // 2), axis=(0, 1))
    offset_img = Image.fromarray(offset_arr, mode="RGBA")

    # Blur the whole offset image once; we'll only use it near the seam.
    blurred = offset_img.filter(ImageFilter.GaussianBlur(radius=max(1, blend_width / 3)))

    yy, xx = np.mgrid[0:h, 0:w]
    dist_from_center_x = np.abs(xx - w / 2)
    dist_from_center_y = np.abs(yy - h / 2)
    seam_dist = np.minimum(dist_from_center_x, dist_from_center_y)
    weight = np.clip(1 - seam_dist / blend_width, 0, 1)  # 1 right on the seam, 0 by blend_width away
    weight_img = Image.fromarray((weight * 255).astype(np.uint8), mode="L")

    result = Image.composite(blurred, offset_img, weight_img)
    return result


def check_seamlessness(image) -> float:
    """Rough heuristic: compare the average pixel difference between opposite
    edges (top vs bottom, left vs right) of the ORIGINAL (pre-roll) image.
    Lower = more seamless. Not a precise metric — a sanity check, not a gate."""
    import numpy as np

    arr = np.array(image.convert("RGB"), dtype=np.float32)
    top, bottom = arr[0, :, :], arr[-1, :, :]
    left, right = arr[:, 0, :], arr[:, -1, :]
    diff = (np.abs(top - bottom).mean() + np.abs(left - right).mean()) / 2
    return float(diff)  # 0-255 scale; under ~15 is generally a good sign


def main():
    parser = argparse.ArgumentParser(description="Make a texture more tileable via offset + seam feathering.")
    parser.add_argument("--input", "-i", type=Path, required=True)
    parser.add_argument("--output", "-o", type=Path, required=True)
    parser.add_argument("--blend-width", type=int, default=48, help="Feather width in px around the seam (default 48).")

    args = parser.parse_args()

    if not args.input.exists():
        print(f"[ERROR] Input file not found: {args.input}")
        return 1

    from PIL import Image

    image = Image.open(args.input)
    before_score = check_seamlessness(image)

    result = make_tileable(image, blend_width=args.blend_width)

    after_score = check_seamlessness(result)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.save(args.output, "PNG")

    print(f"[OK] Saved to {args.output}")
    print(f"     Edge-mismatch score before: {before_score:.1f} / after: {after_score:.1f} (lower is better)")
    if after_score > 20:
        print("[WARN] Edges still don't match well — this source image may have large,")
        print("       distinct shapes crossing the original edges. Consider regenerating")
        print("       with a prompt more oriented toward a flat, repeating pattern, or")
        print("       do a manual retouch pass on this output.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
