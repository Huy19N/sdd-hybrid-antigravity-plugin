---
id: product-carousel
name: "Product Carousel Showcase"
category: product-store
tags:
  - e-commerce
  - carousel
  - product
  - showcase
  - retail
  - shop
requires_transparent_images: true
color_palette:
  primary: "#F4845F"
  secondary: "#6BBF7A"
  accent: "#E882B4"
  background: "#F4845F"
  text: "#FFFFFF"
  panel: "#F79B7F"
  variations:
    - bg: "#F4845F"
      panel: "#F79B7F"
    - bg: "#6BBF7A"
      panel: "#85CC92"
    - bg: "#E882B4"
      panel: "#ED9DC4"
    - bg: "#6EB5FF"
      panel: "#8DC4FF"
reactbits_components:
  - name: "Depth Carousel"
    url: "https://www.reactbits.dev/components/depth-carousel"
  - name: "Sticker Peel"
    url: "https://www.reactbits.dev/animations/sticker-peel"
best_for: "Cửa hàng bán sản phẩm vật lý cần hero section nổi bật với ảnh sản phẩm tách nền xoay carousel — trà sữa, figurines, giày dép, mỹ phẩm, đồ chơi"
fonts:
  display: "Anton"
  body: "Inter"
---

# Template: Product Carousel Showcase

## Preview Description
A bold, full-viewport hero section featuring a **4-item character/product carousel**
with transparent cutout images floating on a vibrant, color-shifting background.
The active product dominates center screen at large scale while supporting items
sit smaller to the left, right, and behind — creating a layered depth effect.
Giant ghost typography sits behind the products. Navigation arrows rotate items
with a smooth 650ms crossfade. Each product has its own unique background color
that transitions seamlessly. A grain texture overlay adds premium print-like feel.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

- **Display font** (ghost text, CTA link): `'Anton', sans-serif`
- **Body font** (labels, descriptions, buttons): `'Inter', sans-serif`

## Color Palette

Each carousel item has its own background + panel color pair. When the active item
changes, the entire viewport background transitions to that item's color.

| Role | Color | Usage |
|---|---|---|
| Item 1 BG | `#F4845F` (Coral) | Warm, energetic — default active state |
| Item 1 Panel | `#F79B7F` | Lighter variant for secondary elements |
| Item 2 BG | `#6BBF7A` (Mint) | Fresh, natural |
| Item 2 Panel | `#85CC92` | Lighter variant |
| Item 3 BG | `#E882B4` (Pink) | Playful, feminine |
| Item 3 Panel | `#ED9DC4` | Lighter variant |
| Item 4 BG | `#6EB5FF` (Sky) | Calm, trustworthy |
| Item 4 Panel | `#8DC4FF` | Lighter variant |
| Text | `#FFFFFF` | All text is white on colored backgrounds |

## Layout Structure

### 1. Grain Overlay (z-50)
- `position: absolute; inset: 0; pointer-events: none;`
- SVG `fractalNoise` filter: `baseFrequency=0.9`, `numOctaves=4`
- Inner SVG opacity: `0.08`, container opacity: `0.4`
- `backgroundSize: 200px 200px`, repeat
- Creates a subtle film grain / print texture effect

### 2. Giant Ghost Text (z-2)
- Text: **"3D SHAPE"** (or customize to product category)
- Font: `Anton`, weight 900, uppercase
- `fontSize: clamp(90px, 28vw, 380px)`
- Color: white, opacity: 1, positioned behind products
- `top: 18%`, centered horizontally
- `letterSpacing: -0.02em`, `whiteSpace: nowrap`

### 3. Top-Left Brand Label (z-60)
- Text: **Brand name** in uppercase
- `text-xs font-semibold`, white, opacity 0.9
- `letterSpacing: 0.18em`
- Position: `top-6 left-4 sm:left-8`

### 4. Carousel Layer (z-3)
- 4 product images, each `position: absolute`
- `aspectRatio: 0.6 / 1`
- **All product images must be transparent/cutout PNGs**
- `<img>` with `objectFit: contain; objectPosition: bottom center;`
- Preload all 4 images on mount via `new Image()`

#### Per-Role Positioning:
| Role | Transform | Blur | Opacity | z-Index | Left | Height | Bottom |
|---|---|---|---|---|---|---|---|
| **Center** | `translateX(-50%) scale(1.68)` | none | 1 | 20 | `50%` | `92%` | `0` |
| **Left** | `translateX(-50%) scale(1)` | `2px` | 0.85 | 10 | `30%` | `28%` | `12%` |
| **Right** | `translateX(-50%) scale(1)` | `2px` | 0.85 | 10 | `70%` | `28%` | `12%` |
| **Back** | `translateX(-50%) scale(1)` | `4px` | 1 | 5 | `50%` | `22%` | `12%` |

#### Mobile Overrides (`< 640px`):
| Role | Left | Height | Bottom | Scale (center) |
|---|---|---|---|---|
| Center | `50%` | `60%` | `22%` | `1.25` |
| Left | `20%` | `16%` | `32%` | - |
| Right | `80%` | `16%` | `32%` | - |
| Back | `50%` | `13%` | `32%` | - |

### 5. Bottom-Left Info Block (z-60)
- Position: `bottom-6 left-4 sm:bottom-20 sm:left-24`
- `maxWidth: 320px`
- **Title**: Brand/product line name, bold uppercase, tracking-widest
  - `mb-2 sm:mb-3 text-base sm:text-[22px]`, white, opacity 0.95
- **Description** (hidden on mobile): Product tagline or testimonial
  - `text-xs sm:text-sm`, white, opacity 0.85, `lineHeight: 1.6`
- **Nav Buttons**: Two circular arrow buttons
  - `w-12 h-12 sm:w-16 sm:h-16`
  - Transparent bg, 2px white border, white arrow icons
  - Hover: `scale(1.08)` + `bg rgba(255,255,255,0.12)`
  - Uses `ArrowLeft` and `ArrowRight` from `lucide-react`

### 6. Bottom-Right CTA Link (z-60)
- Position: `bottom-6 right-4 sm:bottom-20 sm:right-10`
- Text: **"DISCOVER IT"** (or custom CTA)
- Font: `Anton`, `fontSize: clamp(20px, 4vw, 56px)`
- White, opacity 0.95 → 1 on hover
- Followed by `ArrowRight` icon

## State & Logic

```typescript
// State
const [activeIndex, setActiveIndex] = useState(0); // 0-3
const [isAnimating, setIsAnimating] = useState(false);
const [isMobile, setIsMobile] = useState(window.innerWidth < 640);

// Resize listener
useEffect(() => {
  const handleResize = () => setIsMobile(window.innerWidth < 640);
  window.addEventListener('resize', handleResize);
  return () => window.removeEventListener('resize', handleResize);
}, []);

// Preload images on mount
useEffect(() => {
  IMAGES.forEach(item => { const img = new Image(); img.src = item.src; });
}, []);

// Navigation
const navigate = (direction: 'next' | 'prev') => {
  if (isAnimating) return;
  setIsAnimating(true);
  setActiveIndex(prev =>
    direction === 'next' ? (prev + 1) % 4 : (prev + 3) % 4
  );
  setTimeout(() => setIsAnimating(false), 650);
};

// Role assignment
const center = activeIndex;
const left = (activeIndex + 3) % 4;
const right = (activeIndex + 1) % 4;
const back = (activeIndex + 2) % 4;
```

## Prompt

Build a single full-viewport hero section in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. The component is a product carousel showcase.

**Fonts:** Load Anton (display) and Inter (body) from Google Fonts in `index.html`.

**Image data structure:**
```ts
const IMAGES = [
  { src: '/assets/no-bg/product-01.png', bg: '#F4845F', panel: '#F79B7F' },
  { src: '/assets/no-bg/product-02.png', bg: '#6BBF7A', panel: '#85CC92' },
  { src: '/assets/no-bg/product-03.png', bg: '#E882B4', panel: '#ED9DC4' },
  { src: '/assets/no-bg/product-04.png', bg: '#6EB5FF', panel: '#8DC4FF' },
];
```

**Outer container:** `backgroundColor` transitions with active item's `bg` color over `650ms cubic-bezier(0.4,0,0.2,1)`. Full viewport height, `overflow: hidden`.

**Layers (back to front):**
1. Grain overlay — SVG fractalNoise texture, subtle film grain effect.
2. Giant ghost text — Huge Anton text behind products, white, full-width.
3. Carousel — 4 product images with role-based positioning (center=large, left/right=small+blurred, back=smallest+most-blurred). All transitions 650ms.
4. Bottom-left: brand title + description (hidden mobile) + two circular nav arrow buttons.
5. Bottom-right: CTA link with arrow icon, Anton font.
6. Top-left: brand label, small uppercase.

**Behavior:** Clicking arrows rotates roles. Background color, positions, scales, blurs, and opacities all crossfade simultaneously. Animation lock prevents rapid clicks. Responsive breakpoint at 640px for mobile layout adjustments.

## Required Assets
- `product-01` — Main product image (will be background-removed)
- `product-02` — Second product variant
- `product-03` — Third product variant
- `product-04` — Fourth product variant
- All products should be photographed/generated with clean backgrounds for easy removal

## ReactBits Components Used
- **Depth Carousel** (`https://www.reactbits.dev/components/depth-carousel`) — Reference for the depth/layering effect. The template implements a custom version with 4 role positions instead of using the component directly.
- **Sticker Peel** (`https://www.reactbits.dev/animations/sticker-peel`) — Optional: add sticker peel effect on product cards in secondary pages/sections.
