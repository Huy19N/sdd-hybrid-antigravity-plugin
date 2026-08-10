---
name: sdd-video-generator
version: 1
description: "Sub-skill invoked by sdd-build when a chosen template or _shared module needs a generated video asset (e.g. a hero background video, or a source clip for the scroll-scrubbing-video module). Also invocable directly when the user asks to generate a video. Generates video using Google's Veo 3.1 model via the Gemini API — NOT via the Google Flow web app, which has no public API (see 'Flow vs. API' below)."
---

# SDD Video Generator (sub-skill of sdd-build)

## Purpose
Generate short video assets (8s max per clip) for use as: web scroll-effect
source material (see companion module `_shared/viewers/scroll-scrubbing-video.md`),
hero background video, or general media resources for other modules/templates.

## Flow vs. API — đọc trước khi dùng skill này
"Google Flow" (labs.google/flow) là **web app sáng tạo**, không phải API. Nó
chạy trên nền model **Veo** (cùng model, khác lớp vỏ) nhưng bản thân Flow
**không có API công khai** — Flow dùng credit theo gói Google AI Pro/Ultra,
thao tác qua giao diện web, không tự động hoá được trong pipeline.

Route lập trình được thật sự là **Gemini API + model Veo 3.1** trực tiếp — đây
là route skill này dùng. Cùng model Veo mà Flow dùng, chỉ khác là gọi thẳng
qua API thay vì qua giao diện Flow.

| | Cách A — Gemini API (skill này dùng) | Cách B — Flow (thủ công) |
|---|---|---|
| Tự động hoá trong `sdd-build`? | ✅ Có | ❌ Không — cần người vào labs.google/flow |
| Cần gì | `GEMINI_API_KEY` (aistudio.google.com/apikey) | Tài khoản Google AI Pro/Ultra (Flow: 1.000 credit/tháng ở gói Pro) |
| Phù hợp khi | Sinh video theo pipeline, batch, không cần chỉnh tay | Cần storyboard nhiều cảnh, character consistency phức tạp, chỉnh camera thủ công lặp lại nhiều lần |
| Chi phí | Tính theo giây/độ phân giải qua Gemini API billing | Theo credit gói subscription |

Skill này **chỉ tự động hoá Cách A**. Với Cách B, skill có thể soạn sẵn 1
"prompt package" chuẩn theo khung viết prompt của Veo (xem mục Process bước
3) để user tự dán vào Flow khi cần kiểm soát sáng tạo cao hơn.

## Invocation
- Tự động: khi `sdd-build` gặp task cần asset video (template/module frontmatter
  có yêu cầu video, hoặc `_shared/viewers/scroll-scrubbing-video.md` được chọn
  ở bước `sdd-plan` và chưa có source video).
- Thủ công: khi user yêu cầu trực tiếp "tạo video cho...".

## Preconditions
- Python 3.10+.
- `pip install google-genai`
- Biến môi trường `GEMINI_API_KEY` đã set (lấy tại https://aistudio.google.com/apikey).
- (Tuỳ chọn, chỉ cần nếu dùng module scroll-scrubbing-video theo hướng canvas
  frame-sequence) `ffmpeg` cài sẵn trên PATH.

## Model tiers

| Tier | Model ID (Gemini API) | Đặc điểm | Dùng khi |
|---|---|---|---|
| `lite` | `veo-3.1-lite-generate-preview` | Rẻ/nhanh nhất, 720p/1080p, **không** hỗ trợ video extension hay reference images | Draft, test prompt, video ngắn không cần hiệu ứng nâng cao |
| `fast` (mặc định) | `veo-3.1-fast-generate-preview` | Cân bằng, đầy đủ tính năng (extension, reference images), lên tới 4K | Phần lớn use case sản xuất — mặc định hợp lý |
| `standard` | `veo-3.1-generate-preview` | Chất lượng cao nhất, chậm/đắt nhất, cùng feature set với `fast` | Hero video chính, cảnh cần chất lượng cinematic cao |

⚠️ Cả 3 model đang ở trạng thái **Preview** (theo tài liệu chính thức của
Google) — tên model ID và tham số config có thể đổi. Nếu script lỗi tham số,
kiểm tra lại https://ai.google.dev/gemini-api/docs/veo trước khi debug sâu.
Model Veo 3.0/2.0 cũ đã bị deprecate (Veo 3.0 shutdown 30/6/2026) — script này
**không** dùng các model ID cũ đó.

## Process

### 1. Check dependencies
```bash
pip show google-genai
echo $GEMINI_API_KEY   # phải có giá trị
```

### 2. Xác định thông số video cần tạo
Đọc `plan.md`/module đã chọn để biết: mục đích dùng (hero background / nguồn
cho scroll-scrubbing / asset khác), aspect ratio (`16:9` desktop hero,
`9:16` nếu dùng cho mobile-first hoặc social), độ dài (`4`/`6`/`8` giây —
`8` bắt buộc nếu dùng `1080p`/`4k`).

### 3. Soạn prompt theo khung chuẩn của Veo
Không viết prompt tuỳ hứng — theo đúng khung Google khuyến nghị, lấy dữ liệu
từ `brainstorm.md` + `constitution.md` (palette, tone thương hiệu):

| Yếu tố | Ví dụ |
|---|---|
| Subject (bắt buộc) | "một tách cà phê phin đang nhỏ giọt" |
| Action (bắt buộc) | "giọt cà phê rơi chậm rãi xuống ly, hơi nước bốc lên" |
| Style | "cinematic, tối giản, ánh sáng tự nhiên" |
| Camera positioning/motion | "macro lens, dolly in chậm" |
| Composition | "close-up, shallow focus" |
| Ambiance | "tông màu ấm, warm tones, ánh nắng sáng sớm" |

Nếu video **không có tiếng** trong layout dùng (VD: nguồn cho scroll-scrubbing
— video sẽ bị "mổ" thành từng khung hình tĩnh nên audio vô nghĩa), vẫn nên mô
tả action rõ ràng vì nó ảnh hưởng tới chuyển động hình ảnh — bỏ qua audio cue
trong prompt (không cần thoại/SFX) để tránh tốn generation cho phần không dùng
tới.

### 4. Run generation
```bash
python skills/sdd-video-generator/scripts/generate_video.py \
  --prompt "..." \
  --output public/assets/video/hero-coffee.mp4 \
  --tier fast \
  --aspect-ratio 16:9 \
  --resolution 720p \
  --duration 8
```

### 5. Tải về ngay — quan trọng
Video sinh ra chỉ lưu trên server Google **2 ngày**. Script tự tải file .mp4
về máy ngay khi xong (không có bước "tải sau"). Nếu quá trình bị gián đoạn
giữa chừng, phải chạy lại từ đầu (không resume được từ operation cũ sau 2
ngày).

### 6. Nếu bị chặn bởi safety filter
Veo có filter an toàn — nếu bị chặn, **không bị tính phí** (theo tài liệu
chính thức). Kiểm tra lại prompt có nội dung nhạy cảm/vi phạm chính sách
không, sửa và thử lại. Không cố "lách" filter bằng cách diễn đạt vòng vo.

### 7. Handoff
Trả về đường dẫn file cho `sdd-build`:
```
hero-coffee.mp4 → public/assets/video/hero-coffee.mp4  ✅ (tier: fast, 8s, 720p)
```
Nếu asset này sẽ dùng cho `scroll-scrubbing-video` theo hướng canvas
frame-sequence, tiếp tục chạy `extract_frames.py` (xem SKILL.md của module đó).

## Cách B — Prompt package cho Flow (thủ công)
Khi user cần kiểm soát sáng tạo cao hơn API cho phép (storyboard nhiều cảnh
liên tục, character consistency phức tạp qua nhiều clip), thay vì tự động
generate, in ra prompt đã soạn ở bước 3 dưới dạng khối text sẵn sàng copy, và
hướng dẫn: "Dán prompt này vào labs.google/flow (cần tài khoản Google AI
Pro/Ultra). Sau khi xuất video, đặt file vào `public/assets/video/` và báo lại
đường dẫn để tiếp tục pipeline."

## Constraints
- Mỗi clip tối đa 8 giây (giới hạn model, không phải giới hạn skill) — với nhu
  cầu video dài hơn (VD: background loop dài), dùng video extension
  (`--tier fast` hoặc `standard` hỗ trợ, `lite` không hỗ trợ) hoặc lặp
  (loop) video ngắn ở tầng CSS/JS thay vì cố sinh 1 clip dài.
- Không tự ý nâng `resolution` lên `4k` mặc định — chi phí cao hơn đáng kể,
  chỉ dùng khi user xác nhận cần chất lượng đó.
- Video có watermark SynthID (không nhìn thấy bằng mắt thường) — đây là cơ chế
  của Google, không phải lỗi hay có thể tắt.

## Handoff
Trả danh sách file đã tạo + tier đã dùng cho `sdd-build`, tương tự cách
`sdd-bg-remover` báo cáo kết quả.
