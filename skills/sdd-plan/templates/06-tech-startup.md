---
id: tech-startup
name: "Tech / AI Startup"
category: tech-startup
tags:
  - tech
  - ai
  - startup
  - saas
  - innovation
  - machine-learning
  - api
requires_transparent_images: false
color_palette:
  primary: "#06B6D4"
  secondary: "#A855F7"
  accent: "#22D3EE"
  background: "#0F172A"
  surface: "#1E293B"
  text: "#F8FAFC"
  muted: "#64748B"
reactbits_components:
  - name: "Dot Field"
    url: "https://www.reactbits.dev/backgrounds/dot-field"
  - name: "Glitch Text"
    url: "https://www.reactbits.dev/text-animations/glitch-text"
  - name: "Blob Cursor"
    url: "https://www.reactbits.dev/animations/blob-cursor"
best_for: "Công ty công nghệ, AI startup, API platform, developer tools — dark futuristic theme với particle effects và glassmorphism"
fonts:
  display: "Space Grotesk"
  body: "Inter"
---

# Template: Tech / AI Startup

## Preview Description
A futuristic dark-mode tech startup landing page with an animated **dot field**
particle background, **glitch text** effects on the hero headline, and a **blob
cursor** that follows mouse movement. Glassmorphism cards showcase features and
API capabilities. Code snippets and terminal-style UI elements reinforce the
developer-friendly aesthetic. Neon cyan and electric purple accent colors pop
against the deep navy background.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#06B6D4` (Cyan) | CTAs, links, accent borders |
| Secondary | `#A855F7` (Purple) | Gradient endpoints, highlights |
| Accent | `#22D3EE` (Light Cyan) | Glow effects, badges |
| Background | `#0F172A` (Dark Navy) | Page bg |
| Surface | `#1E293B` (Slate) | Card bg |
| Text | `#F8FAFC` | Primary text |
| Muted | `#64748B` | Secondary text |
| Glow gradient | `#06B6D4 → #A855F7` | Borders, button gradients |

## Layout Structure

### 1. Dot Field Background
- ReactBits **Dot Field** component, full viewport fixed
- Particles in cyan/purple, slow movement, connecting lines
- Opacity: `0.2-0.3`

### 2. Blob Cursor
- ReactBits **Blob Cursor** — gradient blob follows mouse
- Colors: cyan → purple gradient
- Size: `200px`, blur `60px`
- Only on desktop

### 3. Navigation (z-50)
- Glassmorphism: `backdrop-blur-xl bg-slate-900/50 border-b border-cyan-500/10`
- Logo (left) + nav links + "Get API Key" gradient button (right)
- Mobile: slide-out drawer

### 4. Hero
- **Headline** with ReactBits **Glitch Text** effect on key word
  - `text-5xl sm:text-7xl`, Space Grotesk, weight 700
  - Example: "Build [glitch]Intelligent[/glitch] Software"
- Subheadline: Inter, muted, max-w-2xl
- Two CTAs: "Start Building" (gradient) + "View Docs" (outline cyan border)
- Below: terminal-style code snippet window
  - Dark bg with cyan/green syntax highlighting
  - Typing animation on the code
  - Mock: `curl -X POST api.yourapp.com/v1/analyze`

### 5. Stats Bar
- 3-4 metrics in a row: "10M+ API Calls" / "99.9% Uptime" / "150ms Avg Latency"
- Animated counter on scroll (count up effect)
- Glassmorphism pills with cyan border

### 6. Feature Grid
- 2x3 grid of glassmorphism cards
- Each: icon (lucide, cyan), title, description, learn-more link
- Cards have `border: 1px solid cyan-500/20`, hover `border: cyan-500/40`
- Subtle glow on hover
- Stagger animation on scroll

### 7. How It Works
- 3-step process: Connect → Process → Deploy
- Horizontal timeline with connecting line
- Each step: number circle + title + description + mini illustration
- Timeline line animated from left to right on scroll

### 8. Code Demo
- Split: interactive demo (left) + live output (right)
- Left: code editor with syntax highlighting (dark theme)
- Right: live response JSON or visual output
- Tab to switch between languages: Python, JavaScript, cURL

### 9. Integrations
- Logo grid of compatible platforms/tools
- `opacity: 0.3`, hover `opacity: 1`
- "Works with everything" headline

### 10. Pricing
- 3 tiers: Free / Pro / Enterprise
- Glassmorphism cards, Pro highlighted with gradient border
- Feature comparison list with check/x marks

### 11. CTA
- Gradient bg section (cyan → purple)
- Large headline + "Start Free" button

### 12. Footer
- Dark bg, 4-column links, social icons
- Status indicator: green dot + "All Systems Operational"

## State & Logic

```typescript
// Stats counter animation
const [statsVisible, setStatsVisible] = useState(false);

// Code demo tab
const [activeLanguage, setActiveLanguage] = useState<'python' | 'javascript' | 'curl'>('python');

// Typing animation for terminal
const [typedText, setTypedText] = useState('');
useEffect(() => {
  const fullText = 'curl -X POST api.yourapp.com/v1/analyze';
  let i = 0;
  const timer = setInterval(() => {
    setTypedText(fullText.slice(0, i + 1));
    i++;
    if (i >= fullText.length) clearInterval(timer);
  }, 50);
  return () => clearInterval(timer);
}, []);
```

## Prompt

Build a tech/AI startup landing page in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Futuristic dark-mode design with particle effects.

**Fonts:** Space Grotesk (display, 400-700) and Inter (body, 400-600).

**Key visual elements:**
- Dot field particle background (cyan/purple, 0.2 opacity, fixed)
- Blob cursor (cyan-purple gradient, 200px, blur 60px, desktop only)
- Glitch text effect on hero headline key word
- Glassmorphism cards (`backdrop-blur-xl bg-slate-900/50 border-cyan-500/20`)
- Terminal/code snippet with typing animation
- Gradient accents (cyan #06B6D4 → purple #A855F7)

**Sections:** Nav → Hero (glitch headline + terminal) → Stats (animated counters) → Features (glassmorphism grid) → How It Works (timeline) → Code Demo (tabbed) → Integrations (logo grid) → Pricing → CTA → Footer.

**Color system:** Dark navy `#0F172A`, slate surface `#1E293B`, cyan primary `#06B6D4`, purple secondary `#A855F7`, white text.

## Required Assets
- `logo` — Brand logo (SVG, works on dark bg)
- `integration-logos` — 6-8 platform logos (grayscale)

## ReactBits Components Used
- **Dot Field** (`https://www.reactbits.dev/backgrounds/dot-field`) — Animated particle background.
- **Glitch Text** (`https://www.reactbits.dev/text-animations/glitch-text`) — Glitch effect on hero keyword.
- **Blob Cursor** (`https://www.reactbits.dev/animations/blob-cursor`) — Gradient blob following cursor.
