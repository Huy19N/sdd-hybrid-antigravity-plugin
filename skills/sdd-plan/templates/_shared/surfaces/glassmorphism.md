---
id: glassmorphism
name: "Glassmorphism"
type: shared-module
module_category: surface
tags:
  - glass
  - frosted
  - blur
  - translucent
  - modern
compatible_with: all
pairs_well_with:
  - 3d-motion-frame
best_for: "Nav bar sticky, card nổi trên ảnh nền, modal/quick-view, mobile menu overlay — bất kỳ nơi nào cần lớp UI 'nổi' trên nội dung mà vẫn thấy được nội dung phía sau"
---

# Shared Module: Glassmorphism

## Preview Description
Bề mặt kính mờ — nền trong suốt + `backdrop-filter: blur()` + viền sáng mỏng
+ đổ bóng mềm. Khác biệt so với card trắng/đục thông thường ở chỗ vẫn thấy mờ
mờ nội dung phía sau, tạo cảm giác nhiều lớp (layered depth) hiện đại.

## Công thức CSS cơ bản

### Light glass (dùng trên nền tối/ảnh — chữ trắng)
```css
.glass-light {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.18);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  border-radius: 16px;
}
```

### Dark glass (dùng trên nền sáng — chữ tối)
```css
.glass-dark {
  background: rgba(20, 20, 20, 0.55);
  backdrop-filter: blur(16px) saturate(150%);
  -webkit-backdrop-filter: blur(16px) saturate(150%);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
  border-radius: 16px;
}
```

## ⚠️ Lưu ý contrast — dễ bị bỏ qua nhất
Glass panel đặt trực tiếp trên **ảnh photo phức tạp** (không phải gradient
đơn giản) rất dễ khiến text phía trên khó đọc ở một số vùng ảnh sáng/tối
không đều — vi phạm WCAG contrast dù bản thân glass trông đẹp. Khi glass nằm
trên ảnh:
```css
.glass-on-photo {
  /* thêm 1 lớp scrim tối trước khi blur, không chỉ dựa vào backdrop-filter */
  background: linear-gradient(rgba(0,0,0,0.15), rgba(0,0,0,0.15)), rgba(255,255,255,0.08);
  backdrop-filter: blur(20px);
}
```
Luôn kiểm tra tỷ lệ tương phản text/nền thực tế sau khi áp glass, không giả
định blur tự động đủ để đọc được.

## Fallback trình duyệt cũ
```css
@supports not (backdrop-filter: blur(1px)) {
  .glass-light { background: rgba(30, 30, 30, 0.85); }
  .glass-dark { background: rgba(255, 255, 255, 0.92); }
}
```

## Nơi áp dụng phổ biến
- **Sticky nav** khi scroll (chuyển từ transparent sang glass khi user cuộn
  xuống ~50px)
- **Card nổi trên hero photo** (VD: search form trong `real-estate`, product
  quick-view popover)
- **Mobile menu overlay** — full-screen glass panel trượt vào
- **Pricing card nổi bật** — dùng glass cho gói "Popular" để tách biệt khỏi
  các card thường (solid)

## Prompt (condensed)

Apply a glassmorphism surface treatment in Tailwind CSS. Use
`background: rgba(255,255,255,0.08); backdrop-filter: blur(20px)
saturate(180%); border: 1px solid rgba(255,255,255,0.18); box-shadow: 0 8px
32px rgba(0,0,0,0.12)` for light glass on dark/photo backgrounds, or the dark
variant for light backgrounds. When placed directly over a busy photo, add an
extra `rgba(0,0,0,0.15)` scrim layer under the blur to protect text contrast
— verify contrast manually, don't assume blur alone is enough. Add
`@supports not (backdrop-filter: blur(1px))` fallback to a solid semi-opaque
background for older browsers.

## Required Assets
Không cần asset riêng.

## ReactBits Components Used
Không dùng component ReactBits có sẵn — thuần CSS.
