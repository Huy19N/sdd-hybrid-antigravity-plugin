---
id: fitness-gym
name: "Fitness & Gym"
category: fitness
tags:
  - fitness
  - gym
  - workout
  - health
  - training
  - sport
  - exercise
requires_transparent_images: false
color_palette:
  primary: "#39FF14"
  secondary: "#71717A"
  accent: "#FACC15"
  background: "#0A0A0A"
  surface: "#171717"
  text: "#FAFAFA"
  muted: "#71717A"
reactbits_components:
  - name: "Pixel Trail"
    url: "https://www.reactbits.dev/animations/pixel-trail"
  - name: "Text Pressure"
    url: "https://www.reactbits.dev/text-animations/text-pressure"
best_for: "Phòng tập gym, fitness app, personal trainer, chương trình tập luyện — bold typography, high energy, membership tiers"
fonts:
  display: "Bebas Neue"
  body: "Barlow"
---

# Template: Fitness & Gym

## Preview Description
A high-energy, bold fitness website with **neon green on black**, oversized Bebas Neue
typography, pixel trail cursor effect, and text that responds to mouse pressure.
Everything screams intensity and motivation. Membership tiers with comparison,
class schedule, trainer profiles, and transformation gallery.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#39FF14` (Neon Green) | CTAs, highlights, active |
| Secondary | `#71717A` (Steel) | Borders, muted elements |
| Accent | `#FACC15` (Yellow) | Badges, special offers |
| Background | `#0A0A0A` (Deep Black) | Page bg |
| Surface | `#171717` (Near Black) | Cards |
| Text | `#FAFAFA` | Primary text |
| Muted | `#71717A` | Secondary text |

## Layout Structure

### 1. Pixel Trail Cursor (desktop only)
- ReactBits Pixel Trail following cursor
- Neon green pixelated trail

### 2. Nav — aggressive minimal
- Logo (left, Bebas Neue) + Classes / Trainers / Pricing (center)
- "JOIN NOW" neon green button (right), uppercase

### 3. Hero
- Full-bleed gym/workout video or image background, dark overlay
- Text Pressure headline: "PUSH YOUR LIMITS" — reacts to cursor proximity
- `text-7xl sm:text-9xl`, Bebas Neue
- "Start Free Trial" neon green CTA + "View Classes" outline button

### 4. Stats Strip
- 4 metrics: "500+ Members" / "30+ Classes" / "15 Trainers" / "24/7 Open"
- Neon green numbers, animated count-up

### 5. Classes Grid
- 3x2 grid: HIIT, Yoga, CrossFit, Boxing, Spinning, Strength
- Cards: background image + overlay + class name + time + difficulty badge
- Hover: overlay lifts, reveals description

### 6. Trainers
- Horizontal scroll trainer cards
- Photo, name, specialty, certifications
- "Book Session" CTA on each

### 7. Membership Pricing
- 3 tiers: Basic / Pro / Elite
- Dark cards, neon green highlights on Elite
- Feature comparison with check/x
- Yellow "Best Value" badge on Pro

### 8. Transformations Gallery
- Before/After slider component
- Member name, program, duration

### 9. CTA
- "YOUR TRANSFORMATION STARTS TODAY"
- Bebas Neue, huge, neon green gradient
- "Join Now" button

### 10. Footer — minimal, dark

## Prompt

Build a fitness/gym website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. High-energy, bold, dark design with neon accents.

**Fonts:** Bebas Neue (display) and Barlow (body, 400-700).

**Key elements:** Pixel Trail cursor (neon green), Text Pressure on hero headline, neon green on deep black, bold uppercase everything, before/after transformation sliders.

**Sections:** Nav → Hero (pressure text + dark bg) → Stats → Classes (grid) → Trainers (scroll) → Pricing (3 tiers) → Transformations (before/after) → CTA → Footer.

**Color system:** Deep black `#0A0A0A`, neon green `#39FF14`, steel `#71717A`, yellow accent `#FACC15`.

## Required Assets
- `hero-gym` — Gym/workout hero background (dark, dramatic)
- `class-01` through `class-06` — Class category images
- `trainer-01` through `trainer-04` — Trainer photos
- `transform-before-01`, `transform-after-01` — Transformation before/after

## ReactBits Components Used
- **Pixel Trail** (`https://www.reactbits.dev/animations/pixel-trail`) — Pixelated cursor trail effect.
- **Text Pressure** (`https://www.reactbits.dev/text-animations/text-pressure`) — Hero text reacts to mouse proximity.
