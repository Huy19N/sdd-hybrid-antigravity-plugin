# Shared Module Index — Distinctive Design Modules (Universal Web & Mobile Catalog)

Khác với `templates/` (22 bộ giao diện đầy đủ theo ngành), thư mục `_shared/`
chứa các **module riêng biệt, độc lập chủ đề** — có thể ghép vào bất kỳ
template nào trên **Web, React Native, Flutter hoặc Kotlin Compose** để tạo sự
khác biệt, tránh việc 2 project cùng chọn 1 template ra kết quả giống hệt nhau.

## Nguyên tắc cốt lõi — Cross-Platform Haute-Design & Tương thích Asset

**Một template + 2-3 module khác nhau = 2-3 tác phẩm giao diện độc bản hoàn toàn.**
Thư viện hiện có **18 module sáng tạo cao cấp** (13 module Universal/Web và 5
module Mobile-First chuyên sâu).

**Đồng bộ hóa 100% với `sdd-asset-generator`**: Tự động sinh asset chuyên biệt theo
yêu cầu của từng module (cặp ảnh Dual-State cho split-slider, 3D chrome cho
hologram, đại cảnh cho scene annotation, khay ảnh dọc 9:16 cho mobile stories).

---

## Danh mục 18 Module Sáng Tạo (Universal, Web & Mobile)

| id | Tên | Loại | Nền tảng | Hợp với | Yêu cầu Asset từ `sdd-asset-generator` |
|---|---|---|---|---|---|
| `mobile-bottom-sheet` | Mobile Interactive Bottom Sheet | mobile | Mobile / Responsive | Lọc sản phẩm, size/color picker, checkout, mini player | Thumbnail hoặc icon vuông 1:1 trong header sheet |
| `swipeable-card-stack` | Swipeable Gesture Card Stack | mobile | Mobile / Touch | Khám phá sản phẩm (Shop-by-Swipe), tin ngắn, lookbook | Danh sách 3-5 ảnh tỷ lệ dọc 4:5 hoặc 9:16 |
| `haptic-tab-bar` | Floating Haptic Frosted Tab Bar | mobile | Mobile / Touch | Thanh điều hướng chính app di động (Home/Shop/Cart/Profile) | Bộ icon 1:1 cho từng tab |
| `stories-avatar-tray` | Stories Avatar Tray & Fullscreen Viewer | mobile | Mobile / Responsive | Fashion, Cafe, Lifestyle, Flash-sale, sự kiện | Bộ ảnh Story 9:16 + avatar tròn 1:1 |
| `pull-to-refresh-mesh` | Elastic Pull-to-Refresh Mesh Indicator | mobile | Mobile / Touch | Feeds tin tức, danh sách sản phẩm, bảng giá crypto | Không cần asset (dùng code shader/gradient) |
| `hand-drawn-annotation` | Hand-Drawn Scene Annotation **(v2)** | interaction | Universal | Bối cảnh không gian thật (F&B, real estate, pet, boutique) | Ảnh đại cảnh góc rộng (24mm/35mm) phân tầng chi tiết |
| `holographic-shimmer` | Holographic Iridescent Shimmer | surface | Universal | Thẻ VIP, sản phẩm giới hạn, tech badge, giải thưởng | Ảnh 3D Liquid Chrome hoặc kim loại bóng trên nền tối |
| `ambient-glow-cursor` | Ambient Glow Cursor Spotlight | surface | Universal | Hero SaaS, Bento grid cards, fintech, dark portfolio | Ảnh icon 3D / banner nền tối có ánh sáng viền (*rim-light*) |
| `circular-badge-stamp` | Rotating Circular Badge Stamp | interaction | Universal | Cafe, thời trang thủ công, sản phẩm organic, studio | Ảnh sản phẩm có khoảng trống bố cục (*negative space*) |
| `interactive-split-slider` | Interactive Dual-State Split Slider | viewer | Universal | Kiến trúc (ngày/đêm), thời trang, spa, đồ ăn (nguyên liệu/món) | **CẶP 2 ẢNH ĐỒNG BỘ** (cùng góc máy, khác trạng thái) |
| `3d-motion-frame` | 3D Motion Frame | surface | Universal | Product card, feature card, pricing card | Ảnh sản phẩm chụp studio bục đá hoặc render 3D có chiều sâu |
| `glassmorphism` | Glassmorphism & Frosted Acrylic | surface | Universal | Nav bar, card nổi trên ảnh, modal, floating widgets | Nền có ánh sáng màu sắc hoặc ảnh texture phức tạp |
| `product-360-drag-rotate` | 360° Drag-Rotate Product Viewer | viewer | Universal | Giày dép, đồng hồ, xe hơi, nội thất, đồ thủ công | Chuỗi ảnh xoay 360 độ hoặc render 3D quay quanh trục |
| `magnetic-cursor` | Magnetic Cursor | interaction | Web / Desktop | Nút CTA, icon nhỏ (≤120px), link điều hướng | Không yêu cầu asset riêng |
| `scroll-velocity-marquee` | Scroll Velocity Marquee | interaction | Universal | Dải tagline, thương hiệu đối tác, quote triết lý | Không yêu cầu asset riêng |
| `grain-noise-overlay` | Grain & Noise Overlay | surface | Universal | Hầu hết mọi hero/section màu đặc, Kinfolk/Editorial | Giúp tăng độ mịn màng xúc giác cho ảnh render |
| `liquid-blob-background` | Liquid Blob Background | surface | Universal | Hero SaaS, công nghệ, y tế, giáo dục, sáng tạo | Nền chuyển động mềm mại bổ trợ cho các khối UI |
| `scroll-scrubbing-video` | Scroll-Scrubbing Video | viewer | Universal | Hero section hoặc section giới thiệu sản phẩm kiểu Apple | Video nguồn .mp4 (≤8s) từ `sdd-video-generator` |

---

## Cấu trúc thư mục `_shared/`

```
_shared/
├── mobile/         # Các component & cử chỉ chuyên biệt cho điện thoại
│   ├── haptic-tab-bar.md
│   ├── mobile-bottom-sheet.md
│   ├── pull-to-refresh-mesh.md
│   ├── stories-avatar-tray.md
│   └── swipeable-card-stack.md
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

## Bộ Công Thức Phối Hợp Cho Mobile App (Mobile Personality Recipes)

Khi thiết kế ứng dụng cho điện thoại (React Native / Flutter / Kotlin), Agent **phải đề xuất 2-3 tổ hợp di động khác biệt**:

### 📱 Tổ hợp Mobile A — "Social Discovery & Engagement"
- **Modules**: `stories-avatar-tray` + `swipeable-card-stack` + `haptic-tab-bar`
- **Phong cách**: Khám phá trực quan sinh động như Instagram/TikTok, vuốt chạm mượt mà, phù hợp thời trang và F&B.

### 💼 Tổ hợp Mobile B — "Haute-Commerce & Seamless Checkout"
- **Modules**: `mobile-bottom-sheet` + `haptic-tab-bar` + `holographic-shimmer`
- **Phong cách**: Sang trọng, mua sắm nhanh chóng với Bottom Sheet chọn size/color mà không rời màn hình chính.

### 🌟 Tổ hợp Mobile C — "Artisanal Craft & Visual Inspection"
- **Modules**: `circular-badge-stamp` + `interactive-split-slider` + `pull-to-refresh-mesh`
- **Phong cách**: Thủ công mỹ nghệ, so sánh chi tiết chất liệu bằng thanh trượt chạm vuốt.
