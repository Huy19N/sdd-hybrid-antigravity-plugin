---
id: ambient-glow-cursor
name: "Ambient Glow Cursor Spotlight"
type: shared-module
module_category: surface
tags:
  - ambient-glow
  - spotlight
  - cursor-follower
  - radial-gradient
  - border-glow
  - dark-mode
compatible_with: all
pairs_well_with:
  - glassmorphism
  - 3d-motion-frame
  - holographic-shimmer
best_for: "Hero section, Bento grid feature cards, dark-mode SaaS pricing tables, fintech dashboards — tạo ánh sáng lan tỏa huyền bí bám theo con trỏ chuột, thắp sáng các đường viền kim loại và bề mặt tối."
requires_asset: "Hình ảnh có phông nền tối hoặc độ tương phản cao từ sdd-asset-generator để vệt sáng spotlight nổi bật rực rỡ."
---

# Shared Module: Ambient Glow Cursor Spotlight

## Preview Description
Module tạo hiệu ứng quầng sáng lan tỏa đa sắc (**ambient spotlight glow**) bám theo con trỏ chuột trong không gian 2D/3D. Khi di chuyển chuột qua một lưới thẻ (Bento Grid) hoặc section Hero, luồng ánh sáng mềm mại sẽ tự động "soi rọi" làm sáng bừng đường viền kim loại 1px (`border-glow`) và để lại vệt phản quang huyền ảo trên bề mặt vật liệu tối màu.

---

## Kỹ thuật triển khai

### Component Bento Grid Glow (React + Tailwind CSS + TypeScript)

```tsx
import React, { useRef, useEffect } from 'react';

interface GlowContainerProps {
  children: React.ReactNode;
  className?: string;
  glowColor?: string; // Mặc định rgba(140, 90, 255, 0.15)
  spotlightSize?: number; // Bán kính vệt sáng (px)
}

export const AmbientGlowContainer: React.FC<GlowContainerProps> = ({
  children,
  className = '',
  glowColor = 'rgba(120, 119, 198, 0.2)',
  spotlightSize = 450,
}) => {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    const handleMouseMove = (e: MouseEvent) => {
      const rect = container.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      container.style.setProperty('--glow-x', `${x}px`);
      container.style.setProperty('--glow-y', `${y}px`);
    };

    container.addEventListener('mousemove', handleMouseMove);
    return () => container.removeEventListener('mousemove', handleMouseMove);
  }, []);

  return (
    <div
      ref={containerRef}
      className={`relative overflow-hidden ${className}`}
      style={
        {
          '--glow-color': glowColor,
          '--spotlight-size': `${spotlightSize}px`,
        } as React.CSSProperties
      }
    >
      {/* Spotlight Layer phủ toàn container */}
      <div
        className="pointer-events-none absolute inset-0 transition-opacity duration-300"
        style={{
          background: `radial-gradient(
            var(--spotlight-size) circle at var(--glow-x, -500px) var(--glow-y, -500px),
            var(--glow-color),
            transparent 80%
          )`,
        }}
      />
      {children}
    </div>
  );
};

export const AmbientGlowCard: React.FC<{
  children: React.ReactNode;
  className?: string;
}> = ({ children, className = '' }) => {
  return (
    <div
      className={`group relative overflow-hidden rounded-2xl border border-white/10 bg-neutral-950/80 p-6 backdrop-blur-md transition-all duration-300 hover:border-white/20 ${className}`}
    >
      {/* Vệt sáng cục bộ trên từng card */}
      <div
        className="pointer-events-none absolute inset-0 opacity-0 transition-opacity duration-500 group-hover:opacity-100"
        style={{
          background: `radial-gradient(
            300px circle at var(--glow-x, -500px) var(--glow-y, -500px),
            rgba(255, 255, 255, 0.08),
            transparent 80%
          )`,
        }}
      />
      <div className="relative z-10">{children}</div>
    </div>
  );
};
```

---

## Hướng dẫn kết hợp với `sdd-asset-generator`
Khi áp dụng module này, các ảnh icon và minh họa 3D nên có ánh sáng ven (*rim-light*) cùng tông màu với `--glow-color` (ví dụ: tím neon hoặc xanh ngọc), giúp giao diện đạt độ hài hòa ánh sáng như một tác phẩm 3D thời gian thực.
