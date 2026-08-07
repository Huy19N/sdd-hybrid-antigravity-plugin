---
id: liquid-blob-background
name: "Liquid Blob Background"
type: shared-module
module_category: surface
tags:
  - blob
  - organic
  - morph
  - background
  - abstract
compatible_with: all
pairs_well_with:
  - glassmorphism
best_for: "Hero background cho SaaS/tech/startup/healthcare muốn nền động nhưng mềm mại, không sắc cạnh — thay thế cho particle/grid distortion khi cần cảm giác 'sống, hữu cơ' hơn là 'công nghệ, góc cạnh'"
---

# Shared Module: Liquid Blob Background

## Preview Description
Một khối hình hữu cơ (blob) mềm mại, biến đổi hình dạng chậm rãi phía sau nội
dung hero — gradient màu nhẹ, chuyển động liên tục nhưng rất chậm (8-15s/chu
kỳ) để không gây xao nhãng. Khác biệt so với các background động khác (Aurora,
Particles, Grid Distortion đã dùng ở các template khác) ở chỗ cảm giác "hữu
cơ, mềm" thay vì "công nghệ, sắc cạnh" — hợp với brand muốn tông ấm/nhẹ nhàng.

## Kỹ thuật — bản cơ bản (không cần thư viện thêm)

```tsx
const BLOB_PATHS = [
  "M42.5,-58.5C54.8,-49.8,64.4,-36.8,68.8,-22.1C73.2,-7.4,72.4,9,66.4,23.1C60.4,37.2,49.2,49,35.8,57.6C22.4,66.2,6.8,71.6,-9.8,71.9C-26.4,72.2,-44,67.4,-56.8,56.6C-69.6,45.8,-77.6,29,-79.4,11.4C-81.2,-6.2,-76.8,-24.6,-66.8,-38.4C-56.8,-52.2,-41.2,-61.4,-25.6,-68.4C-10,-75.4,5.6,-80.2,20.4,-76.8C35.2,-73.4,49.2,-67.2,42.5,-58.5Z",
  "M38.4,-52.8C48.6,-45.2,54.6,-31.8,58.4,-17.6C62.2,-3.4,63.8,11.6,58.8,24.2C53.8,36.8,42.2,47,29,54.2C15.8,61.4,1,65.6,-14.6,64.8C-30.2,64,-46.6,58.2,-56.8,46.8C-67,35.4,-71,18.4,-70.8,1.6C-70.6,-15.2,-66.2,-30.4,-56.4,-38.6C-46.6,-46.8,-31.4,-48,-17.8,-52.6C-4.2,-57.2,7.8,-65.2,20.6,-64.4C33.4,-63.6,46.2,-54,38.4,-52.8Z",
  "M45.2,-61.4C57.8,-52.6,65.4,-37.4,68.4,-21.6C71.4,-5.8,69.8,10.6,63,24.6C56.2,38.6,44.2,50.2,30.4,58.2C16.6,66.2,1,70.6,-14.8,69.4C-30.6,68.2,-46.6,61.4,-57.8,49.8C-69,38.2,-75.4,21.8,-76.2,4.8C-77,-12.2,-72.2,-29.8,-61.8,-42.4C-51.4,-55,-35.4,-62.6,-19.6,-67.6C-3.8,-72.6,11.8,-75,26.4,-70.6C41,-66.2,54.6,-55,45.2,-61.4Z",
];

function LiquidBlob({ colorStart = '#7C3AED', colorEnd = '#EC4899' }) {
  const [pathIndex, setPathIndex] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setPathIndex(prev => (prev + 1) % BLOB_PATHS.length);
    }, 10000); // đổi path mỗi 10s, animate transition qua CSS
    return () => clearInterval(interval);
  }, []);

  return (
    <svg viewBox="-100 -100 200 200" style={{ position: 'absolute', width: '140%', filter: 'blur(40px)', opacity: 0.5 }}>
      <defs>
        <linearGradient id="blobGradient" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor={colorStart} />
          <stop offset="100%" stopColor={colorEnd} />
        </linearGradient>
      </defs>
      <path
        d={BLOB_PATHS[pathIndex]}
        fill="url(#blobGradient)"
        style={{ transition: 'd 6s cubic-bezier(0.45, 0, 0.55, 1)' }}
      />
    </svg>
  );
}
```
Lưu ý: CSS `transition: d` cho phần tử `<path>` **chỉ hoạt động mượt trên các
trình duyệt hiện đại hỗ trợ animatable `d`** (Chrome/Edge/Safari mới, Firefox
từ bản gần đây) — kiểm tra target browser trước khi dùng làm giải pháp chính.

## Nâng cấp tuỳ chọn — morph mượt hơn với `flubber`
Nếu cần chuyển động mượt hơn giữa các hình dạng phức tạp (không chỉ dựa vào
CSS `d` transition), có thể dùng thư viện `flubber` (npm, chuyên nội suy hình
dạng SVG path) để tính toán các bước trung gian rồi animate bằng
`requestAnimationFrame`. Đây là **nâng cấp tuỳ chọn**, không bắt buộc — bản
CSS thuần ở trên đã đủ dùng cho phần lớn trường hợp.

## Thông số khuyến nghị
- `blur(40px)` + `opacity: 0.4-0.6` — blob phải mờ, là background chứ không
  phải hình khối rõ nét cạnh tranh với nội dung
- Chu kỳ đổi hình: 8-15s — nhanh hơn sẽ gây xao nhãng, chậm hơn sẽ khó nhận ra
  là có chuyển động
- Màu: dùng 2 màu từ chính color palette của template (primary + accent),
  không thêm màu ngoài palette

## Nơi áp dụng phổ biến
Hero background cho `saas-landing`, `tech-startup`, `healthcare-clinic`,
`education-lms` — bất kỳ đâu cần nền động nhưng tông "mềm" thay vì "công nghệ
sắc cạnh" (khác với Aurora/Grid Distortion đã dùng ở các template hiện có).

## Prompt (condensed)

Add a soft morphing blob background behind hero content using an SVG `<path>`
with a gradient fill (using the template's primary and accent colors), `blur(40px)`,
`opacity: 0.4-0.6`. Cycle through 3 pre-defined organic blob path strings every
8-10s using CSS `transition: d 6s cubic-bezier(0.45,0,0.55,1)` on the path
element. Keep the blob visually behind and clearly subordinate to foreground
content — it's atmosphere, not a focal shape.

## Required Assets
Không cần asset riêng — dùng SVG path thuần code.

## ReactBits Components Used
Không dùng component ReactBits có sẵn — thuần SVG + CSS, có thể tham khảo
tinh thần tương tự **Aurora**/**Blob Cursor** của ReactBits nhưng module này
dùng path morph thay vì WebGL shader.
