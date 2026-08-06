---
id: scene-doodle-annotation
name: "Scene Doodle Annotation"
version: 1
category: lifestyle-scene
tags:
  - doodle
  - hand-drawn
  - annotation
  - hotspot
  - interactive-scene
  - bakery
  - cafe
  - boutique
  - interior
  - storytelling
requires_transparent_images: false
uses_shared_interactions:
  - hand-drawn-annotation
color_palette:
  primary: "#3A2A1D"
  secondary: "#E8D9B5"
  accent: "#FFFFFF"
  background: "#2A1F16"
  surface: "#4A3626"
  text: "#FFFFFF"
  muted: "#C9B896"
reactbits_components:
  - name: "Sticker Peel"
    url: "https://www.reactbits.dev/animations/sticker-peel"
best_for: "Bakery, café, cửa hàng boutique, thương hiệu nội thất/lifestyle muốn kể câu chuyện không gian bằng một bức ảnh thật thay vì text — hover để khám phá từng chi tiết như đang xem một cuốn sổ tay được chú thích bằng tay"
fonts:
  display: "Fraunces"
  body: "Inter"
  handwritten: "Caveat"
---

# Template: Scene Doodle Annotation

## Preview Description
Một hero section full-viewport dùng **một bức ảnh không gian thật** (quán café,
bakery, cửa hàng, phòng khách...) làm nền chính — không phải ảnh sản phẩm tách
nền. Toàn bộ tương tác nằm ở việc hover/tap vào các điểm được đánh dấu ngầm
trong ảnh: mỗi điểm khi hover sẽ "tự vẽ" một viền outline nét vẽ tay quanh chi
tiết đó, kéo ra một đường connector cong, và hiện một label chữ viết tay ở cuối
— y hệt cảm giác lật một cuốn sổ tay du lịch được ai đó chú thích bằng bút.
Đây là cách kể câu chuyện thương hiệu bằng không gian thật, thay vì bằng
copywriting hay ảnh sản phẩm dàn dựng.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600&family=Caveat:wght@500;600;700&display=swap" rel="stylesheet" />
```

- **Display font**: `'Fraunces', serif` — headline lớn, tiêu đề section
- **Body font**: `'Inter', sans-serif` — nav, mô tả, nút bấm
- **Handwritten font**: `'Caveat', cursive` — **chỉ** dùng cho label annotation,
  không dùng ở đâu khác trong trang để giữ sự đặc biệt cho hiệu ứng

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#3A2A1D` (Dark Umber) | Text trên nền sáng |
| Secondary | `#E8D9B5` (Warm Sand) | Section background xen kẽ |
| Accent | `#FFFFFF` | Toàn bộ outline/connector/label doodle — luôn trắng để nổi trên ảnh tối |
| Background | `#2A1F16` (Espresso Dark) | Nền tổng thể, viền overlay tối trên ảnh hero |
| Surface | `#4A3626` (Warm Brown) | Card, nav bg on scroll |
| Text | `#FFFFFF` | Trên ảnh hero |
| Muted | `#C9B896` (Sand Gray) | Caption, meta text |

## Layout Structure

### 1. Navigation
- Fixed top, transparent → `surface` color on scroll
- Logo trái, menu phải (Inter, uppercase, tracking-wide)
- CTA nhỏ bên phải: "Ghé thăm chúng tôi"

### 2. Hero — Doodle Annotation Scene (điểm nhấn chính)
- Full-viewport, ảnh không gian thật làm background (`object-fit: cover`)
- Overlay gradient tối nhẹ ở đáy ảnh (giúp text phía dưới dễ đọc): `linear-gradient(to top, rgba(0,0,0,0.5), transparent 40%)`
- 4-6 hotspot đặt tại các chi tiết thật trong ảnh — xem đầy đủ kỹ thuật tại
  `_shared/interactions/hand-drawn-annotation.md`
- Góc dưới trái: tiêu đề thương hiệu (Fraunces, lớn) + 1 dòng tagline
- Góc dưới phải: nút "Khám phá thực đơn" / CTA chính
- Gợi ý nhỏ ở góc trên: text mờ "Di chuột để khám phá" (`hidden sm:block`,
  fade out sau lần hover đầu tiên — chỉ xuất hiện 1 lần để hướng dẫn user)

### 3. Story Strip
- 3 cột ngắn ngay dưới hero: mỗi cột 1 icon + 1 câu ngắn kể một khía cạnh
  thương hiệu (ví dụ: "Nguyên liệu mỗi sáng", "Không gian ấm cúng", "Công thức
  gia truyền")
- Nền `secondary`, text `primary`

### 4. Second Annotation Scene (biến thể nhỏ hơn)
- Một ảnh không gian thứ 2 (góc khác, hoặc cận cảnh khu vực khác) — cùng kỹ
  thuật hotspot nhưng chỉ 2-3 điểm, layout dạng card thay vì full-viewport
  (`aspect-ratio: 16/9`, bo góc, đặt trong container có padding)
- Dùng để kể một câu chuyện phụ (VD: "Góc pha chế", "Bàn làm việc")

### 5. Product/Menu Grid
- Grid chuẩn (không cần hiệu ứng đặc biệt) — ảnh sản phẩm/món, tên, giá
- Có thể tách nền ảnh sản phẩm ở đây nếu muốn (khác với ảnh scene ở hero —
  ảnh scene giữ nguyên background thật)

### 6. Testimonial / Quote
- Trích dẫn lớn, Fraunces italic, giữa trang, nền `secondary`

### 7. Location & Hours
- Giống pattern của template `restaurant-food`: map + giờ mở cửa + địa chỉ

### 8. Footer
- Logo, social, nav, copyright — nền `background` tối

## State & Logic

```typescript
// Hotspot data cho 1 scene
interface Hotspot {
  id: string;
  x: number; y: number; width: number; height: number; // % theo ảnh
  label: string;
  connectorAngle: number;
  connectorLength: number;
}

const [activeHotspot, setActiveHotspot] = useState<string | null>(null);
const [hasHoveredOnce, setHasHoveredOnce] = useState(false); // ẩn hint "di chuột" sau lần đầu
const [isMobile, setIsMobile] = useState(window.innerWidth < 640);

// Mobile: tap thay vì hover, tự tắt sau 3s
useEffect(() => {
  if (isMobile && activeHotspot) {
    const timer = setTimeout(() => setActiveHotspot(null), 3000);
    return () => clearTimeout(timer);
  }
}, [activeHotspot, isMobile]);
```
Full chi tiết render outline/connector/label: xem `hand-drawn-annotation.md`.

## Prompt

Build a full-viewport hero section in React + TypeScript + Vite + Tailwind CSS
using a **real photographic space** (not a product cutout) as the background,
with **hover-triggered hand-drawn SVG annotations**.

**Fonts:** Fraunces (display), Inter (body), Caveat (handwritten labels only).

**Hero:** Full-bleed photo (`object-fit: cover`), dark gradient overlay at
bottom. Place 4-6 invisible `<button>` hotspots over meaningful details in the
photo. On hover/focus: (1) a wobbly white SVG outline draws itself around the
hotspot zone via `stroke-dashoffset` animation + `feTurbulence`/
`feDisplacementMap` filter for hand-drawn jitter (500ms); (2) a curved SVG
connector path draws outward from the zone (400ms, starts 150ms after outline);
(3) a handwritten-font (`Caveat`) label fades + scales in at the connector's
end (250ms, starts 500ms after hover). Only one hotspot active at a time.
Bottom-left: brand title (Fraunces) + tagline. Bottom-right: CTA button.
One-time hint text "Di chuột để khám phá" that fades out after first hover.

**Mobile:** tap instead of hover, auto-dismiss the active hotspot after 3s.

**Below hero:** 3-column story strip, a second smaller annotation scene card
(2-3 hotspots), product/menu grid, testimonial quote, location/hours, footer.

## Required Assets
- `hero-scene` — Ảnh không gian chính, độ phân giải cao, đủ chi tiết để đặt
  4-6 hotspot có ý nghĩa (KHÔNG tách nền — giữ nguyên ảnh chụp thật)
- `secondary-scene` — Ảnh không gian phụ cho section 4
- Ảnh sản phẩm/món cho grid ở section 5 (có thể tách nền tuỳ ý)

## ReactBits Components Used
- **Sticker Peel** (`https://www.reactbits.dev/animations/sticker-peel`) —
  optional, dùng cho các badge/sticker trang trí phụ (VD: "Mới!", "Bán chạy")
  đặt cạnh hero, không phải cho chính hiệu ứng annotation (đó là SVG tự viết).
