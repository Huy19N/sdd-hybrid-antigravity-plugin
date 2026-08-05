---
id: crypto-fintech
name: "Crypto & Fintech"
category: crypto-fintech
tags:
  - crypto
  - fintech
  - blockchain
  - trading
  - defi
  - wallet
  - finance
requires_transparent_images: false
color_palette:
  primary: "#3B82F6"
  secondary: "#22C55E"
  accent: "#EAB308"
  background: "#0C1222"
  surface: "#1A2332"
  text: "#F1F5F9"
  muted: "#64748B"
reactbits_components:
  - name: "Aurora"
    url: "https://www.reactbits.dev/backgrounds/aurora"
  - name: "Blob Cursor"
    url: "https://www.reactbits.dev/animations/blob-cursor"
best_for: "Sàn giao dịch crypto, ứng dụng tài chính, fintech dashboard, DeFi platform, digital wallet"
fonts:
  display: "Satoshi"
  body: "Inter"
---

# Template: Crypto & Fintech

## Preview Description
A sleek, data-driven crypto/fintech landing page with **aurora gradient** background,
**blob cursor** effect, live-style chart previews, and glassmorphism wallet/portfolio
cards. Dark navy background with electric blue and success green accents. Numbers
and data visualizations are prominent. Trust and security are communicated through
design language.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
```

Note: Using Space Grotesk as proxy for Satoshi (which requires fontshare.com hosting).

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#3B82F6` (Electric Blue) | CTAs, charts, links |
| Secondary | `#22C55E` (Green) | Positive changes, success |
| Accent | `#EAB308` (Yellow) | Warnings, premium badges |
| Background | `#0C1222` (Deep Navy) | Page bg |
| Surface | `#1A2332` (Dark Slate) | Cards |
| Text | `#F1F5F9` | Primary text |
| Muted | `#64748B` | Secondary |
| Negative | `#EF4444` (Red) | Negative changes, errors |

## Layout Structure

### 1. Aurora Background — hero section, blue/green tones
### 2. Blob Cursor — blue gradient, desktop only

### 3. Nav
- Glassmorphism, logo + Markets / Products / About / Blog
- "Connect Wallet" gradient button or "Sign Up"

### 4. Hero
- "The Future of Finance" headline, Space Grotesk bold
- Live ticker strip: BTC $XX,XXX ▲2.4% | ETH $X,XXX ▲1.8%
- Two CTAs: "Start Trading" + "Explore Markets"
- Mini chart visualization (animated line chart preview)

### 5. Live Market Data
- Table or card grid of top assets
- Columns: Asset, Price, 24h Change (green/red), Volume, Mini Sparkline
- Real-time feel (can be mock data)

### 6. Features
- 3 glassmorphism cards: Security / Speed / Low Fees
- Icons, descriptions, metrics

### 7. Portfolio Preview
- Mock wallet/portfolio dashboard card
- Balance, asset allocation donut chart, recent transactions
- Glassmorphism with blue glow

### 8. How It Works
- 3 steps: Create Account → Deposit → Trade
- Numbered, connected by dotted line

### 9. Security Section
- "Bank-Grade Security" with security badges/certifications
- Shield icon, encryption details
- Trust indicators

### 10. CTA — gradient section, "Start Your Journey"
### 11. Footer — legal disclaimers prominent, regulatory info

## Prompt

Build a crypto/fintech landing page in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Data-driven dark design.

**Fonts:** Space Grotesk (display, 400-700) and Inter (body, 400-600).

**Key elements:** Aurora background, blob cursor, live market data table with sparklines, glassmorphism portfolio card, animated ticker strip, mini chart visualizations (CSS/SVG), green/red for positive/negative.

**Sections:** Nav → Hero (ticker + mini chart + aurora bg) → Market Data (table) → Features (glass cards) → Portfolio Preview → How It Works → Security → CTA → Footer.

**Color system:** Deep navy `#0C1222`, blue `#3B82F6`, green `#22C55E`, yellow `#EAB308`, red `#EF4444`.

## Required Assets
- `logo` — Brand logo (SVG, works on dark)
- No heavy image assets needed — this template is data/chart focused

## ReactBits Components Used
- **Aurora** (`https://www.reactbits.dev/backgrounds/aurora`) — Gradient mesh background for hero.
- **Blob Cursor** (`https://www.reactbits.dev/animations/blob-cursor`) — Gradient cursor follower.
