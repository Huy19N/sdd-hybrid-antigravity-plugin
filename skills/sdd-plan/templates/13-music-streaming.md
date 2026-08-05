---
id: music-streaming
name: "Music & Entertainment"
category: music-entertainment
tags:
  - music
  - streaming
  - audio
  - podcast
  - entertainment
  - artist
  - album
requires_transparent_images: false
color_palette:
  primary: "#581C87"
  secondary: "#EC4899"
  accent: "#A855F7"
  background: "#09090B"
  surface: "#18181B"
  text: "#FAFAFA"
  muted: "#71717A"
reactbits_components:
  - name: "Magic Rings"
    url: "https://www.reactbits.dev/animations/magic-rings"
  - name: "Particle Text"
    url: "https://www.reactbits.dev/text-animations/particle-text"
best_for: "Nền tảng âm nhạc, streaming, artist portfolio, podcast, entertainment — dark immersive UI, audio visualizer, album grid"
fonts:
  display: "Orbitron"
  body: "Rubik"
---

# Template: Music & Entertainment

## Preview Description
A dark, immersive music/entertainment platform with **magic rings** pulsating audio
visualizer effect and **particle text** for the brand name. Deep purple and hot pink
create an electric nightlife atmosphere. Album/artist grids, playlist cards, and a
mini player bar at the bottom. Everything feels like a premium audio experience.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rubik:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#581C87` (Deep Purple) | Gradient start, active states |
| Secondary | `#EC4899` (Hot Pink) | Gradient end, highlights |
| Accent | `#A855F7` (Violet) | Buttons, badges, links |
| Background | `#09090B` (True Black) | Page bg |
| Surface | `#18181B` (Zinc) | Cards |
| Text | `#FAFAFA` | Primary text |
| Muted | `#71717A` | Secondary |
| Gradient | `#581C87 → #EC4899` | Key gradient |

## Layout Structure

### 1. Magic Rings Background
- Hero section only — pulsating concentric rings
- Purple → pink gradient colors
- Simulates audio/speaker wave visualization

### 2. Nav — sleek, minimal
- Logo (Orbitron) + Browse / Artists / Playlists / Podcasts
- Search + profile avatar (right)
- Transparent, blur on scroll

### 3. Hero
- Particle Text brand name, massive, dissolves/reforms
- "Your Music, Your Way" subheadline
- "Start Listening" gradient button + "Free Trial" outline
- Magic Rings behind

### 4. Featured This Week
- Large featured album/artist spotlight
- Album art + artist name + "Play Now" + tracklist preview

### 5. Trending Tracks
- List view: # + cover + track name + artist + duration + play button
- Hover: row highlights, play button appears
- Alternating row colors

### 6. Popular Artists
- Circular avatar grid
- Name below, genre badge
- Hover: purple glow ring

### 7. Curated Playlists
- Card grid: playlist cover (mosaic of 4 albums), title, track count
- Gradient overlay on hover

### 8. Podcast Section
- Horizontal scroll of podcast cards
- Cover art, title, episode count, latest episode date

### 9. Mini Player Bar (fixed bottom)
- Album art (small) + track name + artist + play/pause/skip + progress bar + volume
- Glassmorphism bar
- Always visible on page

### 10. CTA — "Go Premium" + feature comparison
### 11. Footer — minimal

## Prompt

Build a music/entertainment platform in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Dark immersive design with audio-inspired visuals.

**Fonts:** Orbitron (display, 400-900) and Rubik (body, 400-700).

**Key elements:** Magic Rings pulsating visualizer in hero, Particle Text brand name, fixed mini player bar, trending tracks list, circular artist grid, gradient-heavy UI.

**Sections:** Nav → Hero (particle text + magic rings) → Featured → Trending Tracks (list) → Artists (circular grid) → Playlists (card grid) → Podcasts (scroll) → Premium CTA → Fixed Mini Player → Footer.

**Color system:** True black `#09090B`, deep purple `#581C87`, hot pink `#EC4899`, violet `#A855F7`.

## Required Assets
- `album-01` through `album-08` — Album cover art
- `artist-01` through `artist-06` — Artist portrait photos (square, for circular crop)
- `podcast-01` through `podcast-04` — Podcast cover art
- `featured-album` — Large featured album art

## ReactBits Components Used
- **Magic Rings** (`https://www.reactbits.dev/animations/magic-rings`) — Pulsating ring visualizer in hero.
- **Particle Text** (`https://www.reactbits.dev/text-animations/particle-text`) — Brand name made of particles.
