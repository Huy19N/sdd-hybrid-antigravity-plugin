---
name: sdd-asset-generator
version: 3
changelog:
  - "v3: added Game Asset Generation Mode (2D/2.5D) — parallax composite scenes (paired with sdd-bg-remover's new segment_layers.py for layer decomposition), character sprites with pose/frame consistency guidance, and tileable textures (paired with the new scripts/make_tileable.py seam-fixing script)."
description: "Sub-skill automatically invoked by sdd-build when plan.md contains a Design Template section (web) OR a Game Asset Requirements section (2D/2.5D game). Do NOT trigger manually. Functions as an elite Art Director & Visual Concept Designer using the generate_image tool to produce high-artistry, curated visual assets tailored to the chosen template's mood/theme, or to a game project's parallax layers, sprites, and textures."
---

# SDD Asset Generator (Art Director Edition v3)

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
This skill is **automatically called** by `sdd-build` in one of two modes:
- **Web mode**: when `plan.md` contains a `## Design Template` section. Runs
  before the first UI-related task in the plan.
- **Game mode** (mới, v3): when `plan.md` contains a `## Game Asset
  Requirements` section. Runs before the first scene/sprite integration task.

Never trigger this skill directly — `sdd-build` handles the orchestration.

## Preconditions

**Web mode:**
- `docs/sdd/<feature-slug>/plan.md` exists with a `## Design Template` section.
- The Design Template section includes a `Required Assets` list.
- The template's color palette is specified.

**Game mode:**
- `docs/sdd/<feature-slug>/plan.md` exists with a `## Game Asset Requirements`
  section listing: game type (2D side-scroller / 2.5D / top-down...), art
  style (pixel art / painterly / flat vector...), and a list of needed scenes/
  sprites/textures.
- If any asset needs tileable-texture post-processing, Python 3.10+ and
  `Pillow`/`numpy` available (for `scripts/make_tileable.py`).
- If any asset is a Parallax Composite Scene requiring layer decomposition,
  `sdd-bg-remover`'s `segment_layers.py` dependencies must be installable
  later in the pipeline (not required at this skill's own run time — this
  skill only produces the composite image + label list; decomposition is
  `sdd-bg-remover`'s job).

---

## The 7-Pillar Master Prompt Architecture (Web Mode)

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

---

## Multi-Tier Cascade Generation Engine (Cơ Chế Chống Tràn Quota Đa Tầng)

Để đảm bảo việc sinh ảnh **không bao giờ bị dừng hay báo lỗi hết quota**, skill sử dụng cơ chế thác đổ đa tầng (*Cascade Fallback Engine*):

| Tầng (Tier) | Engine / Nguồn | Chi phí / Quota | Khi nào kích hoạt |
|---|---|---|---|
| **Tier 1 (Default Native)** | Antigravity IDE `generate_image` Tool (Google Nano Banana / Imagen 3) | Sử dụng trực tiếp Quota của Antigravity IDE Session | Luôn được ưu tiên gọi đầu tiên khi chạy trên Antigravity IDE (Không cần API key) |
| **Tier 2 (API Key)** | Google GenAI SDK (`imagen-3.0-generate-002`) | Sử dụng quota `GEMINI_API_KEY` của người dùng | Khi `generate_image` báo lỗi hoặc chạy ngoài IDE và có sẵn `GEMINI_API_KEY` |
| **Tier 3 (Free Zero-Quota)** | Pollinations.ai FLUX.1 / SDXL Engine | **Miễn phí 100%, không giới hạn lượt, không cần API Key** | Tự động kích hoạt khi Tier 1 & Tier 2 hết quota hoặc gặp lỗi 429 Rate Limit |
| **Tier 4 (Custom Provider)** | OpenAI DALL-E 3 / Stability AI / MCP Server | Quota theo key `OPENAI_API_KEY` | Khi người dùng cấu hình key OpenAI hoặc MCP server tùy biến |

### Quy tắc thực thi tự động của Agent:
1. **Bước 1**: Agent gọi tool `generate_image` với prompt đã chuẩn hóa theo 7-Pillar Formula.
2. **Bước 2**: Nếu tool `generate_image` thành công → Tiến hành bước tiếp theo.
3. **Bước 3**: Nếu tool `generate_image` trả về lỗi Quota Exhausted / Rate Limit (429) hoặc không khả dụng:
   - Agent **ngay lập tức chạy script fallback tự động**:
     ```bash
     python skills/sdd-asset-generator/scripts/generate_image_fallback.py \
       --prompt "<7-pillar prompt>" \
       --output public/assets/generated/<file-name>.webp \
       --aspect-ratio <16:9 | 1:1 | 9:16>
     ```
   - Script sẽ tự động luân chuyển qua các provider khả dụng để sinh ảnh thành công mà không làm gián đoạn tiến trình build!

---

## Execution Workflow

```
1. Parse Manifest
   └── Extract Asset Type, Description, Aspect Ratio, Template Context & Palette
2. Apply 7-Pillar Formula
   └── Blend Subject with Template's Art Direction Archetype & Trend Styling
3. Generate Asset via Cascade Engine
   ├── Try 1: Call `generate_image` tool (Antigravity IDE Native Quota)
   └── If Quota Limit: Run `scripts/generate_image_fallback.py` (FLUX.1 Zero-Quota Fallback)
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

## Module-Specific Art Asset Generation (Đồng bộ hóa với Shared Modules)

Khi `plan.md` liệt kê các module đặc thù từ `_shared/`, áp dụng quy chuẩn prompt sau:

### 1. Module `interactive-split-slider` (CẶP ẢNH SONG SINH DUAL-STATE)
- **Quy tắc**: Phải sinh **2 bức ảnh** (`split-before.webp` và `split-after.webp`) có cùng góc máy (cùng tiêu cự, tỷ lệ khung hình, khoảng cách camera và góc nhìn), chỉ thay đổi trạng thái hoặc thời điểm:
  - *Ví dụ Day/Night cho Bất động sản / Quán cafe*:
    - Ảnh 1 (Day): `"Sunlit modern architecture with floor-to-ceiling glass, bright morning sunbeams, 24mm architectural lens, natural bright daylight."`
    - Ảnh 2 (Night): `"Same modern architecture angle, moody blue hour night scene, warm amber interior lights glowing through glass, dusk atmosphere, 24mm architectural lens."`
  - *Ví dụ Raw/Finished cho Sản phẩm thủ công / F&B*:
    - Ảnh 1 (Raw): `"Uncut raw cocoa pods and raw organic ingredients styled on dark stone, macro 100mm f/2.8."`
    - Ảnh 2 (Finished): `"Exquisite artisanal dark chocolate bonbons with golden leaf flakes in the exact same staging and camera angle, macro 100mm f/2.8."`

### 2. Module `holographic-shimmer` (CHẤT LIỆU CHROME & THỦY TINH TÁN SẮC)
- **Quy tắc**: Tạo vật thể/sản phẩm có bề mặt chrome bóng, thủy tinh hữu cơ mờ gân sóng hoặc kim loại đánh bóng. Nền tối màu (Obsidian / Dark Charcoal) để lớp phủ gradient cầu vồng CSS tỏa sáng rực rỡ mà không bị bão hòa màu trắng.

### 3. Module `ambient-glow-cursor` (ĐỘ TƯƠNG PHẢN & ÁNH SÁNG VEN RIM-LIGHT)
- **Quy tắc**: Sinh ảnh icon 3D hoặc banner có ánh sáng viền (*Fresnel rim-light*) sắc sảo, tông màu chủ đạo hài hòa với màu của vệt sáng spotlight (`--glow-color`).

### 4. Module `circular-badge-stamp` (BỐ CỤC THOÁNG CHỜ CON DẤU)
- **Quy tắc**: Bố cục sản phẩm theo quy tắc 1/3 (lệch trái hoặc lệch phải), chừa khoảng trống âm tự nhiên (*negative space*) ở góc đối diện để con dấu xoay SVG ngự trị tự nhiên.

### 5. Module `stories-avatar-tray` (ẢNH DỌC 9:16 & AVATAR TRÒN 1:1)
- **Quy tắc**: Sinh ảnh chất lượng cao định dạng dọc 9:16 (`story-01.webp`, `story-02.webp`) và avatar tròn 1:1 (`avatar-01.webp`) có độ bão hòa màu cao, tương phản ấn tượng để hút mắt khi hiển thị trong khay story.

### 6. Module `kinetic-splash-layering` (CHẤT LỎNG TỐC ĐỘ CAO & VỆT BẮN LI TI HIGH-SPEED 1/8000s)
- **Quy tắc**: Yêu cầu chụp tốc độ cực cao (*ultra-high-speed freeze motion at 1/8000s shutter speed*) để bắt trọn từng giọt nước, vệt trà sữa văng trong không trung, bọt khí và khúc xạ ánh sáng caustics sắc như dao.
- **Background**: Đặt trên nền tối tuyền (*solid matte obsidian/black background*) hoặc nền tương phản đơn sắc với ánh sáng viền (*volumetric rim light*) để `sdd-bg-remover` (tier `fine-detail` / `birefnet-dis`) bóc tách viền giọt nước siêu mảnh mà không bị viền lem.
- **Decomposition Labels (nếu dùng segment_layers.py)**: `["back liquid splash corona", "main glass cup with beverage", "flying toppings and front droplets"]`.

---

## Mobile & Store-Ready Asset Specifications (Dành cho App Android & iOS)

Khi `plan.md` nhắm tới nền tảng Mobile App (Expo / Flutter / Kotlin), tự động tạo các asset sau:

1. **App Icon 1:1 (`app-icon.webp` / `icon.png` 1024x1024)**:
   - *"Minimalist luxury app icon for [App Name], sleek geometric emblem with subtle gold metallic sheen, isolated on dark matte obsidian background, vector clarity, iOS App Store & Google Play style, centered composition, 1:1 square."*
2. **Android Adaptive Icon Foreground (`adaptive-icon-foreground.webp`)**:
   - Biểu tượng chính độc lập trên nền trong suốt (hoặc nền trắng), an toàn trong vùng safe zone tròn 66dp.
3. **Mobile Splash Screen 9:16 (`splash.webp`)**:
   - Logo hoặc biểu tượng tối giản đặt chính giữa nền chuyển sắc êm dịu, không chứa text nhỏ, tỷ lệ chuẩn 9:16 (1242x2688 hoặc 1080x1920).
4. **Mobile Hero Cards 4:5 & 9:16**:
   - Ảnh sản phẩm và bối cảnh bố cục dọc, vùng nét tập trung ở 2/3 phần trên, 1/3 phần dưới tối dần để phủ text thông tin sản phẩm và nút bấm.



---

## Game Asset Generation Mode (2D / 2.5D) — mới, v3

Khi `plan.md` có section `## Game Asset Requirements`, chuyển hẳn sang bộ quy
tắc này thay vì 7-Pillar Formula ở trên (dành cho web UI). Có 3 loại asset
chính, mỗi loại có yêu cầu prompt khác hẳn nhau.

### Loại 1 — Parallax Composite Scene
Một ảnh cảnh DUY NHẤT, chứa nhiều vùng ngữ nghĩa rõ ràng để sau này
`sdd-bg-remover` (`segment_layers.py`) tách thành các layer riêng cho hiệu
ứng parallax (nền xa cuộn chậm, tiền cảnh cuộn nhanh).

**Nguyên tắc prompt bắt buộc — quyết định segmentation có chính xác hay
không:**
- Vẽ theo phong cách **phẳng/hoạt hình có đường viền rõ** (flat illustration,
  painterly with clear silhouettes) thay vì photoreal có gradient mờ hoà lẫn
  giữa các vùng — CLIPSeg tách vùng có ranh giới rõ tốt hơn nhiều so với ảnh
  mọi thứ hoà vào nhau (VD: sương mù làm mây và trời dính liền).
- Liệt kê **rõ ràng từng vùng cần tách được** ngay trong prompt, dùng đúng từ
  sẽ dùng làm nhãn sau này (không đổi từ giữa chừng — "cloud" trong prompt
  phải khớp đúng nhãn "cloud" đưa cho `segment_layers.py`).
- Composition theo lớp độ sâu rõ ràng: bầu trời/nền xa ở trên/phía sau, tiền
  cảnh ở dưới/phía trước — layer xa nên đơn giản/ít chi tiết hơn (vì sẽ cuộn
  chậm, ít bị soi kỹ), layer gần chi tiết hơn (cuộn nhanh, ở gần mắt người
  chơi).

**Prompt mẫu:**
```
"2D side-scroller game background, flat painterly illustration style with
clean silhouettes and clear color separation between elements. Layered scene
from back to front: pale gradient sky, 3 distinct puffy white clouds with
crisp edges, a row of soft blue-gray distant mountains, a cluster of green
pine trees with clear trunk silhouettes, a weathered wooden fence post in the
foreground, and a grassy ground plane. Warm afternoon lighting, cohesive
color palette, no photorealistic blending between elements — each element
must read as a distinct clean shape."
```

**Output đi kèm bắt buộc**: danh sách "Decomposition Labels" theo đúng thứ tự
từ xa tới gần, khớp chính xác với các vùng đã mô tả trong prompt — đây là
input trực tiếp cho `segment_layers.py --labels`.

### Loại 2 — 2D Character Sprite
Nhân vật/vật thể động, luôn cần nền trong suốt, và **nhất quán qua nhiều
frame** (idle, walk, run...) — đây là điểm khó nhất vì `generate_image` không
có trí nhớ nhân vật giữa các lần gọi độc lập.

**Kỹ thuật giữ nhất quán (bắt buộc áp dụng):**
- Viết 1 đoạn "character sheet" mô tả cực chi tiết (màu sắc chính xác, tỷ lệ,
  trang phục, kiểu tóc/đặc điểm riêng) — **copy nguyên văn đoạn này vào đầu
  mọi prompt frame khác nhau** của cùng nhân vật, không diễn đạt lại bằng từ
  khác mỗi lần (dù chỉ đổi 1 từ cũng có thể làm model vẽ ra người khác).
- Nếu tool `generate_image` hỗ trợ ảnh tham chiếu (image-to-image/reference
  image) — dùng frame đầu tiên làm ảnh tham chiếu cho các frame sau, đáng tin
  cậy hơn nhiều so với chỉ dựa vào text. Kiểm tra khả năng này của tool trước
  khi cần nhất quán nhiều frame.
- Luôn có "single frame, transparent background, consistent [X]px pixel grid"
  (nếu pixel art) hoặc "consistent line weight and color palette" (nếu vector/
  painterly) trong mọi prompt.

**Prompt mẫu (character sheet + 1 frame):**
```
"[CHARACTER SHEET: A small fox knight, orange fur with white chest patch,
wearing a dented bronze breastplate and a tiny red cape, round black eyes,
holding a wooden sword. Flat 2D game art style, thick 3px black outline,
cel-shaded flat colors, no gradients.]
Pose: mid-stride walk cycle frame 2 of 8, facing right, front-left leg raised.
Transparent background, isolated character only, consistent proportions with
reference."
```

### Loại 3 — Tileable/Seamless Texture
Texture nền lặp lại (đất, tường, sàn platform) — cần khớp mép khi tile liên
tục.

**Nguyên tắc prompt:**
- Thêm rõ "seamless tileable texture, repeating pattern, no focal point, edge
  content matches opposite edge" vào prompt.
- Tránh yêu cầu chi tiết lớn/độc nhất gần rìa ảnh (VD: "một tảng đá lớn ở góc")
  — chi tiết lớn gần biên gần như luôn lộ rõ khi tile.

**Hậu kỳ bắt buộc sau khi generate** (image-gen hiếm khi seamless hoàn hảo
ngay lần đầu):
```bash
python skills/sdd-asset-generator/scripts/make_tileable.py \
  --input public/assets/generated/ground-tile-raw.webp \
  --output public/assets/generated/ground-tile.png \
  --blend-width 48
```
Script này dùng kỹ thuật offset+feather chuẩn (dời ảnh nửa chu kỳ rồi làm mờ
có kiểm soát đúng vùng mép) — không phải phép màu, chỉ là xấp xỉ tự động của
thao tác retouch thủ công. Với texture cần nhìn cận cảnh/hero, vẫn nên chỉnh
tay thêm sau bước này. Script tự báo điểm "edge-mismatch" trước/sau để biết
có cần chỉnh tay tiếp không.

### Depth cue cho cảm giác 2.5D (áp dụng cho mọi loại asset trên)
- Layer càng xa: màu nhạt hơn/lạnh hơn (aerial perspective), ít chi tiết hơn,
  contrast thấp hơn.
- Layer càng gần: màu đậm/ấm hơn, nhiều chi tiết hơn, contrast cao hơn.
- Gợi ý tốc độ parallax tương đối theo độ sâu, ghi vào Asset Inventory (xem
  bảng mới bên dưới): trời/mây xa nhất ≈ 0.1-0.2x tốc độ cuộn chính, núi xa
  ≈ 0.3-0.4x, cây/tiền cảnh giữa ≈ 0.6-0.8x, tiền cảnh sát nhất ≈ 1.0x+ (có
  thể nhanh hơn tốc độ cuộn chính để tăng cảm giác chiều sâu).

---

## Asset Inventory Specification — Game Mode

```markdown
## Generated Game Assets Manifest

| File | Type | Description | Decomposition Labels | Layer Order | Parallax Speed |
|---|---|---|---|---|---|
| forest-scene.webp | parallax-composite | Layered forest background, 6 regions | sky, cloud, distant mountain, tree, wooden fence post, ground | 1 (composite, cần tách) | — |
| fox-knight-walk-01.webp | character-sprite | Fox knight walk frame 1/8 | — | — | — |
| ground-tile.png | tileable-texture | Grass/dirt ground tile, đã qua make_tileable.py | — | — | 1.0x (tiền cảnh) |
```

---

## Asset Inventory Specification — Web Mode

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
