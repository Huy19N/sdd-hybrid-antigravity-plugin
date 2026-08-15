---
name: sdd-asset-generator
version: 2
description: "Sub-skill automatically invoked by sdd-build when plan.md contains a Design Template section. Do NOT trigger manually. Functions as an elite Art Director & Visual Concept Designer using the generate_image tool to produce high-artistry, curated visual assets (editorial photography, 3D liquid chrome surrealism, tactile still lifes, cinematic scenes, textures) tailored precisely to the chosen template's mood and theme."
---

# SDD Asset Generator (Art Director Edition v2)

## Purpose & Philosophy: The Art Director Manifesto
Visual assets are not mere "placeholders" or generic stock photos — they define the **soul, credibility, and visual hierarchy** of the entire user interface.

As an AI Art Director inspired by high-end curation (Pinterest moodboards, avant-garde Instagram 3D design, Kinfolk editorial, and Awwwards-winning art direction), this skill crafts bespoke, premium imagery with deliberate lighting, tactile material textures, and sophisticated color grading.

### Anti-Stock & Anti-AI-Slop Rules
1. **Never generate bland corporate stock**: No forced smiling businessmen pointing at blank air, no sterile generic conference rooms.
2. **Never generate cheap 3D cartoon clay characters**: No flat, plasticky emoji-like avatars.
3. **No flat, washed-out lighting**: Every image must have intentional lighting dynamics (volumetric light, chiaroscuro, caustics, softbox rim glow, or hard editorial strobe).
4. **Emphasize tactile materiality**: Capture tangible surface details — brushed anodized titanium, fluted frosted glass, raw linen weave, porous travertine, condensation droplets, subtle 35mm film grain.
5. **Harmonize with the template palette**: Images must actively weave in the primary, secondary, and accent colors of the selected design template.

---

## Invocation
This skill is **automatically called** by `sdd-build` when `plan.md` contains a `## Design Template` section. It runs **before** the first UI-related task in the plan. Never trigger this skill directly — `sdd-build` handles the orchestration.

## Preconditions
- `docs/sdd/<feature-slug>/plan.md` exists with a `## Design Template` section.
- The Design Template section includes a `Required Assets` list.
- The template's color palette is specified.

---

## The 7-Pillar Master Prompt Architecture

When generating any image, construct the prompt using this 7-pillar formula:

```
[1. Subject & Spatial Staging] + [2. Art Movement & Aesthetic Archetype] + [3. Lighting & Atmospheric Design] + [4. Materiality & Tactile Textures] + [5. Color Grading & Chromatic Harmony] + [6. Camera, Lens & Optical Physics] + [7. Background & Cutout Readiness]
```

### 1. Subject & Spatial Staging
- Clearly define the focal element, sculptural composition, model pose, or environmental scene.
- Apply compositional rules: dynamic diagonal, golden ratio, generous negative space for UI text overlay, or centered sculptural symmetry.

### 2. Art Movement & Aesthetic Archetype
Select the movement fitting the project's brand identity:
- **3D Liquid Chrome & Glass Surrealism** (Cyber-avant-garde, floating metallic forms, iridescent fluid drops)
- **High-Fashion Editorial** (Vogue/Dazed aesthetic, stark contrast, architectural silhouette)
- **Organic Wabi-Sabi & Minimalist Still-Life** (Kinfolk/Cereal aesthetic, serene, earthy, raw materials)
- **Cyber-Luxe & Dark Matter** (Dark glassmorphism, laser holography, glowing neon fiber-optics)
- **Cinematic Chiaroscuro & Gourmet Gastronomy** (Moody dark-room culinary art, steam wisps, rich shadows)
- **Architectural Digest Modernism** (Warm sunlit spaces, clean concrete, warm oak, floor-to-ceiling glass)

### 3. Lighting & Atmospheric Design
- *Natural / Warm*: Dappled morning sunlight (komorebi), golden hour glow, soft ambient window light.
- *Editorial / Studio*: Direct hard flash with sharp shadows, multi-point softbox with subtle rim light.
- *Cinematic / Moody*: Dramatic chiaroscuro, volumetric god rays, misty fog, neon ambient bounce.
- *Refractive*: Light caustics through water/textured glass, iridescent chromatic dispersion.

### 4. Materiality & Micro-Textures
- Specify tactile surfaces: frosted fluted glass, brushed anodized aluminum, liquid mercury/chrome, raw travertine stone, woven bouclé/linen, wet condensation dew, fine 35mm analog film grain.

### 5. Color Grading & Chromatic Harmony
- Explicitly integrate the palette from `plan.md` (e.g., *"monochromatic obsidian black with electric ultraviolet and icy cyan accents"*, or *"warm terracotta, sage green, and raw cream tones"*).

### 6. Camera, Lens & Optical Physics
- *Portraits & Products*: 85mm or 100mm f/1.4 lens, shallow depth of field, creamy creamy bokeh background.
- *Macro Detail*: 100mm macro f/2.8, extreme close-up focus on texture and condensation.
- *Hero / Architecture*: 24mm or 35mm architectural wide lens, tilt-shift perspective control, natural depth.
- *Film Quality*: Shot on Hasselblad H6D-100c medium format or Kodak Portra 400 35mm film.

### 7. Background & Cutout Readiness
- **If `requires_transparent_images: true`**: Place on a *"seamless solid studio background with a soft natural ground contact shadow, isolated for clean background removal"*.
- **If full scene / hero banner**: Create an immersive environmental background with rich depth and negative space tailored for headline readability.

---

## Curated Aesthetic Library (Instagram & Pinterest Trends)

### Trend A: 3D Liquid Chrome & Glass Surrealism (Instagram @design / Avant-Garde 3D)
*Best for: Tech Startups, Crypto/Fintech, Creative Portfolios, Modern SaaS Hero Banners.*
```
Prompt Recipe:
"Abstract 3D sculptural composition with floating liquid chrome droplets, warped iridescent fluted glass ribbons, and smooth matte geometric spheres. Ethereal studio backlighting with caustic light refractions and chromatic dispersion. Obsidian dark backdrop with subtle neon violet and cyan ambient glow. Ultra-high resolution 3D octane render, sleek futuristic editorial art direction, 16:9 aspect ratio."
```

### Trend B: Organic Wabi-Sabi & Tactile Minimalist Still-Life (Pinterest / Kinfolk Style)
*Best for: Cafes, Bakeries, Shoppable Lifestyle, Pet Care, Wellness, Organic Products.*
```
Prompt Recipe:
"Artisanal still life composition with [Subject], resting on a raw beige travertine stone pedestal with textured raw linen draping. Soft dappled morning sunlight filtering through olive tree branches creating gentle leaf shadows. Earthy muted color palette of terracotta, warm sand, and sage green. Shot on 35mm film with delicate organic grain, shallow depth of field, warm cozy tranquil ambiance."
```

### Trend C: High-Fashion Editorial & Monochromatic Noir (Pinterest / High-End Lookbook)
*Best for: Fashion Ecommerce, Photography Studios, Luxury Goods, Event Conferences.*
```
Prompt Recipe:
"High-fashion editorial photography of [Subject/Model], striking sculptural pose with architectural silhouette. Direct hard studio flash lighting creating crisp dramatic cast shadows against a neutral textured concrete wall. Minimalist haute-couture styling, rich textile detail, deep contrast, Kodak Portra 400 film aesthetic, French Vogue magazine cover quality."
```

### Trend D: Dark Chiaroscuro Gourmet Culinary Art (Michelin Guide / Dark-room F&B)
*Best for: Restaurant & Food, Bubble Tea / Specialty Drinks, Gourmet Groceries.*
```
Prompt Recipe:
"Gourmet culinary photography of [Dish/Drink], styled on dark slate with scattered micro-herbs and sea salt flakes. Dramatic chiaroscuro side lighting highlighting wisps of warm rising steam and glistening condensation droplets. Rich deep shadows, warm golden amber highlights, macro 100mm f/2.8 lens focus on exquisite food texture, Michelin-star culinary presentation."
```

---

## Template-Specific Art Direction Matrix (22 Templates)

| # | Template ID & Name | Signature Art Style | Key Lighting & Texture Elements | Prompt Direction Archetype |
|---|---|---|---|---|
| 1 | `01-product-carousel` | Sculptural Luxury Studio | Travertine/acrylic pedestal, soft directional key light, ground shadow | Studio product hero, isolated on clean backdrop for cutout, ultra-tactile material finish. |
| 2 | `02-saas-landing` | Neo-Digital 3D Glassmorphism | Frosted glass cards, liquid gradient orbs, subtle grid mesh | Abstract 3D UI floating elements, vibrant violet/blue glow, dark minimalist background. |
| 3 | `03-portfolio-creative` | Avant-Garde Gallery Still-Life | Kinetic geometric sculptures, brutalist plaster, dramatic shadows | High-concept artist workspace or sculptural still life, museum-grade aesthetic. |
| 4 | `04-restaurant-food` | Dark Moody Chiaroscuro | Side-lit rim light, condensation beads, rising steam, rustic wood/slate | Gastronomy fine art, rich savory tones, mouthwatering macro depth of field. |
| 5 | `05-fashion-ecommerce` | Vogue High-Fashion Lookbook | Hard direct flash, architectural silhouettes, silk/leather textures | Editorial model lookbook, stark minimalism, Kodak Portra 400 film grain. |
| 6 | `06-tech-startup` | Cyber-Luxe & Dark Matter | Holographic wireframes, glowing fiber-optic particles, obsidian | Deep space dark mode, neon accent pulses, cutting-edge AI / quantum vibe. |
| 7 | `07-real-estate` | Architectural Digest Sunlit | Floor-to-ceiling glass, golden hour sunlight, concrete & oak | Warm modernist architectural interior, clean lines, airy spacious elegance. |
| 8 | `08-education-lms` | Inspiring Bauhaus Modernism | Warm morning light, tactile stationery, soft geometric papercraft | Enlightening clean atmosphere, warm energizing tones, human-centric learning. |
| 9 | `09-healthcare-clinic` | Biophilic Zen & Clean Sanctuary | Dappled sunbeams, soft frosted glass, lush eucalyptus leaves | Reassuring, pure, sterile-yet-warm medical wellness aesthetic with pastel hues. |
| 10 | `10-event-conference` | Dynamic Arena & Laser Prisms | Volumetric stage spotlights, subtle mist, kinetic crowd silhouettes | High-energy keynote stage, vibrant laser refractions, premium summit feel. |
| 11 | `11-fitness-gym` | High-Contrast Athletic Grit | Rim-lit muscle definition, dramatic arena spot, mist/sweat droplets | Cinematic sports photography, raw power, dark charcoal with neon punch. |
| 12 | `12-travel-tourism` | Sun-Drenched Mediterranean Cinema | Golden hour warmth, turquoise sea spray, warm coastal stone | National Geographic editorial travel, authentic wanderlust, sun flare. |
| 13 | `13-music-streaming` | Fluid Soundwave Synthwave | Iridescent neon fluid, glowing acoustic waves, chrome headphones | Vibrant nocturnal ambiance, holographic chromatic glows, sound-reactive visuals. |
| 14 | `14-crypto-fintech` | Obsidian & Laser Holography | Dark glass cards, gold/platinum laser tracery, prismatic cubes | Swiss banking meets Web3 luxury, deep navy/black with emerald/gold accents. |
| 15 | `15-photography-studio` | Fine-Art Monochrome & Shadow Play | High-contrast black & white, Venetian blind shadows, silver grain | Masterclass photography portfolio, sculptural light studies, Hasselblad BW. |
| 16 | `16-automotive` | Commercial Automotive Masterpiece | Wet asphalt reflections, neon light streaks, metallic body curvature | Sleek sports vehicle in neon-lit night city or golden hour mountain pass. |
| 17 | `17-pet-care` | Heartwarming Editorial Pet Portrait | Soft studio window light, fluffy tactile fur detail, playful props | High-end pet lifestyle, joyful and clean, crisp eyes and soft bokeh. |
| 18 | `18-coworking-space` | Boutique Scandinavian Workspace | Terrazzo, fluted timber, lush indoor monstera plants, bright sun | Inspiring collaborative hub, design-forward furniture, community warmth. |
| 19 | `19-wedding-planner` | Ethereal Romantic Editorial | Soft lace, champagne bokeh, delicate floral arrangements, golden haze | Dreamy bridal luxury, warm soft-focus romance, fine-art wedding magazine look. |
| 20 | `20-news-magazine` | Documentary Photojournalism | Authentic candid emotion, natural street light, editorial framing | Pulled-from-the-scene journalism, powerful storytelling, gritty authenticity. |
| 21 | `21-scene-doodle-annotation` | Rich Environmental Storytelling Scene | Wide interior shot, layered objects (espresso machine, pastries, counter) | Wide immersive lifestyle scene perfectly framed for interactive hand-drawn hotspots. |
| 22 | `22-shoppable-lifestyle-scene` | Curated Kinfolk Living Space | Staged living room/kitchen with organic products naturally placed | Aesthetic room scene where individual products can be discovered and clicked. |

---

## Execution Workflow

```
1. Parse Manifest
   └── Extract Asset Type, Description, Aspect Ratio, Template Context & Palette
2. Apply 7-Pillar Formula
   └── Blend Subject with Template's Art Direction Archetype & Trend Styling
3. Call `generate_image`
   └── High-fidelity generation, descriptive filenames (hero-banner.webp, product-01.webp)
4. Build Asset Inventory
   └── Classify Needs BG Removal? (Yes/No) and Suggested Tier (standard/high/fine-detail)
5. Handoff to `sdd-build` / `sdd-bg-remover`
```

### Prompt Construction Examples

#### Example 1: Milk Tea / Cafe Hero Product (`04-restaurant-food` or `01-product-carousel`)
```
"Artisanal brown sugar boba milk tea in a sleek ribbed glass cup with tiger stripes of caramelized brown sugar dripping down the sides, topped with delicate foam and a fresh mint leaf. Resting on a smooth circular travertine stone pedestal. Studio lighting with warm golden rim light and subtle backlighting catching liquid translucency. Isolated on a solid clean neutral light-beige background with soft contact shadow for background removal. Shot on 100mm macro f/2.8 lens, high-end commercial beverage photography."
```

#### Example 2: Tech / AI SaaS Hero Graphic (`02-saas-landing` or `06-tech-startup`)
```
"Abstract 3D futuristic AI data sculpture with floating translucent frosted glass sheets, glowing neon purple neural pathways, and liquid mercury metallic spheres. Volumetric soft studio lighting with subtle ambient smoke and caustic glass refractions. Dark obsidian background with deep indigo gradient. Octane render, ultra-modern tech editorial art, 16:9 aspect ratio."
```

#### Example 3: Interactive Bakery Cafe Scene (`21-scene-doodle-annotation`)
```
"Warm sunlit artisanal European bakery interior viewed from a wide perspective. Wooden counter displaying freshly baked golden croissants, sourdough loaves on rustic linen cloths, a polished copper espresso machine with subtle rising steam, and a blackboard menu in the background. Soft morning sunbeams streaming through a large window creating gentle dust motes and warm highlights. Editorial Kinfolk interior photography, richly detailed scene designed for interactive visual exploration."
```

---

## Asset Inventory Specification

After all assets are generated in `public/assets/generated/`, output the structured table:

```markdown
## Generated Assets Manifest (Art Director Curation)

| File | Type | Art Archetype & Description | Needs BG Removal? | Suggested Tier |
|---|---|---|---|---|
| hero-sculpture.webp | hero-banner | 3D Liquid Chrome & Glass Surrealism banner | No | — |
| product-01.webp | product-photo | Artisanal ceramic vase on travertine pedestal | Yes | standard |
| product-02.webp | product-photo | Fluffy hand-knitted alpaca wool scarf | Yes | fine-detail |
| scene-ambiance.webp | lifestyle-scene | Wide sunlit cafe interior for doodle annotations | No | — |
```

### Suggested Tier Guidelines for `sdd-bg-remover`:
- `standard`: Smooth hard edges (bottles, ceramics, phones, solid boxes, cups).
- `high`: Multi-layered complex shapes with partial transparency or interior cutouts (furniture, bicycles, gift baskets).
- `fine-detail`: Delicate organic edges (fluffy animals, spiky fruits, frayed fabrics, intricate lace, hair strands).
- `—`: Environmental scenes, hero banners, background textures (no BG removal needed).

---

## Quality Control & Recovery
- If an image appears overly generic or plastic: immediately revise the prompt with stronger tactile materials (*"raw travertine"*, *"brushed titanium"*, *"35mm film grain"*) and specific lighting conditions (*"chiaroscuro side lighting"*, *"dappled morning sunbeams"*).
- Always ensure visual continuity across all assets generated for the same project — they must share the same lighting temperature and color grading family.
