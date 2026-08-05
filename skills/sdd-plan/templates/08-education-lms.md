---
id: education-lms
name: "Education / LMS"
category: education
tags:
  - education
  - learning
  - course
  - lms
  - school
  - training
  - tutorial
requires_transparent_images: false
color_palette:
  primary: "#0EA5E9"
  secondary: "#F97316"
  accent: "#8B5CF6"
  background: "#FFFFFF"
  surface: "#F0F9FF"
  text: "#0F172A"
  muted: "#64748B"
reactbits_components:
  - name: "Animated List"
    url: "https://www.reactbits.dev/components/animated-list"
  - name: "Split Flap Text"
    url: "https://www.reactbits.dev/text-animations/split-flap-text"
best_for: "Nền tảng học tập online, khóa học, LMS, trường học, bootcamp — cần course cards, progress indicators, gamification"
fonts:
  display: "Sora"
  body: "Inter"
---

# Template: Education / LMS

## Preview Description
A bright, engaging education platform with **gamification elements**, animated
course cards with progress rings, and a split-flap counter showing live enrollment
stats. The design feels friendly and motivating — sky blue primary with orange
energy accents. Course cards use staggered list animations. Progress tracking is
visual and prominent, encouraging course completion.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#0EA5E9` (Sky Blue) | CTAs, progress rings, active states |
| Secondary | `#F97316` (Orange) | Badges, alerts, gamification |
| Accent | `#8B5CF6` (Violet) | Premium badges, special categories |
| Background | `#FFFFFF` | Page bg |
| Surface | `#F0F9FF` (Light Blue) | Card backgrounds, sections |
| Text | `#0F172A` | Primary text |
| Muted | `#64748B` | Descriptions |

## Layout Structure

### 1. Navigation
- White bg, shadow-sm
- Logo (left) + Browse Courses / Teach / Community (center)
- Search bar (expandable) + notifications bell + avatar dropdown (right)
- Orange "Start Learning" CTA

### 2. Hero
- Illustrated hero with student/teacher character (right)
- Left: headline "Learn Without Limits", subheadline, search bar
- Split Flap counter: "25,000+ Students Enrolled" (animated number)
- Category quick links below: Design, Development, Business, Marketing
- Light blue gradient bg

### 3. Popular Courses
- Animated List stagger reveal
- Course cards (4 cols desktop, 2 mobile):
  - Thumbnail image, category badge (colored pill)
  - Title, instructor name + avatar
  - Rating (stars + number), student count
  - Progress ring (if enrolled) or price
  - Hover: subtle lift + shadow
- "View All Courses" button

### 4. Learning Paths
- 3-4 curated paths as horizontal cards
- Each: icon + title + course count + duration + difficulty badge
- Gradient border on hover

### 5. Stats Section
- 4 metrics: Courses, Students, Instructors, Completion Rate
- Animated count-up on scroll
- Icons from lucide-react

### 6. Featured Instructors
- Horizontal scroll of instructor cards
- Avatar, name, expertise, course count, rating
- "Become an Instructor" CTA

### 7. Testimonials
- Student success stories with before/after
- Avatar, quote, course completed, outcome

### 8. CTA
- "Start Your Learning Journey Today"
- Email signup or "Browse Free Courses"
- Illustrated background

### 9. Footer
- Links, social, app download buttons

## Prompt

Build an education/LMS platform landing page in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Bright, engaging, gamification-friendly design.

**Fonts:** Sora (display, 400-800) and Inter (body, 400-600).

**Key features:**
- Split Flap animated counter for enrollment stats
- Course cards with progress rings (SVG circle), animated stagger reveal
- Category color-coded badges
- Gamification: streak indicators, achievement badges, completion percentages

**Sections:** Nav → Hero (illustrated, search bar, split-flap counter) → Popular Courses (animated list grid) → Learning Paths (horizontal cards) → Stats → Instructors → Testimonials → CTA → Footer.

**Color system:** White bg, light blue surface `#F0F9FF`, sky blue `#0EA5E9`, orange `#F97316`, violet `#8B5CF6`.

## Required Assets
- `hero-illustration` — Student/learning illustration for hero
- `course-thumb-01` through `course-thumb-08` — Course thumbnail images
- `instructor-01` through `instructor-04` — Instructor avatars

## ReactBits Components Used
- **Animated List** (`https://www.reactbits.dev/components/animated-list`) — Staggered reveal for course cards.
- **Split Flap Text** (`https://www.reactbits.dev/text-animations/split-flap-text`) — Animated counter for enrollment/completion stats.
