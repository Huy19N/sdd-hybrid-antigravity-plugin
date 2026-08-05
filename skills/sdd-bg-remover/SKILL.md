---
name: sdd-bg-remover
description: "Sub-skill automatically invoked by sdd-build after sdd-asset-generator completes, only when the chosen template requires transparent/cutout images (requires_transparent_images: true in template frontmatter). Do NOT trigger manually. Removes backgrounds from product images using the rembg Python library, producing clean transparent PNGs ready for overlay-style layouts."
---

# SDD Background Remover (sub-skill of sdd-build)

## Purpose
Remove backgrounds from product/item images so they can be used in overlay-style
layouts where the product appears to float on a colored background — a common
pattern in e-commerce, product showcase, and food/beverage templates.

## Invocation
This skill is **automatically called** by `sdd-build` immediately after
`sdd-asset-generator` completes, but **only when** the chosen template has
`requires_transparent_images: true` in its frontmatter. Never trigger manually.

## Preconditions
- `sdd-asset-generator` has completed and produced images in `public/assets/generated/`.
- The asset inventory from `sdd-asset-generator` lists files with `Needs BG Removal? = Yes`.
- Python 3.8+ is available on the system.

## Process

### 1. Check for Python + rembg
```bash
python --version
pip show rembg
```
If `rembg` is not installed:
```bash
pip install rembg[gpu]   # if GPU available
# or
pip install rembg         # CPU fallback
```

### 2. Identify files to process
Read the asset inventory from `sdd-asset-generator`. Only process files marked
with `Needs BG Removal? = Yes`.

### 3. Run background removal
Use the bundled script at `skills/sdd-bg-remover/scripts/remove_bg.py`:

```bash
python skills/sdd-bg-remover/scripts/remove_bg.py \
  --input public/assets/generated/ \
  --output public/assets/no-bg/ \
  --files product-01.webp product-02.webp ...
```

Or process all images in the input directory:
```bash
python skills/sdd-bg-remover/scripts/remove_bg.py \
  --input public/assets/generated/ \
  --output public/assets/no-bg/ \
  --all
```

### 4. Verify output
- Check that each output file exists and has a transparent background (PNG format).
- Verify file sizes are reasonable (not 0 bytes, not corrupted).
- If any file fails processing, log the error and continue with remaining files.

### 5. Update asset paths
After processing, report back to `sdd-build` the updated asset paths:
```
product-01.webp → public/assets/no-bg/product-01.png  ✅
product-02.webp → public/assets/no-bg/product-02.png  ✅
```

## Fallback: remove.bg API
If `rembg` installation fails (e.g., missing system dependencies on Windows),
use the remove.bg free API as fallback:

1. Inform the user they need a free API key from https://www.remove.bg/api
2. Once provided, use the API:
```bash
curl -H "X-Api-Key: YOUR_KEY" \
  -F "image_file=@public/assets/generated/product-01.webp" \
  -F "size=auto" \
  -o public/assets/no-bg/product-01.png \
  https://api.remove.bg/v1.0/removebg
```

## Constraints
- Only process files explicitly marked for background removal. Do not process
  hero banners, icons, or background textures.
- Output format is always PNG (to preserve transparency).
- Do not modify the original files in `public/assets/generated/` — output to
  a separate `public/assets/no-bg/` directory.
- If both rembg and remove.bg fail, clearly inform the user and suggest
  manual background removal as last resort.

## Handoff
Return the list of processed files with their new paths to `sdd-build`.
`sdd-build` will then reference these transparent images in the UI code
using the `public/assets/no-bg/` paths.
