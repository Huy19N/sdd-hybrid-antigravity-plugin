---
id: mobile-bottom-sheet
name: "Mobile Interactive Bottom Sheet"
type: shared-module
module_category: mobile
platform: mobile-first
tags:
  - bottom-sheet
  - modal
  - gestures
  - snap-points
  - mobile-navigation
  - touch-ui
compatible_with: all
pairs_well_with:
  - haptic-tab-bar
  - ambient-glow-cursor
  - glassmorphism
best_for: "Menu bộ lọc sản phẩm, bảng chọn thuộc tính mua hàng (Size/Color picker), chi tiết checkout, giỏ hàng mini, trình điều khiển audio/video — chuẩn giao diện native iOS & Android vuốt trượt từ đáy màn hình."
requires_asset: "Ảnh thumbnail sản phẩm hoặc icon chức năng tỉ lệ vuông 1:1 từ sdd-asset-generator để hiển thị trong header của Bottom Sheet."
---

# Shared Module: Mobile Interactive Bottom Sheet

## Preview Description
Modal tương tác kéo vuốt từ đáy màn hình (**Interactive Bottom Sheet**) với hiệu ứng mờ nền (*backdrop blur*), các điểm dừng linh hoạt (*snap points: 25%, 50%, 90%*), thanh gạt kéo (*drag handle*), và phản hồi rung xúc giác khi snap vào vị trí. Hỗ trợ đầy đủ Safe Area đáy (Home Indicator trên iOS và thanh điều hướng Android).

---

## Kỹ thuật triển khai Đa Nền Tảng

### 1. React Native / Expo (TypeScript + NativeWind + `@gorhom/bottom-sheet`)

```tsx
import React, { useCallback, useMemo, useRef } from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import BottomSheet, { BottomSheetBackdrop, BottomSheetView } from '@gorhom/bottom-sheet';
import * as Haptics from 'expo-haptics';

interface MobileBottomSheetProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
}

export const MobileBottomSheet: React.FC<MobileBottomSheetProps> = ({
  isOpen,
  onClose,
  title,
  children,
}) => {
  const bottomSheetRef = useRef<BottomSheet>(null);
  const snapPoints = useMemo(() => ['30%', '60%', '90%'], []);

  const handleSheetChanges = useCallback((index: number) => {
    if (index === -1) {
      onClose();
    } else {
      Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
    }
  }, [onClose]);

  const renderBackdrop = useCallback(
    (props: any) => (
      <BottomSheetBackdrop
        {...props}
        disappearsOnIndex={-1}
        appearsOnIndex={0}
        opacity={0.6}
      />
    ),
    []
  );

  if (!isOpen) return null;

  return (
    <BottomSheet
      ref={bottomSheetRef}
      index={1}
      snapPoints={snapPoints}
      onChange={handleSheetChanges}
      enablePanDownToClose
      backdropComponent={renderBackdrop}
      backgroundStyle={{ backgroundColor: '#171717', borderRadius: 28 }}
      handleIndicatorStyle={{ backgroundColor: '#525252', width: 40, height: 4 }}
    >
      <BottomSheetView className="flex-1 px-6 pb-8">
        <View className="flex-row items-center justify-between pb-4 border-b border-neutral-800">
          <Text className="text-lg font-bold text-white tracking-wide">{title}</Text>
          <TouchableOpacity
            onPress={() => bottomSheetRef.current?.close()}
            className="w-8 h-8 rounded-full bg-neutral-800 items-center justify-center"
          >
            <Text className="text-neutral-400 font-bold">✕</Text>
          </TouchableOpacity>
        </View>
        <View className="pt-4 flex-1">{children}</View>
      </BottomSheetView>
    </BottomSheet>
  );
};
```

---

### 2. Flutter (Dart + Material 3 ModalBottomSheet)

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class MobileBottomSheet {
  static Future<T?> show<T>({
    required BuildContext context,
    required String title,
    required Widget child,
  }) {
    HapticFeedback.mediumImpact();
    return showModalBottomSheet<T>(
      context: context,
      isScrollControlled: true,
      backgroundColor: const Color(0xFF171717),
      barrierColor: Colors.black.withOpacity(0.6),
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(28)),
      ),
      builder: (context) {
        return DraggableScrollableSheet(
          initialChildSize: 0.6,
          minChildSize: 0.3,
          maxChildSize: 0.92,
          expand: false,
          builder: (context, scrollController) {
            return Padding(
              padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
              child: Column(
                children: [
                  Container(
                    width: 40,
                    height: 4,
                    decoration: BoxDecoration(
                      color: Colors.grey[700],
                      borderRadius: BorderRadius.circular(2),
                    ),
                  ),
                  const SizedBox(height: 16),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        title,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      IconButton(
                        onPressed: () => Navigator.pop(context),
                        icon: const Icon(Icons.close, color: Colors.grey),
                      ),
                    ],
                  ),
                  const Divider(color: Color(0xFF262626)),
                  Expanded(
                    child: SingleChildScrollView(
                      controller: scrollController,
                      child: child,
                    ),
                  ),
                ],
              ),
            );
          },
        );
      },
    );
  }
}
```

---

### 3. Kotlin + Jetpack Compose (`ModalBottomSheet`)

```kotlin
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MobileBottomSheet(
    onDismissRequest: () -> Unit,
    title: String,
    sheetState: SheetState = rememberModalBottomSheetState(skipPartiallyExpanded = false),
    content: @Composable ColumnScope.() -> Unit
) {
    val haptics = LocalHapticFeedback.current

    ModalBottomSheet(
        onDismissRequest = {
            haptics.performHapticFeedback(HapticFeedbackType.LongPress)
            onDismissRequest()
        },
        sheetState = sheetState,
        containerColor = Color(0xFF171717),
        shape = RoundedCornerShape(topStart = 28.dp, topEnd = 28.dp),
        dragHandle = {
            Box(
                modifier = Modifier
                    .padding(vertical = 12.dp)
                    .width(40.dp)
                    .height(4.dp)
                    .background(Color(0xFF525252), RoundedCornerShape(2.dp))
            )
        }
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 24.dp, vertical = 8.dp)
                .navigationBarsPadding()
        ) {
            Text(
                text = title,
                style = MaterialTheme.typography.titleMedium,
                color = Color.White
            )
            Spacer(modifier = Modifier.height(16.dp))
            content()
        }
    }
}
```
