---
id: scroll-velocity-marquee
name: "Scroll Velocity Marquee"
type: shared-module
module_category: interaction
tags:
  - marquee
  - scroll
  - kinetic-typography
  - text-animation
compatible_with: all
pairs_well_with: []
best_for: "Dải tagline/brand giữa các section, strip logo khách hàng, category tag strip — nơi cần thêm 'sự sống' vào khoảng trắng giữa 2 section mà không cần thêm nội dung mới"
reactbits_components:
  - name: "Scroll Velocity"
    url: "https://www.reactbits.dev/text-animations/scroll-velocity"
---

# Shared Module: Scroll Velocity Marquee

## Preview Description
Dải chữ/logo chạy ngang, tốc độ chạy **phản ứng theo tốc độ cuộn trang** —
cuộn nhanh thì chữ chạy nhanh theo, cuộn ngược thì chữ đảo chiều. Dùng
ReactBits **Scroll Velocity** — có sẵn, dùng `useVelocity` + `useSpring` để
mượt, không giật.

## Cách dùng

```tsx
import ScrollVelocity from './ScrollVelocity'; // copy từ reactbits.dev/text-animations/scroll-velocity

<ScrollVelocity
  texts={['NGUYÊN LIỆU HỮU CƠ 100%', 'GIAO TRONG NGÀY']}
  velocity={40}
  className="tagline-marquee"
/>
```

## Nơi áp dụng phổ biến
- Dải tagline mỏng giữa Hero và section tiếp theo (thay cho khoảng trắng tĩnh)
- Strip logo khách hàng/đối tác trong `saas-landing`, `tech-startup`
- Category tag strip trong `shoppable-lifestyle-scene` (thay category strip
  tĩnh bằng bản chạy, tăng chuyển động cho trang có nhiều ảnh tĩnh)
- Dải "ĐANG MỞ CỬA · GIAO HÀNG TẬN NƠI · ..." trong `restaurant-food`

## Lưu ý
- Không dùng quá 1 dải marquee/trang — nhiều hơn 1 chỗ sẽ rối, mất tác dụng
  điểm nhấn
- Text ngắn, dạng khẩu hiệu/nhãn — không nhét đoạn văn dài vào marquee, khó
  đọc khi đang chạy

## Prompt (condensed)

Add ReactBits' Scroll Velocity component
(`https://www.reactbits.dev/text-animations/scroll-velocity`) as a single thin
marquee strip between two sections (e.g. right after the hero). Text speed
should track page scroll velocity via the component's built-in
`useVelocity`/`useSpring` behavior — scrolling faster speeds up the marquee,
scrolling up reverses direction. Use short tagline/label text, not paragraphs.
Limit to one marquee strip per page.

## Required Assets
Không cần asset riêng.

## ReactBits Components Used
- **Scroll Velocity** (`https://www.reactbits.dev/text-animations/scroll-velocity`)
  — dùng nguyên bản.
