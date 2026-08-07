---
id: real-estate
name: "Real Estate"
version: 2
changelog:
  - "v2: added Property Scene Annotation section (hand-drawn hover doodle overlay), uses shared interaction _shared/interactions/hand-drawn-annotation.md"
category: real-estate
uses_shared_interactions:
  - hand-drawn-annotation
tags:
  - real-estate
  - property
  - housing
  - apartment
  - rental
  - listing
requires_transparent_images: false
color_palette:
  primary: "#2D5016"
  secondary: "#F5F5F0"
  accent: "#B8860B"
  background: "#FFFFFF"
  surface: "#F8F8F5"
  text: "#1C1C1C"
  muted: "#6B7280"
reactbits_components:
  - name: "Grid Distortion"
    url: "https://www.reactbits.dev/backgrounds/grid-distortion"
  - name: "Magic Bento"
    url: "https://www.reactbits.dev/components/magic-bento"
best_for: "Bất động sản, agency property, listing căn hộ/nhà, virtual tour — cần property cards, search filters, và gallery ảnh bất động sản"
fonts:
  display: "Fraunces"
  body: "Source Sans 3"
---

# Template: Real Estate

## Preview Description
A sophisticated real estate website with **bento grid** property showcases, an
interactive search/filter hero, and earthy green-and-gold color palette conveying
trust and luxury. Properties displayed in Magic Bento layout with varying card sizes.
Grid distortion background adds subtle depth to the hero. Clean, professional
typography with a warm serif display font balances approachability with authority.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,500;0,700;0,900;1,400&family=Source+Sans+3:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#2D5016` (Forest Green) | CTAs, badges, key elements |
| Secondary | `#F5F5F0` (Warm Gray) | Section backgrounds |
| Accent | `#B8860B` (Gold) | Price highlights, premium badges |
| Background | `#FFFFFF` | Page background |
| Surface | `#F8F8F5` | Card backgrounds |
| Text | `#1C1C1C` | Primary text |
| Muted | `#6B7280` | Descriptions, metadata |

## Layout Structure

### 1. Hero with Search
- Full-width hero with large property image background
- Grid Distortion overlay (subtle, on the image)
- Dark gradient overlay for text readability
- Centered search form:
  - Location input + Property type dropdown + Price range + "Search" button
  - Glassmorphism form container
- Below: "500+ Properties Listed" stat

### 2. Featured Properties (Magic Bento)
- ReactBits Magic Bento grid layout
- Varying card sizes: 1 large (2x2), 2 medium (1x2), 3 small (1x1)
- Each card: property image, overlay with price (gold), location, specs (beds/baths/sqft)
- Hover: subtle scale + shadow increase
- "View All Properties" CTA

### 3. Property Categories
- Horizontal cards: Apartments | Houses | Villas | Commercial
- Each: icon + name + property count
- Hover: green border accent

### 4. Why Choose Us
- 3 columns: Experience, Trust, Results
- Icon + metric + description
- Green icon accents

### 5. Featured Listing Detail
- Large split section for premium property
- Left: large image gallery (main + thumbnails)
- Right: property details, agent info, CTA buttons
- Gold "Premium" badge

### 5B. Property Scene Annotation (NEW v2)
Trong gallery của Featured Listing (mục 5), thêm 1 ảnh phòng khách/bếp/ban công
với **hand-drawn hover annotation** thay cho ảnh tĩnh thông thường — hover vào
từng chi tiết thật trong phòng để "khám phá" thay vì đọc mô tả text. Full spec:
`_shared/interactions/hand-drawn-annotation.md`.
- 4-6 hotspot đặt tại các điểm bán hàng thực sự của căn nhà (VD: "Sàn gỗ tự
  nhiên", "Bếp mở liên thông", "View ban công hướng Nam", "Trần cao 3.2m")
- Dùng đúng lúc muốn nhấn mạnh **tính năng** thay vì chỉ show ảnh đẹp — khác
  với ảnh thumbnail gallery vẫn giữ nguyên cho các phòng còn lại
- Mobile: tap-to-reveal, tự tắt sau 3s

### 6. Testimonials
- Cards with client photo, quote, property purchased
- Clean white cards with subtle shadow

### 7. CTA
- "Find Your Dream Home" + search bar
- Forest green background, white text

### 8. Footer
- Company info, quick links, contact, social
- Real estate license info

## Prompt

Build a real estate website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Professional, trustworthy design with earthy tones.

**Fonts:** Fraunces (display serif, 400-900) and Source Sans 3 (body, 300-700).

**Sections:** Hero with property search form (glassmorphism overlay on large image with grid distortion) → Featured Properties (Magic Bento grid with varying card sizes) → Property Categories (horizontal cards) → Why Choose Us (3-column stats) → Premium Listing spotlight, including a Property Scene Annotation room photo with 4-6 hover hotspots (wobbly SVG outline draws in 500ms → connector draws out 400ms → handwritten label fades in, see `_shared/interactions/hand-drawn-annotation.md`; tap-to-reveal on mobile) → Testimonials → CTA → Footer.

**Color system:** White bg, warm gray sections `#F5F5F0`, forest green `#2D5016`, gold accent `#B8860B`, dark text `#1C1C1C`.

## Required Assets
- `hero-property` — Large hero background property image
- `property-01` through `property-06` — Property listing photos
- `premium-property-01` through `premium-property-04` — Premium listing gallery
- `annotation-scene` — 1 wide room photo (living room/kitchen/balcony) with 4-6 distinct visible features for hover hotspots (does NOT need background removal — keep as a real photographic scene)
- `agent-portrait` — Real estate agent headshot

## ReactBits Components Used
- **Grid Distortion** (`https://www.reactbits.dev/backgrounds/grid-distortion`) — Subtle distortion effect on hero background.
- **Magic Bento** (`https://www.reactbits.dev/components/magic-bento`) — Varying-size grid layout for property showcases.
