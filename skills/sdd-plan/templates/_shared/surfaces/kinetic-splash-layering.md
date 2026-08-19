---
id: kinetic-splash-layering
name: "Kinetic Liquid Splash & Sandwich Depth Layering"
type: shared-module
module_category: surface
platform: universal
tags:
  - liquid-splash
  - sandwich-layering
  - depth-parallax
  - high-speed-photography
  - kinetic-particles
  - 3d-depth
compatible_with: all
pairs_well_with:
  - 3d-motion-frame
  - ambient-glow-cursor
  - grain-noise-overlay
  - holographic-shimmer
best_for: "Quán trà sữa/cafe nghệ thuật, cocktail bar cao cấp, nước hoa/mỹ phẩm sang trọng, đồ uống năng lượng/thể thao, đồng hồ chống nước — tạo hiệu ứng giọt nước/chất lỏng bắn tung tóe đa lớp kẹp giữa chữ và sản phẩm, chuyển động thị giác 3D siêu thực."
requires_asset: "Bộ ảnh chất lỏng tốc độ cao (High-speed freeze splash 1/8000s) đã qua sdd-asset-generator và tách nền chi tiết siêu vi qua sdd-bg-remover (fine-detail / segment_layers) thành 3 lớp: Back Splash, Main Container, và Front Droplets."
---

# Shared Module: Kinetic Liquid Splash & Sandwich Depth Layering

## Preview Description
Hiệu ứng phân lớp thị giác nghệ thuật đỉnh cao (**Sandwich Depth Layering & Kinetic Liquid Splash**):
Khai thác sức mạnh tách ảnh chi tiết từng giọt nước của `sdd-bg-remover` và `sdd-asset-generator` để tạo ra bố cục đa tầng Z-Index có chiều sâu không gian:
1. **Lớp nền (Back Splash Layer)**: Vệt nước/trà sữa bắn rộng phía sau chữ, chuyển động cuộn chậm (*Parallax 0.4x*).
2. **Lớp chữ Typography (Middle Layer)**: Tiêu đề khổng lồ (VD: *"MATCHA ROYALE"*, *"VELVET BOBA"*) nằm kẹp ở giữa.
3. **Lớp chủ thể chính (Main Product)**: Ly trà sữa / chai nước hoa với ánh sáng viền sắc sảo và hiệu ứng nghiêng 3D theo chuột/con quay hồi chuyển (*3D Tilt*).
4. **Lớp tiền cảnh (Foreground Droplets & Toppings)**: Những giọt nước li ti, trân xoay, lá bạc hà, đá viên bay lơ lửng phía trước chữ và sản phẩm, chuyển động nhanh hơn (*Parallax 1.2x*) tạo cảm giác như đang bắn ra khỏi màn hình về phía mắt người xem.

---

## Cấu trúc Phân Tầng Z-Index (Sandwich Hierarchy)

```
┌───────────────────────────────────────────────────────────┐
│ [Z-Index 40] Foreground Droplets / Flying Toppings (1.2x)  │
│ ┌───────────────────────────────────────────────────────┐ │
│ │ [Z-Index 30] Main Glass / Cup with 3D Tilt (1.0x)     │ │
│ │ ┌───────────────────────────────────────────────────┐ │ │
│ │ │ [Z-Index 20] Big Kinetic Typography ("ROYALE TEA")│ │ │
│ │ │ ┌───────────────────────────────────────────────┐ │ │ │
│ │ │ │ [Z-Index 10] Back Liquid Splash & Corona (0.4x)│ │ │ │
│ │ │ │ ┌───────────────────────────────────────────┐ │ │ │ │
│ │ │ │ │ [Z-Index 0] Dark Radiant Background Canvas │ │ │ │ │
│ │ │ │ └───────────────────────────────────────────┘ │ │ │ │
│ │ │ └───────────────────────────────────────────────┘ │ │ │
│ │ └───────────────────────────────────────────────────┘ │ │
│ └───────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────┘
```

---

## Kỹ thuật triển khai Đa Nền Tảng

### 1. Web (React + Tailwind CSS + Framer Motion / CSS Transforms)

```tsx
import React, { useRef } from 'react';
import { motion, useScroll, useTransform, useMotionValue, useSpring } from 'framer-motion';

interface KineticSplashHeroProps {
  title: string;
  subtitle: string;
  backSplashUrl: string;       // Ảnh vệt nước bắn phía sau (trong suốt)
  mainProductUrl: string;      // Ảnh ly trà sữa / ly cocktail chính (trong suốt)
  frontDropletsUrl: string;    // Ảnh các giọt nước li ti & topping phía trước (trong suốt)
}

export const KineticSplashHero: React.FC<KineticSplashHeroProps> = ({
  title,
  subtitle,
  backSplashUrl,
  mainProductUrl,
  frontDropletsUrl,
}) => {
  const containerRef = useRef<HTMLDivElement>(null);

  // Mouse tilt physics
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);
  const springX = useSpring(mouseX, { stiffness: 120, damping: 18 });
  const springY = useSpring(mouseY, { stiffness: 120, damping: 18 });

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const rect = containerRef.current?.getBoundingClientRect();
    if (!rect) return;
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;
    mouseX.set(x);
    mouseY.set(y);
  };

  // Parallax offsets based on spring
  const backSplashX = useTransform(springX, (x) => x * -25);
  const backSplashY = useTransform(springY, (y) => y * -25);

  const mainProductX = useTransform(springX, (x) => x * 35);
  const mainProductY = useTransform(springY, (y) => y * 35);
  const rotateX = useTransform(springY, (y) => y * -15);
  const rotateY = useTransform(springX, (x) => x * 15);

  const frontDropsX = useTransform(springX, (x) => x * 70);
  const frontDropsY = useTransform(springY, (y) => y * 70);

  return (
    <div
      ref={containerRef}
      onMouseMove={handleMouseMove}
      onMouseLeave={() => { mouseX.set(0); mouseY.set(0); }}
      className="relative w-full h-[750px] overflow-hidden bg-neutral-950 flex items-center justify-center select-none"
    >
      {/* 0. Ambient Radial Glow */}
      <div className="absolute w-[500px] h-[500px] rounded-full bg-amber-500/15 blur-[120px] pointer-events-none" />

      {/* 1. Back Splash Layer (Z-10) */}
      <motion.div
        style={{ x: backSplashX, y: backSplashY }}
        className="absolute inset-0 z-10 flex items-center justify-center pointer-events-none"
      >
        <img
          src={backSplashUrl}
          alt="Back liquid splash"
          className="w-[680px] h-[680px] object-contain opacity-90 filter drop-shadow-[0_20px_50px_rgba(245,158,11,0.25)] animate-pulse"
        />
      </motion.div>

      {/* 2. Middle Typography Layer (Z-20) */}
      <div className="absolute z-20 text-center pointer-events-none">
        <h1 className="text-7xl sm:text-9xl font-black tracking-tighter text-transparent bg-clip-text bg-gradient-to-b from-white via-neutral-200 to-neutral-700 opacity-90 uppercase font-serif">
          {title}
        </h1>
        <p className="text-sm sm:text-base font-medium tracking-[0.3em] text-amber-400/90 uppercase mt-2">
          {subtitle}
        </p>
      </div>

      {/* 3. Main Product Layer (Z-30) */}
      <motion.div
        style={{
          x: mainProductX,
          y: mainProductY,
          rotateX,
          rotateY,
          transformPerspective: 1000,
        }}
        className="relative z-30 flex items-center justify-center"
      >
        <img
          src={mainProductUrl}
          alt="Hero Beverage"
          className="w-[340px] sm:w-[420px] object-contain filter drop-shadow-[0_25px_60px_rgba(0,0,0,0.8)]"
        />
      </motion.div>

      {/* 4. Foreground Droplets & Flying Toppings (Z-40) */}
      <motion.div
        style={{ x: frontDropsX, y: frontDropsY }}
        className="absolute inset-0 z-40 flex items-center justify-center pointer-events-none"
      >
        <img
          src={frontDropletsUrl}
          alt="Flying droplets and toppings"
          className="w-[720px] h-[720px] object-contain filter drop-shadow-[0_10px_25px_rgba(255,255,255,0.2)]"
        />
      </motion.div>
    </div>
  );
};
```

---

### 2. Mobile React Native / Expo (`react-native-reanimated` + Gyroscope / Pan)

```tsx
import React from 'react';
import { View, Text, Image, Dimensions } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
  interpolate,
} from 'react-native-reanimated';
import { GestureDetector, Gesture } from 'react-native-gesture-handler';

const { width: SCREEN_WIDTH } = Dimensions.get('window');

export const MobileKineticSplashHero: React.FC<{
  title: string;
  backSplashUri: string;
  mainProductUri: string;
  frontDropletsUri: string;
}> = ({ title, backSplashUri, mainProductUri, frontDropletsUri }) => {
  const touchX = useSharedValue(0);
  const touchY = useSharedValue(0);

  const panGesture = Gesture.Pan()
    .onUpdate((e) => {
      touchX.value = e.translationX;
      touchY.value = e.translationY;
    })
    .onEnd(() => {
      touchX.value = withSpring(0);
      touchY.value = withSpring(0);
    });

  const backSplashStyle = useAnimatedStyle(() => ({
    transform: [
      { translateX: interpolate(touchX.value, [-100, 100], [-15, 15]) },
      { translateY: interpolate(touchY.value, [-100, 100], [-15, 15]) },
    ],
  }));

  const mainProductStyle = useAnimatedStyle(() => ({
    transform: [
      { translateX: interpolate(touchX.value, [-100, 100], [20, -20]) },
      { translateY: interpolate(touchY.value, [-100, 100], [20, -20]) },
      { rotateZ: `${interpolate(touchX.value, [-100, 100], [-6, 6])}deg` },
    ],
  }));

  const frontDropletsStyle = useAnimatedStyle(() => ({
    transform: [
      { translateX: interpolate(touchX.value, [-100, 100], [45, -45]) },
      { translateY: interpolate(touchY.value, [-100, 100], [45, -45]) },
    ],
  }));

  return (
    <GestureDetector gesture={panGesture}>
      <View className="relative w-full h-[520px] bg-neutral-950 items-center justify-center overflow-hidden">
        {/* Back Splash */}
        <Animated.View style={backSplashStyle} className="absolute z-10">
          <Image source={{ uri: backSplashUri }} className="w-[360px] h-[360px]" resizeMode="contain" />
        </Animated.View>

        {/* Middle Typography */}
        <Text className="absolute z-20 text-5xl font-extrabold text-white/80 uppercase text-center tracking-widest font-serif">
          {title}
        </Text>

        {/* Main Product */}
        <Animated.View style={mainProductStyle} className="relative z-30">
          <Image source={{ uri: mainProductUri }} className="w-[260px] h-[380px]" resizeMode="contain" />
        </Animated.View>

        {/* Foreground Splash Drops */}
        <Animated.View style={frontDropletsStyle} className="absolute z-40">
          <Image source={{ uri: frontDropletsUri }} className="w-[380px] h-[380px]" resizeMode="contain" />
        </Animated.View>
      </View>
    </GestureDetector>
  );
};
```

---

## Quy Chuẩn Tạo Asset Đồng Bộ (`sdd-asset-generator` & `sdd-bg-remover`)

Khi chọn module này, `plan.md` sẽ chỉ định tạo **bộ ảnh chất lỏng tốc độ cao**:

1. **Prompt Tạo Cảnh Splash Tốc Độ Cao (`sdd-asset-generator`)**:
   ```
   "Ultra-high-speed freeze motion commercial photography of an artisanal iced brown sugar milk tea in a crystal fluted glass, captured at 1/8000s shutter speed. Explosive liquid crown of creamy tea and amber caramelized sugar splashing upwards and outwards in mid-air, with sharp translucent fluid arcs, suspended flying tapioca boba pearls, crystalline ice cubes, and thousands of micro condensation droplets catching dramatic strobe light. Obsidian dark background with volumetric rim lighting and crisp caustic refractions. Hasselblad H6D-100c, 100mm macro f/2.8 lens, exquisite Michelin-star beverage art direction."
   ```

2. **Quy Trình Tách Nền & Phân Lớp (`sdd-bg-remover`)**:
   - Sử dụng **Tier `fine-detail`** (`birefnet-dis` + alpha matting) hoặc **Chế độ 2 Multi-Layer Segmentation** (`segment_layers.py` với các nhãn: `["back liquid splash corona", "main glass cup with tea", "flying boba pearls and foreground droplets"]`).
   - Kết quả xuất ra:
     - `public/assets/no-bg/splash-back.png` (vệt nước bắn sau)
     - `public/assets/no-bg/product-core.png` (ly chính)
     - `public/assets/no-bg/splash-front-droplets.png` (giọt nước & trân châu trước)
