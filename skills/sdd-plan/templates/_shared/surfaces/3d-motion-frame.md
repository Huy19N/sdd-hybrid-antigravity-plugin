---
id: 3d-motion-frame
name: "3D Motion Frame"
type: shared-module
module_category: surface
tags:
  - 3d
  - tilt
  - parallax
  - glare
  - card-hover
  - depth
compatible_with: all
pairs_well_with:
  - glassmorphism
best_for: "Product card, feature card, portfolio piece, pricing card — bất kỳ card nào muốn cảm giác 'vật thể có chiều sâu' phản ứng theo con trỏ thay vì phẳng tĩnh"
---

# Shared Module: 3D Motion Frame

## Preview Description
Card nghiêng theo vị trí con trỏ (perspective tilt) với **nhiều lớp ở độ sâu
Z khác nhau** — ảnh, khung viền, và một lớp glare (ánh sáng phản chiếu) di
chuyển lệch pha nhau tạo cảm giác vật thể 3D thật, giống hiệu ứng thẻ bài
holographic. Khác với tilt-card đơn giản (chỉ xoay nguyên khối phẳng), module
này có chiều sâu thật nhờ `translateZ` từng lớp riêng.

## Kỹ thuật

### Cấu trúc lớp (Z-depth)
```
Container (perspective: 1200px)
└── Card (transform-style: preserve-3d, rotateX/rotateY theo cursor)
    ├── Layer 1 — Ảnh/nội dung chính        translateZ(0px)
    ├── Layer 2 — Khung viền trang trí       translateZ(40px)
    └── Layer 3 — Glare (ánh sáng phản chiếu) translateZ(60px)
```

### Tilt theo con trỏ (có lerp mượt, không giật)

```tsx
const cardRef = useRef<HTMLDivElement>(null);
const [rotate, setRotate] = useState({ x: 0, y: 0 });
const target = useRef({ x: 0, y: 0 });

function onMouseMove(e: React.MouseEvent) {
  const rect = cardRef.current!.getBoundingClientRect();
  const px = (e.clientX - rect.left) / rect.width - 0.5;  // -0.5 .. 0.5
  const py = (e.clientY - rect.top) / rect.height - 0.5;
  const MAX_TILT = 12; // độ
  target.current = { x: -py * MAX_TILT, y: px * MAX_TILT };
}

// Vòng lặp lerp mượt — không set transform trực tiếp trong onMouseMove
useEffect(() => {
  let raf: number;
  function loop() {
    setRotate(prev => ({
      x: prev.x + (target.current.x - prev.x) * 0.12,
      y: prev.y + (target.current.y - prev.y) * 0.12,
    }));
    raf = requestAnimationFrame(loop);
  }
  raf = requestAnimationFrame(loop);
  return () => cancelAnimationFrame(raf);
}, []);

function onMouseLeave() {
  target.current = { x: 0, y: 0 }; // lerp tự đưa về 0, có cảm giác "đàn hồi" nhẹ
}
```

```tsx
<div style={{ perspective: '1200px' }}>
  <div
    ref={cardRef}
    onMouseMove={onMouseMove}
    onMouseLeave={onMouseLeave}
    style={{
      transformStyle: 'preserve-3d',
      transform: `rotateX(${rotate.x}deg) rotateY(${rotate.y}deg)`,
    }}
  >
    <img style={{ transform: 'translateZ(0px)' }} />
    <div className="frame-border" style={{ transform: 'translateZ(40px)' }} />
    <div
      className="glare"
      style={{
        transform: 'translateZ(60px)',
        background: `radial-gradient(circle at ${50 + rotate.y * 2}% ${50 - rotate.x * 2}%, rgba(255,255,255,0.35), transparent 60%)`,
        mixBlendMode: 'overlay',
      }}
    />
  </div>
</div>
```
Glare di chuyển theo `rotate.x/y` — vị trí sáng nhất luôn "hướng về" phía cạnh
đang nghiêng lên, mô phỏng ánh sáng phản chiếu thật.

## Thông số khuyến nghị
- `MAX_TILT`: 8-12° (quá 15° trông giả/quá kịch)
- Hệ số lerp `0.12`: tăng lên (~0.2) nếu muốn phản ứng nhanh hơn, giảm xuống
  (~0.08) nếu muốn "nặng"/mượt hơn
- Glare opacity tối đa: 0.25-0.4, quá cao sẽ che nội dung

## Mobile
Không có cursor — dùng `deviceorientation` (gyroscope) làm nâng cấp tuỳ chọn
nếu cần, nhưng mặc định để card tĩnh trên mobile, không cố mô phỏng tilt bằng
touch (kéo ngón tay để tilt dễ nhầm với scroll/swipe gesture khác).

## Prompt (condensed)

Build a 3D tilt card component in React + TypeScript + Tailwind CSS. On
mousemove within the card, compute cursor offset from center (-0.5 to 0.5 on
each axis), map to rotateX/rotateY (max ±12°), smooth toward the target via a
`requestAnimationFrame` lerp loop (factor 0.12) — never set transform directly
in the mousemove handler. Card uses `transform-style: preserve-3d` with 3
layered children at different `translateZ` depths: main image (0px), a
decorative border frame (40px), and a radial-gradient glare overlay (60px,
`mix-blend-mode: overlay`) whose position shifts opposite to the tilt
direction. On mouse leave, target resets to 0 and the lerp naturally springs
back. Static (no tilt) on touch devices.

## Required Assets
Không cần asset riêng — áp dụng lên ảnh sản phẩm/portfolio đã có sẵn của
template đang dùng.

## ReactBits Components Used
Không dùng component ReactBits có sẵn — logic tự viết. Có thể tham khảo tinh
thần tương tự **Tilted Card** (`https://www.reactbits.dev/components/tilted-card`,
đã dùng trong template `coworking-space`) nhưng module này có thêm lớp glare
và Z-depth thật mà Tilted Card gốc không có.
