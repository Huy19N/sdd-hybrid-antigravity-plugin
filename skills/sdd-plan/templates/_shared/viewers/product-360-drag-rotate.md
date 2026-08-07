---
id: product-360-drag-rotate
name: "360° Drag-Rotate Product Viewer"
type: shared-module
module_category: viewer
tags:
  - 360
  - product-viewer
  - drag-rotate
  - interactive-gallery
  - figurine
  - watch
  - shoe
  - vehicle
compatible_with: all
pairs_well_with:
  - 3d-motion-frame
best_for: "Bất kỳ sản phẩm nào user cần 'nhìn từ mọi góc' trước khi mua/quyết định: giày, đồng hồ, mô hình/figurine, xe, đồ nội thất, trang sức — biến 1 sản phẩm tĩnh thành trải nghiệm xoay 360 độ"
---

# Shared Module: 360° Drag-Rotate Product Viewer

## Preview Description
Người dùng giữ chuột (hoặc chạm) và kéo ngang trên sản phẩm → sản phẩm xoay
theo, mô phỏng cảm giác cầm vật thể thật trên tay xoay ngắm. Đây **không phải**
component có sẵn của ReactBits — là kỹ thuật tự viết, có 2 cách triển khai tuỳ
loại asset bạn có.

## Chọn cách triển khai — quan trọng, chọn sai sẽ tốn công làm lại

| | Cách A — Image Sequence Spin | Cách B — True 3D (Three.js) |
|---|---|---|
| Cần gì | Bộ ảnh sản phẩm chụp/render từ nhiều góc (24-72 ảnh) | File model 3D thật (`.glb`/`.gltf`) |
| Độ chân thực | Rất tốt cho xoay ngang, **không xoay dọc/nghiêng được** | Xoay mọi trục, ánh sáng phản ứng thật |
| Chi phí dựng | Thấp — chụp ảnh sản phẩm nhiều góc hoặc render 3D ra ảnh | Cao hơn — cần model 3D + `react-three-fiber` |
| Dùng khi | Không có sẵn model 3D (đa số trường hợp thực tế: giày, mô hình, đồng hồ chụp ảnh thật) | Đã có sẵn model 3D (automotive showroom, sản phẩm công nghiệp) |
| Khớp với template nào | `product-carousel`, `fashion-ecommerce`, `shoppable-lifestyle-scene` | `automotive` — đúng lỗ hổng "360° View CTA (placeholder)" đã có sẵn trong template này |

**Mặc định dùng Cách A** trừ khi project đã xác nhận có model 3D thật.

---

## Cách A — Image Sequence Spin

### Chuẩn bị ảnh
- Chụp/render sản phẩm quay đều 360°, số khung hình khuyến nghị: **36 ảnh**
  (mỗi ảnh cách nhau 10°) — cân bằng giữa mượt và dung lượng. 24 ảnh = nhẹ
  nhưng hơi giật; 72 ảnh = rất mượt nhưng nặng gấp đôi, chỉ dùng khi sản phẩm
  là điểm nhấn duy nhất của trang.
- Cùng kích thước, cùng góc sáng, nền đồng nhất (lý tưởng: nền trong suốt/nền
  trắng để dễ tách) — không tách nền lẫn lộn giữa các khung, sẽ bị "nhấp nháy"
  khi xoay.
- Tối ưu: WebP, preload khung đầu tiên ngay (`<link rel="preload">`), các
  khung còn lại tải nền sau khi khung đầu hiển thị.

### Logic xoay

```tsx
const TOTAL_FRAMES = 36;
const SENSITIVITY = 5; // px kéo = 1 khung hình; số càng nhỏ xoay càng nhanh

const [frameIndex, setFrameIndex] = useState(0);
const dragRef = useRef({
  dragging: false,
  startX: 0,
  startFrame: 0,
  velocityLog: [] as { x: number; t: number }[],
});

function onPointerDown(e: React.PointerEvent) {
  dragRef.current = { dragging: true, startX: e.clientX, startFrame: frameIndex, velocityLog: [] };
  (e.target as Element).setPointerCapture(e.pointerId);
}

function onPointerMove(e: React.PointerEvent) {
  if (!dragRef.current.dragging) return;
  const deltaX = e.clientX - dragRef.current.startX;
  const framesDelta = Math.round(deltaX / SENSITIVITY);
  const next = ((dragRef.current.startFrame - framesDelta) % TOTAL_FRAMES + TOTAL_FRAMES) % TOTAL_FRAMES;
  setFrameIndex(next);
  dragRef.current.velocityLog.push({ x: e.clientX, t: performance.now() });
  if (dragRef.current.velocityLog.length > 5) dragRef.current.velocityLog.shift();
}

function onPointerUp() {
  dragRef.current.dragging = false;
  applyInertia(); // xem phần Inertia bên dưới
}
```

### Inertia (quán tính khi thả tay) — cho cảm giác "vật thật"
Tính vận tốc từ vài điểm di chuyển gần nhất trước khi thả, rồi giảm dần bằng
`requestAnimationFrame`:

```tsx
function applyInertia() {
  const log = dragRef.current.velocityLog;
  if (log.length < 2) return;
  const [a, b] = [log[0], log[log.length - 1]];
  let velocity = (b.x - a.x) / (b.t - a.t); // px/ms

  function decay() {
    if (Math.abs(velocity) < 0.02) return;
    setFrameIndex(prev => {
      const framesDelta = Math.round(velocity * 16 / SENSITIVITY); // ~1 frame @ 60fps
      return ((prev - framesDelta) % TOTAL_FRAMES + TOTAL_FRAMES) % TOTAL_FRAMES;
    });
    velocity *= 0.94; // hệ số giảm tốc — 0.9-0.96 là khoảng hợp lý
    requestAnimationFrame(decay);
  }
  requestAnimationFrame(decay);
}
```

### Input bổ sung — lăn chuột & chuột phải

**Lăn chuột (scroll wheel):**
```tsx
function onWheel(e: React.WheelEvent) {
  e.preventDefault(); // chỉ chặn scroll TRÊN viewer, không chặn scroll toàn trang
  const framesDelta = Math.sign(e.deltaY) * 2; // mỗi tick lăn = 2 khung
  setFrameIndex(prev => ((prev + framesDelta) % TOTAL_FRAMES + TOTAL_FRAMES) % TOTAL_FRAMES);
}
```
⚠️ **Cảnh báo UX quan trọng**: nếu viewer nằm giữa trang và cho phép lăn chuột
xoay mọi lúc, người dùng đang cố cuộn trang xuống sẽ bị "kẹt" ở viewer, rất
khó chịu. Khuyến nghị: **chỉ bật lăn-chuột-để-xoay khi viewer đang ở trạng
thái "focused"** (user đã click vào viewer trước, có viền highlight rõ ràng
báo hiệu "đang điều khiển"), hoặc dùng phím bổ trợ (`e.shiftKey`), thay vì bật
mặc định toàn thời gian.

**Chuột phải + kéo:**
```tsx
function onContextMenu(e: React.MouseEvent) {
  e.preventDefault(); // chỉ chặn menu chuột phải TRÊN viewer, không global
}
function onPointerDown(e: React.PointerEvent) {
  if (e.button === 2) {
    // chuột phải: dùng cho xoay nhanh/xoay chi tiết hơn (VD: sensitivity thấp hơn)
  }
  // ... phần còn lại giống pointer down thường
}
```
Chỉ `preventDefault()` trên `onContextMenu` của **chính element viewer**,
tuyệt đối không set global — sẽ chặn luôn chuột phải của cả trang, phá trải
nghiệm chuẩn của trình duyệt ở mọi nơi khác.

### UI phụ trợ
- Icon xoay nhỏ + text hint "Kéo để xoay 360°" — hiện lần đầu, tự fade sau khi
  user tương tác lần đầu tiên (cùng pattern one-time-hint đã dùng ở
  `21-scene-doodle-annotation.md`)
- Progress dots hình tròn quanh viewer thể hiện góc hiện tại (tuỳ chọn, đẹp
  nhưng không bắt buộc)
- Cursor đổi thành `grab` / `grabbing` khi hover/kéo

---

## Cách B — True 3D (react-three-fiber + OrbitControls)

Dùng khi đã có file `.glb`/`.gltf`. Khớp trực tiếp với template `automotive`
(mục "6. Gallery / 360° View" hiện có placeholder "360° View CTA button
(placeholder for future integration)" — module này chính là phần lấp vào đó).

```tsx
import { Canvas } from '@react-three/fiber';
import { OrbitControls, useGLTF } from '@react-three/drei';

function Model() {
  const { scene } = useGLTF('/models/product.glb');
  return <primitive object={scene} />;
}

function Viewer360() {
  return (
    <Canvas camera={{ position: [0, 1, 4], fov: 40 }}>
      <ambientLight intensity={0.6} />
      <directionalLight position={[5, 5, 5]} intensity={1} />
      <Model />
      <OrbitControls
        enablePan={false}
        enableZoom={true}
        minPolarAngle={Math.PI / 4}
        maxPolarAngle={Math.PI / 1.6}
        autoRotate
        autoRotateSpeed={0.6}   // tự xoay chậm khi không tương tác — dừng khi user chạm vào
      />
    </Canvas>
  );
}
```
`OrbitControls` đã tự xử lý kéo-chuột-trái-để-xoay, lăn-chuột-để-zoom, và có
thể cấu hình `mouseButtons={{ RIGHT: THREE.MOUSE.ROTATE }}` nếu muốn chuột
phải cũng xoay được thay vì mặc định pan.

## Prompt (condensed, cho Cách A — mặc định)

Build a 360° drag-rotate product viewer in React + TypeScript + Tailwind CSS.
Load a 36-frame image sequence of the product (preload frame 0 immediately,
lazy-load the rest). On pointer drag (left-click or touch), map horizontal
drag delta to frame index (~5px per frame), wrapping around 36 frames. On
release, apply inertia: compute velocity from the last few move events, decay
it each animation frame (×0.94) while advancing frames, stop below a small
velocity threshold. Support right-click-drag as an alternate rotate gesture
(`preventDefault` on `contextmenu` scoped to the viewer only). Support scroll
wheel to step frames **only while the viewer is in a focused/clicked state**
— do not hijack page scroll by default. Show a one-time "Kéo để xoay 360°"
hint that fades after first interaction. Cursor: `grab` idle, `grabbing` while
dragging.

## Required Assets
- `product-360-frames` — 36 ảnh sản phẩm chụp/render đều góc quanh 360° (Cách
  A), hoặc 1 file `.glb`/`.gltf` model 3D (Cách B) — nêu rõ cách nào khi giao
  cho `sdd-asset-generator`

## ReactBits Components Used
Không dùng component ReactBits có sẵn — toàn bộ là logic tự viết (Cách A) hoặc
`@react-three/fiber` + `@react-three/drei` (Cách B, thư viện ngoài ReactBits).
