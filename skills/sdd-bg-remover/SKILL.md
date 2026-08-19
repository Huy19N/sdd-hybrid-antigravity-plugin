---
name: sdd-bg-remover
version: 3
changelog:
  - "v3: added a second mode — multi-layer segmentation (scripts/segment_layers.py) for splitting ONE composite scene into several separately-labeled transparent layers (e.g. sky/cloud/tree/fence-post), for 2D/2.5D game parallax backgrounds. Uses CLIPSeg (text-prompted zero-shot segmentation), a different technique from remove_bg.py's single-subject rembg pipeline — see 'Two modes' below."
  - "v2: replaced single default u2net model with tiered model selection (isnet-general-use / birefnet-general / birefnet-dis), enabled alpha matting, added connected-component alpha cleanup to remove leftover semi-transparent background noise, and added automated edge-quality checking with auto-escalation to a stronger tier when needed."
description: "Sub-skill automatically invoked by sdd-build after sdd-asset-generator completes, when the chosen template/game asset requires transparent/cutout images. Has two modes: single-subject background removal (remove_bg.py, requires_transparent_images: true) and multi-layer scene decomposition for game parallax layers (segment_layers.py, used when sdd-asset-generator produces a 'Parallax Composite Scene' asset with Decomposition Labels). Do NOT trigger manually."
---

# SDD Background Remover (sub-skill of sdd-build)

## Hai chế độ — chọn đúng chế độ trước khi dùng

| | `remove_bg.py` (v1-v2, không đổi) | `segment_layers.py` (mới, v3) |
|---|---|---|
| Bài toán | 1 vật thể chính vs. nền — tách nhị phân | N vùng có tên trong CÙNG 1 ảnh — tách đa nhãn |
| Kỹ thuật | rembg (u2net/isnet/birefnet) | CLIPSeg (segmentation theo text prompt, zero-shot) |
| Input | 1 ảnh sản phẩm | 1 ảnh scene + danh sách nhãn text (VD: "sky", "cloud", "tree") |
| Output | 1 file PNG trong suốt | N file PNG, mỗi file 1 layer, loại trừ lẫn nhau |
| Dùng khi | Ảnh sản phẩm e-commerce, item overlay trên web | Background game 2D/2.5D cần tách layer để parallax |
| Dependency | `rembg`, nhẹ | `torch` + `transformers`, nặng hơn đáng kể — tách riêng script để không bắt buộc mọi người dùng `remove_bg.py` phải cài thêm |

Nếu chỉ cần tách 1 vật thể ra khỏi nền đơn giản → dùng `remove_bg.py` như
trước, không đổi gì. Nếu cần tách 1 ảnh cảnh thành nhiều lớp riêng để dùng
làm parallax background cho game → dùng `segment_layers.py`.

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
| Biên có gai/lông/chi tiết mảnh, nhiều răng cưa nhỏ, hoặc giọt nước bắn li ti | `fine-detail` | `birefnet-dis` | Giọt nước trà sữa bắn tung tóe (liquid splash corona), bọt khí, sầu riêng nguyên vỏ (gai), thú nhồi bông (lông), ren/vải có tua |

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

## Chế độ 2: Multi-Layer Segmentation (Game Assets) — `segment_layers.py`

### Khi nào dùng
`sdd-asset-generator` tạo ra 1 asset loại "Parallax Composite Scene" (xem
SKILL.md của skill đó) — 1 ảnh cảnh game 2D/2.5D với nhiều vùng ngữ nghĩa rõ
ràng (bầu trời, mây, cây, hàng rào...) cần tách thành từng layer riêng để mỗi
layer di chuyển với tốc độ khác nhau khi cuộn (parallax).

### 1. Check dependencies (nặng hơn `remove_bg.py`)
```bash
pip show torch transformers
```
Nếu thiếu:
```bash
pip install torch transformers Pillow numpy scipy
```
Lần chạy đầu tiên sẽ tải model CLIPSeg (~600MB), cache lại cho các lần sau.

### 2. Lấy danh sách nhãn từ `sdd-asset-generator`
`plan.md`/asset inventory sẽ liệt kê "Decomposition Labels" cho asset loại
composite scene, VD: `["sky", "cloud", "distant mountain", "tree", "wooden
fence post", "ground"]`. Thứ tự nhãn **quan trọng** — đây cũng là thứ tự
stack layer từ xa tới gần khi ghép lại trong game.

### 3. Run segmentation
```bash
python skills/sdd-bg-remover/scripts/segment_layers.py \
  --input public/assets/generated/forest-scene.webp \
  --output public/assets/game-layers/forest-scene/ \
  --labels "sky" "cloud" "distant mountain" "tree" "wooden fence post" "ground"
```

### 4. Kiểm tra output
Script tự báo % diện tích khung hình mỗi layer chiếm — nếu một layer gần 0%,
nhãn đó khả năng không khớp với gì trong ảnh (VD: gõ "cloud" nhưng ảnh không
có mây rõ ràng) → cần sửa lại nhãn hoặc yêu cầu `sdd-asset-generator` tạo lại
ảnh có đủ chi tiết cho nhãn đó.

### 5. Giới hạn cần biết — không phải phép màu
- CLIPSeg là model zero-shot nhẹ — **không** chính xác bằng segmentation
  chuyên dụng train riêng cho 1 domain. Biên layer có thể hơi "nhòe"/không
  sát pixel-perfect như tách sản phẩm bằng `remove_bg.py`. Với game pixel-art
  độ chi tiết cao, luôn xem output trước khi dùng, không mặc định là đúng.
- Nhãn mơ hồ (VD: "background" chung chung) cho kết quả kém hơn nhãn cụ thể
  (VD: "distant blue mountain range"). Viết nhãn càng mô tả cụ thể, kết quả
  càng chính xác — áp dụng nguyên tắc này khi `sdd-asset-generator` soạn danh
  sách nhãn.
- Các layer được resolve **loại trừ lẫn nhau** (mỗi pixel chỉ thuộc về 1 layer
  duy nhất, layer nào có confidence cao nhất thắng) — nếu 2 vùng thật sự chồng
  lấn trong ảnh gốc (VD: cây che một phần bầu trời), việc này là đúng và cần
  thiết, không phải lỗi.

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
