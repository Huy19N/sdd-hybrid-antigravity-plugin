---
id: portfolio-creative
name: "Creative Portfolio"
category: portfolio
tags:
  - portfolio
  - agency
  - creative
  - case-study
  - freelancer
  - designer
requires_transparent_images: false
color_palette:
  primary: "#2D2D2D"
  secondary: "#F5F0E8"
  accent: "#D4AF37"
  background: "#1A1A1A"
  text: "#F5F0E8"
  muted: "#8A8A8A"
reactbits_components:
  - name: "Magnet Lines"
    url: "https://www.reactbits.dev/animations/magnet-lines"
  - name: "Tilted Card"
    url: "https://www.reactbits.dev/components/tilted-card"
  - name: "Blur Text"
    url: "https://www.reactbits.dev/text-animations/blur-text"
best_for: "Portfolio cá nhân, agency sáng tạo, freelancer designer/developer — showcase dự án với hiệu ứng hover reveal và layout editorial"
fonts:
  display: "Playfair Display"
  body: "DM Sans"
---

# Template: Creative Portfolio

## Preview Description
A sophisticated dark portfolio with **editorial-style layout**, oversized serif
typography, and interactive hover reveals. Projects are displayed in an asymmetric
masonry grid where hovering reveals full-color imagery from monochrome. The cursor
has a magnetic effect near interactive elements. Text appears with a blur-to-sharp
animation on scroll. Gold accent color adds luxury feel against the dark charcoal
background. Minimal chrome — the work speaks for itself.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;700;900&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet" />
```

- **Display font**: `'Playfair Display', serif` — headings, project titles, hero text
- **Body font**: `'DM Sans', sans-serif` — descriptions, nav, labels

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#2D2D2D` (Charcoal) | Card backgrounds, secondary surfaces |
| Secondary | `#F5F0E8` (Cream) | Primary text, light accents |
| Accent | `#D4AF37` (Gold) | Hover states, active indicators, CTA |
| Background | `#1A1A1A` (Near Black) | Page background |
| Text | `#F5F0E8` (Cream) | Headlines, body text |
| Muted | `#8A8A8A` (Gray) | Captions, dates, secondary info |

## Layout Structure

### 1. Magnet Lines Background
- ReactBits Magnet Lines component as a subtle interactive background
- Lines follow cursor movement, creating depth
- Colors: `#2D2D2D` lines, low opacity
- `position: fixed; inset: 0; z-index: 0;`

### 2. Navigation (z-50)
- Fixed top, full-width
- Left: Name/Logo in Playfair Display
- Right: Minimal links — Work, About, Contact
- Gold dot indicator on active link
- `backdrop-blur-sm bg-[#1A1A1A]/80`
- Mobile: hamburger → fullscreen overlay menu with large typography

### 3. Hero Section
- Full viewport height
- Large headline using ReactBits **Blur Text** — text starts blurred, sharpens on load
- `text-5xl sm:text-7xl lg:text-[120px]`, Playfair Display, weight 900
- Example: "Design.\nDevelop.\nDeliver."
- Below: one-line tagline in DM Sans, muted color
- Scroll indicator: thin animated line at bottom center
- Minimal — no buttons, no images, just typography

### 4. Selected Work Grid
- Section header: "Selected Work" + project count
- **Asymmetric masonry grid** — alternating large and small cards
  - Row 1: One large card (60% width) + one small card (40%)
  - Row 2: Two equal cards (50/50)
  - Row 3: One small (40%) + one large (60%)
- Each project card:
  - Default: grayscale image, project title overlay at bottom
  - Hover: image transitions to full color, title slides up to reveal category + year
  - Use ReactBits **Tilted Card** for subtle 3D tilt on hover
  - `border: 1px solid #2D2D2D`, `rounded-lg`
  - Image `transition: filter 400ms ease`

### 5. About Section
- Two-column layout: text (left) + portrait photo (right)
- Left: short bio in Playfair Display, skills list
- Right: professional photo with gold border accent
- Skills displayed as minimal pills/tags
- Scroll-triggered stagger animation

### 6. Testimonials / Awards
- Horizontal marquee of awards or client testimonials
- Serif typography, oversized quotation marks in gold
- Auto-scrolling, pausable on hover

### 7. Contact Section
- Large headline: "Let's Work Together"
- Email address displayed large, hover → gold color
- Social links row
- Optional: minimal contact form

### 8. Footer
- Single line: © Year Name — Built with ♥
- Muted gray text

## State & Logic

```typescript
// Cursor position for magnetic effects
const [cursorPos, setCursorPos] = useState({ x: 0, y: 0 });

useEffect(() => {
  const handleMouseMove = (e: MouseEvent) => {
    setCursorPos({ x: e.clientX, y: e.clientY });
  };
  window.addEventListener('mousemove', handleMouseMove);
  return () => window.removeEventListener('mousemove', handleMouseMove);
}, []);

// Scroll-based blur text animation
// IntersectionObserver triggers blur → sharp transition

// Project hover state
const [hoveredProject, setHoveredProject] = useState<string | null>(null);

// Mobile menu
const [menuOpen, setMenuOpen] = useState(false);
```

## Prompt

Build a creative portfolio website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Dark editorial design with serif typography.

**Fonts:** Load Playfair Display (display, 400-900) and DM Sans (body, 400-700) from Google Fonts.

**Sections:**
1. **Magnet Lines background** — subtle interactive lines that follow cursor, `#2D2D2D` color, low opacity, fixed behind all content.
2. **Fixed navigation** — name (left, Playfair Display) + Work/About/Contact links (right, DM Sans). Gold dot on active link. Glassmorphism bg. Mobile: fullscreen overlay menu.
3. **Hero** — Full viewport. Huge Playfair Display text ("Design.\nDevelop.\nDeliver.") that animates from blurred to sharp on load. Tagline below in muted gray. Scroll indicator line at bottom.
4. **Selected Work** — Asymmetric masonry grid. Project cards: default grayscale images with title overlay. Hover: transition to full color + reveal category/year + subtle 3D tilt. Alternating large/small card sizes.
5. **About** — Two-column: bio text + skills tags (left), portrait photo with gold border (right). Stagger animation on scroll.
6. **Testimonial marquee** — Auto-scrolling quotes in serif font, oversized gold quotation marks.
7. **Contact** — Large "Let's Work Together" heading, oversized email link (hover → gold), social links.
8. **Footer** — Minimal single line.

**Color system:** Near-black bg `#1A1A1A`, charcoal surface `#2D2D2D`, cream text `#F5F0E8`, gold accent `#D4AF37`, muted gray `#8A8A8A`.

**Interactions:** Project cards grayscale→color on hover (400ms). Blur text animation on hero load. Scroll-triggered stagger animations via IntersectionObserver. Magnetic cursor effect near interactive elements.

## Required Assets
- `project-01` through `project-06` — Portfolio project screenshots/images
- `portrait` — Professional headshot/portrait for About section
- `client-logos` — Optional client/brand logos for social proof

## ReactBits Components Used
- **Magnet Lines** (`https://www.reactbits.dev/animations/magnet-lines`) — Interactive background lines following cursor movement.
- **Tilted Card** (`https://www.reactbits.dev/components/tilted-card`) — 3D tilt effect on project cards on hover.
- **Blur Text** (`https://www.reactbits.dev/text-animations/blur-text`) — Hero text blur-to-sharp reveal animation.
