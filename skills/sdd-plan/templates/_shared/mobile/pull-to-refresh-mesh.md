---
id: pull-to-refresh-mesh
name: "Elastic Pull-to-Refresh Mesh Indicator"
type: shared-module
module_category: mobile
platform: mobile-first
tags:
  - pull-to-refresh
  - spring-physics
  - mesh-gradient
  - fluid-motion
  - touch-gestures
compatible_with: all
pairs_well_with:
  - haptic-tab-bar
  - ambient-glow-cursor
  - grain-noise-overlay
best_for: "Bảng tin (Feeds), danh sách sản phẩm mới, cập nhật thị trường crypto/chứng khoán, trang tin tức magazine — hiệu ứng kéo thả mượt mà với chuyển động hạt màu lò xo thay thế cho vòng xoay mặc định."
requires_asset: "Không yêu cầu asset riêng — sử dụng CSS/Canvas/SVG shader sinh hạt màu gradient theo bảng màu của template."
---

# Shared Module: Elastic Pull-to-Refresh Mesh Indicator

## Preview Description
Hiệu ứng kéo làm mới danh sách (**Elastic Pull-to-Refresh Indicator**) tích hợp lò xo đàn hồi (*spring physics*): Khi người dùng kéo ngón tay từ đầu danh sách xuống dưới, một khối chất lỏng gradient đa sắc (*fluid mesh blob*) sẽ giãn nở theo khoảng cách kéo, phát xung rung Haptic khi đạt ngưỡng kích hoạt (*trigger threshold*), và xoay vòng lấp lánh trong lúc tải dữ liệu mới.

---

## Kỹ thuật triển khai Đa Nền Tảng

### 1. React Native / Expo (TypeScript + NativeWind + `RefreshControl` + Reanimated)

```tsx
import React, { useState } from 'react';
import { ScrollView, RefreshControl, View, Text } from 'react-native';
import * as Haptics from 'expo-haptics';

export const ElasticRefreshScrollView: React.FC<{
  onRefresh: () => Promise<void>;
  children: React.ReactNode;
}> = ({ onRefresh, children }) => {
  const [refreshing, setRefreshing] = useState(false);

  const handleRefresh = async () => {
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium);
    setRefreshing(true);
    await onRefresh();
    setRefreshing(false);
    Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
  };

  return (
    <ScrollView
      refreshControl={
        <RefreshControl
          refreshing={refreshing}
          onRefresh={handleRefresh}
          tintColor="#A855F7" // Màu tím neon hoặc accent của template
          colors={['#A855F7', '#EC4899', '#3B82F6']} // Gradient animation trên Android
        />
      }
      className="flex-1 bg-neutral-950"
    >
      {children}
    </ScrollView>
  );
};
```

---

### 2. Flutter (Dart + `RefreshIndicator` / `CustomScrollView`)

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class ElasticRefreshView extends StatelessWidget {
  final Future<void> Function() onRefresh;
  final Widget child;

  const ElasticRefreshView({
    Key? key,
    required this.onRefresh,
    required this.child,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return RefreshIndicator(
      color: Colors.purpleAccent,
      backgroundColor: const Color(0xFF1E1E1E),
      strokeWidth: 3.0,
      displacement: 40,
      onRefresh: () async {
        HapticFeedback.mediumImpact();
        await onRefresh();
        HapticFeedback.lightImpact();
      },
      child: child,
    );
  }
}
```
