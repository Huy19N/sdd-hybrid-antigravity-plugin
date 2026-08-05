---
id: saas-landing
name: "SaaS Landing Page"
category: saas
tags:
  - saas
  - software
  - landing-page
  - pricing
  - features
  - b2b
  - dashboard
requires_transparent_images: false
color_palette:
  primary: "#4F46E5"
  secondary: "#7C3AED"
  accent: "#06B6D4"
  background: "#0F172A"
  surface: "#1E293B"
  text: "#F8FAFC"
  muted: "#94A3B8"
reactbits_components:
  - name: "Aurora"
    url: "https://www.reactbits.dev/backgrounds/aurora"
  - name: "Shiny Text"
    url: "https://www.reactbits.dev/text-animations/shiny-text"
  - name: "Animated List"
    url: "https://www.reactbits.dev/components/animated-list"
best_for: "Landing page cho sản phẩm SaaS, phần mềm B2B/B2C, ứng dụng web — cần hero section với gradient mesh, feature cards, pricing table, testimonials"
fonts:
  display: "Plus Jakarta Sans"
  body: "Inter"
---

# Template: SaaS Landing Page

## Preview Description
A premium dark-mode SaaS landing page with an **aurora gradient mesh background**,
animated feature cards that reveal on scroll, a toggle-able pricing table with
monthly/annual switch, social proof testimonials, and smooth micro-interactions
throughout. The design feels modern, professional, and data-driven — perfect for
B2B/B2C software products.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
```

- **Display font** (headings, hero text): `'Plus Jakarta Sans', sans-serif`
- **Body font** (paragraphs, labels): `'Inter', sans-serif`

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#4F46E5` (Indigo) | CTAs, active states, links |
| Secondary | `#7C3AED` (Violet) | Gradient endpoints, hover states |
| Accent | `#06B6D4` (Cyan) | Badges, highlights, sparkle effects |
| Background | `#0F172A` (Dark Navy) | Page background |
| Surface | `#1E293B` (Slate) | Card backgrounds, input fields |
| Text | `#F8FAFC` (Near White) | Primary text |
| Muted | `#94A3B8` (Slate Gray) | Secondary text, descriptions |
| Gradient | `#4F46E5 → #7C3AED → #06B6D4` | Hero section gradient mesh |

## Layout Structure

### 1. Aurora Background
- ReactBits Aurora component as full-page background
- Colors: Indigo → Violet → Cyan gradient, slowly animating
- Opacity: `0.3` so text remains readable
- `position: fixed; inset: 0; z-index: 0;`

### 2. Sticky Navigation (z-50)
- Glassmorphism: `backdrop-blur-xl bg-slate-900/60 border-b border-white/5`
- Logo (left) + nav links (center) + CTA button (right)
- Nav links: Product, Features, Pricing, About
- CTA: "Get Started" button, gradient bg (Indigo → Violet)
- Hides on scroll down, shows on scroll up
- Mobile: hamburger menu with slide-in drawer

### 3. Hero Section
- **Headline**: Large Plus Jakarta Sans, weight 800
  - Use ReactBits **Shiny Text** on key words for shimmer effect
  - `text-4xl sm:text-5xl lg:text-6xl`, white
  - Example: "Ship faster with [shiny]AI-powered[/shiny] workflows"
- **Subheadline**: Inter, `text-lg sm:text-xl`, muted color, max-width 600px
- **CTA Row**: Primary button (gradient) + Secondary button (outline)
  - Primary: `px-8 py-4 rounded-xl`, gradient bg, white text, hover scale 1.02
  - Secondary: `border border-white/20`, white text, hover bg white/5
- **Dashboard Preview**: Screenshot/mockup of the product
  - Wrapped in a perspective container with subtle 3D tilt
  - Border: `1px solid rgba(255,255,255,0.1)`, rounded-2xl
  - Shadow: large colored glow matching primary color
  - Animate in from bottom with opacity on load

### 4. Logos / Social Proof Bar
- "Trusted by 500+ teams" + row of greyscale company logos
- `opacity: 0.4`, hover → `opacity: 0.8`
- Horizontal scroll on mobile, grid on desktop

### 5. Feature Cards Section
- Section title + subtitle
- 3-column grid (desktop), 1-column (mobile)
- Each card:
  - `bg: surface`, `border: 1px solid white/5`, `rounded-2xl`
  - Icon (top, colored with accent), title, description
  - Hover: `border-color: primary/30`, subtle translateY(-2px)
  - Use ReactBits **Animated List** for staggered reveal on scroll

### 6. Pricing Table
- Toggle: Monthly / Annual (annual = discount badge)
- 3 tiers: Starter / Pro / Enterprise
- Each tier card:
  - Price, feature list with checkmarks, CTA button
  - **Pro** (recommended): highlighted with gradient border, "Popular" badge
  - Hover effects on cards
- All prices fade-transition when toggling monthly/annual

### 7. Testimonials
- 3-column grid or horizontal carousel
- Each testimonial: avatar, quote, name, title, company
- Star rating or quote marks
- Cards have glassmorphism effect

### 8. CTA Section
- Full-width gradient background (Indigo → Violet)
- Large headline + subtext + email input + button
- Floating decorative shapes/orbs in background

### 9. Footer
- Dark background, 4-column link grid
- Logo, social links, copyright
- Border-top: `1px solid white/5`

## State & Logic

```typescript
// Pricing toggle
const [isAnnual, setIsAnnual] = useState(false);

// Scroll-based animations
// Use IntersectionObserver for reveal-on-scroll
const observerRef = useRef<IntersectionObserver>();
useEffect(() => {
  observerRef.current = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate-in');
        }
      });
    },
    { threshold: 0.1 }
  );
  // Observe all [data-animate] elements
}, []);

// Navbar hide/show on scroll
const [navVisible, setNavVisible] = useState(true);
const lastScrollY = useRef(0);
useEffect(() => {
  const handleScroll = () => {
    setNavVisible(window.scrollY < lastScrollY.current || window.scrollY < 100);
    lastScrollY.current = window.scrollY;
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  return () => window.removeEventListener('scroll', handleScroll);
}, []);
```

## Prompt

Build a complete SaaS landing page in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Dark-mode design with aurora gradient background.

**Fonts:** Load Plus Jakarta Sans (display, 400-800) and Inter (body, 400-600) from Google Fonts.

**Sections (top to bottom):**
1. **Aurora background** — animated gradient mesh (Indigo/Violet/Cyan) at 0.3 opacity, fixed position behind all content.
2. **Sticky navbar** — glassmorphism (`backdrop-blur-xl bg-slate-900/60`), logo + nav links + "Get Started" gradient CTA button. Hides on scroll-down, shows on scroll-up. Mobile hamburger.
3. **Hero** — Large headline with shiny text effect on key words, subheadline, two CTA buttons (gradient primary + outline secondary), and a product dashboard screenshot with perspective tilt and colored glow shadow. Content animates in from bottom.
4. **Social proof** — "Trusted by 500+ teams" + greyscale logo row.
5. **Features** — 3-column grid of cards with icons, titles, descriptions. Cards stagger-animate on scroll using IntersectionObserver. Hover: subtle lift + border highlight.
6. **Pricing** — Monthly/Annual toggle with 3 tiers (Starter/Pro/Enterprise). Pro card highlighted with gradient border + "Popular" badge. Prices fade-transition on toggle.
7. **Testimonials** — 3 cards with avatar, quote, name, title. Glassmorphism card style.
8. **Bottom CTA** — Full-width gradient section with headline + email capture form.
9. **Footer** — 4-column link grid, logo, social icons, copyright.

**Animations:** All sections use `IntersectionObserver` with `threshold: 0.1` for reveal-on-scroll (translateY + opacity). Transitions: `300ms ease-out`. Buttons have hover `scale(1.02)` + subtle shadow changes.

**Color system:** Dark navy bg `#0F172A`, slate surface `#1E293B`, Indigo primary `#4F46E5`, Violet secondary `#7C3AED`, Cyan accent `#06B6D4`, white text, slate-gray muted text.

## Required Assets
- `dashboard-preview` — Product dashboard screenshot/mockup (hero section)
- `logo` — Brand logo (SVG preferred)
- `client-logos` — 4-6 greyscale client/partner logos (social proof bar)

## ReactBits Components Used
- **Aurora** (`https://www.reactbits.dev/backgrounds/aurora`) — Animated gradient mesh background. Copy component code, set colors to `['#4F46E5', '#7C3AED', '#06B6D4']`, opacity 0.3.
- **Shiny Text** (`https://www.reactbits.dev/text-animations/shiny-text`) — Shimmer effect on hero headline key words.
- **Animated List** (`https://www.reactbits.dev/components/animated-list`) — Staggered reveal for feature cards on scroll.
