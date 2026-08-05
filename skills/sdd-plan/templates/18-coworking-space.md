---
id: coworking-space
name: "Coworking Space"
category: coworking
tags:
  - coworking
  - office
  - workspace
  - rental
  - community
  - flex-space
requires_transparent_images: false
color_palette:
  primary: "#CA8A04"
  secondary: "#78716C"
  accent: "#059669"
  background: "#FAFAF9"
  surface: "#FFFFFF"
  text: "#292524"
  muted: "#78716C"
reactbits_components:
  - name: "Magic Bento"
    url: "https://www.reactbits.dev/components/magic-bento"
  - name: "Tilted Card"
    url: "https://www.reactbits.dev/components/tilted-card"
best_for: "Không gian làm việc chung, cho thuê văn phòng, co-working hub, flexible workspace"
fonts:
  display: "Cabinet Grotesk"
  body: "Inter"
---

# Template: Coworking Space

## Preview Description
A modern, professional coworking space website with **Magic Bento** grid layout for
space showcases, **tilted cards** for pricing tiers, and a warm industrial palette.
Mustard yellow accents on stone/wood tones convey productivity and creativity.
Floor plan viewer, amenity icons, community events calendar, and a straightforward
booking flow.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
```

Note: Using Outfit as proxy for Cabinet Grotesk.

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#CA8A04` (Mustard) | CTAs, highlights, active |
| Secondary | `#78716C` (Warm Gray) | Borders, secondary |
| Accent | `#059669` (Emerald) | Availability, success |
| Background | `#FAFAF9` (Stone White) | Page bg |
| Surface | `#FFFFFF` | Cards |
| Text | `#292524` (Dark Stone) | Primary text |
| Muted | `#78716C` | Secondary text |

## Layout Structure

### 1. Nav
- Clean, minimal, white bg
- Logo + Spaces / Pricing / Community / Contact
- "Book a Tour" mustard CTA

### 2. Hero
- Large interior photo of the coworking space
- "Work Where Ideas Thrive" headline
- Location + "Book a Tour" + "View Spaces" CTAs
- Amenity icons strip below: WiFi, Coffee, Meeting Rooms, Printer, 24/7

### 3. Our Spaces — Magic Bento Grid
- Varying-size cards showing different space types
- Hot Desk, Dedicated Desk, Private Office, Meeting Room, Event Space
- Each: photo + name + capacity + starting price
- Magic Bento layout: 1 large + 2 medium + 2 small

### 4. Amenities
- Icon grid of all amenities
- Categories: Tech, Comfort, Community, Business
- Clean icon + label pairs

### 5. Pricing — Tilted Cards
- 3-4 plans: Day Pass / Hot Desk / Dedicated / Private Office
- ReactBits Tilted Card for 3D tilt on hover
- Price, features, "Get Started" button
- Popular plan highlighted

### 6. Community
- Events calendar or upcoming events cards
- Member testimonials
- Community photos (people working, events)

### 7. Location & Contact
- Map, address, hours
- Virtual tour link
- Contact form

### 8. Footer — links, social, locations list

## Prompt

Build a coworking space website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Modern professional design with industrial warmth.

**Fonts:** Outfit (display, 400-800) and Inter (body, 400-600).

**Key elements:** Magic Bento grid for space showcases, Tilted Card pricing tiers, amenity icon grid, warm mustard-and-stone palette, interior photography focus.

**Sections:** Nav → Hero (interior photo + CTAs) → Spaces (Magic Bento) → Amenities (icon grid) → Pricing (tilted cards) → Community (events + testimonials) → Location → Footer.

**Color system:** Stone white `#FAFAF9`, mustard `#CA8A04`, warm gray `#78716C`, emerald `#059669`, dark stone `#292524`.

## Required Assets
- `hero-interior` — Main coworking space interior photo
- `space-hotdesk`, `space-dedicated`, `space-private`, `space-meeting`, `space-event` — Space type photos
- `community-01` through `community-03` — People working / community event photos

## ReactBits Components Used
- **Magic Bento** (`https://www.reactbits.dev/components/magic-bento`) — Varying-size grid for space showcases.
- **Tilted Card** (`https://www.reactbits.dev/components/tilted-card`) — 3D tilt effect on pricing tier cards.
