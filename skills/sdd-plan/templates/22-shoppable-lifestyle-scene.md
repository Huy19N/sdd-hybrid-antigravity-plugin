---
id: shoppable-lifestyle-scene
name: "Shoppable Lifestyle Scene"
version: 1
category: shoppable-scene
tags:
  - ecommerce
  - shop-the-look
  - lifestyle
  - hotspot
  - product-scene
  - organic
  - grocery
  - home-decor
  - interactive-scene
requires_transparent_images: false
uses_shared_interactions:
  - hand-drawn-annotation
color_palette:
  primary: "#2F4A34"
  secondary: "#F3EDE0"
  accent: "#D97B4F"
  background: "#FBF8F1"
  surface: "#FFFFFF"
  text: "#2F4A34"
  muted: "#8C9A87"
reactbits_components:
  - name: "Circular Gallery"
    url: "https://www.reactbits.dev/components/circular-gallery"
  - name: "Sticker Peel"
    url: "https://www.reactbits.dev/animations/sticker-peel"
best_for: "Cửa hàng thực phẩm hữu cơ, rau củ, grocery, home-decor, thời trang lifestyle — nơi user 'mua trực tiếp từ khung cảnh' thay vì lướt grid sản phẩm rời rạc. Tham khảo tinh thần Vegist (Shopify organic/grocery theme)"
fonts:
  display: "Fraunces"
  body: "Inter"
  handwritten: "Caveat"
---

# Template: Shoppable Lifestyle Scene

## Preview Description
Khác với `scene-doodle-annotation` (kể chuyện thương hiệu bằng label chữ),
template này dùng **cùng kỹ thuật hand-drawn hover** nhưng mỗi hotspot khi
active sẽ mở ra một **mini product card nổi** (ảnh, tên, giá, nút thêm giỏ
hàng nhanh) ngay trên khung cảnh — biến một bức ảnh lifestyle (bàn bếp, kệ
hàng, góc phòng khách) thành một "cửa hàng ẩn trong ảnh". Đây là hướng tiếp
cận "shop the scene" — lấy cảm hứng tinh thần tương tác/hình ảnh sản phẩm của
theme Vegist (Shopify, organic/grocery) nhưng thay vì grid sản phẩm tĩnh, sản
phẩm "sống" trong một khung cảnh thật.

## Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=Caveat:wght@500;600&display=swap" rel="stylesheet" />
```

- **Display font**: `'Fraunces', serif` — tiêu đề, tên section
- **Body font**: `'Inter', sans-serif` — giá, mô tả, nút bấm, product card
- **Handwritten font**: `'Caveat', cursive` — chỉ dùng cho micro-label kiểu
  "Mới hái sáng nay 🌱" xuất hiện thoáng qua trước khi product card hiện ra
  (xem "Interaction Sequence" bên dưới)

## Color Palette

| Role | Color | Usage |
|---|---|---|
| Primary | `#2F4A34` (Deep Forest) | Text, nút chính |
| Secondary | `#F3EDE0` (Warm Linen) | Section background xen kẽ |
| Accent | `#D97B4F` (Terracotta) | Giá tiền, nút "Thêm vào giỏ", badge |
| Background | `#FBF8F1` (Off-White) | Nền tổng thể |
| Surface | `#FFFFFF` | Product card |
| Text | `#2F4A34` | Text chính |
| Muted | `#8C9A87` (Sage Gray) | Mô tả phụ, meta |

## Interaction Sequence (khác với scene-doodle-annotation ở bước cuối)

Dùng chung Layer 1 + Layer 2 (outline + connector) từ
`_shared/interactions/hand-drawn-annotation.md`, nhưng thay Layer 3:

1. Outline nét vẽ tay quanh sản phẩm trong ảnh (500ms) — giống hệt spec chung.
2. Connector line cong vẽ ra (400ms).
3. Thay vì label text đơn thuần, một **micro-label viết tay** hiện trước
   (VD: "Mới hái sáng nay") trong 400ms.
4. Ngay sau đó, micro-label mờ dần và được thay bằng **product card** nổi
   (fade + scale from 0.9 → 1, 250ms): ảnh thumbnail nhỏ (80x80, bo góc),
   tên sản phẩm (Inter semibold), giá (Inter bold, màu accent), nút tròn nhỏ
   "+" để thêm giỏ hàng nhanh (không rời khỏi trang).
5. Click nút "+" → animation ảnh sản phẩm "bay" về icon giỏ hàng trên nav
   (dùng FLIP animation hoặc đơn giản là scale+fade tại chỗ nếu muốn giữ
   nhẹ nhàng) + badge số lượng trên icon giỏ hàng tăng lên.

## Layout Structure

### 1. Navigation
- Fixed top, nền `background` với border-bottom mỏng
- Logo trái, nav links giữa, icon giỏ hàng phải (có badge số lượng, animate
  khi có item mới)
- Nút nav CTA (nếu có) wrap với `HandDrawnButton` border-only (biến thể
  `button-hover` từ `_shared/interactions/hand-drawn-annotation.md`)

### 2. Hero — Shoppable Scene
- Full-viewport hoặc `80vh`, ảnh lifestyle thật (bàn ăn bày biện, kệ bếp, góc
  sống...) làm nền
- 4-6 hotspot đặt tại các sản phẩm thật xuất hiện trong ảnh
- Text overlay góc trên: headline ngắn (Fraunces) — VD: "Từ nông trại đến bàn
  ăn của bạn"
- Không cần CTA rời rạc — bản thân hotspot chính là CTA

### 3. Category Strip
- Thanh ngang các category tròn (ảnh tròn + tên): Rau củ, Trái cây, Đồ khô,
  Gia vị... — style giống mega-menu/category filter mà Vegist dùng, nhưng bo
  tròn và có hover lift nhẹ

### 4. Second Shoppable Scene (biến thể nhỏ)
- Một khung cảnh khác (VD: góc bếp, kệ gia vị) dạng card `aspect-ratio: 4/3`,
  2-3 hotspot, cùng interaction sequence

### 5. Featured Products (Circular Gallery)
- Dùng ReactBits Circular Gallery cho các sản phẩm nổi bật — bổ sung, không
  thay thế shoppable scene, dành cho user muốn lướt nhanh thay vì khám phá

### 6. Trust Strip
- 3-4 icon ngắn: "100% hữu cơ", "Giao trong ngày", "Không hoá chất"...

### 7. Newsletter / Farm Story
- Ảnh nông trại/nguồn gốc + form đăng ký nhận tin, nền `secondary`

### 8. Footer
- Logo, social, nav, payment icons, copyright

## State & Logic

```typescript
interface ShoppableHotspot {
  id: string;
  x: number; y: number; width: number; height: number;
  microLabel: string;      // "Mới hái sáng nay"
  product: {
    thumbnail: string;
    name: string;
    price: string;
  };
  connectorAngle: number;
  connectorLength: number;
}

type HotspotPhase = 'idle' | 'outline' | 'micro-label' | 'product-card';

const [activeHotspot, setActiveHotspot] = useState<string | null>(null);
const [phase, setPhase] = useState<HotspotPhase>('idle');
const [cartCount, setCartCount] = useState(0);

// Chuyển phase theo timeline: outline(0ms) -> micro-label(500ms) -> product-card(900ms)
useEffect(() => {
  if (!activeHotspot) { setPhase('idle'); return; }
  setPhase('outline');
  const t1 = setTimeout(() => setPhase('micro-label'), 500);
  const t2 = setTimeout(() => setPhase('product-card'), 900);
  return () => { clearTimeout(t1); clearTimeout(t2); };
}, [activeHotspot]);

const addToCart = (productId: string) => {
  setCartCount(prev => prev + 1);
  // trigger fly-to-cart animation
};
```

## Prompt

Build a shoppable hero scene in React + TypeScript + Vite + Tailwind CSS. A real
lifestyle photo (not a product cutout) is the background, with hover/tap
hotspots that reveal a hand-drawn annotation sequence ending in a live product
card.

**Fonts:** Fraunces (display), Inter (body/product data), Caveat (micro-label
only).

**Interaction per hotspot** (reuse SVG spec from
`_shared/interactions/hand-drawn-annotation.md` for outline + connector):
outline draws in (500ms) → connector draws out (400ms) → a handwritten
micro-label appears briefly (400ms) → fades and is replaced by a floating
product card (thumbnail 80x80, name, price in accent color, round "+"
add-to-cart button) that scale+fades in. Clicking "+" increments a cart badge
in the nav with a small fly/scale animation.

**Sections:** shoppable hero scene (4-6 hotspots) → rounded category strip →
second smaller shoppable scene card (2-3 hotspots) → Circular Gallery featured
products → trust strip icons → farm-story newsletter section → footer.

**Color system:** deep forest green `#2F4A34`, warm linen `#F3EDE0`,
terracotta accent `#D97B4F`, off-white background `#FBF8F1`.

## Required Assets
- `hero-lifestyle-scene` — Ảnh khung cảnh chính có nhiều sản phẩm thật trong
  khung hình (KHÔNG tách nền)
- `secondary-scene` — Ảnh khung cảnh phụ cho section 4
- Ảnh thumbnail sản phẩm (vuông, có thể tách nền) cho product card + category
  strip + Circular Gallery
- `farm-story` — Ảnh nguồn gốc/nông trại cho section 7

## ReactBits Components Used
- **Circular Gallery** (`https://www.reactbits.dev/components/circular-gallery`)
  — Featured Products section.
- **Sticker Peel** (`https://www.reactbits.dev/animations/sticker-peel`) —
  optional badge hiệu ứng cho nhãn "Hữu cơ 100%" trên category strip.
