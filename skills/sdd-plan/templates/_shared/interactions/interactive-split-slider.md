---
id: interactive-split-slider
name: "Interactive Dual-State Split Slider"
type: shared-module
module_category: viewer
tags:
  - split-slider
  - before-after
  - dual-state
  - comparison
  - interactive-drag
  - showcase
compatible_with: all
pairs_well_with:
  - 3d-motion-frame
  - grain-noise-overlay
  - scroll-velocity-marquee
best_for: "Kiến trúc/nội thất (ngày vs đêm, trước vs sau cải tạo), thời trang (vải mộc vs trang phục hoàn thiện), làm đẹp/spa (before vs after), xe hơi (khung gầm vs ngoại thất), đồ ăn/đồ uống (nguyên liệu thô vs món ăn hoàn chỉnh)."
requires_asset: "CẶP 2 ẢNH ĐỒNG BỘ (Dual-State Pair) từ sdd-asset-generator: cùng góc chụp (camera angle, focal length, framing) nhưng khác trạng thái/ánh sáng/chất liệu."
---

# Shared Module: Interactive Dual-State Split Slider

## Preview Description
Thanh trượt so sánh 2 nửa khung hình (**Interactive Comparison Split Slider**) cho phép người dùng kéo thả đường phân cách theo chiều ngang để khám phá sự chuyển biến kỳ diệu giữa hai trạng thái của cùng một đối tượng (Ngày / Đêm, Trước / Sau, Nguyên liệu thô / Tác phẩm hoàn mỹ, Thiết kế 3D / Thực tế thi công).

---

## Kỹ thuật triển khai

### Component Split Slider (React + Tailwind CSS + TypeScript)

```tsx
import React, { useState, useRef, useCallback } from 'react';

interface InteractiveSplitSliderProps {
  beforeImage: string; // URL ảnh trạng thái 1 (VD: Ban ngày / Nguyên liệu)
  afterImage: string;  // URL ảnh trạng thái 2 (VD: Ban đêm / Thành phẩm)
  beforeLabel?: string;
  afterLabel?: string;
  aspectRatio?: string; // Mặc định "16/9" hoặc "4/3"
  className?: string;
}

export const InteractiveSplitSlider: React.FC<InteractiveSplitSliderProps> = ({
  beforeImage,
  afterImage,
  beforeLabel = 'ORIGIN',
  afterLabel = 'FINISHED',
  aspectRatio = '16/9',
  className = '',
}) => {
  const [sliderPosition, setSliderPosition] = useState(50); // 0 .. 100%
  const [isDragging, setIsDragging] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  const handleMove = useCallback((clientX: number) => {
    if (!containerRef.current) return;
    const rect = containerRef.current.getBoundingClientRect();
    const x = clientX - rect.left;
    const position = Math.max(0, Math.min(100, (x / rect.width) * 100));
    setSliderPosition(position);
  }, []);

  const handleTouchMove = (e: React.TouchEvent) => {
    if (e.touches.length > 0) {
      handleMove(e.touches[0].clientX);
    }
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (isDragging) {
      handleMove(e.clientX);
    }
  };

  return (
    <div
      ref={containerRef}
      onMouseDown={() => setIsDragging(true)}
      onMouseUp={() => setIsDragging(false)}
      onMouseLeave={() => setIsDragging(false)}
      onMouseMove={handleMouseMove}
      onTouchMove={handleTouchMove}
      className={`group relative select-none overflow-hidden rounded-2xl border border-white/10 shadow-2xl ${className}`}
      style={{ aspectRatio }}
    >
      {/* Ảnh 2 (After / Lớp dưới) */}
      <img
        src={afterImage}
        alt={afterLabel}
        className="absolute inset-0 h-full w-full object-cover"
        draggable={false}
      />
      <div className="absolute bottom-4 right-4 z-10 rounded-full bg-black/60 px-3 py-1 text-xs font-semibold tracking-wider text-white backdrop-blur-md">
        {afterLabel}
      </div>

      {/* Ảnh 1 (Before / Lớp trên bị cắt theo SliderPosition) */}
      <div
        className="absolute inset-0 overflow-hidden"
        style={{ width: `${sliderPosition}%` }}
      >
        <img
          src={beforeImage}
          alt={beforeLabel}
          className="absolute inset-0 h-full w-full object-cover"
          style={{
            width: containerRef.current ? `${containerRef.current.offsetWidth}px` : '100vw',
            maxWidth: 'none',
          }}
          draggable={false}
        />
        <div className="absolute bottom-4 left-4 z-10 rounded-full bg-black/60 px-3 py-1 text-xs font-semibold tracking-wider text-white backdrop-blur-md">
          {beforeLabel}
        </div>
      </div>

      {/* Đường phân cách & Nút kéo */}
      <div
        className="absolute top-0 bottom-0 z-20 w-0.5 cursor-ew-resize bg-white shadow-[0_0_12px_rgba(255,255,255,0.8)]"
        style={{ left: `${sliderPosition}%` }}
      >
        <div className="absolute top-1/2 -translate-y-1/2 -translate-x-1/2 flex h-10 w-10 items-center justify-center rounded-full border border-white/40 bg-neutral-900/90 text-white shadow-xl backdrop-blur-md transition-transform duration-200 group-hover:scale-110">
          <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M8 9l-4 3 4 3m8-6l4 3-4 3" />
          </svg>
        </div>
      </div>
    </div>
  );
};
```

---

## Hướng dẫn kết hợp với `sdd-asset-generator` (Cặp ảnh Dual-State)
Khi chọn module này, `sdd-plan` sẽ yêu cầu `sdd-asset-generator` sinh **cặp 2 bức ảnh** với cùng mô tả bối cảnh và góc chụp camera (ví dụ: `100mm macro f/2.8` hoặc `24mm architectural lens`), chỉ thay đổi yếu tố trạng thái (ánh sáng, vật liệu, giai đoạn hoàn thiện).
