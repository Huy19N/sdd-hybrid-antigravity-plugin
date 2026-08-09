---
name: sdd-asset-generator
description: "Sub-skill automatically invoked by sdd-build when plan.md contains a Design Template section. Do NOT trigger manually. Uses the generate_image tool to create all required visual assets (product photos, hero banners, icons, backgrounds) matching the chosen template's color palette and style. Outputs generated images to public/assets/generated/ ready for the build phase."
---

# SDD Asset Generator (sub-skill of sdd-build)

## Purpose
Create all visual assets required by the chosen design template before UI code
is written. This ensures the build phase has real images to work with instead
of placeholder rectangles, resulting in a polished deliverable from the first
build iteration.

## Invocation
This skill is **automatically called** by `sdd-build` when `plan.md` contains
a `## Design Template` section. It runs **before** the first UI-related task
in the plan. Never trigger this skill directly — `sdd-build` handles the
orchestration.

## Preconditions
- `docs/sdd/<feature-slug>/plan.md` exists with a `## Design Template` section.
- The Design Template section includes a `Required Assets` list.
- The template's color palette is specified.

## Process

### 1. Parse the asset manifest
Read `plan.md` → `## Design Template` → `Required Assets` field.
Each asset entry should specify:
- Asset type (product-photo, hero-banner, icon, background-texture, person-portrait, illustration)
- Description (what the image should depict)
- Dimensions or aspect ratio if relevant
- Quantity needed

### 2. Build prompts per asset type
For each asset, construct a `generate_image` prompt following these guidelines:

#### Product Photos
```
"[Product description], professional product photography, studio lighting,
clean [background color from palette] background, high quality, commercial
photography style, centered composition"
```
- If template has `requires_transparent_images: true`, add: "isolated on pure
  white background for easy background removal"

#### Hero Banners
```
"[Scene description], cinematic wide-angle shot, [mood from template],
color palette: [primary] [secondary] [accent], modern web design hero image,
16:9 aspect ratio, high resolution"
```

#### Icons / Illustrations
```
"[Icon description], flat design icon, [style: minimal/playful/corporate],
[accent color] on transparent background, consistent line weight,
modern UI icon style"
```

#### Person Portraits
```
"Professional headshot portrait, [description], friendly expression,
neutral background, business casual, high quality photography"
```

#### Background Textures
```
"Abstract [texture type] texture, [colors from palette], seamless pattern,
subtle and elegant, suitable for web background, high resolution"
```

### 3. Generate each asset
- Call `generate_image` for each asset in the manifest.
- Name files descriptively: `hero-banner.webp`, `product-01.webp`,
  `icon-feature-search.webp`, etc.
- Save to `public/assets/generated/` (create directory if needed).

### 4. Asset inventory
After all assets are generated, create a brief inventory:
```markdown
## Generated Assets
| File | Type | Description | Needs BG Removal? | Suggested Tier |
|---|---|---|---|---|
| hero-banner.webp | hero-banner | ... | No | — |
| product-01.webp | product-photo | Smooth bottle on white bg | Yes | standard |
| product-02.webp | product-photo | Spiky durian with husk detail | Yes | fine-detail |
```

The `Suggested Tier` column helps `sdd-build` pass the right `--tier` to
`sdd-bg-remover` (see its SKILL.md step 3 for the full tier guide). Use:
- `standard` — smooth/simple edges (bottles, boxes, flat objects)
- `high` — complex/multi-object scenes (product in a gift box)
- `fine-detail` — spiky, furry, or lacy edges (durian, plush toys, lace)
- `—` — not applicable (no BG removal needed)

Return this inventory to `sdd-build` so it knows:
- Which files are ready to use directly.
- Which files need to go through `sdd-bg-remover` next.

## Prompt Engineering Tips
- Always reference the template's **color palette** to maintain visual cohesion.
- For product-store templates, emphasize **clean backgrounds** for easier removal.
- For tech/SaaS templates, lean toward **abstract, gradient-heavy** imagery.
- For food/restaurant templates, emphasize **warm lighting, appetizing styling**.
- For fashion templates, emphasize **editorial, high-contrast** photography.
- Keep prompts concise but specific — 2-3 sentences max per image.

## Constraints
- Generate only assets listed in the `Required Assets` manifest. Do not
  improvise extra images without the plan specifying them.
- If `generate_image` fails for a specific prompt, retry once with a simplified
  prompt. If it fails again, log the failure and continue with remaining assets.
- Do not modify any source code during this sub-skill. Only produce image files.

## Handoff
Return the asset inventory to `sdd-build`. If any assets have
`Needs BG Removal? = Yes` AND the template has `requires_transparent_images: true`,
`sdd-build` will automatically invoke `sdd-bg-remover` next.
