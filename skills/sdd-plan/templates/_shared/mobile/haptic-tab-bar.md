---
id: haptic-tab-bar
name: "Floating Haptic Frosted Tab Bar"
type: shared-module
module_category: mobile
platform: mobile-first
tags:
  - haptic-tab-bar
  - bottom-navigation
  - frosted-glass
  - blur
  - micro-interactions
  - safe-area
compatible_with: all
pairs_well_with:
  - mobile-bottom-sheet
  - ambient-glow-cursor
  - stories-avatar-tray
best_for: "Thanh điều hướng chính của toàn bộ app di động (Home, Explore, Orders, Profile) — thiết kế dạng viên thuốc lơ lửng (floating pill) với kính mờ và rung phản hồi chạm."
requires_asset: "Bộ icon vector hoặc icon 3D tỉ lệ 1:1 cho từng tab từ sdd-asset-generator."
---

# Shared Module: Floating Haptic Frosted Tab Bar

## Preview Description
Thanh điều hướng đáy màn hình (**Floating Frosted Tab Bar**) phong cách iOS/macOS đương đại: Lơ lửng cách đáy màn hình 16-24dp, bo tròn mềm mại (*pill shape*), phủ lớp kính mờ (*backdrop blur*), có chấm sáng hoặc viên nang phát quang lướt theo tab đang chọn, và phát ra xung rung xúc giác nhẹ (*Light Haptic Feedback*) mỗi khi người dùng chạm chuyển tab.

---

## Kỹ thuật triển khai Đa Nền Tảng

### 1. React Native / Expo (TypeScript + NativeWind + `expo-blur` + `expo-haptics`)

```tsx
import React from 'react';
import { View, Text, TouchableOpacity, Platform } from 'react-native';
import { BlurView } from 'expo-blur';
import * as Haptics from 'expo-haptics';
import { useSafeAreaInsets } from 'react-native-safe-area-context';

interface TabItem {
  key: string;
  label: string;
  icon: string;
}

export const FloatingHapticTabBar: React.FC<{
  tabs: TabItem[];
  activeTab: string;
  onTabPress: (key: string) => void;
}> = ({ tabs, activeTab, onTabPress }) => {
  const insets = useSafeAreaInsets();

  const handlePress = (key: string) => {
    if (Platform.OS !== 'web') {
      Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
    }
    onTabPress(key);
  };

  return (
    <View
      style={{ paddingBottom: Math.max(insets.bottom, 16) }}
      className="absolute bottom-0 left-0 right-0 items-center pointer-events-box-none px-6"
    >
      <BlurView
        intensity={80}
        tint="dark"
        className="flex-row items-center justify-around w-full max-w-md h-16 rounded-full border border-white/10 overflow-hidden bg-neutral-900/60 shadow-2xl px-2"
      >
        {tabs.map((tab) => {
          const isActive = activeTab === tab.key;
          return (
            <TouchableOpacity
              key={tab.key}
              onPress={() => handlePress(tab.key)}
              className={`flex-1 items-center justify-center h-12 rounded-full transition-all duration-300 ${
                isActive ? 'bg-white/15' : 'bg-transparent'
              }`}
            >
              <Text className={`text-base ${isActive ? 'text-white' : 'text-neutral-400'}`}>
                {tab.icon}
              </Text>
              <Text
                className={`text-[10px] font-semibold tracking-wider mt-0.5 ${
                  isActive ? 'text-white' : 'text-neutral-500'
                }`}
              >
                {tab.label}
              </Text>
            </TouchableOpacity>
          );
        })}
      </BlurView>
    </View>
  );
};
```

---

### 2. Flutter (Dart + `BackdropFilter` + `HapticFeedback`)

```dart
import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class FloatingHapticTabBar extends StatelessWidget {
  final int activeIndex;
  final Function(int) onTabSelected;

  const FloatingHapticTabBar({
    Key? key,
    required this.activeIndex,
    required this.onTabSelected,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final bottomInset = MediaQuery.of(context).padding.bottom;

    return Positioned(
      bottom: bottomInset > 0 ? bottomInset + 8 : 20,
      left: 24,
      right: 24,
      child: ClipRRect(
        borderRadius: BorderRadius.circular(36),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
          child: Container(
            height: 64,
            decoration: BoxDecoration(
              color: Colors.black.withOpacity(0.65),
              borderRadius: BorderRadius.circular(36),
              border: Border.all(color: Colors.white.withOpacity(0.12)),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _buildTab(0, Icons.home_rounded, "Trang chủ"),
                _buildTab(1, Icons.explore_rounded, "Khám phá"),
                _buildTab(2, Icons.shopping_bag_rounded, "Giỏ hàng"),
                _buildTab(3, Icons.person_rounded, "Tài khoản"),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildTab(int index, IconData icon, String label) {
    final isActive = activeIndex == index;
    return GestureDetector(
      onTap: () {
        HapticFeedback.lightImpact();
        onTabSelected(index);
      },
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
        decoration: BoxDecoration(
          color: isActive ? Colors.white.withOpacity(0.15) : Colors.transparent,
          borderRadius: BorderRadius.circular(20),
        ),
        child: Icon(icon, color: isActive ? Colors.white : Colors.grey),
      ),
    );
  }
}
```

---

### 3. Kotlin + Jetpack Compose (`NavigationBar` + Blur)

```kotlin
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.unit.dp

@Composable
fun FloatingHapticTabBar(
    selectedIndex: Int,
    onTabSelected: (Int) -> Unit
) {
    val haptic = LocalHapticFeedback.current

    Box(
        modifier = Modifier
            .fillMaxWidth()
            .navigationBarsPadding()
            .padding(horizontal = 24.dp, vertical = 12.dp),
        contentAlignment = Alignment.Center
    ) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .height(64.dp)
                .clip(CircleShape)
                .background(Color(0xE6171717))
                .border(1.dp, Color(0x33FFFFFF), CircleShape)
                .padding(horizontal = 8.dp),
            horizontalArrangement = Arrangement.SpaceAround,
            verticalAlignment = Alignment.CenterVertically
        ) {
            listOf("Home", "Explore", "Cart", "Profile").forEachIndexed { index, title ->
                val isSelected = selectedIndex == index
                Box(
                    modifier = Modifier
                        .clip(CircleShape)
                        .background(if (isSelected) Color(0x33FFFFFF) else Color.Transparent)
                        .clickable {
                            haptic.performHapticFeedback(HapticFeedbackType.TextHandleMove)
                            onTabSelected(index)
                        }
                        .padding(horizontal = 16.dp, vertical = 8.dp)
                ) {
                    Text(text = title, color = if (isSelected) Color.White else Color.Gray)
                }
            }
        }
    }
}
```
