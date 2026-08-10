---
id: scroll-scrubbing-video
name: "Scroll-Scrubbing Video"
type: shared-module
module_category: viewer
tags:
  - video
  - scroll
  - scrubbing
  - pinned-section
  - cinematic
compatible_with: all
pairs_well_with:
  - grain-noise-overlay
best_for: "Hero section hoặc section giới thiệu sản phẩm muốn video 'tua' theo đúng vị trí cuộn trang — kiểu hiệu ứng Apple product page. Nguồn video nên tạo qua sdd-video-generator (Veo 3.1) hoặc video có sẵn."
requires_asset: "1 video .mp4 ngắn (khuyến nghị ≤8s) — xem sdd-video-generator"
---

# Shared Module: Scroll-Scrubbing Video

## Preview Description
Video không tự chạy — nó "đứng yên" và **tua tới đúng khung hình tương ứng
với vị trí cuộn trang** của người dùng: cuộn xuống thì video tiến, cuộn lên
thì video lùi, y hệt cảm giác đang "vặn" thời gian bằng con lăn chuột. Section
chứa video được ghim (pin) tại chỗ trong lúc cuộn qua một vùng cao hơn màn
hình nhiều lần, tạo cảm giác "màn hình đứng yên nhưng thời gian trong video
trôi theo tay mình".

## Chọn cách triển khai — ảnh hưởng lớn tới độ mượt

| | Cách A — Native `<video>` seeking | Cách B — Canvas + frame sequence (khuyến nghị) |
|---|---|---|
| Input | 1 file `.mp4` | Chuỗi ảnh WebP tách từ video (`extract_frames.py`) |
| Độ mượt | Có thể giật — `currentTime` seek không tức thời trên mọi trình duyệt | Mượt tuyệt đối — vẽ đúng frame đã có sẵn lên canvas, không tốn công decode video mỗi lần |
| Độ phức tạp setup | Thấp — chỉ cần 1 thẻ `<video>` | Cao hơn — cần chạy `extract_frames.py` trước, preload N ảnh |
| Nguồn cảm hứng | — | Đây chính là kỹ thuật Apple dùng cho trang sản phẩm (AirPods, iPhone) |

**Mặc định dùng Cách B** nếu section này là điểm nhấn chính của trang (hero).
Cách A chỉ nên dùng cho case phụ/ít quan trọng, chấp nhận độ mượt thấp hơn để
đổi lấy setup đơn giản.

---

## Cơ chế ghim (pin) — dùng chung cho cả 2 cách

```tsx
// Wrapper cao hơn viewport nhiều lần — độ cao này quyết định "quãng cuộn"
// tương ứng với toàn bộ chiều dài video. Càng cao, cuộn càng "chậm"/chi tiết.
<div style={{ height: '400vh', position: 'relative' }}>
  <div style={{ position: 'sticky', top: 0, height: '100vh', overflow: 'hidden' }}>
    {/* video hoặc canvas nằm ở đây, luôn lấp đầy 100vh trong lúc bị ghim */}
  </div>
</div>
```
`position: sticky` xử lý phần "ghim" thuần CSS, không cần JS can thiệp vào việc
pin — JS chỉ cần đọc % cuộn đã đi qua vùng `400vh` đó để suy ra frame/thời gian
tương ứng.

## Tính % cuộn (dùng chung)

```tsx
function useScrollProgress(wrapperRef: React.RefObject<HTMLDivElement>) {
  const [progress, setProgress] = useState(0); // 0 -> 1

  useEffect(() => {
    function onScroll() {
      if (!wrapperRef.current) return;
      const rect = wrapperRef.current.getBoundingClientRect();
      const wrapperHeight = wrapperRef.current.offsetHeight;
      const viewportHeight = window.innerHeight;
      // Quãng đường cuộn thực tế bên trong wrapper (đã trừ phần pin 100vh)
      const scrolled = -rect.top;
      const scrollable = wrapperHeight - viewportHeight;
      const raw = scrolled / scrollable;
      setProgress(Math.min(1, Math.max(0, raw)));
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  return progress; // dùng requestAnimationFrame throttle nếu cần mượt hơn nữa
}
```
Cân nhắc throttle bằng `requestAnimationFrame` nếu thấy giật trên máy yếu —
không bắt buộc, tuỳ mức độ phức tạp của trang.

---

## Cách A — Native `<video>` seeking

```tsx
function ScrollVideoNative({ src }: { src: string }) {
  const wrapperRef = useRef<HTMLDivElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);
  const progress = useScrollProgress(wrapperRef);

  useEffect(() => {
    const video = videoRef.current;
    if (!video || !video.duration) return;
    video.currentTime = progress * video.duration;
  }, [progress]);

  return (
    <div ref={wrapperRef} style={{ height: '400vh', position: 'relative' }}>
      <div style={{ position: 'sticky', top: 0, height: '100vh', overflow: 'hidden' }}>
        <video
          ref={videoRef}
          src={src}
          muted
          playsInline
          preload="auto"
          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        />
      </div>
    </div>
  );
}
```
`muted` + `playsInline` bắt buộc — trình duyệt (đặc biệt Safari/iOS) chặn
autoplay/seek script trên video có âm thanh hoặc không có `playsInline`.

---

## Cách B — Canvas + frame sequence (khuyến nghị)

### Bước 1 — Tách frame (chạy trước, 1 lần)
```bash
python skills/sdd-video-generator/scripts/extract_frames.py \
  --input public/assets/video/hero.mp4 \
  --output public/assets/video/hero-frames/ \
  --fps 12
```
8 giây × 12fps ≈ 96 frame — đủ mượt cho scroll-scrub, không quá nặng.

### Bước 2 — Component

```tsx
function ScrollVideoCanvas({ framePathPattern, frameCount }: {
  framePathPattern: string; // VD: '/assets/video/hero-frames/frame-%04d.webp'
  frameCount: number;
}) {
  const wrapperRef = useRef<HTMLDivElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const imagesRef = useRef<HTMLImageElement[]>([]);
  const [loaded, setLoaded] = useState(false);
  const progress = useScrollProgress(wrapperRef);

  // Preload toàn bộ frame — chấp nhận vì đã downsample fps ở bước tách
  useEffect(() => {
    const images: HTMLImageElement[] = [];
    let loadedCount = 0;
    for (let i = 1; i <= frameCount; i++) {
      const img = new Image();
      img.src = framePathPattern.replace('%04d', String(i).padStart(4, '0'));
      img.onload = () => {
        loadedCount++;
        if (loadedCount === frameCount) setLoaded(true);
      };
      images.push(img);
    }
    imagesRef.current = images;
  }, [framePathPattern, frameCount]);

  // Vẽ frame tương ứng với progress
  useEffect(() => {
    if (!loaded || !canvasRef.current) return;
    const frameIndex = Math.min(
      frameCount - 1,
      Math.floor(progress * frameCount)
    );
    const img = imagesRef.current[frameIndex];
    const ctx = canvasRef.current.getContext('2d');
    if (ctx && img) {
      // cover-fit thủ công để khớp objectFit: cover
      const canvas = canvasRef.current;
      const scale = Math.max(canvas.width / img.width, canvas.height / img.height);
      const x = (canvas.width - img.width * scale) / 2;
      const y = (canvas.height - img.height * scale) / 2;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, x, y, img.width * scale, img.height * scale);
    }
  }, [progress, loaded, frameCount]);

  return (
    <div ref={wrapperRef} style={{ height: '400vh', position: 'relative' }}>
      <div style={{ position: 'sticky', top: 0, height: '100vh', overflow: 'hidden' }}>
        {!loaded && <div className="absolute inset-0 flex items-center justify-center">
          Đang tải video...
        </div>}
        <canvas
          ref={canvasRef}
          width={1920} height={1080}
          style={{ width: '100%', height: '100%' }}
        />
      </div>
    </div>
  );
}
```

### Lưu ý hiệu năng
- Preload TOÀN BỘ frame chấp nhận được vì đã downsample fps xuống 12 — với
  video dài hơn 8s hoặc fps cao hơn, cân nhắc lazy-load theo cụm (load trước
  20 frame quanh vị trí hiện tại, load thêm khi cuộn tới gần).
- `canvas.width`/`height` cố định (VD: 1920×1080) rồi CSS scale xuống —
  không set kích thước canvas bằng % để tránh vẽ lại toàn bộ ảnh ở độ phân
  giải sai mỗi lần resize.

## Prompt (condensed, Cách B)

Build a scroll-scrubbing video section in React + TypeScript + Tailwind CSS.
Wrap content in a `400vh` tall container with a `position: sticky, top: 0,
height: 100vh` inner section (pure CSS pin, no scroll-jacking JS). Track scroll
progress (0-1) through the wrapper via `getBoundingClientRect` on scroll
(passive listener). Preload a sequence of WebP frames (extracted via ffmpeg at
~12fps from an 8s source video), and on each progress update, draw the
frame at `Math.floor(progress * frameCount)` onto a `<canvas>` with manual
cover-fit scaling. Show a loading state until all frames are preloaded.

## Required Assets
- 1 video nguồn `.mp4` (từ `sdd-video-generator` hoặc có sẵn) — Cách A dùng
  trực tiếp, Cách B cần chạy qua `extract_frames.py` trước để có chuỗi WebP.

## ReactBits Components Used
Không dùng component ReactBits có sẵn — thuần React state + Canvas API +
`position: sticky`.
