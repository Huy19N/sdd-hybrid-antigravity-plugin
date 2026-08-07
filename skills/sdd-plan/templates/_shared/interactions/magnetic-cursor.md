---
id: magnetic-cursor
name: "Magnetic Cursor"
type: shared-module
module_category: interaction
tags:
  - magnetic
  - cursor
  - button-hover
  - micro-interaction
compatible_with: all
pairs_well_with:
  - glassmorphism
best_for: "CTA button, icon nav, social icon nhỏ — không dùng cho card/element lớn, cảm giác 'hút nhẹ' chỉ hợp với element nhỏ gọn"
reactbits_components:
  - name: "Magnet"
    url: "https://www.reactbits.dev/animations/magnet"
---

# Shared Module: Magnetic Cursor

## Preview Description
Khi con trỏ đến gần một nút/icon, element "bị hút nhẹ" về phía con trỏ trong
một bán kính nhất định, rồi bật trở lại vị trí gốc khi con trỏ rời đi hoặc
click. Dùng ReactBits **Magnet** — component có sẵn, không cần tự viết từ đầu.

## Cách dùng

```tsx
import Magnet from './Magnet'; // copy từ reactbits.dev/animations/magnet

<Magnet strength={0.3} range={100}>
  <button className="cta-button">Đặt lịch ngay</button>
</Magnet>
```
- `strength`: độ mạnh hút, 0.2-0.4 là khoảng tự nhiên (cao hơn cảm giác quá
  "dính")
- `range`: bán kính (px) mà con trỏ bắt đầu kích hoạt hiệu ứng hút, 80-120px
  hợp với nút cỡ trung bình

## Giới hạn kích thước — quan trọng
Chỉ áp dụng cho element **nhỏ gọn, ≤120px** mỗi chiều: nút CTA, icon social,
icon nav. Áp lên card lớn hoặc cả section sẽ tạo cảm giác "trôi nổi" khó chịu
thay vì tinh tế — đây là lỗi thường gặp khi lạm dụng hiệu ứng này.

## Nơi áp dụng phổ biến
- Nút CTA chính trong hero
- Icon mạng xã hội ở footer
- Nút mũi tên điều hướng carousel/gallery
- Nút "+" thêm giỏ hàng nhanh trong `shoppable-lifestyle-scene`

## Prompt (condensed)

Wrap CTA buttons and small icon elements (≤120px) with ReactBits' Magnet
component (`https://www.reactbits.dev/animations/magnet`), `strength={0.3}`,
`range={100}`. Do not apply to large cards or full sections — magnetic pull
only reads as intentional on compact clickable elements.

## Required Assets
Không cần asset riêng.

## ReactBits Components Used
- **Magnet** (`https://www.reactbits.dev/animations/magnet`) — hiệu ứng hút
  con trỏ, dùng nguyên bản không cần custom thêm.
