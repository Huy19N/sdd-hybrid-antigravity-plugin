---
id: fashion-ecommerce
name: "Fashion E-Commerce"
category: fashion
tags:
  - fashion
  - clothing
  - apparel
  - lookbook
  - style
  - boutique
  - accessories
requires_transparent_images: true
color_palette:
  primary: "#1A1A1A"
  secondary: "#FFFFF0"
  accent: "#FFB6C1"
  background: "#FAFAFA"
  surface: "#FFFFFF"
  text: "#1A1A1A"
  muted: "#6B7280"
reactbits_components:
  - name: "Morph Slider"
    url: "https://www.reactbits.dev/components/morph-slider"
  - name: "Infinite Menu"
    url: "https://www.reactbits.dev/components/infinite-menu"
best_for: "Cửa hàng thời trang, boutique, lookbook, phụ kiện — editorial product display với ảnh model, quick-view cards, và infinite scroll collections"
fonts:
  display: "Bodoni Moda"
  body: "Manrope"
---

# Template: Fashion E-Commerce

## Preview Description
A sleek, editorial fashion e-commerce site with a **morph slider** hero showcasing
seasonal lookbook images, infinite scrolling product collections, and clean
typographic hierarchy using a serif display font. Products feature transparent
backgrounds for a float-on-white effect. The design balances high-fashion editorial
aesthetics with practical e-commerce functionality — quick-view product cards,
size selectors, and add-to-cart interactions.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,500;0,700;0,900;1,400&family=Manrope:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
```

- **Display font**: `'Bodoni Moda', serif` — headings, brand, prices
- **Body font**: `'Manrope', sans-serif` — descriptions, nav, buttons

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#1A1A1A` (Noir) | Text, buttons, nav |
| Secondary | `#FFFFF0` (Ivory) | Hero backgrounds, accent sections |
| Accent | `#FFB6C1` (Blush) | Sale badges, highlights, hover |
| Background | `#FAFAFA` (Off White) | Page background |
| Surface | `#FFFFFF` (White) | Product cards |
| Text | `#1A1A1A` (Noir) | Primary text |
| Muted | `#6B7280` (Gray) | Descriptions, stock info |

## Layout Structure

### 1. Navigation (z-50)
- Full-width, `bg-white`, `border-bottom: 1px solid #E5E5E5`
- Logo center (Bodoni Moda, italic, large)
- Left: Hamburger menu → fullscreen nav overlay with categories
- Right: Search icon + Heart (wishlist) + Cart (item count badge)
- Sticky on scroll
- Announcement bar above: "Free shipping on orders over $100" — blush bg

### 2. Hero — Morph Slider
- Full-width, `height: 80vh`
- ReactBits **Morph Slider** with 3-4 lookbook campaign images
- Each slide: full-bleed image + overlaid text
  - Collection name (Bodoni Moda, `text-4xl sm:text-6xl`, white/black)
  - Season tag
  - "Shop Now" button
- Smooth morphing transition between slides
- Auto-advance every 5s, manual navigation dots at bottom

### 3. Category Bar
- Horizontal scroll row of category pills
- Categories: New Arrivals | Dresses | Tops | Bottoms | Accessories | Sale
- Active category: underline in noir
- Smooth scroll behavior

### 4. Product Grid
- Responsive grid: 4 cols (desktop), 2 cols (mobile)
- Each product card:
  - Product image (transparent bg on white card)
  - On hover: second image (alternate angle) crossfades in
  - Product name (Manrope, `font-medium`)
  - Price (Bodoni Moda) | Original price strikethrough if on sale
  - Blush "Sale" badge if discounted
  - Quick-view button appears on hover (bottom of image)
  - Heart/wishlist icon (top-right corner on hover)
- Load more: "View All" button or infinite scroll
- Use ReactBits **Infinite Menu** pattern for smooth infinite browsing

### 5. Featured Collection
- Full-width editorial banner
- Split: large lifestyle image (70%) + text block (30%)
- Collection name in large Bodoni Moda
- "Explore Collection" CTA with arrow

### 6. Trending / Best Sellers
- Horizontal scrollable product row
- Draggable on mobile and desktop
- Category label above: "Trending Now"
- Same card style as product grid

### 7. Brand Story Strip
- Full-width, ivory background
- Three columns: icon + stat + label
  - "100% Sustainable" / "Free Returns" / "Handcrafted"
- Serif typography for labels

### 8. Newsletter Signup
- Minimal section: headline + email input + submit
- "Join our community" — Bodoni Moda, italic
- Input: minimal underline style
- Blush accent on submit button

### 9. Footer
- 4 columns: Shop, About, Support, Follow Us
- Social icons row
- Payment method icons
- Copyright in muted gray

## State & Logic

```typescript
// Cart state
const [cartItems, setCartItems] = useState<CartItem[]>([]);
const cartCount = cartItems.reduce((sum, item) => sum + item.quantity, 0);

// Wishlist
const [wishlist, setWishlist] = useState<Set<string>>(new Set());

// Quick view modal
const [quickViewProduct, setQuickViewProduct] = useState<Product | null>(null);

// Product image hover
const [hoveredProduct, setHoveredProduct] = useState<string | null>(null);

// Category filter
const [activeCategory, setActiveCategory] = useState('all');

// Mobile menu
const [menuOpen, setMenuOpen] = useState(false);

// Search overlay
const [searchOpen, setSearchOpen] = useState(false);
```

## Prompt

Build a fashion e-commerce website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Clean editorial design with serif display typography.

**Fonts:** Load Bodoni Moda (display, 400-900 + italic) and Manrope (body, 300-700) from Google Fonts.

**Sections:**
1. **Announcement bar** — blush bg, free shipping message.
2. **Sticky nav** — center logo (Bodoni italic), left hamburger (fullscreen overlay nav), right search/wishlist/cart icons (cart has item count badge).
3. **Hero** — 80vh morph slider with 3-4 lookbook images. Each slide: full-bleed image + collection name overlay + "Shop Now" button. Auto-advance 5s.
4. **Category bar** — horizontal scroll pills (New Arrivals/Dresses/Tops/etc). Active underline.
5. **Product grid** — 4-col desktop, 2-col mobile. Cards: transparent-bg product image, hover shows alternate image + quick-view button + wishlist heart. Price in Bodoni Moda. Sale badge in blush.
6. **Featured collection** — editorial split: lifestyle image (70%) + text + CTA (30%).
7. **Trending row** — horizontal draggable product scroll.
8. **Brand values strip** — 3 columns on ivory bg: sustainability, returns, craftsmanship.
9. **Newsletter** — italic Bodoni headline + minimal email input + blush submit button.
10. **Footer** — 4-col links, social icons, payment methods.

**Color system:** Off-white bg `#FAFAFA`, noir text `#1A1A1A`, ivory sections `#FFFFF0`, blush accent `#FFB6C1`, gray muted `#6B7280`.

**Interactions:** Morph slider auto-advance + manual dots. Product card image swap on hover (300ms crossfade). Quick-view modal. Wishlist toggle with heart animation. Smooth category scroll. Infinite scroll or "View All" for products.

## Required Assets
- `lookbook-01` through `lookbook-04` — Campaign/lookbook lifestyle images
- `product-01` through `product-12` — Product images (transparent background)
- `product-01-alt` through `product-12-alt` — Alternate angle product images
- `lifestyle-editorial` — Large editorial lifestyle image for featured collection
- `brand-icon-sustainable`, `brand-icon-returns`, `brand-icon-crafted` — Brand value icons

## ReactBits Components Used
- **Morph Slider** (`https://www.reactbits.dev/components/morph-slider`) — Hero section lookbook slider with morphing transitions between slides.
- **Infinite Menu** (`https://www.reactbits.dev/components/infinite-menu`) — Inspiration for infinite scrolling product browsing pattern.
