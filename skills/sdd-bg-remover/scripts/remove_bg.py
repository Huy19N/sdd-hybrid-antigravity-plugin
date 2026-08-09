#!/usr/bin/env python3
"""
SDD Background Remover v2 — Batch background removal for product images.

v1 used rembg's default `u2net` model with no post-processing, which left
semi-transparent "haze" and scattered noise pixels around complex edges
(spiky/textured subjects, multi-object scenes). v2 fixes this with:

  1. Model tiers (isnet-general-use / birefnet-general / birefnet-dis) instead
     of always using the older, lower-quality u2net default.
  2. Alpha matting (rembg's built-in edge-refinement post-process).
  3. A custom alpha-channel cleanup pass: hard-threshold near-zero alpha,
     morphological opening, and connected-component filtering — this removes
     leftover background speckle while correctly preserving legitimately
     separate object parts (e.g. two fruit segments in one shot).
  4. An automated edge-quality check that flags files likely to still have
     leftover noise, with optional auto-escalation to a stronger model tier
     instead of silently accepting a bad result.

Usage:
    # Process specific files (default tier = standard):
    python remove_bg.py --input ./assets/generated/ --output ./assets/no-bg/ \
        --files product-01.webp product-02.webp

    # Process all images, starting at a specific quality tier:
    python remove_bg.py --input ./assets/generated/ --output ./assets/no-bg/ \
        --all --tier fine-detail

Requirements:
    pip install rembg Pillow numpy
    pip install scipy   # optional but strongly recommended — enables the
                         # connected-component cleanup step; without it, only
                         # the hard-threshold + feather steps run.
"""

import argparse
import sys
from pathlib import Path

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff", ".tif"}

# Model tiers — see SKILL.md "Chọn tier theo loại vật thể" for full guidance.
# Ladder order matters: escalation walks this list left-to-right.
MODEL_PRESETS = {
    "standard": "isnet-general-use",  # default — better edge quality than u2net, still fast
    "high": "birefnet-general",        # best general-purpose quality, slower — complex/multi-object scenes
    "fine-detail": "birefnet-dis",     # Dichotomous Image Segmentation — built for fine/thin boundary
                                         # detail: spiky husks, fur, hair, lace
    "legacy": "u2net",                  # v1 default, kept only for backward compatibility
}
ESCALATION_LADDER = ["standard", "high", "fine-detail"]

# Exact parameter names/defaults per rembg's own USAGE.md
ALPHA_MATTING_DEFAULTS = dict(
    alpha_matting_foreground_threshold=270,
    alpha_matting_background_threshold=20,
    alpha_matting_erode_size=11,
)


def check_dependencies() -> bool:
    """Verify required dependencies; warn (not fail) if optional scipy is missing."""
    missing = []
    try:
        import rembg  # noqa: F401
    except ImportError:
        missing.append("rembg")
    try:
        from PIL import Image  # noqa: F401
    except ImportError:
        missing.append("Pillow")
    try:
        import numpy  # noqa: F401
    except ImportError:
        missing.append("numpy")

    if missing:
        print(f"[ERROR] Missing dependencies: {', '.join(missing)}")
        print("Install with: pip install rembg Pillow numpy")
        return False

    try:
        import scipy  # noqa: F401
    except ImportError:
        print("[WARN] scipy not installed — connected-component cleanup will be")
        print("       skipped (hard-threshold + feather steps still run).")
        print("       Install with: pip install scipy   (recommended)")

    return True


def clean_alpha_channel(
    img,
    min_component_ratio: float = 0.005,
    hard_threshold: int = 15,
    feather_radius: float = 1.0,
):
    """Post-process an RGBA image's alpha channel to remove leftover background noise.

    Args:
        img: PIL Image in RGBA mode.
        min_component_ratio: connected components smaller than this fraction of
            total image area are treated as noise and zeroed out. Default 0.5%
            — small enough to keep legitimately separate object parts (e.g. two
            fruit segments), large enough to drop scattered speckle.
        hard_threshold: alpha values below this are forced to 0 (removes
            semi-transparent "haze" left by the segmentation model).
        feather_radius: Gaussian blur radius applied to the alpha channel only,
            after cleanup, to re-smooth edges made blocky by morphological ops.

    Returns:
        A new PIL Image with the cleaned alpha channel.
    """
    import numpy as np
    from PIL import Image, ImageFilter

    r, g, b, a = img.split()
    alpha = np.array(a, dtype=np.uint8)

    # Step 1 — hard threshold near-zero alpha (kills semi-transparent haze)
    alpha[alpha < hard_threshold] = 0

    # Step 2 & 3 — morphological opening + connected-component filtering
    # (skipped gracefully if scipy isn't installed; step 1 alone still helps)
    try:
        from scipy import ndimage

        binary_mask = alpha > 0
        opened = ndimage.binary_opening(binary_mask, structure=np.ones((3, 3)), iterations=1)

        labeled, num_features = ndimage.label(opened)
        if num_features > 0:
            total_pixels = alpha.size
            component_sizes = ndimage.sum(opened, labeled, range(1, num_features + 1))
            keep_labels = {
                i + 1
                for i, size in enumerate(component_sizes)
                if size / total_pixels >= min_component_ratio
            }
            keep_mask = np.isin(labeled, list(keep_labels))
            alpha[~keep_mask] = 0
    except ImportError:
        pass

    # Step 4 — light feather to re-smooth edges after morphological cleanup
    a_cleaned = Image.fromarray(alpha, mode="L")
    if feather_radius > 0:
        a_cleaned = a_cleaned.filter(ImageFilter.GaussianBlur(radius=feather_radius))

    return Image.merge("RGBA", (r, g, b, a_cleaned))


def assess_edge_quality(img) -> float:
    """Rough proxy for leftover-noise risk: fraction of pixels that are
    semi-transparent (5 < alpha < 250) rather than cleanly opaque/transparent.
    Higher = more likely to still have visible artifacts."""
    import numpy as np

    alpha = np.array(img.split()[-1], dtype=np.uint8)
    semi = np.logical_and(alpha > 5, alpha < 250)
    return float(semi.sum()) / float(alpha.size)


def remove_background_once(
    input_path: Path,
    output_path: Path,
    model_name: str,
    use_alpha_matting: bool,
    quality_review_threshold: float,
):
    """Run one background-removal attempt. Returns (success, needs_review, edge_noise_ratio)."""
    from rembg import remove, new_session
    from PIL import Image

    try:
        with Image.open(input_path) as img:
            if img.mode != "RGBA":
                img = img.convert("RGBA")

            session = new_session(model_name)
            kwargs = dict(ALPHA_MATTING_DEFAULTS) if use_alpha_matting else {}
            result = remove(img, session=session, alpha_matting=use_alpha_matting, **kwargs)
            result = clean_alpha_channel(result)

            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_file = output_path.with_suffix(".png")
            result.save(output_file, "PNG")

            if output_file.stat().st_size == 0:
                print(f"  [WARN] Output file is empty: {output_file}")
                return False, False, 1.0

            edge_noise_ratio = assess_edge_quality(result)
            needs_review = edge_noise_ratio > quality_review_threshold
            return True, needs_review, edge_noise_ratio

    except Exception as e:
        print(f"  [FAIL] {input_path.name}: {e}")
        return False, False, 1.0


def process_file(
    input_path: Path,
    output_path: Path,
    start_tier: str,
    auto_escalate: bool,
    use_alpha_matting: bool,
    quality_review_threshold: float,
    max_escalations: int,
):
    """Process one file, auto-escalating to a stronger model tier if the
    quality check flags leftover noise. Returns (success, needs_review, final_tier)."""
    start_idx = ESCALATION_LADDER.index(start_tier) if start_tier in ESCALATION_LADDER else 0
    tiers_to_try = ESCALATION_LADDER[start_idx : start_idx + 1 + (max_escalations if auto_escalate else 0)]

    for i, tier in enumerate(tiers_to_try):
        model_name = MODEL_PRESETS[tier]
        success, needs_review, noise = remove_background_once(
            input_path, output_path, model_name, use_alpha_matting, quality_review_threshold
        )
        if not success:
            return False, False, tier

        is_last_attempt = i == len(tiers_to_try) - 1
        if not needs_review or is_last_attempt:
            tag = "✅" if not needs_review else "⚠️  NEEDS REVIEW"
            escalated_note = f" (escalated to '{tier}')" if i > 0 else ""
            print(
                f"  [OK] {input_path.name} → {output_path.with_suffix('.png').name}"
                f"  [tier={tier}, noise={noise:.1%}]{escalated_note} {tag}"
            )
            return True, needs_review, tier
        else:
            print(f"  [RETRY] {input_path.name}: tier '{tier}' left {noise:.1%} noisy edges — escalating...")

    return True, True, tiers_to_try[-1]  # unreachable, safety fallback


def get_image_files(input_dir: Path, file_names=None) -> list[Path]:
    """Get list of image files to process."""
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
        description="Remove backgrounds from product images using rembg (v2: tiered models + cleanup)."
    )
    parser.add_argument("--input", "-i", type=Path, required=True)
    parser.add_argument("--output", "-o", type=Path, required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--files", "-f", nargs="+")
    group.add_argument("--all", "-a", action="store_true")
    parser.add_argument(
        "--tier", choices=list(MODEL_PRESETS.keys()), default="standard",
        help="Starting quality tier. Default: standard (isnet-general-use).",
    )
    parser.add_argument(
        "--no-auto-escalate", action="store_true",
        help="Disable automatic escalation to a stronger model when quality check fails.",
    )
    parser.add_argument(
        "--max-escalations", type=int, default=2,
        help="Max number of tier escalations per file (default: 2, i.e. up to 'fine-detail').",
    )
    parser.add_argument("--no-alpha-matting", action="store_true")
    parser.add_argument(
        "--quality-threshold", type=float, default=0.03,
        help="Fraction of semi-transparent pixels above which a file is flagged 'needs review' (default 0.03 = 3%%).",
    )

    args = parser.parse_args()

    if not args.input.is_dir():
        print(f"[ERROR] Input directory does not exist: {args.input}")
        sys.exit(1)

    if not check_dependencies():
        sys.exit(1)

    files = get_image_files(args.input, args.files if not args.all else None)
    if not files:
        print("[WARN] No image files found to process.")
        sys.exit(0)

    print(f"\n{'='*60}")
    print("SDD Background Remover v2")
    print(f"Input:  {args.input.resolve()}")
    print(f"Output: {args.output.resolve()}")
    print(f"Files:  {len(files)}")
    print(f"Starting tier: {args.tier}  |  Auto-escalate: {not args.no_auto_escalate}")
    print(f"{'='*60}\n")

    success_count = 0
    failed_count = 0
    needs_review_files = []

    for file_path in files:
        output_path = args.output / file_path.name
        success, needs_review, final_tier = process_file(
            file_path,
            output_path,
            start_tier=args.tier,
            auto_escalate=not args.no_auto_escalate,
            use_alpha_matting=not args.no_alpha_matting,
            quality_review_threshold=args.quality_threshold,
            max_escalations=args.max_escalations,
        )
        if success:
            success_count += 1
            if needs_review:
                needs_review_files.append((file_path.name, final_tier))
        else:
            failed_count += 1

    print(f"\n{'='*60}")
    print(f"Done: {success_count} succeeded, {failed_count} failed out of {len(files)} total")
    if needs_review_files:
        print(f"\n⚠️  {len(needs_review_files)} file(s) still flagged after max escalation — manual review suggested:")
        for name, tier in needs_review_files:
            print(f"   - {name} (tried up to tier '{tier}')")
        print("   Consider: manual crop/retouch, or a different source photo with a")
        print("   more uniform background.")
    print(f"{'='*60}")

    if failed_count > 0:
        sys.exit(1)
    elif needs_review_files:
        sys.exit(2)  # distinct exit code: succeeded but needs human review


if __name__ == "__main__":
    main()
