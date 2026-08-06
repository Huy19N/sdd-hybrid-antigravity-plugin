---
id: hand-drawn-annotation
name: "Hand-Drawn Scene Annotation"
type: shared-interaction
used_by:
  - restaurant-food
  - scene-doodle-annotation
  - shoppable-lifestyle-scene
---

# Shared Interaction: Hand-Drawn Scene Annotation

Kỹ thuật hover: viền outline nét vẽ tay (wobbly SVG border) bao quanh vùng hover,
kèm connector line cong animate + label chữ viết tay ở cuối đường — phong cách
annotation/doodle overlay trên một background scene thật (ảnh chụp không gian).
Đây **không phải** component có sẵn của ReactBits — là SVG filter + path
animation tự viết, dùng chung cho các template cần "chấm điểm" (hotspot) trên
một ảnh nền.

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
