---
id: travel-tourism
name: "Travel & Tourism"
category: travel
tags:
  - travel
  - tourism
  - hotel
  - booking
  - destination
  - adventure
  - vacation
requires_transparent_images: false
color_palette:
  primary: "#0077B6"
  secondary: "#E9C46A"
  accent: "#F4845F"
  background: "#FFFFFF"
  surface: "#F0F7FF"
  text: "#1B2A4A"
  muted: "#6B7280"
reactbits_components:
  - name: "Morph Slider"
    url: "https://www.reactbits.dev/components/morph-slider"
  - name: "Ripple Distortion"
    url: "https://www.reactbits.dev/animations/ripple-distortion"
best_for: "Du lịch, tour, khách sạn, trải nghiệm du lịch, booking platform — hero video, destination cards, booking widget"
fonts:
  display: "Unbounded"
  body: "Nunito Sans"
---

# Template: Travel & Tourism

## Preview Description
An immersive travel website with **fullscreen hero morph slider** of breathtaking
destinations, **ripple distortion** interactive effect on images, and an integrated
booking search widget. Ocean blues and golden sand accents evoke wanderlust.
Destination cards with hover zoom and quick-book functionality.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;600;700;900&family=Nunito+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#0077B6` (Ocean Blue) | CTAs, headers, active |
| Secondary | `#E9C46A` (Sand Gold) | Accents, ratings, prices |
| Accent | `#F4845F` (Coral) | Badges, alerts, highlights |
| Background | `#FFFFFF` | Page bg |
| Surface | `#F0F7FF` (Sky Tint) | Cards, sections |
| Text | `#1B2A4A` (Navy) | Primary text |
| Muted | `#6B7280` | Descriptions |

## Layout Structure

### 1. Hero — Morph Slider
- Fullscreen destination images with morphing transitions
- Overlay: destination name + "Explore" button
- Booking search bar floating at bottom:
  - Where (autocomplete) + When (date range) + Travelers (counter) + Search
  - Glassmorphism container

### 2. Popular Destinations
- 6 cards with Ripple Distortion on image hover
- Each: destination image, name, country flag, "from $XXX", rating
- Hover: ripple effect + overlay with "Book Now"

### 3. Featured Experiences
- 3 large horizontal cards: Adventure / Cultural / Relaxation
- Parallax images, category badge, description

### 4. Why Travel With Us
- 4 trust pillars: Best Price / 24/7 Support / Verified Reviews / Flexible Booking
- Icons + descriptions

### 5. Deals & Offers
- Countdown deal banner
- Special package cards with discount badges

### 6. Traveler Stories
- Photo + quote + destination
- Star ratings

### 7. Newsletter
- "Get Travel Inspiration" + email signup
- Beach/travel illustration bg

### 8. Footer — destinations list, company info, social, certifications

## Prompt

Build a travel/tourism website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Immersive, wanderlust-inducing design.

**Fonts:** Unbounded (display, 400-900) and Nunito Sans (body, 400-700).

**Key elements:** Fullscreen morph slider hero with booking search, ripple distortion on destination images, booking widget (where/when/travelers/search), countdown deal timer.

**Sections:** Hero (morph slider + booking search) → Destinations (ripple cards) → Experiences (parallax cards) → Trust Pillars → Deals → Testimonials → Newsletter → Footer.

**Color system:** White bg, sky surface `#F0F7FF`, ocean `#0077B6`, gold `#E9C46A`, coral `#F4845F`, navy text `#1B2A4A`.

## Required Assets
- `destination-01` through `destination-06` — Destination landscape photos
- `experience-adventure`, `experience-cultural`, `experience-relaxation` — Experience category images
- `hero-slides-01` through `hero-slides-04` — Fullscreen hero destination images

## ReactBits Components Used
- **Morph Slider** (`https://www.reactbits.dev/components/morph-slider`) — Fullscreen hero destination slider.
- **Ripple Distortion** (`https://www.reactbits.dev/animations/ripple-distortion`) — Interactive ripple effect on destination images.
