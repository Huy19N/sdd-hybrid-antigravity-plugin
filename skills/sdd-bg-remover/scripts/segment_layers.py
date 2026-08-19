#!/usr/bin/env python3
"""
SDD Background Remover — Multi-Layer Segmentation (v3)

Splits ONE composite scene image into several separate labeled layers (e.g.
"sky", "cloud", "tree", "wooden fence post", "ground") — for 2D/2.5D game
parallax backgrounds where each layer needs to move at a different scroll
speed. This is a DIFFERENT problem from remove_bg.py's single-subject
foreground/background separation, and uses a different technique:
CLIPSeg (open-vocabulary, text-prompted zero-shot segmentation) instead of
rembg. rembg answers "what is THE subject vs. everything else"; this answers
"where is EACH of these N things I named, in the same image".

Usage:
    python segment_layers.py \
        --input scene.png \
        --output ./layers/ \
        --labels "sky" "cloud" "distant mountain" "tree" "wooden fence post" "ground"

Requirements:
    pip install torch transformers Pillow numpy scipy
    (first run downloads the CIDAS/clipseg-rd64-refined model, ~600MB,
    cached locally after — this is a heavier dependency set than remove_bg.py's
    rembg-only requirements, kept in a separate script so single-subject
    background removal doesn't pay this cost unless you actually need it.)
"""

import argparse
import sys
from pathlib import Path

_model_cache: dict = {}


def check_dependencies() -> bool:
    missing = []
    try:
        import torch  # noqa: F401
    except ImportError:
        missing.append("torch")
    try:
        import transformers  # noqa: F401
    except ImportError:
        missing.append("transformers")
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
        print("Install with: pip install torch transformers Pillow numpy")
        return False

    try:
        import scipy  # noqa: F401
    except ImportError:
        print("[WARN] scipy not installed — layer cleanup will be weaker (see remove_bg.py notes).")

    return True


def load_model():
    if "model" not in _model_cache:
        from transformers import CLIPSegProcessor, CLIPSegForImageSegmentation

        print("[INFO] Loading CLIPSeg model (first run downloads ~600MB, cached after)...")
        _model_cache["processor"] = CLIPSegProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
        _model_cache["model"] = CLIPSegForImageSegmentation.from_pretrained("CIDAS/clipseg-rd64-refined")
    return _model_cache["processor"], _model_cache["model"]


def predict_label_masks(image, labels: list[str]):
    """Run CLIPSeg once for all labels. Returns {label: numpy float32 array in
    [0,1], resized to the original image size} — raw per-label confidence,
    NOT yet resolved for overlap between labels."""
    import torch
    import numpy as np
    from PIL import Image

    processor, model = load_model()
    inputs = processor(text=labels, images=[image] * len(labels), padding=True, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    if logits.ndim == 2:  # single label collapses the batch dim — restore it
        logits = logits.unsqueeze(0)

    masks = {}
    for i, label in enumerate(labels):
        probs = torch.sigmoid(logits[i]).numpy()  # low-res heatmap, values 0-1
        mask_img = Image.fromarray((probs * 255).astype("uint8"), mode="L")
        mask_img = mask_img.resize(image.size, Image.BILINEAR)
        masks[label] = np.array(mask_img, dtype=np.float32) / 255.0

    return masks


def resolve_overlap(masks: dict, labels_order: list[str]):
    """CLIPSeg predicts each label independently, so overlapping high-confidence
    regions between labels are common (e.g. "sky" and "cloud" both firing on
    the same pixels). Resolve by assigning each pixel to whichever label has
    the single highest confidence there (argmax across all label masks),
    instead of letting multiple layers claim the same pixels."""
    import numpy as np

    stack = np.stack([masks[label] for label in labels_order], axis=0)  # (N, H, W)
    winner = np.argmax(stack, axis=0)  # (H, W)

    resolved = {}
    for i, label in enumerate(labels_order):
        claimed = (winner == i).astype(np.float32)
        resolved[label] = stack[i] * claimed
    return resolved


def build_layer_pngs(
    image,
    resolved_masks: dict,
    output_dir: Path,
    hard_threshold: int = 25,
    min_component_ratio: float = 0.001,
    feather_radius: float = 1.5,
):
    """Turn each resolved confidence mask into a saved RGBA PNG layer, reusing
    remove_bg.py's alpha-cleanup pipeline for consistency. Note the much lower
    default min_component_ratio than remove_bg.py (0.001 vs 0.005) — a layer
    like "cloud" can legitimately be several small, scattered, disconnected
    puffs, unlike a single product photo where scattered specks are noise."""
    import numpy as np
    from PIL import Image

    sys.path.insert(0, str(Path(__file__).parent))
    from remove_bg import clean_alpha_channel  # reuse v2's cleanup logic

    saved = []
    for label, confidence in resolved_masks.items():
        alpha = (confidence * 255).astype(np.uint8)
        alpha_img = Image.fromarray(alpha, mode="L")

        layer = image.convert("RGBA").copy()
        layer.putalpha(alpha_img)
        layer = clean_alpha_channel(
            layer,
            min_component_ratio=min_component_ratio,
            hard_threshold=hard_threshold,
            feather_radius=feather_radius,
        )

        safe_name = label.lower().replace(" ", "-")
        out_path = output_dir / f"layer-{safe_name}.png"
        output_dir.mkdir(parents=True, exist_ok=True)
        layer.save(out_path, "PNG")

        coverage = float((alpha > hard_threshold).sum()) / alpha.size
        saved.append((label, out_path, coverage))

    return saved


def main():
    parser = argparse.ArgumentParser(
        description="Decompose one composite scene image into labeled parallax layers using CLIPSeg."
    )
    parser.add_argument("--input", "-i", type=Path, required=True)
    parser.add_argument("--output", "-o", type=Path, required=True)
    parser.add_argument("--labels", "-l", nargs="+", required=True, help="Text labels, one per layer, e.g. sky cloud tree")
    parser.add_argument("--min-component-ratio", type=float, default=0.001)
    parser.add_argument("--hard-threshold", type=int, default=25)

    args = parser.parse_args()

    if not args.input.exists():
        print(f"[ERROR] Input file not found: {args.input}")
        sys.exit(1)
    if len(args.labels) < 2:
        print("[ERROR] Provide at least 2 labels — with only 1 label, use remove_bg.py instead.")
        sys.exit(1)

    if not check_dependencies():
        sys.exit(1)

    from PIL import Image

    image = Image.open(args.input).convert("RGB")

    print(f"[INFO] Segmenting {len(args.labels)} labels from {args.input.name}: {', '.join(args.labels)}")
    raw_masks = predict_label_masks(image, args.labels)
    resolved = resolve_overlap(raw_masks, args.labels)
    saved = build_layer_pngs(
        image, resolved, args.output,
        hard_threshold=args.hard_threshold,
        min_component_ratio=args.min_component_ratio,
    )

    print(f"\n{'='*60}")
    for label, path, coverage in saved:
        flag = "⚠️  very small/empty — label may not match anything in the image" if coverage < 0.005 else "✅"
        print(f"  {label:30s} → {path.name:35s} [{coverage:5.1%} of frame] {flag}")
    print(f"{'='*60}")
    print(f"Layers saved to {args.output.resolve()}")
    print("Reminder: layers are resolved to be mutually exclusive (no pixel claimed")
    print("by two layers) — stack them in the SAME order as --labels was given,")
    print("back-to-front, to reconstruct the original scene with no gaps.")


if __name__ == "__main__":
    main()
