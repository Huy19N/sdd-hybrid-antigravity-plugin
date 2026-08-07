---
id: wedding-planner
name: "Wedding & Event Planning"
version: 2
changelog:
  - "v2: added Venue Scene Annotation section (hand-drawn hover doodle overlay), uses shared interaction _shared/interactions/hand-drawn-annotation.md"
category: wedding-event
uses_shared_interactions:
  - hand-drawn-annotation
tags:
  - wedding
  - event-planning
  - bridal
  - ceremony
  - celebration
requires_transparent_images: false
color_palette:
  primary: "#BE185D"
  secondary: "#F5E6CC"
  accent: "#6B8E6B"
  background: "#FFFBF7"
  surface: "#FFFFFF"
  text: "#3D2B1F"
  muted: "#8B7D6B"
reactbits_components:
  - name: "Falling Text"
    url: "https://www.reactbits.dev/text-animations/falling-text"
  - name: "Circular Gallery"
    url: "https://www.reactbits.dev/components/circular-gallery"
best_for: "Đám cưới, tổ chức sự kiện, wedding planner, bridal shop, ceremony venue"
fonts:
  display: "Cormorant"
  body: "Lato"
---

# Template: Wedding & Event Planning

## Preview Description
An elegant, romantic wedding website with **falling text** animation for the couple's
names, a **circular gallery** of ceremony photos, and a soft rose-champagne-sage color
palette. Refined serif typography (Cormorant) creates timeless elegance. Includes
RSVP form, event timeline, registry links, and venue details. Every element
breathes romance and sophistication.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Lato:wght@300;400;700&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#BE185D` (Rose) | CTAs, accents, decorative |
| Secondary | `#F5E6CC` (Champagne) | Section backgrounds |
| Accent | `#6B8E6B` (Sage) | Secondary accents, nature |
| Background | `#FFFBF7` (Warm White) | Page bg |
| Surface | `#FFFFFF` | Cards |
| Text | `#3D2B1F` (Dark Walnut) | Primary text |
| Muted | `#8B7D6B` | Secondary text |

## Layout Structure

### 1. Nav — elegant, thin
- Couple's initials (monogram) — center
- Our Story / Details / Gallery / RSVP — evenly spaced
- Thin serif typography, rose hover color
- No heavy background — transparent or soft white

### 2. Hero
- Fullscreen engagement/couple photo
- Falling Text animation: couple's names fall into place
- Date + venue below names
- "RSVP" button (rose, elegant rounded)
- Subtle floral/botanical decorative border (CSS or SVG)

### 3. Our Story
- Timeline of relationship milestones
- Vertical timeline with alternating sides
- Each: date, event, small photo, description
- Soft sage and rose accents
- Champagne section background

### 4. Wedding Details
- 2-3 cards: Ceremony / Reception / After Party
- Each: venue name, time, address, map link
- Elegant icon for each event type
- Dress code note

### 4B. Venue Scene Annotation (NEW v2)
Một ảnh không gian venue thật (sảnh chính, khu tiệc ngoài trời, bàn tiệc) với
**hand-drawn hover annotation** — cảm giác như đang xem một cuốn sổ tay đám
cưới được chú thích bằng tay. Full spec:
`_shared/interactions/hand-drawn-annotation.md`.
- 4-6 hotspot, VD: "Sảnh chính 200 khách", "Khu tiệc ngoài trời", "Góc chụp
  ảnh cưới", "Bàn tiệc chính"
- Label dùng font `Caveat` — rất hợp với tông lãng mạn/thủ công của template
  này, gần như không cần điều chỉnh gì so với spec chung
- Mobile: tap-to-reveal, tự tắt sau 3s

### 5. Gallery — Circular Gallery
- Engagement photos in circular gallery
- Click to view full-size
- Rose gold decorative frame feel

### 6. Wedding Party
- Bridesmaids + Groomsmen cards
- Photo, name, role, fun description
- Grid layout

### 7. Registry
- Links to gift registries
- Styled as elegant cards with store logos
- Or: contribution fund info

### 8. RSVP Form
- Name, email, attending (yes/no), meal preference, +1 name, dietary notes
- "Submit RSVP" rose button
- Elegant form styling with thin borders

### 9. Footer
- Couple's names, date, hashtag (#NameAndName)
- "Made with ♥" — thin serif

## Prompt

Build a wedding/event planning website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Elegant, romantic, timeless design.

**Fonts:** Cormorant (display serif, 400-700 + italic) and Lato (body, 300-700).

**Key elements:** Falling Text for couple's names, Circular Gallery for photos, relationship timeline, RSVP form, floral/botanical decorative elements (CSS borders), rose-champagne-sage palette.

**Sections:** Nav (monogram center) → Hero (couple photo + falling text names) → Our Story (timeline) → Details (ceremony/reception cards), including a Venue Scene Annotation photo with 4-6 hover hotspots (wobbly SVG outline draws in 500ms → connector draws out 400ms → handwritten `Caveat` label fades in, see `_shared/interactions/hand-drawn-annotation.md`; tap-to-reveal on mobile) → Gallery (circular) → Wedding Party → Registry → RSVP Form → Footer.

**Color system:** Warm white `#FFFBF7`, rose `#BE185D`, champagne `#F5E6CC`, sage `#6B8E6B`, walnut text `#3D2B1F`.

## Required Assets
- `hero-couple` — Engagement/couple photo (fullscreen)
- `story-01` through `story-04` — Relationship milestone photos
- `annotation-scene` — 1 wide venue photo (main hall/outdoor area/reception table) with 4-6 distinct visible zones for hover hotspots (does NOT need background removal)
- `gallery-01` through `gallery-08` — Engagement photos
- `party-01` through `party-08` — Bridesmaids/groomsmen photos

## ReactBits Components Used
- **Falling Text** (`https://www.reactbits.dev/text-animations/falling-text`) — Names animation in hero.
- **Circular Gallery** (`https://www.reactbits.dev/components/circular-gallery`) — Engagement photo gallery.
