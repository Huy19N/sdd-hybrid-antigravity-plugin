---
id: news-magazine
name: "News & Magazine"
category: news-blog
tags:
  - news
  - blog
  - magazine
  - editorial
  - article
  - media
  - journalism
requires_transparent_images: false
color_palette:
  primary: "#2563EB"
  secondary: "#F8F5F0"
  accent: "#DC2626"
  background: "#FFFFFF"
  surface: "#F8F5F0"
  text: "#1E1E1E"
  muted: "#6B7280"
reactbits_components:
  - name: "Infinite Menu"
    url: "https://www.reactbits.dev/components/infinite-menu"
  - name: "Split Flap Text"
    url: "https://www.reactbits.dev/text-animations/split-flap-text"
best_for: "Trang tin tức, blog, tạp chí online, editorial platform, content publishing — grid editorial layout, reading progress, categories"
fonts:
  display: "Newsreader"
  body: "Source Sans 3"
---

# Template: News & Magazine

## Preview Description
A classic editorial news/magazine website with **newspaper-inspired grid layout**,
**infinite scrolling category menu**, and **split-flap breaking news ticker**.
Traditional serif headlines meet modern sans-serif body text. Category color-coding,
reading progress bar, and a clean reading experience. Red accent for breaking/urgent
content, blue for standard CTAs.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#2563EB` (Blue) | Links, CTAs, standard |
| Secondary | `#F8F5F0` (Paper) | Section backgrounds |
| Accent | `#DC2626` (Red) | Breaking news, urgent, live |
| Background | `#FFFFFF` | Page bg |
| Surface | `#F8F5F0` (Paper) | Cards, sidebar |
| Text | `#1E1E1E` (Ink) | Headlines, body text |
| Muted | `#6B7280` | Bylines, dates, captions |

## Layout Structure

### 1. Breaking News Ticker
- Top strip, red bg
- Split Flap Text for breaking news headline
- Auto-scrolling multiple headlines

### 2. Navigation
- White bg, shadow, multi-level
- Logo (left, large Newsreader serif)
- Category menu: Infinite Menu component
  - Categories: Politics, Tech, Business, Sports, Culture, Science, Opinion
  - Each with color accent
- Search + Subscribe button (right)
- Secondary nav: Trending topics

### 3. Hero / Featured Stories
- Large featured article (hero): full-width image + headline + excerpt + byline
- 2-3 smaller featured articles beside (sidebar-style)
- "FEATURED" label badge

### 4. Latest Articles Grid
- 3-column editorial grid (desktop), 1-column (mobile)
- Each article: thumbnail, category badge (color-coded), headline, excerpt, author + date
- Hover: headline turns blue
- Load more: infinite scroll or "More Articles" button

### 5. Category Sections
- Section per major category
- Horizontal article row per category
- "View All [Category]" link
- Category color accent on border-left

### 6. Opinion / Editorial
- Distinguished section with paper bg
- Columnist photo + name + column title
- Pull quotes styled distinctly

### 7. Sidebar Widgets (on article pages)
- Most Read (numbered list)
- Newsletter signup
- Social follow buttons
- Ad placeholder

### 8. Reading Progress Bar (article pages)
- Fixed top, thin blue line showing scroll progress

### 9. Newsletter CTA
- "Stay Informed" + email input
- Clean, paper bg section

### 10. Footer
- Large: All categories, about, contact, legal, social
- RSS feed link
- Copyright, editorial policy links

## Prompt

Build a news/magazine website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Classic editorial design with modern interactions.

**Fonts:** Newsreader (display serif, 400-800 + italic) and Source Sans 3 (body, 400-700).

**Key elements:** Split Flap breaking news ticker, Infinite Menu category navigation, newspaper editorial grid layout, reading progress bar, category color-coding, serif headlines + sans-serif body.

**Sections:** Breaking Ticker (split flap) → Nav (logo + infinite category menu) → Hero (featured story) → Latest Grid (3-col) → Category Sections (horizontal rows) → Opinion → Newsletter → Footer.

**Color system:** White bg, paper `#F8F5F0`, ink text `#1E1E1E`, blue links `#2563EB`, red breaking `#DC2626`.

## Required Assets
- `featured-article-hero` — Large featured article image
- `article-thumb-01` through `article-thumb-12` — Article thumbnail images
- `columnist-01` through `columnist-03` — Opinion columnist portraits
- `logo` — Publication logo/masthead

## ReactBits Components Used
- **Infinite Menu** (`https://www.reactbits.dev/components/infinite-menu`) — Scrollable category navigation.
- **Split Flap Text** (`https://www.reactbits.dev/text-animations/split-flap-text`) — Breaking news ticker with split-flap animation.
