---
id: circular-badge-stamp
name: "Rotating Circular Badge Stamp"
type: shared-module
module_category: interaction
tags:
  - circular-text
  - rotating-stamp
  - badge
  - kinetic-typography
  - artisan
  - emblem
compatible_with: all
pairs_well_with:
  - hand-drawn-annotation
  - grain-noise-overlay
  - magnetic-cursor
best_for: "Quán cafe, tiệm bánh, thời trang thủ công, sản phẩm organic/wellness, studio kiến trúc, thương hiệu di sản — tạo con dấu xoay tròn tinh tế chứng nhận chất lượng thủ công hoặc năm thành lập ('Est. 2026 • Artisanal Quality')."
requires_asset: "Ảnh hero hoặc sản phẩm có góc đặt hoặc khoảng trống bố cục (negative space) tự nhiên để gắn con dấu mà không che lấp chi tiết chính."
---

# Shared Module: Rotating Circular Badge Stamp

## Preview Description
Con dấu xoay kinetic hình tròn (**Rotating Kinetic Badge**) với dòng chữ uốn cong theo đường tròn SVG xoay đều đặn 360 độ, bao quanh một biểu tượng trung tâm (ngôi sao, giọt nước, lá cây, logo tối giản hoặc năm thành lập). Hiệu ứng mang đậm tính nghệ nhân (*artisan / craft heritage*), tạo điểm nhấn thị giác tinh tế trên góc ảnh sản phẩm, nút CTA, hoặc lơ lửng giữa các section.

---

## Kỹ thuật triển khai

### Component Circular Badge (React + Tailwind CSS + TypeScript)

```tsx
import React, { useState } from 'react';

interface CircularBadgeStampProps {
  text?: string; // Chữ uốn cong vòng tròn, VD: "• HANDCRAFTED • ARTISANAL QUALITY • EST. 2026 "
  centerIcon?: React.ReactNode;
  size?: number; // Đường kính px (mặc định 120px)
  speedSeconds?: number; // Tốc độ xoay (mặc định 18s/vòng)
  className?: string;
  badgeBg?: string;
  textColor?: string;
}

export const CircularBadgeStamp: React.FC<CircularBadgeStampProps> = ({
  text = '• HANDCRAFTED • ARTISANAL QUALITY • EST. 2026 ',
  centerIcon,
  size = 120,
  speedSeconds = 18,
  className = '',
  badgeBg = 'rgba(255, 255, 255, 0.06)',
  textColor = 'currentColor',
}) => {
  const [isHovered, setIsHovered] = useState(false);
  const radius = size * 0.38;
  const circumference = 2 * Math.PI * radius;

  return (
    <div
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className={`group relative flex items-center justify-center cursor-pointer rounded-full backdrop-blur-md transition-transform duration-500 hover:scale-110 ${className}`}
      style={{
        width: size,
        height: size,
        backgroundColor: badgeBg,
      }}
    >
      {/* Vòng chữ SVG xoay tròn */}
      <svg
        className="absolute inset-0 w-full h-full"
        viewBox={`0 0 ${size} ${size}`}
        style={{
          animation: `spin ${isHovered ? speedSeconds / 2 : speedSeconds}s linear infinite`,
        }}
      >
        <defs>
          <path
            id="circlePath"
            d={`M ${size / 2}, ${size / 2} m -${radius}, 0 a ${radius},${radius} 0 1,1 ${radius * 2},0 a ${radius},${radius} 0 1,1 -${radius * 2},0`}
          />
        </defs>
        <text
          fill={textColor}
          className="text-[9px] font-mono uppercase tracking-[0.28em] font-semibold"
        >
          <textPath href="#circlePath" startOffset="0%">
            {text}
          </textPath>
        </text>
      </svg>

      {/* Biểu tượng trung tâm tĩnh hoặc xoay ngược */}
      <div className="relative z-10 flex items-center justify-center text-primary transition-transform duration-300 group-hover:rotate-45">
        {centerIcon || (
          <span className="text-sm font-bold">✦</span>
        )}
      </div>

      <style>{`
        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
};
```

---

## Hướng dẫn kết hợp với `sdd-asset-generator`
Khi kết hợp module này với template F&B (`04-restaurant-food`), Thời trang (`05-fashion-ecommerce`) hoặc Tiệm bánh (`21-scene-doodle-annotation`), prompt của `sdd-asset-generator` sẽ được chỉ đạo để bố cục đối tượng chính hơi lệch một bên (theo quy tắc 1/3), chừa một khoảng trống thoáng đãng ở góc trên/dưới để đặt con dấu xoay mà không làm che khuất sản phẩm.
