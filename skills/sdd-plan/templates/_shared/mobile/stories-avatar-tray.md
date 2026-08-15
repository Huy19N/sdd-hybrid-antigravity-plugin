---
id: stories-avatar-tray
name: "Stories Avatar Tray & Fullscreen Viewer"
type: shared-module
module_category: mobile
platform: mobile-first
tags:
  - stories-tray
  - avatar-carousel
  - fullscreen-stories
  - 9-16-story
  - social-commerce
  - mobile-feed
compatible_with: all
pairs_well_with:
  - haptic-tab-bar
  - swipeable-card-stack
  - mobile-bottom-sheet
best_for: "Cửa hàng thời trang, quán cafe/nhà hàng, thương hiệu phong cách sống, app tin tức/sự kiện — hiển thị tin tức nổi bật, hậu trường làm bánh/sản phẩm hoặc ưu đãi flash sale dạng Story toàn màn hình 9:16."
requires_asset: "Bộ ảnh Story tỷ lệ dọc 9:16 từ sdd-asset-generator (Trend B: Organic Wabi-Sabi hoặc Trend C: High-Fashion) và ảnh avatar tròn 1:1."
---

# Shared Module: Stories Avatar Tray & Fullscreen Viewer

## Preview Description
Dải khay câu chuyện (**Stories Avatar Tray**) nằm ngang ở đầu màn hình app: Mỗi avatar được bao bọc bởi một vòng tròn gradient xoay nhẹ khi có story chưa xem. Khi người dùng chạm vào một avatar, ứng dụng sẽ mở một **Trình xem Story toàn màn hình (9:16 Fullscreen Story Viewer)** với thanh tiến trình tự động chạy (*progress bar segment*), hỗ trợ chạm bên trái (Story trước) / chạm bên phải (Story kế tiếp) / nhấn giữ để tạm dừng (*press & hold to pause*).

---

## Kỹ thuật triển khai Đa Nền Tảng

### 1. React Native / Expo (TypeScript + NativeWind + Modal)

```tsx
import React, { useState } from 'react';
import { View, Text, ScrollView, TouchableOpacity, Image, Modal, Dimensions } from 'react-native';
import * as Haptics from 'expo-haptics';

interface StoryItem {
  id: string;
  userName: string;
  avatarUrl: string;
  storyImage: string;
  hasUnseen: boolean;
}

export const StoriesAvatarTray: React.FC<{ stories: StoryItem[] }> = ({ stories }) => {
  const [selectedStory, setSelectedStory] = useState<StoryItem | null>(null);

  const openStory = (story: StoryItem) => {
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
    setSelectedStory(story);
  };

  return (
    <View className="py-3">
      <ScrollView horizontal showsHorizontalScrollIndicator={false} className="px-4">
        {stories.map((story) => (
          <TouchableOpacity
            key={story.id}
            onPress={() => openStory(story)}
            className="items-center mr-4"
          >
            <View
              className={`p-0.5 rounded-full ${
                story.hasUnseen
                  ? 'bg-gradient-to-tr from-amber-500 via-rose-500 to-violet-600'
                  : 'bg-neutral-700'
              }`}
            >
              <View className="p-0.5 bg-black rounded-full">
                <Image
                  source={{ uri: story.avatarUrl }}
                  className="w-16 h-16 rounded-full object-cover"
                />
              </View>
            </View>
            <Text className="text-xs text-neutral-300 mt-1 max-w-[68px] text-center" numberOfLines={1}>
              {story.userName}
            </Text>
          </TouchableOpacity>
        ))}
      </ScrollView>

      {/* Fullscreen Story Modal 9:16 */}
      <Modal visible={!!selectedStory} animationType="fade" transparent>
        <View className="flex-1 bg-black justify-center items-center">
          {selectedStory && (
            <View className="w-full h-full relative">
              <Image source={{ uri: selectedStory.storyImage }} className="w-full h-full object-cover" />
              {/* Top Progress Bars */}
              <View className="absolute top-12 left-4 right-4 flex-row gap-1">
                <View className="flex-1 h-1 bg-white/40 rounded-full overflow-hidden">
                  <View className="w-full h-full bg-white animate-pulse" />
                </View>
              </View>
              {/* Close Button */}
              <TouchableOpacity
                onPress={() => setSelectedStory(null)}
                className="absolute top-16 right-6 w-9 h-9 rounded-full bg-black/50 items-center justify-center"
              >
                <Text className="text-white font-bold">✕</Text>
              </TouchableOpacity>
            </View>
          )}
        </View>
      </Modal>
    </View>
  );
};
```

---

### 2. Flutter (Dart + Horizontal ListView & PageView)

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class StoriesAvatarTray extends StatelessWidget {
  final List<Map<String, String>> stories;
  const StoriesAvatarTray({Key? key, required this.stories}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 100,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        padding: const EdgeInsets.symmetric(horizontal: 16),
        itemCount: stories.length,
        itemBuilder: (context, index) {
          final story = stories[index];
          return GestureDetector(
            onTap: () {
              HapticFeedback.lightImpact();
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => FullscreenStoryViewer(story: story),
                ),
              );
            },
            child: Container(
              margin: const EdgeInsets.only(right: 14),
              child: Column(
                children: [
                  Container(
                    padding: const EdgeInsets.all(2.5),
                    decoration: const BoxDecoration(
                      shape: BoxShape.circle,
                      gradient: LinearGradient(
                        colors: [Colors.amber, Colors.purpleAccent],
                      ),
                    ),
                    child: CircleAvatar(
                      radius: 30,
                      backgroundImage: NetworkImage(story['avatarUrl']!),
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    story['userName'] ?? '',
                    style: const TextStyle(color: Colors.white70, fontSize: 11),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}

class FullscreenStoryViewer extends StatelessWidget {
  final Map<String, String> story;
  const FullscreenStoryViewer({Key? key, required this.story}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Stack(
        children: [
          Positioned.fill(
            child: Image.network(story['storyImage']!, fit: BoxFit.cover),
          ),
          Positioned(
            top: 50,
            right: 20,
            child: IconButton(
              icon: const Icon(Icons.close, color: Colors.white, size: 28),
              onPressed: () => Navigator.pop(context),
            ),
          ),
        ],
      ),
    );
  }
}
```
