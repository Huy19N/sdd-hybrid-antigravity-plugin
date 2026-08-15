---
id: swipeable-card-stack
name: "Swipeable Gesture Card Stack"
type: shared-module
module_category: mobile
platform: mobile-first
tags:
  - swipe-cards
  - gestures
  - pan-responder
  - tinder-swipe
  - card-stack
  - mobile-discovery
compatible_with: all
pairs_well_with:
  - haptic-tab-bar
  - holographic-shimmer
  - mobile-bottom-sheet
best_for: "Khám phá sản phẩm thời trang/ẩm thực (Shop-by-Swipe), chọn outfit, tìm kiếm bất động sản, app hẹn hò/kết nối, xem tin tức ngắn — tương tác vuốt trái/phải vật lý tự nhiên."
requires_asset: "Danh sách 3-5 ảnh tỷ lệ dọc 4:5 hoặc 9:16 từ sdd-asset-generator với chủ thể rõ nét và ánh sáng kịch tính."
---

# Shared Module: Swipeable Gesture Card Stack

## Preview Description
Ngăn xếp thẻ bài tương tác vuốt vật lý (**Physics-Based Swipeable Card Stack**): Người dùng dùng ngón tay kéo thẻ bài trên cùng — thẻ sẽ xoay theo lực kéo và góc ngón tay. Vuốt sang phải (Yêu thích / Thêm vào giỏ), vuốt sang trái (Bỏ qua), hoặc vuốt lên (Xem chi tiết). Kèm nhãn "LIKE" / "NOPE" phát sáng theo lực kéo và rung phản hồi Haptic khi thẻ rời khỏi màn hình.

---

## Kỹ thuật triển khai Đa Nền Tảng

### 1. React Native / Expo (TypeScript + Reanimated 3 + Gesture Handler)

```tsx
import React from 'react';
import { View, Text, Image, Dimensions } from 'react-native';
import { GestureDetector, Gesture } from 'react-native-gesture-handler';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
  runOnJS,
  interpolate,
} from 'react-native-reanimated';
import * as Haptics from 'expo-haptics';

const { width: SCREEN_WIDTH } = Dimensions.get('window');
const SWIPE_THRESHOLD = SCREEN_WIDTH * 0.35;

interface CardItem {
  id: string;
  title: string;
  subtitle: string;
  imageUrl: string;
}

export const SwipeableCard: React.FC<{
  card: CardItem;
  onSwipeRight: (card: CardItem) => void;
  onSwipeLeft: (card: CardItem) => void;
}> = ({ card, onSwipeRight, onSwipeLeft }) => {
  const translateX = useSharedValue(0);
  const translateY = useSharedValue(0);

  const triggerHaptic = () => {
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium);
  };

  const panGesture = Gesture.Pan()
    .onUpdate((e) => {
      translateX.value = e.translationX;
      translateY.value = e.translationY;
    })
    .onEnd(() => {
      if (translateX.value > SWIPE_THRESHOLD) {
        translateX.value = withSpring(SCREEN_WIDTH * 1.5);
        runOnJS(triggerHaptic)();
        runOnJS(onSwipeRight)(card);
      } else if (translateX.value < -SWIPE_THRESHOLD) {
        translateX.value = withSpring(-SCREEN_WIDTH * 1.5);
        runOnJS(triggerHaptic)();
        runOnJS(onSwipeLeft)(card);
      } else {
        translateX.value = withSpring(0);
        translateY.value = withSpring(0);
      }
    });

  const animatedStyle = useAnimatedStyle(() => {
    const rotate = `${interpolate(translateX.value, [-SCREEN_WIDTH, SCREEN_WIDTH], [-18, 18])}deg`;
    return {
      transform: [
        { translateX: translateX.value },
        { translateY: translateY.value },
        { rotate },
      ],
    };
  });

  return (
    <GestureDetector gesture={panGesture}>
      <Animated.View
        style={animatedStyle}
        className="absolute w-full h-[520px] rounded-3xl overflow-hidden shadow-2xl bg-neutral-900 border border-white/10"
      >
        <Image source={{ uri: card.imageUrl }} className="w-full h-full object-cover" />
        <View className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent p-6 justify-end">
          <Text className="text-2xl font-bold text-white">{card.title}</Text>
          <Text className="text-sm text-neutral-300 mt-1">{card.subtitle}</Text>
        </View>
      </Animated.View>
    </GestureDetector>
  );
};
```

---

### 2. Flutter (Dart + `Dismissible` / Drag Gestures)

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class SwipeableCardStack extends StatefulWidget {
  final List<Map<String, String>> items;
  final Function(Map<String, String>) onLiked;
  final Function(Map<String, String>) onPassed;

  const SwipeableCardStack({
    Key? key,
    required this.items,
    required this.onLiked,
    required this.onPassed,
  }) : super(key: key);

  @override
  State<SwipeableCardStack> createState() => _SwipeableCardStackState();
}

class _SwipeableCardStackState extends State<SwipeableCardStack> {
  int currentIndex = 0;

  @override
  Widget build(BuildContext context) {
    if (currentIndex >= widget.items.length) {
      return const Center(child: Text("Đã xem hết danh mục", style: TextStyle(color: Colors.white70)));
    }
    final item = widget.items[currentIndex];

    return Dismissible(
      key: Key(item['id'] ?? UniqueKey().toString()),
      onDismissed: (direction) {
        HapticFeedback.lightImpact();
        if (direction == DismissDirection.endToStart) {
          widget.onPassed(item);
        } else {
          widget.onLiked(item);
        }
        setState(() {
          currentIndex++;
        });
      },
      child: Container(
        height: 520,
        margin: const EdgeInsets.symmetric(horizontal: 16),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(28),
          image: DecorationImage(
            image: NetworkImage(item['imageUrl']!),
            fit: BoxFit.cover,
          ),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.4),
              blurRadius: 20,
              offset: const Offset(0, 10),
            )
          ],
        ),
        child: Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(28),
            gradient: const LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [Colors.transparent, Colors.black87],
            ),
          ),
          padding: const EdgeInsets.all(24),
          alignment: Alignment.bottomLeft,
          child: Text(
            item['title'] ?? '',
            style: const TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.bold),
          ),
        ),
      ),
    );
  }
}
```

---

### 3. Kotlin + Jetpack Compose (`PointerInput` & `Animatable`)

```kotlin
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.spring
import androidx.compose.foundation.gestures.detectDragGestures
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.launch

@Composable
fun SwipeableCardItem(
    title: String,
    onSwipeRight: () -> Unit,
    onSwipeLeft: () -> Unit
) {
    val offsetX = remember { Animatable(0f) }
    val scope = rememberCoroutineScope()

    Card(
        shape = RoundedCornerShape(28.dp),
        modifier = Modifier
            .fillMaxWidth()
            .height(520.dp)
            .graphicsLayer {
                translationX = offsetX.value
                rotationZ = (offsetX.value / 40f).coerceIn(-20f, 20f)
            }
            .pointerInput(Unit) {
                detectDragGestures(
                    onDragEnd = {
                        scope.launch {
                            if (offsetX.value > 300f) {
                                offsetX.animateTo(1200f, spring())
                                onSwipeRight()
                            } else if (offsetX.value < -300f) {
                                offsetX.animateTo(-1200f, spring())
                                onSwipeLeft()
                            } else {
                                offsetX.animateTo(0f, spring())
                            }
                        }
                    },
                    onDrag = { change, dragAmount ->
                        change.consume()
                        scope.launch { offsetX.snapTo(offsetX.value + dragAmount.x) }
                    }
                )
            }
    ) {
        Box(modifier = Modifier.fillMaxSize().padding(24.dp)) {
            Text(text = title)
        }
    }
}
```
