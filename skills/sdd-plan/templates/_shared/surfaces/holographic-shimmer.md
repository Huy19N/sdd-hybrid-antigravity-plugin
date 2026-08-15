---
id: holographic-shimmer
name: "Holographic Iridescent Shimmer"
type: shared-module
module_category: surface
tags:
  - holographic
  - iridescent
  - foil
  - chrome
  - luxury
  - card-hover
  - chromatic-aberration
compatible_with: all
pairs_well_with:
  - 3d-motion-frame
  - magnetic-cursor
  - ambient-glow-cursor
best_for: "Thẻ sản phẩm bản giới hạn (Limited Edition), thẻ thành viên VIP, tác phẩm nghệ thuật/NFT, badge công nghệ, card giải thưởng — tạo cảm giác phủ lớp quang phổ đổi màu óng ánh khi di chuột hoặc nghiêng thiết bị."
requires_asset: "Ảnh sản phẩm/khối 3D có chi tiết kim loại, chrome bóng hoặc thủy tinh phản quang từ sdd-asset-generator (Trend A: 3D Liquid Chrome) để cộng hưởng hoàn hảo với hiệu ứng tán sắc."
---

# Shared Module: Holographic Iridescent Shimmer

## Preview Description
Hiệu ứng bề mặt tráng gương đa sắc (**iridescent holographic foil**) lấy cảm hứng từ các thẻ bài sưu tầm cao cấp, bao bì in kim loại hologram và xu hướng đồ họa 3D Chrome đương đại. Khi di chuyển con trỏ chuột trên card, một dải quang phổ tán sắc cầu vồng (*chromatic spectrum*) sẽ trượt mượt mà theo góc chiếu sáng, kết hợp với các vệt lấp lánh phản chiếu (*specular glint*) và đường viền kim loại tán xạ.

---

## Kỹ thuật triển khai

### Cấu trúc lớp CSS
```
HolographicCard (overflow: hidden, position: relative, border-radius)
├── BaseLayer (Ảnh sản phẩm/nội dung card)
├── HolographicFoilOverlay (CSS linear-gradient quang phổ, mix-blend-mode: color-dodge/overlay)
├── SpecularGlint (Radial gradient ánh sáng chói lóa theo tọa độ chuột)
└── PrismaticBorder (Đường viền 1px gradient phát quang)
```

### Component Code (React + Tailwind CSS + TypeScript)

```tsx
import React, { useRef, useState, useEffect } from 'react';

interface HolographicCardProps {
  children: React.ReactNode;
  className?: string;
  intensity?: number; // 0.1 .. 1.0 (mặc định 0.7)
}

export const HolographicCard: React.FC<HolographicCardProps> = ({
  children,
  className = '',
  intensity = 0.7,
}) => {
  const cardRef = useRef<HTMLDivElement>(null);
  const [coords, setCoords] = useState({ x: 50, y: 50 });
  const [isHovered, setIsHovered] = useState(false);
  const targetCoords = useRef({ x: 50, y: 50 });

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!cardRef.current) return;
    const rect = cardRef.current.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;
    targetCoords.current = { x, y };
  };

  // Lerp smoothing for liquid-like motion
  useEffect(() => {
    let raf: number;
    const update = () => {
      setCoords((prev) => ({
        x: prev.x + (targetCoords.current.x - prev.x) * 0.1,
        y: prev.y + (targetCoords.current.y - prev.y) * 0.1,
      }));
      raf = requestAnimationFrame(update);
    };
    raf = requestAnimationFrame(update);
    return () => cancelAnimationFrame(raf);
  }, []);

  return (
    <div
      ref={cardRef}
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => {
        setIsHovered(false);
        targetCoords.current = { x: 50, y: 50 };
      }}
      className={`relative overflow-hidden rounded-2xl border border-white/10 bg-neutral-900 transition-all duration-300 ${className}`}
      style={{
        boxShadow: isHovered
          ? '0 20px 40px -15px rgba(255,255,255,0.07), 0 0 25px 2px rgba(180,120,255,0.15)'
          : 'none',
      }}
    >
      {/* Nội dung bên trong */}
      <div className="relative z-10">{children}</div>

      {/* Lớp màng tán sắc cầu vồng (Holographic Foil) */}
      <div
        className="pointer-events-none absolute inset-0 z-20 transition-opacity duration-500"
        style={{
          opacity: isHovered ? intensity : 0,
          background: `linear-gradient(
            ${coords.x * 2 + coords.y * 1.5}deg,
            rgba(255, 0, 128, 0.25) 0%,
            rgba(255, 154, 0, 0.2) 20%,
            rgba(208, 222, 33, 0.25) 40%,
            rgba(0, 255, 128, 0.2) 60%,
            rgba(0, 192, 255, 0.25) 80%,
            rgba(180, 0, 255, 0.3) 100%
          )`,
          mixBlendMode: 'color-dodge',
          backgroundSize: '200% 200%',
          backgroundPosition: `${coords.x}% ${coords.y}%`,
        }}
      />

      {/* Vệt sáng lấp lánh (Specular Glint) */}
      <div
        className="pointer-events-none absolute inset-0 z-30 transition-opacity duration-300"
        style={{
          opacity: isHovered ? 0.8 : 0,
          background: `radial-gradient(
            circle at ${coords.x}% ${coords.y}%,
            rgba(255, 255, 255, 0.4) 0%,
            rgba(255, 255, 255, 0.08) 35%,
            transparent 70%
          )`,
          mixBlendMode: 'overlay',
        }}
      />

      {/* Đường viền phản quang Prismatic */}
      <div
        className="pointer-events-none absolute inset-0 z-40 rounded-2xl transition-opacity duration-500"
        style={{
          opacity: isHovered ? 1 : 0.3,
          padding: '1px',
          background: `linear-gradient(
            ${coords.x * 3}deg,
            rgba(255,255,255,0.4),
            rgba(255,100,200,0.5),
            rgba(100,200,255,0.5),
            rgba(255,255,255,0.2)
          )`,
          mask: 'linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0)',
          WebkitMask: 'linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0)',
          WebkitMaskComposite: 'xor',
          maskComposite: 'exclude',
        }}
      />
    </div>
  );
};
```

---

## Hướng dẫn kết hợp với `sdd-asset-generator`
Khi chọn module này, `sdd-plan` sẽ yêu cầu `sdd-asset-generator` sinh ảnh có tông màu chủ đạo đen sâu (Obsidian/Charcoal) kết hợp với các khối 3D chrome/thủy tinh phản quang để lớp hologram phát huy độ tương phản và chiều sâu thị giác cực đại.
