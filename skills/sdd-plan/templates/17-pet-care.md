---
id: pet-care
name: "Pet Care"
version: 2
changelog:
  - "v2: added Grooming Salon Scene Annotation section (hand-drawn hover doodle overlay), uses shared interaction _shared/interactions/hand-drawn-annotation.md"
category: pet-care
uses_shared_interactions:
  - hand-drawn-annotation
tags:
  - pet
  - veterinary
  - animal
  - dog
  - cat
  - pet-shop
  - grooming
requires_transparent_images: true
color_palette:
  primary: "#9CAF88"
  secondary: "#FFDAB9"
  accent: "#E8845C"
  background: "#FFF8F0"
  surface: "#FFFFFF"
  text: "#4A3728"
  muted: "#8B7355"
reactbits_components:
  - name: "Sticker Peel"
    url: "https://www.reactbits.dev/animations/sticker-peel"
  - name: "Animated List"
    url: "https://www.reactbits.dev/components/animated-list"
best_for: "Thú cưng, pet shop, dịch vụ thú y, pet grooming, pet adoption — playful rounded UI, cute illustrations, warm tones"
fonts:
  display: "Baloo 2"
  body: "Quicksand"
---

# Template: Pet Care

## Preview Description
A warm, playful pet care website with **rounded everything**, soft peach-and-sage
color palette, **sticker peel** effects on pet cards, and **animated lists** for
services. Transparent-bg pet cutout images float on warm backgrounds. Typography
is friendly and approachable. The whole design feels like a warm hug for pet lovers.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#9CAF88` (Sage) | CTAs, borders, active |
| Secondary | `#FFDAB9` (Soft Peach) | Section backgrounds |
| Accent | `#E8845C` (Warm Orange) | Badges, highlights |
| Background | `#FFF8F0` (Warm Cream) | Page bg |
| Surface | `#FFFFFF` | Cards |
| Text | `#4A3728` (Cocoa) | Primary text |
| Muted | `#8B7355` | Secondary text |

## Layout Structure

### 1. Nav — rounded, playful
- Rounded pill navigation
- Paw print logo icon + brand name (Baloo 2)
- Services / Shop / Adoption / Blog
- "Book Grooming" sage CTA with rounded-full

### 2. Hero
- Split: text (left) + transparent-bg happy pet image (right)
- "Happy Pets, Happy Life" in Baloo 2
- Decorative paw prints and bones scattered (subtle)
- "Our Services" + "Adopt a Pet" buttons
- Peach section bg with soft gradient

### 3. Services
- Animated List of service cards (4-6)
- Each: cute icon + service name + description + price range
- Services: Grooming, Vet Checkup, Pet Hotel, Training, Walking
- Rounded-2xl cards, hover: sage border
- Sticker Peel on featured service

### 4. Featured Pets (Adoption)
- Grid of pet cards with transparent-bg pet photos
- Name, breed, age, temperament tags
- "Meet [Name]" button
- Heart/favorite toggle
- Sticker Peel effect on cards

### 5. About Us
- Team photos with pets
- Mission statement
- Warm, inviting imagery

### 5B. Grooming Salon Scene Annotation (NEW v2)
Một ảnh không gian salon/phòng khám thật (khu tắm gội, phòng chờ, phòng khám)
với **hand-drawn hover annotation** — hover vào từng khu vực để hiện label
viết tay giới thiệu. Full spec:
`_shared/interactions/hand-drawn-annotation.md`.
- 4-6 hotspot, VD: "Khu tắm gội", "Góc chờ có nước uống", "Phòng khám riêng",
  "Kệ đồ chơi cho bé"
- Giữ đúng phong cách playful/rounded của template — label dùng font viết tay
  `Caveat` như spec chung, không cần đổi để hợp tông (viết tay tự nhiên hợp
  với style ấm áp của pet-care)
- Mobile: tap-to-reveal, tự tắt sau 3s

### 6. Testimonials
- Pet owner + pet photos together
- "Our pet loves it here!" quotes
- Star ratings, rounded bubble cards

### 7. Pet Tips Blog
- 3 article cards: pet care tips
- Cute thumbnails, category badges

### 8. CTA — "Give Your Pet the Best Care" + booking form
### 9. Footer — playful, rounded elements, paw print decorations

## Prompt

Build a pet care website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Warm, playful, rounded design.

**Fonts:** Baloo 2 (display, 400-800) and Quicksand (body, 400-700).

**Key elements:** Rounded-2xl everything, Sticker Peel on pet/service cards, Animated List for services, transparent-bg pet cutout images, paw print decorative elements, warm peach-sage palette, playful but trustworthy.

**Sections:** Nav (pill style) → Hero (split with pet cutout) → Services (animated list) → Adoption Grid (sticker peel cards) → About, including a Grooming Salon Scene Annotation photo with 4-6 hover hotspots (wobbly SVG outline draws in 500ms → connector draws out 400ms → handwritten `Caveat` label fades in, see `_shared/interactions/hand-drawn-annotation.md`; tap-to-reveal on mobile) → Testimonials → Blog → CTA → Footer.

**Color system:** Warm cream bg `#FFF8F0`, sage `#9CAF88`, peach `#FFDAB9`, orange accent `#E8845C`, cocoa text `#4A3728`.

## Required Assets
- `hero-pet` — Happy pet (transparent background)
- `pet-adopt-01` through `pet-adopt-06` — Adoptable pets (transparent background)
- `team-01` through `team-03` — Team member + pet photos
- `annotation-scene` — 1 wide salon/clinic interior photo with 4-6 distinct visible zones for hover hotspots (does NOT need background removal)
- `service-icons` — Cute service icons (grooming, vet, hotel, training, walking)

## ReactBits Components Used
- **Sticker Peel** (`https://www.reactbits.dev/animations/sticker-peel`) — Peel effect on pet and service cards.
- **Animated List** (`https://www.reactbits.dev/components/animated-list`) — Staggered reveal for service listings.
