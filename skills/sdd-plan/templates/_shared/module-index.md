# Shared Module Index — Distinctive Design Modules

Khác với `templates/` (22 bộ giao diện đầy đủ theo ngành), thư mục `_shared/`
chứa các **module riêng biệt, độc lập chủ đề** — có thể ghép vào bất kỳ
template nào để tạo sự khác biệt, tránh việc 2 project cùng chọn template
`pet-care` ra kết quả giống hệt nhau.

## Nguyên tắc cốt lõi — đọc trước khi chọn module

**Một template + 2-3 module khác nhau = 2-3 website trông khác nhau rõ rệt.**
Đây là cách hệ thống này giải quyết vấn đề "trùng template = trùng giao
diện": không giới hạn ở việc chọn 1 trong 22 template, mà là chọn 1 template
**rồi tổ hợp thêm 1-3 module** trong thư viện dưới đây. Thư viện càng lớn
(hiện 7 module, sẽ tăng theo thời gian), số tổ hợp khả dĩ càng nhiều.

**Quan trọng — không tự động chọn 1 tổ hợp "tốt nhất" duy nhất.** Nếu agent
luôn chọn đúng 1 tổ hợp "hợp lý nhất" cho một loại brainstorm nhất định, thì
những project có brainstorm tương tự nhau (VD: 2 quán pet-care khác nhau) vẫn
sẽ hội tụ về cùng 1 tổ hợp — quay lại đúng vấn đề ban đầu. Agent **phải**
trình bày 2-3 tổ hợp khác nhau và để user chọn, xem chi tiết ở mục "Quy trình
chọn module" bên dưới.

## Danh mục module

| id | Tên | Loại | Tags | Hợp với | Ghi chú |
|---|---|---|---|---|---|
| `hand-drawn-annotation` | Hand-Drawn Scene Annotation **(v2)** | interaction | doodle, hand-drawn, hotspot, storytelling, button-hover | `scene-hotspot`: Template có ảnh không gian thật (F&B, real-estate, pet-care, wedding, coworking, automotive). `button-hover`: **mọi** template có CTA button | Đã tích hợp sẵn trong 8 template (6 bắt buộc scene-hotspot + 2 scene-dedicated). Button-hover áp thêm cho CTA buttons, thuần CSS không cần JS state |
| `3d-motion-frame` | 3D Motion Frame | surface | 3d, tilt, parallax, glare | Product/feature/portfolio/pricing card | Cần cursor — hạn chế trên mobile |
| `glassmorphism` | Glassmorphism | surface | glass, frosted, blur, modern | Nav, card nổi trên ảnh, modal | Cẩn thận contrast khi đặt trên ảnh phức tạp |
| `product-360-drag-rotate` | 360° Drag-Rotate Product Viewer | viewer | 360, product-viewer, drag-rotate | Sản phẩm cần "xem mọi góc": giày, đồng hồ, figurine, xe, nội thất | 2 cách triển khai (ảnh tuần tự / true 3D) — đọc kỹ trước khi chọn |
| `magnetic-cursor` | Magnetic Cursor | interaction | magnetic, cursor, button-hover | Nút CTA, icon nhỏ (≤120px) | Không dùng cho element lớn |
| `scroll-velocity-marquee` | Scroll Velocity Marquee | interaction | marquee, scroll, kinetic-typography | Dải tagline/logo giữa 2 section | Tối đa 1 dải/trang |
| `grain-noise-overlay` | Grain & Noise Overlay | surface | grain, noise, texture, premium | Hầu hết mọi hero/section màu đặc | Mặc định static, animate tốn hiệu năng |
| `liquid-blob-background` | Liquid Blob Background | surface | blob, organic, morph | Hero SaaS/tech/healthcare/education | Tông "mềm", khác Aurora/Grid Distortion đã có |

Chi tiết kỹ thuật đầy đủ nằm trong file riêng của từng module, theo cấu trúc:
```
_shared/
├── interactions/   # hành vi hover/scroll của user lên 1 vùng cụ thể
│   ├── hand-drawn-annotation.md
│   ├── magnetic-cursor.md
│   └── scroll-velocity-marquee.md
├── surfaces/        # xử lý hình ảnh/chất liệu cho card, nền, khung
│   ├── 3d-motion-frame.md
│   ├── glassmorphism.md
│   ├── grain-noise-overlay.md
│   └── liquid-blob-background.md
└── viewers/          # component tương tác độc lập, phức tạp hơn 1 hiệu ứng đơn
    └── product-360-drag-rotate.md
```

## Quy trình chọn module (dùng trong `sdd-plan`)

1. Sau khi user đã chọn 1 template nền (từ `templates/template-index.md`),
   đọc file `module-index.md` này.
2. Đối chiếu `brainstorm.md`: loại sản phẩm (có phải vật thể cần "xem mọi
   góc" không → ưu tiên `product-360-drag-rotate`?), mood/tone được nhắc tới,
   có đối thủ/site tham chiếu nào user từng nhắc không.
3. Tạo **2-3 tổ hợp module khác nhau** (mỗi tổ hợp 1-3 module, không trùng
   nhau hoàn toàn giữa các tổ hợp), mỗi tổ hợp có một "cá tính" rõ ràng khác
   biệt — không phải 3 biến thể nhỏ của cùng 1 ý tưởng. Ví dụ với brainstorm
   là 1 startup bán giày thủ công:
   - Tổ hợp A — "Tactile & premium": `3d-motion-frame` + `grain-noise-overlay`
   - Tổ hợp B — "Xem trước khi mua": `product-360-drag-rotate` +
     `magnetic-cursor`
   - Tổ hợp C — "Hiện đại tối giản": `glassmorphism` + `scroll-velocity-marquee`
4. Trình bày cả 2-3 tổ hợp cho user kèm lý do ngắn gọn mỗi tổ hợp phù hợp ở
   điểm nào — **để user chọn**, hoặc user có thể tự trộn module khác đi nếu
   muốn (không giới hạn trong 3 gợi ý).
5. Sau khi chọn, đọc đầy đủ file từng module đã chọn, đưa spec vào phần
   "Distinctive Modules" trong `plan.md` (xem `SKILL.md` để biết format).

## Tương thích & xung đột cần lưu ý
- `glassmorphism` + `grain-noise-overlay` chồng lên cùng 1 bề mặt sẽ làm mờ
  cả hai hiệu ứng — nếu dùng cả hai, đặt ở 2 khu vực khác nhau của trang,
  không chồng trực tiếp.
- `3d-motion-frame` cần cursor thật — không hiệu quả trên mobile, luôn có
  fallback tĩnh.
- `product-360-drag-rotate` **chiếm vai trò trung tâm của 1 section** — không
  nên nhồi thêm module khác (VD: `3d-motion-frame`) ngay trên chính viewer đó,
  chỉ nên kết hợp ở các phần khác của trang (VD: `magnetic-cursor` cho nút "+"
  cạnh viewer thì được, nhưng đừng tilt cả viewer).
