---
id: hand-drawn-annotation
name: "Hand-Drawn Scene Annotation"
type: shared-interaction
version: 2
changelog:
  - "v2: added Button Hover Border variant — same wobbly SVG technique applied directly to buttons on hover/focus, with an optional connector+label callout for standalone hero CTAs. Pure CSS, no JS state needed for this variant."
variants:
  - scene-hotspot   # bản gốc: hotspot trên ảnh nền, đa điểm, cần JS state điều phối
  - button-hover     # mới v2: viền quanh 1 button, đơn điểm, không cần JS state
used_by:
  - restaurant-food
  - scene-doodle-annotation
  - shoppable-lifestyle-scene
compatible_with_buttons: all   # biến thể button-hover dùng được cho MỌI template có CTA button
---

# Shared Interaction: Hand-Drawn Scene Annotation

Kỹ thuật hover: viền outline nét vẽ tay (wobbly SVG border) bao quanh vùng hover,
kèm connector line cong animate + label chữ viết tay ở cuối đường — phong cách
annotation/doodle overlay. File này có **2 biến thể** dùng cùng 1 kỹ thuật lõi:

1. **`scene-hotspot`** (bản gốc) — nhiều điểm trên 1 ảnh nền, cần JS state để
   chỉ 1 điểm active tại một thời điểm. Xem Layer 1-3 bên dưới.
2. **`button-hover`** (mới, v2) — viền quanh 1 button khi hover/focus, dùng
   thuần CSS `:hover`/`:focus-visible`, **không cần JS state**. Xem mục
   "Biến thể: Button Hover Border" ở cuối file.

Đây **không phải** component có sẵn của ReactBits — là SVG filter + path
animation tự viết.

## Biến thể `scene-hotspot` — chi tiết kỹ thuật (bản gốc)
*(Các mục Font → Giới hạn hiệu năng bên dưới đều thuộc biến thể này. Biến thể
`button-hover` mới nằm ở mục riêng cuối file.)*

## Font chữ viết tay

```html
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&display=swap" rel="stylesheet" />
```
Dùng `'Caveat', cursive` cho label. Phương án thay thế nếu muốn nét đậm hơn:
`Kalam` hoặc `Patrick Hand`.

## Cấu trúc dữ liệu 1 hotspot

```typescript
interface Hotspot {
  id: string;
  x: number;              // % theo chiều ngang trên ảnh nền (0-100)
  y: number;               // % theo chiều dọc
  width: number;            // % width vùng outline (relative to image)
  height: number;
  label: string;            // text viết tay, VD: "Floral Delight"
  connectorAngle: number;   // góc (deg) đường connector toả ra từ hotspot
  connectorLength: number;  // px, độ dài đường connector
}
```

## Layer 1 — Outline nét vẽ tay quanh vùng hover

SVG filter tạo độ "wobble" tự nhiên như nét bút chì, áp lên một `<rect>` viền:

```html
<filter id="handDrawnWobble">
  <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="3" result="noise" />
  <feDisplacementMap in="SourceGraphic" in2="noise" scale="4" />
</filter>
```

```tsx
<rect
  x={hotspot.x} y={hotspot.y}
  width={hotspot.width} height={hotspot.height}
  rx="6" fill="none" stroke="#FFFFFF" strokeWidth="2.5"
  filter="url(#handDrawnWobble)"
  style={{
    strokeDasharray: perimeter,
    strokeDashoffset: isActive ? 0 : perimeter,
    transition: 'stroke-dashoffset 500ms cubic-bezier(0.65,0,0.35,1)',
  }}
/>
```
`perimeter` = `2*(width+height)`, tính 1 lần khi mount, không tính lại mỗi render.

## Layer 2 — Connector line cong + dot marker

```tsx
const pathRef = useRef<SVGPathElement>(null);
const [pathLength, setPathLength] = useState(0);

useEffect(() => {
  if (pathRef.current) setPathLength(pathRef.current.getTotalLength());
}, []);

<path
  ref={pathRef}
  d={`M ${startX} ${startY} Q ${controlX} ${controlY} ${endX} ${endY}`}
  fill="none" stroke="#FFFFFF" strokeWidth="1.5" strokeLinecap="round"
  style={{
    strokeDasharray: pathLength,
    strokeDashoffset: isActive ? 0 : pathLength,
    transition: 'stroke-dashoffset 400ms ease-out 150ms', // delay sau khi outline vẽ xong
  }}
/>
<circle cx={startX} cy={startY} r="3" fill="#FFFFFF"
  style={{ opacity: isActive ? 1 : 0, transition: 'opacity 200ms' }} />
```

## Layer 3 — Label viết tay ở cuối connector

```tsx
<div style={{
  position: 'absolute', left: endX, top: endY,
  fontFamily: "'Caveat', cursive", fontSize: '28px', color: '#FFFFFF',
  transform: `rotate(${hotspot.id.length % 2 === 0 ? -3 : 4}deg) scale(${isActive ? 1 : 0.85})`,
  opacity: isActive ? 1 : 0,
  transition: 'opacity 250ms ease-out 500ms, transform 250ms ease-out 500ms',
  pointerEvents: 'none',
}}>
  {hotspot.label}
</div>
```
Delay `500ms` = sau khi outline (500ms) + connector (400ms bắt đầu ở 150ms) vẽ
gần xong — label xuất hiện cuối cùng, đúng thứ tự "vẽ tay" tự nhiên.

## Trạng thái & trigger

```typescript
const [activeHotspot, setActiveHotspot] = useState<string | null>(null);
// Desktop: onMouseEnter(hotspot.id) / onMouseLeave(() => setActiveHotspot(null))
// Mobile: onClick toggle, tự tắt sau 3000ms hoặc khi tap ra ngoài ảnh
```
Chỉ 1 hotspot active tại một thời điểm để tránh rối mắt — hotspot khác được
hover sẽ tự tắt hotspot đang active trước đó (không cần đợi animation reverse).

## Accessibility
- Mỗi hotspot trigger là `<button>` (không phải `<div>` bare) với
  `aria-label={hotspot.label}`, `tabIndex={0}`.
- Trigger animation giống hệt trên `:focus-visible` như trên `:hover`.
- Touch target tối thiểu 44x44px kể cả khi outline vùng ảnh nhỏ hơn.

## Giới hạn hiệu năng
- Tối đa 5-6 hotspot trên một ảnh nền — nhiều hơn sẽ rối và tốn animation
  frame đồng thời nếu user di chuột nhanh qua nhiều điểm.
- Precompute toàn bộ `perimeter`/`pathLength` một lần khi mount, không tính lại
  trong render loop.

---

## Biến thể `button-hover` — Viền nét vẽ tay quanh button (v2)

Khác với `scene-hotspot` (nhiều điểm trên ảnh, cần JS điều phối), biến thể
này áp cho **1 button đơn lẻ** — dùng thuần `:hover`/`:focus-visible`,
**không cần JS state**. Dùng được cho **mọi** button ở mọi template, không
giới hạn ở các template đã tích hợp `scene-hotspot`.

### Vấn đề kỹ thuật cần giải quyết
Hotspot trên ảnh có vị trí/kích thước cố định theo %, tính `perimeter` một
lần là đủ. Button thì **auto-width theo text** (VD: "Đặt Món Tại Quầy" và
"Khám Phá Menu" trong ảnh bạn gửi dài ngắn khác nhau) — không thể precompute
1 path cố định cho mọi button. Giải pháp: dùng thuộc tính SVG `pathLength`
(chuẩn hoá độ dài path về đúng 100 bất kể kích thước thật render ra), kết hợp
`viewBox` + `preserveAspectRatio="none"` để SVG tự giãn theo đúng kích thước
button — không cần đo `getBoundingClientRect()` hay `getTotalLength()` bằng
JS.

### Component

```tsx
interface HandDrawnButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  rounded?: 'pill' | 'lg'; // 'pill' cho nút bo tròn hoàn toàn, 'lg' cho bo góc vừa
  showCallout?: boolean;    // true = có thêm connector + label viết tay (xem bên dưới)
  calloutLabel?: string;
  calloutSide?: 'top-right' | 'top-left';
}

function HandDrawnButton({
  children, onClick, rounded = 'pill', showCallout = false,
  calloutLabel, calloutSide = 'top-right',
}: HandDrawnButtonProps) {
  const rx = rounded === 'pill' ? 50 : 14; // % theo viewBox 0-100

  return (
    <div className="relative inline-block group">
      <button
        onClick={onClick}
        className="relative z-10 px-6 py-3 rounded-full focus-visible:outline-none"
      >
        {children}
      </button>

      {/* Viền nét vẽ tay — ẩn mặc định, vẽ dần khi hover/focus */}
      <svg
        className="absolute pointer-events-none"
        style={{ left: -8, top: -8, width: 'calc(100% + 16px)', height: 'calc(100% + 16px)' }}
        viewBox="0 0 100 100"
        preserveAspectRatio="none"
      >
        <defs>
          <filter id="handDrawnWobbleBtn">
            <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="5" result="noise" />
            <feDisplacementMap in="SourceGraphic" in2="noise" scale="2.5" />
          </filter>
        </defs>
        <rect
          x="2" y="4" width="96" height="92" rx={rx}
          fill="none" stroke="#FFFFFF" strokeWidth="2.5"
          filter="url(#handDrawnWobbleBtn)"
          pathLength={100}
          className="
            [stroke-dasharray:100] [stroke-dashoffset:100]
            transition-[stroke-dashoffset] duration-500
            [transition-timing-function:cubic-bezier(0.65,0,0.35,1)]
            group-hover:[stroke-dashoffset:0]
            group-focus-within:[stroke-dashoffset:0]
          "
        />
      </svg>

      {showCallout && calloutLabel && (
        <ButtonCallout side={calloutSide} label={calloutLabel} />
      )}
    </div>
  );
}
```

Toàn bộ animation chạy bằng **CSS thuần** (`group-hover:`/`group-focus-within:`
của Tailwind) — không có `useState`, không re-render khi hover. `:focus-within`
đảm bảo bàn phím (Tab) cũng kích hoạt được, không chỉ chuột.

### Lưu ý về `baseFrequency` khi button rất dẹt (pill dài)
Vì SVG dùng `preserveAspectRatio="none"` để giãn theo đúng kích thước button,
với button rất dài/dẹt (ratio width:height lớn), noise wobble có thể hơi kéo
giãn theo chiều ngang thay vì đều tự nhiên như trên hotspot vuông. Nếu thấy
viền bị "kéo dài" bất thường trên button rất dài, tăng nhẹ `baseFrequency` lên
`0.05-0.06` để bù lại — không ảnh hưởng nhiều, viền vẫn đọc được là "nét vẽ
tay" ở cả hai trường hợp.

### Callout tuỳ chọn — connector + label (chỉ dùng cho 1 CTA đơn lẻ)

```tsx
function ButtonCallout({ side, label }: { side: 'top-right' | 'top-left'; label: string }) {
  const isRight = side === 'top-right';
  return (
    <div
      className="absolute pointer-events-none whitespace-nowrap"
      style={{ top: -6, [isRight ? 'left' : 'right']: '100%' }}
    >
      <svg width="70" height="40" className="overflow-visible">
        <path
          d={isRight ? 'M 0 30 Q 30 10 60 8' : 'M 70 30 Q 40 10 10 8'}
          fill="none" stroke="#FFFFFF" strokeWidth="1.5" strokeLinecap="round"
          pathLength={100}
          className="
            [stroke-dasharray:100] [stroke-dashoffset:100]
            transition-[stroke-dashoffset] duration-300 delay-150
            group-hover:[stroke-dashoffset:0]
          "
        />
      </svg>
      <span
        className="absolute font-['Caveat'] text-xl text-white opacity-0
          transition-opacity duration-250 delay-500
          group-hover:opacity-100"
        style={{ top: -4, [isRight ? 'left' : 'right']: 60, transform: 'rotate(-3deg)' }}
      >
        {label}
      </span>
    </div>
  );
}
```
Cùng timeline như bản `scene-hotspot`: viền vẽ trước (500ms) → connector vẽ ra
(300ms, delay 150ms) → label hiện sau cùng (delay 500ms).

### Khi nào dùng border-only vs. border + callout

| Tình huống | Dùng |
|---|---|
| **2+ button đứng cạnh nhau** (VD: "Đặt Món Tại Quầy" + "Khám Phá Menu" trong ảnh bạn gửi) | **Border-only** (`showCallout={false}`) — 2 callout cạnh nhau sẽ chồng chéo, rối mắt |
| **1 CTA chính đứng riêng** (VD: nút "Đặt bàn ngay" nổi bật một mình trong hero) | Border + callout, VD label "Chỉ mất 30 giây!" |
| Button trong nav/footer | Border-only, callout không cần thiết ở vùng phụ |

### Sử dụng

```tsx
<div className="flex gap-4">
  <HandDrawnButton onClick={handleOrder}>Đặt Món Tại Quầy</HandDrawnButton>
  <HandDrawnButton onClick={handleMenu} rounded="pill">
    Khám Phá Menu ↓
  </HandDrawnButton>
</div>

{/* CTA đơn lẻ, có callout */}
<HandDrawnButton showCallout calloutLabel="Chỉ mất 30 giây!" calloutSide="top-right">
  Đặt Bàn Ngay
</HandDrawnButton>
```

### Accessibility (biến thể button-hover)
- Dùng `group-focus-within:` chứ không chỉ `group-hover:` — đảm bảo điều
  hướng bằng bàn phím cũng thấy được viền.
- `<svg>` có `pointer-events: none` để không chặn click vào button bên dưới.
- Callout label chỉ mang tính trang trí — không đặt thông tin bắt buộc (VD:
  giá, điều kiện) chỉ trong callout, vì đây không phải nội dung được đọc bởi
  screen reader theo cách đảm bảo.

### Prompt (condensed)

Wrap CTA buttons with a `HandDrawnButton` component. Overlay an absolutely
positioned SVG (`viewBox="0 0 100 100" preserveAspectRatio="none"`, sized
`calc(100% + 16px)` around the button) containing a rounded `<rect>` with
`pathLength={100}` so `stroke-dasharray`/`stroke-dashoffset` work at exactly
100 regardless of the button's actual rendered width. Apply the same
`feTurbulence`/`feDisplacementMap` wobble filter as the scene-hotspot variant.
Draw the border in via `stroke-dashoffset: 100 → 0` on `group-hover:` and
`group-focus-within:` (pure CSS, Tailwind arbitrary properties, no JS state).
For a single standalone hero CTA, optionally add a small curved connector +
`Caveat` handwritten label callout using the same staggered-delay timeline as
the scene-hotspot variant. Do NOT add the callout when 2+ buttons sit next to
each other — use border-only to avoid overlapping callouts.

