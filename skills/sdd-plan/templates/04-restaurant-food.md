---
id: restaurant-food
name: "Restaurant & Food"
version: 2
changelog:
  - "v2: added Ambiance Scene Annotation section (hand-drawn hover doodle overlay), uses shared interaction _shared/interactions/hand-drawn-annotation.md"
category: food-beverage
uses_shared_interactions:
  - hand-drawn-annotation
tags:
  - restaurant
  - food
  - cafe
  - tea
  - coffee
  - menu
  - dining
  - bubble-tea
requires_transparent_images: true
color_palette:
  primary: "#3C2415"
  secondary: "#F5E6D3"
  accent: "#C67B5C"
  background: "#FDF8F3"
  surface: "#FFFFFF"
  text: "#3C2415"
  muted: "#8B7355"
reactbits_components:
  - name: "Circular Gallery"
    url: "https://www.reactbits.dev/components/circular-gallery"
  - name: "Sticker Peel"
    url: "https://www.reactbits.dev/animations/sticker-peel"
best_for: "Nhà hàng, quán café, trà sữa, bakery, dịch vụ F&B — cần menu đẹp, gallery ảnh đồ ăn với hiệu ứng parallax, và ảnh sản phẩm tách nền"
fonts:
  display: "Cormorant Garamond"
  body: "Outfit"
  handwritten: "Caveat"
---

# Template: Restaurant & Food

## Preview Description
A warm, appetizing restaurant/café website with **parallax food photography**,
transparent cutout dishes floating on cream backgrounds, and an interactive menu
with category tabs. Elegant serif typography meets modern sans-serif body text.
Featured dishes are presented with transparent backgrounds in a circular gallery,
giving a premium editorial food magazine feel. Warm earth-tone color palette
evokes comfort and craftsmanship.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Outfit:wght@300;400;500;600;700&family=Caveat:wght@500;600;700&display=swap" rel="stylesheet" />
```

- **Display font**: `'Cormorant Garamond', serif` — headings, menu item names
- **Body font**: `'Outfit', sans-serif` — descriptions, prices, nav
- **Handwritten font**: `'Caveat', cursive` — annotation labels only (section 3B)

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#3C2415` (Espresso) | Headlines, primary text |
| Secondary | `#F5E6D3` (Cream) | Section backgrounds, cards |
| Accent | `#C67B5C` (Terracotta) | CTAs, prices, highlights |
| Background | `#FDF8F3` (Warm White) | Page background |
| Surface | `#FFFFFF` (White) | Card backgrounds |
| Text | `#3C2415` (Espresso) | Primary text |
| Muted | `#8B7355` (Warm Gray) | Descriptions, secondary text |

## Layout Structure

### 1. Navigation
- Fixed top, transparent → cream bg on scroll
- Logo/brand name center (Cormorant Garamond, italic)
- Left: Menu, About | Right: Reservations, Contact
- Mobile: centered logo + hamburger
- `transition: background-color 300ms`
- CTA button: "Reserve a Table" in accent color

### 2. Hero Section
- Split layout: text (left 40%) + food image (right 60%)
- Left: Large serif headline, tagline, "View Menu" + "Reserve" buttons
- Right: Large transparent-bg hero dish floating on a subtle colored circle
  - Subtle parallax: dish moves slightly on scroll
  - Decorative elements: small herb/spice illustrations scattered
- Background: warm white with faint grain texture

### 3. Featured Dishes (Circular Gallery)
- Section title: "Signature Dishes" in Cormorant Garamond
- Use ReactBits **Circular Gallery** for rotating dish showcase
- Each dish: transparent-bg food image + name + price
- 4-6 featured items
- Cursor interaction: dishes rotate with mouse movement
- Below gallery: "View Full Menu" CTA

### 3B. Ambiance Scene Annotation (NEW v2)
Full-bleed atmospheric interior photo (dining room, counter, or bakery display)
with **hand-drawn hover annotations** — hover over highlighted zones in the
photo to reveal a wobbly white outline + curved connector line + handwritten
label, doodle/sticker style. See full technical spec:
`_shared/interactions/hand-drawn-annotation.md`.
- Section title (small, top-left of photo): "Không gian của chúng tôi" / "Our
  Space" — Outfit font, uppercase, tracking-wide.
- 4-6 hotspots placed over genuinely interesting elements in the photo (a
  pastry display case, a reading corner, a signature lamp, table setting) —
  each with a short handwritten label (1-3 từ, VD: "Bánh mới ra lò", "Góc đọc
  sách", "Ánh sáng ấm").
- On mobile: tap-to-reveal instead of hover, auto-dismiss after 3s.
- This section replaces a plain static "gallery photo" with an interactive one
  — use it as an alternative to, or right before, the Gallery/Instagram Grid
  section if you want the interior story told once instead of twice.

### 4. About / Story Section
- Two-column: large atmospheric photo (left) + story text (right)
- Serif pull-quote highlighted in accent color
- "Since [year]" establishment badge
- Parallax on the photo

### 5. Menu Section
- Category tabs: Appetizers | Mains | Desserts | Drinks
- Tab underline indicator animates between tabs
- Each menu item: name (serif) + description + price
  - Optional: small food thumbnail
- Items stagger-animate on tab switch
- Background: cream/secondary color

### 6. Gallery / Instagram Grid
- Masonry grid of food/ambiance photos
- Hover: subtle zoom + overlay with dish name
- "Follow us @brandname" link to Instagram
- Use Sticker Peel effect on select images

### 7. Reservation CTA
- Full-width section with atmospheric background image (dimmed overlay)
- Large serif text: "Reserve Your Table"
- Date picker + time picker + party size + "Book Now" button
- Or: phone number + email displayed prominently

### 8. Location & Hours
- Map embed (or styled static map image) on one side
- Opening hours table on the other
- Address, phone, email

### 9. Footer
- Logo, social links, quick nav links
- "© [year] Restaurant Name" — warm gray text

## State & Logic

```typescript
// Menu tab state
const [activeTab, setActiveTab] = useState('mains');
const menuCategories = ['appetizers', 'mains', 'desserts', 'drinks'];

// Parallax effect
const [scrollY, setScrollY] = useState(0);
useEffect(() => {
  const handleScroll = () => setScrollY(window.scrollY);
  window.addEventListener('scroll', handleScroll, { passive: true });
  return () => window.removeEventListener('scroll', handleScroll);
}, []);

// Nav background on scroll
const [navScrolled, setNavScrolled] = useState(false);
useEffect(() => {
  const handleScroll = () => setNavScrolled(window.scrollY > 50);
  window.addEventListener('scroll', handleScroll, { passive: true });
  return () => window.removeEventListener('scroll', handleScroll);
}, []);

// Gallery lightbox
const [lightboxImage, setLightboxImage] = useState<string | null>(null);
```

## Prompt

Build a restaurant/café website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Warm, editorial food design with serif display typography.

**Fonts:** Load Cormorant Garamond (display, 400-700) and Outfit (body, 300-700) from Google Fonts.

**Sections:**
1. **Fixed nav** — transparent → cream on scroll. Center logo (italic serif). Left/right nav links. "Reserve a Table" accent CTA. Mobile hamburger.
2. **Hero** — Split: large serif headline + CTAs (left 40%), transparent-bg hero dish on a colored circle with parallax (right 60%). Warm white bg with faint grain.
3. **Featured Dishes** — "Signature Dishes" with circular gallery component. 4-6 dishes with transparent-bg images, names, prices. Rotates with mouse interaction.
3B. **Ambiance Scene Annotation** — full-bleed interior photo with 4-6 hover hotspots. Each hotspot: wobbly white SVG outline draws in around the zone (500ms), then a curved connector line draws out (400ms), then a handwritten-font label fades in (Caveat). See `_shared/interactions/hand-drawn-annotation.md` for exact SVG/animation spec. Tap-to-reveal on mobile, auto-dismiss 3s.
4. **About** — Two-column: atmospheric photo (left, parallax) + story text (right). Serif pull-quote in terracotta.
5. **Menu** — Tab navigation (Appetizers/Mains/Desserts/Drinks). Animated tab indicator. Each item: serif name + description + price. Stagger animation on tab switch. Cream bg.
6. **Gallery** — Masonry grid, hover zoom + overlay. Sticker peel effect on select images.
7. **Reservation CTA** — Full-width with dimmed background image. Large serif "Reserve Your Table" + booking form (date/time/party size).
8. **Location** — Map + hours table + contact info.
9. **Footer** — Logo, social links, nav, copyright.

**Color system:** Warm white bg `#FDF8F3`, cream `#F5E6D3`, espresso text `#3C2415`, terracotta accent `#C67B5C`, warm gray muted `#8B7355`.

**Key interactions:** Parallax on hero dish and about photo. Menu tab switch with staggered list animation. Gallery hover zoom. Nav background transition on scroll. All sections reveal on scroll via IntersectionObserver.

## Required Assets
- `hero-dish` — Main signature dish (transparent background)
- `dish-01` through `dish-06` — Featured menu items (transparent background)
- `restaurant-interior` — Atmospheric interior/ambiance photo
- `ambiance-scene` — Wide interior/counter photo with 4-6 distinct visual zones for hover annotation hotspots (does NOT need background removal — this is a full photographic scene, not a cutout)
- `food-gallery-01` through `food-gallery-06` — Food photography for gallery
- `herb-illustrations` — Small decorative herb/spice illustrations (optional)

## ReactBits Components Used
- **Circular Gallery** (`https://www.reactbits.dev/components/circular-gallery`) — Rotating dish showcase in Featured Dishes section.
- **Sticker Peel** (`https://www.reactbits.dev/animations/sticker-peel`) — Peel effect on select gallery images for playful interaction.
