---
id: photography-studio
name: "Photography Studio"
category: photography
tags:
  - photography
  - studio
  - gallery
  - photographer
  - photo
  - visual
requires_transparent_images: false
color_palette:
  primary: "#27272A"
  secondary: "#FAFAFA"
  accent: "#EF4444"
  background: "#FAFAFA"
  surface: "#FFFFFF"
  text: "#18181B"
  muted: "#71717A"
reactbits_components:
  - name: "Circular Gallery"
    url: "https://www.reactbits.dev/components/circular-gallery"
  - name: "Magnet Lines"
    url: "https://www.reactbits.dev/animations/magnet-lines"
best_for: "Studio chụp ảnh, photographer portfolio, photo gallery — minimal UI, fullscreen images, lightbox, image-first design"
fonts:
  display: "Instrument Serif"
  body: "Work Sans"
---

# Template: Photography Studio

## Preview Description
A minimal, image-first photography portfolio with **circular gallery** for featured
work, **magnet lines** interactive background, and a clean white-on-charcoal design.
Photos are the hero — UI chrome is reduced to near-invisible. Fullscreen lightbox,
smooth transitions, and a single red accent color for CTAs. The serif display font
adds editorial elegance.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Work+Sans:wght@300;400;500;600&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#27272A` (Charcoal) | Nav, text on light bg |
| Secondary | `#FAFAFA` (Near White) | Main background |
| Accent | `#EF4444` (Red) | Single accent — CTAs, hover |
| Background | `#FAFAFA` | Page bg |
| Surface | `#FFFFFF` | Cards |
| Text | `#18181B` | Primary text |
| Muted | `#71717A` | Captions, dates |

## Layout Structure

### 1. Magnet Lines (About section only)
### 2. Nav — ultra-minimal
- Name (Instrument Serif, italic) — left
- Portfolio / About / Contact — right
- No bg, absolute positioned over hero
- White text on dark images, dark on light sections

### 3. Hero — fullscreen single image
- Latest/best photo, 100vh
- Name and tagline overlay (bottom-left), minimal
- Scroll indicator arrow

### 4. Featured Work — Circular Gallery
- 8-12 selected photos in ReactBits Circular Gallery
- Click opens fullscreen lightbox
- Category labels: Portrait / Landscape / Editorial / Event

### 5. Selected Projects
- Vertical stack of project sections
- Each project: full-width hero image + project title + description
- Alternating: image-left/text-right, then image-right/text-left
- Click to expand full project gallery

### 6. About
- Photo of photographer + bio text
- Magnet Lines background effect
- Client list / publication logos
- Equipment/style description

### 7. Services & Pricing
- Minimal: 3-4 service types with starting prices
- Clean table or card layout

### 8. Contact
- "Let's Create Together" — Instrument Serif, italic
- Email, phone, social links
- Optional: booking calendar embed

### 9. Footer — single line, © name

## Prompt

Build a photography portfolio in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Ultra-minimal, image-first design.

**Fonts:** Instrument Serif (display, italic) and Work Sans (body, 300-600).

**Key elements:** Fullscreen hero photo, Circular Gallery for featured work, fullscreen lightbox on click, Magnet Lines in about section, minimal chrome, single red accent color, editorial serif typography.

**Sections:** Nav (minimal, overlaid) → Hero (fullscreen photo) → Featured (circular gallery) → Projects (vertical stack) → About (bio + magnet lines bg) → Services → Contact → Footer.

**Color system:** Near-white bg `#FAFAFA`, charcoal `#27272A`, single red accent `#EF4444`.

## Required Assets
- `hero-photo` — Best/latest photograph (fullscreen)
- `gallery-01` through `gallery-12` — Portfolio photographs
- `project-01` through `project-04` — Project hero images
- `photographer-portrait` — Self-portrait for About section

## ReactBits Components Used
- **Circular Gallery** (`https://www.reactbits.dev/components/circular-gallery`) — Interactive circular photo gallery for featured work.
- **Magnet Lines** (`https://www.reactbits.dev/animations/magnet-lines`) — Interactive lines in About section background.
