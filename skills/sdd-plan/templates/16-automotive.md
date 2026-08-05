---
id: automotive
name: "Automotive"
category: automotive
tags:
  - automotive
  - car
  - vehicle
  - motorcycle
  - dealership
  - showroom
requires_transparent_images: true
color_palette:
  primary: "#DC2626"
  secondary: "#C0C0C0"
  accent: "#FACC15"
  background: "#111111"
  surface: "#1C1C1C"
  text: "#F5F5F5"
  muted: "#737373"
reactbits_components:
  - name: "Grid Distortion"
    url: "https://www.reactbits.dev/backgrounds/grid-distortion"
  - name: "Shiny Text"
    url: "https://www.reactbits.dev/text-animations/shiny-text"
best_for: "Ô tô, xe máy, showroom, car dealership, hãng xe — cinematic hero, spec comparison, vehicle showcase với ảnh tách nền"
fonts:
  display: "Rajdhani"
  body: "Barlow"
---

# Template: Automotive

## Preview Description
A cinematic, high-octane automotive website with **grid distortion** background effect,
**shiny metallic text** for the brand, and a dark-on-dark aesthetic with racing red and
chrome accents. Vehicles showcased with transparent backgrounds floating on dark surfaces.
Spec comparison tables, 360° viewer CTA, and configurator tease. The design feels fast,
precise, and premium.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#DC2626` (Racing Red) | CTAs, highlights, brand |
| Secondary | `#C0C0C0` (Chrome) | Metallic accents, borders |
| Accent | `#FACC15` (Yellow) | Badges, special editions |
| Background | `#111111` | Page bg |
| Surface | `#1C1C1C` | Cards, sections |
| Text | `#F5F5F5` | Primary text |
| Muted | `#737373` | Specs, secondary |

## Layout Structure

### 1. Grid Distortion — hero background, metallic grid effect
### 2. Nav — automotive-minimal, brand logo center, red accent line below
### 3. Hero
- Transparent-bg vehicle image, large, centered
- Shiny Text brand/model name above
- "Configure Yours" + "Book Test Drive" buttons
- Grid Distortion behind
- Specs bar: HP / 0-60 / Top Speed / Price

### 4. Model Lineup
- Horizontal scroll of vehicle cards
- Each: transparent-bg vehicle, model name, starting price, "Explore" link
- Hover: subtle scale + red border

### 5. Specs Comparison
- Side-by-side spec comparison table
- Model selector dropdowns
- Key metrics: engine, power, torque, 0-60, fuel, price

### 6. Gallery / 360° View
- Fullscreen image gallery of vehicle details
- "360° View" CTA button (placeholder for future integration)
- Interior/exterior toggle tabs

### 7. Configurator Teaser
- "Build Your Own" section
- Color swatch selector (visual preview)
- Starting configuration preview

### 8. Test Drive CTA
- Location finder + booking form
- Red gradient background

### 9. Footer — brand heritage, model links, legal, social

## Prompt

Build an automotive/car showcase website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Cinematic dark design with metallic accents.

**Fonts:** Rajdhani (display, 400-700) and Barlow (body, 400-700).

**Key elements:** Grid Distortion metallic background, Shiny Text for brand name, transparent-bg vehicle images, spec bars with large numbers, chrome/racing-red accents, cinematic dark atmosphere.

**Sections:** Nav → Hero (vehicle + shiny brand + specs bar + grid distortion) → Model Lineup (scroll) → Specs Comparison (table) → Gallery + 360° CTA → Configurator Teaser → Test Drive Booking → Footer.

**Color system:** Dark bg `#111111`, racing red `#DC2626`, chrome `#C0C0C0`, yellow accent `#FACC15`.

## Required Assets
- `vehicle-hero` — Main vehicle (transparent background, 3/4 angle)
- `vehicle-01` through `vehicle-04` — Model lineup vehicles (transparent bg)
- `gallery-exterior-01` through `gallery-exterior-04` — Exterior detail shots
- `gallery-interior-01` through `gallery-interior-03` — Interior shots

## ReactBits Components Used
- **Grid Distortion** (`https://www.reactbits.dev/backgrounds/grid-distortion`) — Metallic grid background in hero.
- **Shiny Text** (`https://www.reactbits.dev/text-animations/shiny-text`) — Chrome/metallic text shimmer on brand name.
