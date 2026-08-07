---
id: grain-noise-overlay
name: "Grain & Noise Overlay"
type: shared-module
module_category: surface
tags:
  - grain
  - noise
  - texture
  - film
  - premium
compatible_with: all
pairs_well_with:
  - 3d-motion-frame
best_for: "Hero section hoặc bất kỳ mảng màu/ảnh phẳng nào muốn thêm cảm giác chất liệu, bớt 'nhựa'/kỹ thuật số quá mức — dùng được ở gần như mọi template"
---

# Shared Module: Grain & Noise Overlay

## Preview Description
Lớp nhiễu hạt (film grain) phủ nhẹ lên section, tạo cảm giác chất liệu/analog
thay vì bề mặt số phẳng lì. Chi tiết nhỏ nhưng ảnh hưởng lớn đến cảm giác
"cao cấp" của một trang — nhiều site premium (thời trang, portfolio nhiếp
ảnh) đều có lớp này dù rất khó nhận ra khi nhìn thoáng qua.

## Kỹ thuật

```html
<svg style="position:absolute;width:0;height:0">
  <filter id="grainNoise">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="4" seed="2" />
  </filter>
</svg>
```

```css
.grain-overlay {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 50;
  opacity: 0.4;
  mix-blend-mode: overlay;
  background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="4"/></filter><rect width="100%" height="100%" filter="url(%23n)" opacity="0.08"/></svg>');
  background-size: 200px 200px;
}
```
(Đây chính là kỹ thuật grain đã dùng trong spec TOONHUB carousel gốc — tách
riêng thành module dùng chung thay vì lặp lại mỗi lần cần.)

## ⚠️ Static vs Animated — chọn có chủ đích
- **Static (khuyến nghị mặc định)**: background noise cố định, không animate
  — rẻ, không tốn hiệu năng, đủ hiệu quả trong 95% trường hợp.
- **Animated** (noise dịch chuyển liên tục): chỉ dùng khi thương hiệu thật sự
  cần cảm giác "phim đang chạy" — animate `feTurbulence` bằng cách re-render
  SVG mỗi frame **tốn hiệu năng đáng kể**, cân nhắc kỹ trước khi bật, đặc biệt
  trên mobile.

## Thông số khuyến nghị
- `baseFrequency: 0.9`, `numOctaves: 4` — hạt mịn, không quá thô
- `opacity` tổng thể: 0.04-0.08 — chỉ đủ cảm nhận được, không được nhìn thấy
  rõ như "nhiễu tín hiệu"
- `mix-blend-mode: overlay` giữ màu nền bên dưới không bị xám xịt

## Nơi áp dụng phổ biến
Gần như mọi hero section hoặc section nền màu đặc (không phải ảnh) — đặc biệt
hợp với: `automotive` (tông tối, cinematic), `photography-studio`,
`scene-doodle-annotation`, `music-streaming`.

## Prompt (condensed)

Add a subtle static film-grain overlay using an SVG `feTurbulence` filter
(`baseFrequency: 0.9, numOctaves: 4`) as a repeating background-image data URI,
`position: absolute; inset: 0; pointer-events: none; mix-blend-mode: overlay;
opacity: 0.04–0.08; background-size: 200px 200px`. Keep it static (no
animation) by default for performance — only animate if the brand specifically
needs a "film reel" motion feel, and note the added render cost if so.

## Required Assets
Không cần asset riêng.

## ReactBits Components Used
Không dùng component ReactBits có sẵn — thuần SVG filter + CSS.
