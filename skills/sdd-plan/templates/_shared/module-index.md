# Shared Module Index — Distinctive Design Modules (Haute-Design Catalog)

Khác với `templates/` (22 bộ giao diện đầy đủ theo ngành), thư mục `_shared/`
chứa các **module riêng biệt, độc lập chủ đề** — có thể ghép vào bất kỳ
template nào để tạo sự khác biệt, tránh việc 2 project cùng chọn template
`product-store` hay `restaurant-food` ra kết quả giống hệt nhau.

## Nguyên tắc cốt lõi — Haute-Design & Tương thích Asset

**Một template + 2-3 module khác nhau = 2-3 tác phẩm giao diện độc bản hoàn toàn.**
Đây là giải pháp triệt để cho bài toán "trùng template = trùng giao diện". Thư
viện hiện có **13 module sáng tạo cao cấp**, mang lại hàng trăm tổ hợp thị giác
khác biệt.

**Đồng bộ hóa 100% với `sdd-asset-generator`**: Mỗi module khi được lựa chọn sẽ
tự động gửi yêu cầu asset đặc thù (ví dụ: cặp ảnh so sánh cho `interactive-split-slider`,
ảnh 3D chrome cho `holographic-shimmer`, đại cảnh cho `hand-drawn-annotation`) để
tạo nên một tổng thể thị giác nhất quán và nghệ thuật.

---

## Danh mục 13 Module Sáng Tạo

| id | Tên | Loại | Tags | Hợp với | Yêu cầu Asset từ `sdd-asset-generator` |
|---|---|---|---|---|---|
| `hand-drawn-annotation` | Hand-Drawn Scene Annotation **(v2)** | interaction | doodle, hand-drawn, hotspot, storytelling, button-hover | `scene-hotspot`: Bối cảnh không gian thật (F&B, bất động sản, pet-care, wedding, tiệm bánh). `button-hover`: Mọi nút CTA | Ảnh đại cảnh góc rộng (24mm/35mm) có nhiều chi tiết phân tầng để gắn hotspot |
| `holographic-shimmer` | Holographic Iridescent Shimmer | surface | holographic, iridescent, foil, chrome, luxury | Thẻ sản phẩm bản giới hạn, thẻ thành viên VIP, badge công nghệ, giải thưởng | Ảnh 3D Liquid Chrome hoặc vật thể kim loại/thủy tinh bóng bẩy trên nền tối |
| `ambient-glow-cursor` | Ambient Glow Cursor Spotlight | surface | ambient-glow, spotlight, cursor-follower, dark-mode | Hero SaaS, Bento grid feature cards, fintech dashboard, dark portfolio | Ảnh icon 3D hoặc banner nền tối có ánh sáng viền (*rim-light*) tương phản |
| `circular-badge-stamp` | Rotating Circular Badge Stamp | interaction | circular-text, rotating-stamp, badge, artisan, emblem | Quán cafe, thời trang thủ công, sản phẩm organic, studio kiến trúc, di sản | Ảnh sản phẩm có khoảng trống bố cục (*negative space*) để đặt con dấu xoay |
| `interactive-split-slider` | Interactive Dual-State Split Slider | viewer | split-slider, before-after, dual-state, comparison | Kiến trúc/nội thất (ngày/đêm), thời trang, spa, xe hơi, đồ ăn (nguyên liệu/món) | **CẶP 2 ẢNH ĐỒNG BỘ** (cùng góc máy, cùng chủ thể nhưng khác trạng thái/ánh sáng) |
| `3d-motion-frame` | 3D Motion Frame | surface | 3d, tilt, parallax, glare | Product card, feature card, portfolio piece, pricing card | Ảnh sản phẩm chụp studio bục đá travertine hoặc render 3D có chiều sâu |
| `glassmorphism` | Glassmorphism & Frosted Acrylic | surface | glass, frosted, blur, modern, acrylic | Nav bar, card nổi trên ảnh, modal, floating widgets | Nền có ánh sáng màu sắc hoặc ảnh texture phức tạp để làm nổi vân mờ kính |
| `product-360-drag-rotate` | 360° Drag-Rotate Product Viewer | viewer | 360, product-viewer, drag-rotate | Giày dép, đồng hồ, xe hơi, nội thất, đồ gốm sứ thủ công | Chuỗi ảnh xoay 360 độ hoặc render 3D quay quanh trục |
| `magnetic-cursor` | Magnetic Cursor | interaction | magnetic, cursor, button-hover | Nút CTA, icon nhỏ (≤120px), link điều hướng | Không yêu cầu asset riêng |
| `scroll-velocity-marquee` | Scroll Velocity Marquee | interaction | marquee, scroll, kinetic-typography | Dải tagline, thương hiệu đối tác, quote triết lý giữa 2 section | Không yêu cầu asset riêng |
| `grain-noise-overlay` | Grain & Noise Overlay | surface | grain, noise, texture, premium, film | Hầu hết mọi hero/section màu đặc, phong cách Kinfolk/Editorial | Giúp tăng độ mịn màng xúc giác cho mọi ảnh render và nền màu |
| `liquid-blob-background` | Liquid Blob Background | surface | blob, organic, morph | Hero SaaS, công nghệ, y tế, giáo dục, sáng tạo | Nền chuyển động mềm mại bổ trợ cho các khối UI nổi |
| `scroll-scrubbing-video` | Scroll-Scrubbing Video | viewer | video, scroll, scrubbing, pinned-section, cinematic | Hero section hoặc section giới thiệu sản phẩm — phong cách Apple | Video nguồn .mp4 (≤8s) từ `sdd-video-generator` hoặc frame sequence |

---

## Cấu trúc thư mục `_shared/`

```
_shared/
├── interactions/   # Hành vi tương tác và chuyển động của người dùng
│   ├── circular-badge-stamp.md
│   ├── hand-drawn-annotation.md
│   ├── magnetic-cursor.md
│   └── scroll-velocity-marquee.md
├── surfaces/        # Xử lý chất liệu, ánh sáng và hiệu ứng bề mặt
│   ├── 3d-motion-frame.md
│   ├── ambient-glow-cursor.md
│   ├── glassmorphism.md
│   ├── grain-noise-overlay.md
│   ├── holographic-shimmer.md
│   └── liquid-blob-background.md
└── viewers/          # Component độc lập, tương tác phức tạp
    ├── interactive-split-slider.md
    ├── product-360-drag-rotate.md
    └── scroll-scrubbing-video.md
```

---

## Bộ Công Thức Phối Hợp Cá Tính (Combinatorial Personality Recipes)

Khi thực hiện `sdd-plan`, Agent **phải đối chiếu brainstorm của người dùng và đề xuất 2-3 tổ hợp mang cá tính đối lập**. Ví dụ cùng là một cửa hàng bán sản phẩm vật lý:

### 🌟 Tổ hợp 1 — "Avant-Garde & Futuristic Tech"
- **Modules**: `holographic-shimmer` + `ambient-glow-cursor` + `magnetic-cursor`
- **Asset Sinh ra**: Ảnh 3D Liquid Chrome, chất liệu kim loại bóng lộn xám obsidian, ánh sáng tím neon.
- **Phong cách**: Đậm chất công nghệ tương lai, huyền ảo và sắc sảo.

### 🍃 Tổ hợp 2 — "Organic Heritage & Artisanal Craft"
- **Modules**: `circular-badge-stamp` + `hand-drawn-annotation` + `grain-noise-overlay`
- **Asset Sinh ra**: Ảnh chụp trên bục đá travertine, vải linen thô, ánh nắng ban mai rọi bóng lá cây.
- **Phong cách**: Thủ công mỹ nghệ ấm áp, mộc mạc, đậm chất thơ và tin cậy.

### 🎬 Tổ hợp 3 — "Cinematic & Interactive Discovery"
- **Modules**: `interactive-split-slider` + `3d-motion-frame` + `scroll-velocity-marquee`
- **Asset Sinh ra**: Cặp ảnh so sánh nguyên liệu vs thành phẩm, ảnh sản phẩm có chiều sâu Z-axis.
- **Phong cách**: Hiện đại, giàu tính tương tác chạm vuốt, phô diễn trọn vẹn chất lượng sản phẩm.

---

## Tương thích & Xung đột Cần Lưu Ý
- `glassmorphism` + `grain-noise-overlay` nếu chồng lên cùng 1 layer nhỏ sẽ làm mất độ trong suốt — hãy phân bổ ở các khu vực khác nhau.
- `scroll-scrubbing-video` và `product-360-drag-rotate` đều chiếm vị trí trung tâm viewport — không nên đặt trong cùng một section.
- `holographic-shimmer` và `ambient-glow-cursor` đạt hiệu quả thị giác đẹp nhất trên nền tối (Dark Mode / Charcoal / Obsidian).
