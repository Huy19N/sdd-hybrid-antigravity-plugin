---
id: event-conference
name: "Event & Conference"
category: event
tags:
  - event
  - conference
  - summit
  - workshop
  - meetup
  - festival
  - ticket
requires_transparent_images: false
color_palette:
  primary: "#7E22CE"
  secondary: "#F59E0B"
  accent: "#EC4899"
  background: "#18181B"
  surface: "#27272A"
  text: "#FAFAFA"
  muted: "#A1A1AA"
reactbits_components:
  - name: "Line Waves"
    url: "https://www.reactbits.dev/backgrounds/line-waves"
  - name: "Scrambled Text"
    url: "https://www.reactbits.dev/text-animations/scrambled-text"
best_for: "Sự kiện, hội nghị, conference, summit, workshop, concert, festival — cần countdown, speaker grid, schedule timeline, và bán vé"
fonts:
  display: "Clash Display"
  body: "General Sans"
---

# Template: Event & Conference

## Preview Description
An energetic dark-mode event/conference page with **line waves** animated background,
**scrambled text** reveal on the event name, a live countdown timer, speaker profile
grid, and an interactive schedule timeline. Purple-amber-pink palette creates
excitement and urgency. Bold display typography commands attention.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
```

Note: Using Outfit as proxy for Clash Display (which requires manual hosting). For true Clash Display, self-host from fontshare.com.

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#7E22CE` (Grape Purple) | CTAs, active states, gradient start |
| Secondary | `#F59E0B` (Amber) | Countdown, highlights, badges |
| Accent | `#EC4899` (Hot Pink) | Hover, gradient end, special badges |
| Background | `#18181B` (Dark Zinc) | Page bg |
| Surface | `#27272A` (Zinc) | Cards, sections |
| Text | `#FAFAFA` | Primary text |
| Muted | `#A1A1AA` | Secondary text |

## Layout Structure

### 1. Line Waves Background
- ReactBits Line Waves, full viewport hero
- Colors: purple + pink gradient
- Animated, slow wave motion

### 2. Navigation
- Transparent, switches to dark bg on scroll
- Logo (left) + Schedule / Speakers / Venue / Sponsors (center)
- "Get Tickets" amber gradient button (right)

### 3. Hero
- Event name with Scrambled Text reveal animation
- Large bold display font, `text-6xl sm:text-8xl`
- Date + location below
- **Countdown timer**: Days / Hours / Minutes / Seconds
  - Each unit in its own card, large numbers, amber accent
- "Get Tickets" + "Watch Trailer" buttons
- Line Waves behind everything

### 4. About the Event
- Brief description, 3 key stats:
  - "3 Days" / "50+ Speakers" / "2000+ Attendees"
- Event highlights/tracks listed

### 5. Speaker Grid
- 4-col grid of speaker cards
- Each: photo (circular), name, title/company, topic
- Hover: card lifts + purple border glow
- "View All Speakers" link

### 6. Schedule / Agenda
- Day tabs (Day 1, Day 2, Day 3)
- Timeline layout: time (left) + session card (right)
- Session card: title, speaker avatar, room/track badge, duration
- Color-coded by track
- Active session highlighted

### 7. Venue
- Map + venue photos
- Address, transport info
- Hotel recommendations

### 8. Sponsors / Partners
- Tiered: Platinum / Gold / Silver
- Logo grids, sized by tier
- "Become a Sponsor" CTA

### 9. Ticket Section
- 3 tiers: Standard / VIP / Group
- Each: price, features list, "Buy Now" button
- VIP highlighted with gradient border
- Early bird badge if applicable

### 10. Newsletter
- "Stay Updated" + email input
- Dark section

### 11. Footer
- Event logo, social links, previous events, legal

## Prompt

Build an event/conference landing page in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Energetic dark-mode design.

**Fonts:** Outfit (display, 400-900) and Inter (body, 400-600).

**Key features:**
- Line Waves animated background on hero
- Scrambled Text reveal on event name
- Live countdown timer (days/hours/minutes/seconds)
- Schedule timeline with day tabs
- Speaker grid with hover effects

**Sections:** Nav → Hero (scrambled text title, countdown, Line Waves bg) → About (stats) → Speakers (grid) → Schedule (tabbed timeline) → Venue → Sponsors (tiered logos) → Tickets (3 tiers) → Newsletter → Footer.

**Color system:** Dark zinc bg `#18181B`, purple `#7E22CE`, amber `#F59E0B`, pink `#EC4899`.

## Required Assets
- `speaker-01` through `speaker-08` — Speaker headshots
- `venue-01` through `venue-03` — Venue photos
- `sponsor-logos` — Sponsor/partner logos

## ReactBits Components Used
- **Line Waves** (`https://www.reactbits.dev/backgrounds/line-waves`) — Animated wave background for hero section.
- **Scrambled Text** (`https://www.reactbits.dev/text-animations/scrambled-text`) — Text scramble/decode reveal effect on event title.
