---
id: healthcare-clinic
name: "Healthcare & Clinic"
category: healthcare
tags:
  - healthcare
  - clinic
  - hospital
  - doctor
  - medical
  - wellness
  - booking
requires_transparent_images: false
color_palette:
  primary: "#0D9488"
  secondary: "#DBEAFE"
  accent: "#059669"
  background: "#FFFFFF"
  surface: "#F0FDFA"
  text: "#1E293B"
  muted: "#64748B"
reactbits_components:
  - name: "Color Bends"
    url: "https://www.reactbits.dev/backgrounds/color-bends"
  - name: "Glass Icons"
    url: "https://www.reactbits.dev/components/glass-icons"
best_for: "Phòng khám, bệnh viện, dịch vụ y tế, wellness center — cần trust signals, doctor profiles, và hệ thống đặt lịch khám"
fonts:
  display: "Lexend"
  body: "Inter"
---

# Template: Healthcare & Clinic

## Preview Description
A clean, trustworthy healthcare website with **color bends** gradient background,
**glass-style icons** for services, and a prominent appointment booking system.
Teal-and-white color scheme conveys medical professionalism and calm. Doctor profiles
with credentials build patient trust. Accessible design with clear typography and
generous whitespace.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
```

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#0D9488` (Teal) | CTAs, headers, key elements |
| Secondary | `#DBEAFE` (Soft Blue) | Section backgrounds, badges |
| Accent | `#059669` (Emerald) | Success states, availability |
| Background | `#FFFFFF` | Page bg |
| Surface | `#F0FDFA` (Mint Tint) | Card backgrounds |
| Text | `#1E293B` | Primary text |
| Muted | `#64748B` | Secondary text |

## Layout Structure

### 1. Color Bends Background (Hero only)
- ReactBits Color Bends with teal/blue tones
- Subtle, calming gradient movement
- Contained to hero section, not full page

### 2. Navigation
- White bg, clean, shadow-sm
- Logo (left) + Services / Doctors / About / Blog (center)
- "Book Appointment" teal CTA (right)
- Emergency phone number visible
- Mobile: hamburger

### 3. Hero
- Color Bends background
- Left: "Your Health, Our Priority" headline + subtext + booking CTA + phone
- Right: doctor/clinic image or illustration
- Trust badges below: "20+ Years" / "50+ Doctors" / "100K+ Patients"

### 4. Services
- Glass Icons for each service (6 services, 3x2 grid)
- Each: glassmorphic icon + service name + brief description
- Services: General Medicine, Pediatrics, Cardiology, Dermatology, etc.
- Hover: teal border highlight

### 5. About / Why Choose Us
- 3 trust pillars: Certified Doctors, Modern Equipment, 24/7 Care
- Icons + descriptions
- Clinic photo

### 6. Our Doctors
- Doctor profile cards (4 cols desktop)
- Photo, name, specialization, credentials
- "Book with Dr. X" button
- Rating stars

### 7. Appointment Booking
- Inline booking form:
  - Department dropdown + Doctor dropdown + Date picker + Time slot + "Book" button
- Or: "Call us at XXX" alternative

### 8. Patient Testimonials
- Cards with patient initial avatar, quote, treatment type

### 9. Blog / Health Tips
- 3 recent article cards
- Thumbnail, category, title, excerpt

### 10. Footer
- Contact info, map, hours, departments, social, certifications

## Prompt

Build a healthcare/clinic website in React + TypeScript + Vite + Tailwind CSS, using `lucide-react` for icons. Clean, trustworthy, accessible medical design.

**Fonts:** Lexend (display, 400-700) and Inter (body, 400-600).

**Key elements:**
- Color Bends background on hero (teal/blue, calming)
- Glass Icons for service categories
- Appointment booking form (department, doctor, date, time)
- Doctor profile cards with credentials
- Trust signals throughout

**Sections:** Nav → Hero (Color Bends bg, booking CTA) → Services (glass icons grid) → Trust Pillars → Doctor Profiles → Booking Form → Testimonials → Blog → Footer.

**Color system:** White bg, mint surface `#F0FDFA`, teal `#0D9488`, soft blue `#DBEAFE`, emerald `#059669`.

## Required Assets
- `hero-doctor` — Doctor/clinic hero image or illustration
- `doctor-01` through `doctor-04` — Doctor profile photos
- `clinic-interior` — Clinic photo for About section
- `blog-thumb-01` through `blog-thumb-03` — Blog article thumbnails

## ReactBits Components Used
- **Color Bends** (`https://www.reactbits.dev/backgrounds/color-bends`) — Calming gradient background for hero section.
- **Glass Icons** (`https://www.reactbits.dev/components/glass-icons`) — Glassmorphic service category icons.
