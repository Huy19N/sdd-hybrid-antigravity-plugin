---
name: sdd-bg-remover
version: 2
changelog:
  - "v2: replaced single default u2net model with tiered model selection (isnet-general-use / birefnet-general / birefnet-dis), enabled alpha matting, added connected-component alpha cleanup to remove leftover semi-transparent background noise, and added automated edge-quality checking with auto-escalation to a stronger tier when needed."
description: "Sub-skill automatically invoked by sdd-build after sdd-asset-generator completes, only when the chosen template requires transparent/cutout images (requires_transparent_images: true in template frontmatter). Do NOT trigger manually. Removes backgrounds from product images using the rembg Python library with tiered model quality and automated cleanup, producing clean transparent PNGs ready for overlay-style layouts."
---

# SDD Background Remover (sub-skill of sdd-build)

## Purpose
Remove backgrounds from product/item images so they can be used in overlay-style
layouts where the product appears to float on a colored background — a common
pattern in e-commerce, product showcase, and food/beverage templates.

## Vì sao v1 để sót điểm ảnh nền
v1 luôn dùng model mặc định `u2net` của rembg, không alpha matting, không hậu
kỳ. `u2net` xử lý ảnh ở độ phân giải nội bộ cố định (thường 320×320) rồi phóng
mask trở lại kích thước gốc — với vật thể có biên phức tạp (gai sầu riêng, các
múi rời rạc, cảnh nhiều vật thể như hộp gỗ) mask bị mờ ở biên, để lại các
điểm ảnh bán trong suốt (không phải alpha=0 hoàn toàn) mà mắt thường thấy như
"vương vấn nền". v2 giải quyết bằng model tốt hơn + một bước dọn dẹp riêng chứ
không chỉ trông chờ vào model.

## Invocation
This skill is **automatically called** by `sdd-build` immediately after
`sdd-asset-generator` completes, but **only when** the chosen template has
`requires_transparent_images: true` in its frontmatter. Never trigger manually.

## Preconditions
- `sdd-asset-generator` has completed and produced images in `public/assets/generated/`.
- The asset inventory from `sdd-asset-generator` lists files with `Needs BG Removal? = Yes`.
- Python 3.10+ is available on the system.
- `scipy` recommended (not strictly required) — enables the connected-component
  cleanup step. Without it, background noise removal still runs but is weaker
  (hard-threshold + edge feather only, no speckle-blob filtering).

## Process

### 1. Check for Python + rembg + scipy
```bash
python --version
pip show rembg
pip show scipy
```
If missing:
```bash
pip install rembg[gpu] Pillow numpy scipy   # if GPU available
# or
pip install rembg Pillow numpy scipy         # CPU fallback
```
`scipy` is optional but strongly recommended — see Preconditions.

### 2. Identify files to process
Read the asset inventory from `sdd-asset-generator`. Only process files marked
with `Needs BG Removal? = Yes`.

### 3. Chọn tier theo loại vật thể (mới ở v2)
Đọc mô tả asset (từ `sdd-asset-generator`) và chọn `--tier` khởi điểm — không
bắt buộc phải đúng 100%, vì auto-escalation (bước 5) sẽ tự nâng tier nếu chọn
thấp mà chưa đủ sạch:

| Mô tả asset gợi ý | Tier | Model | Ví dụ |
|---|---|---|---|
| Sản phẩm thông thường, biên rõ, ít chi tiết nhỏ | `standard` (mặc định) | `isnet-general-use` | Hộp bánh, chai lọ, đồ nội thất đơn giản |
| Cảnh nhiều vật thể / bối cảnh phức tạp | `high` | `birefnet-general` | Sản phẩm đặt trong hộp/khay có nhiều lớp (VD: hộp quà mở nắp) |
| Biên có gai/lông/chi tiết mảnh, nhiều răng cưa nhỏ | `fine-detail` | `birefnet-dis` | Sầu riêng nguyên vỏ (gai), thú nhồi bông (lông), ren/vải có tua |

Nếu không chắc, cứ để mặc định `standard` — auto-escalation sẽ tự xử lý các
trường hợp khó hơn dự kiến.

### 4. Run background removal
Use the bundled script at `skills/sdd-bg-remover/scripts/remove_bg.py`:

```bash
python skills/sdd-bg-remover/scripts/remove_bg.py \
  --input public/assets/generated/ \
  --output public/assets/no-bg/ \
  --files product-01.webp product-02.webp \
  --tier standard
```

Hoặc xử lý toàn bộ, bắt đầu ở tier cao hơn cho các asset đã biết trước là khó
(VD: một batch toàn ảnh vật thể có gai/lông):
```bash
python skills/sdd-bg-remover/scripts/remove_bg.py \
  --input public/assets/generated/ \
  --output public/assets/no-bg/ \
  --all --tier fine-detail
```

### 5. Auto-escalation khi chất lượng chưa đạt (mới ở v2)
Script tự đánh giá tỷ lệ điểm ảnh bán-trong-suốt sau khi xử lý (proxy cho
"còn sót nền hay không"). Nếu vượt ngưỡng (`--quality-threshold`, mặc định
3%), script **tự động chạy lại file đó ở tier cao hơn** (tối đa 2 lần nâng
tier, `--max-escalations`) trước khi báo là cần xem xét thủ công — không âm
thầm chấp nhận kết quả kém chỉ vì file không rỗng/không lỗi như v1 từng làm.

### 6. Verify output
- Check exit code: `0` = tất cả sạch, `1` = có file lỗi hoàn toàn, `2` = tất cả
  chạy được nhưng có file vẫn bị flag "needs review" sau khi đã escalate hết.
- Với các file bị flag, đọc log để biết đã thử tới tier nào — nếu đã thử
  `fine-detail` mà vẫn còn noise, khả năng cao vấn đề nằm ở ảnh nguồn (nền quá
  giống màu vật thể, độ phân giải thấp) chứ không phải do model — cân nhắc
  yêu cầu `sdd-asset-generator` tạo lại ảnh nguồn với nền tương phản hơn, hoặc
  báo user cần chỉnh tay.

### 7. Update asset paths
After processing, report back to `sdd-build` the updated asset paths, kèm
trạng thái review:
```
product-01.webp → public/assets/no-bg/product-01.png  ✅ (tier: standard)
product-02.webp → public/assets/no-bg/product-02.png  ⚠️  NEEDS REVIEW (tried up to: fine-detail)
```

## Fallback: remove.bg API
If `rembg` installation fails (e.g., missing system dependencies on Windows),
use the remove.bg free API as fallback:

1. Inform the user they need a free API key from https://www.remove.bg/api
2. Once provided, use the API:
```bash
curl -H "X-Api-Key: YOUR_KEY" \
  -F "image_file=@public/assets/generated/product-01.webp" \
  -F "size=auto" \
  -o public/assets/no-bg/product-01.png \
  https://api.remove.bg/v1.0/removebg
```

## Trường hợp khó nhất — cảnh nhiều vật thể mơ hồ (VD: sản phẩm đặt trong hộp)
Ngay cả `birefnet-general` (tier `high`) đôi khi vẫn khó xác định đâu là "vật
thể chính" khi cảnh có nhiều thành phần cùng nổi bật (hộp gỗ + sản phẩm bên
trong). rembg có hỗ trợ model `sam` (Segment Anything) cho phép chỉ định điểm
prompt cụ thể (VD: click vào giữa sản phẩm) thay vì để model tự đoán — nhưng
đây là chế độ **tương tác**, cần toạ độ point/box do người chỉ định, không
phù hợp để tự động hoá hoàn toàn trong pipeline này. Nếu escalation lên tới
`fine-detail` vẫn không đủ cho một cảnh nhiều-vật-thể, báo cho user và gợi ý:
(a) tách ảnh nguồn thành 2 tấm riêng (chỉ hộp, chỉ sản phẩm) trước khi xử lý,
hoặc (b) xử lý thủ công với công cụ hỗ trợ point-prompt.

## Constraints
- Only process files explicitly marked for background removal. Do not process
  hero banners, icons, or background textures.
- Output format is always PNG (to preserve transparency).
- Do not modify the original files in `public/assets/generated/` — output to
  a separate `public/assets/no-bg/` directory.
- Mặc định tier `standard`, không mặc định `high`/`fine-detail` cho mọi file —
  các tier cao hơn chậm hơn đáng kể, chỉ nên dùng khi thật sự cần (theo bảng
  ở bước 3, hoặc do auto-escalation tự nâng khi cần).
- If both rembg and remove.bg fail, clearly inform the user and suggest
  manual background removal as last resort.

## Handoff
Return the list of processed files with their new paths to `sdd-build`.
`sdd-build` will then reference these transparent images in the UI code
using the `public/assets/no-bg/` paths.
