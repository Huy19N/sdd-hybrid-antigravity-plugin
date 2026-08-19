---
name: sdd-constitution
description: Use when a project has no docs/sdd/constitution.md yet, or when the user wants to add or change a project-wide non-negotiable rule (testing standards, tech-stack constraints, security requirements, architectural principles). This is step 2 of 6 in the SDD-Hybrid workflow. The constitution is PROJECT-WIDE and created ONCE, not per feature — do not confuse it with a per-feature brainstorm.md or plan.md. Unlike brainstorming, this produces binding rules that gate every later step, not design options. Its "Security requirements" section is also read directly by sdd-security-review (step 6).
---

# SDD Constitution (step 2 of 6)

## Purpose
Establish the **non-negotiable, project-wide rules** every future brainstorm, plan,
build, and review must respect. This file exists exactly once per project (not once
per feature) and is amended over time — never silently overwritten.

## Scope check (do this first)
- Does `docs/sdd/constitution.md` already exist?
  - **No** -> this is initial ratification. Run the full process below.
  - **Yes** -> this is an amendment. Read the existing file first, show a summary of
    the proposed changes, bump the version, and record what changed in a
    "Sync Impact Report" at the top of the file.

## Process
1. If this was triggered from a feature idea, read that feature's `brainstorm.md`
   for hints about tech constraints, quality bar, and users — but remember: the
   constitution applies to the whole project, not just this one feature.
2. Ask the user directly about anything not already answered:
   - Testing standards (coverage bar? TDD mandatory? no-mock policy?)
   - Tech stack constraints (approved/banned libraries, language/runtime versions)
   - Security & data-handling requirements
   - Architectural principles (simplicity bar, layering rules, forbidden patterns)
   - Code review / quality gates that must always apply
   - Hard performance or non-functional limits
3. Turn each answer into a **short, testable principle** — not vague aspiration.
   - Bad: "Code should be clean."
   - Good: "Every public function has a unit test; PRs without tests are rejected."
4. Number the principles. Each gets a one-line rationale.
5. Show the full draft to the user for explicit approval before saving — this file
   gates everything downstream, so don't guess and save silently.

## Output
Write to: `docs/sdd/constitution.md`

```markdown
# Project Constitution

Version: <semver> | Ratified: <date> | Last amended: <date>

## Sync Impact Report (only present on amendments)
- Changed: ...
- Added: ...
- Removed: ...

## Principles
### 1. <Principle name>
<statement> — Rationale: <why>

### 2. ...

## Technology constraints
- Platform Target: `<Web | Mobile (iOS & Android) | 2D/2.5D Game | Cross-Platform>`
- Core Framework / Engine: `<React (Vite) | React Native (Expo) | Flutter (Dart) | Kotlin (Jetpack Compose) | Canvas/WebGL (Phaser/PixiJS/ThreeJS)>`
- Styling / Art Direction: `<Tailwind CSS | NativeWind | Flutter ThemeData | Compose Material3 | Pixel-Art/Vector/Painterly Game Art>`

## Game Architecture & Asset Pipeline Standards (bắt buộc với dự án Game)
- **Target Framerate & Performance**: Đảm bảo 60fps ổn định (≤16.6ms render budget), tránh memory leaks khi load sprite sheets/textures.
- **Asset Pipeline Standards**:
  - Parallax layers: Tách riêng bằng `segment_layers.py` theo độ sâu Z-index, parallax factor từ 0.1x (trời/mây xa) đến 1.0x+ (tiền cảnh).
  - Character sprites: Đảm bảo character sheet nhất quán, transparent background.
  - Textures: Chạy `make_tileable.py` để xử lý mép lặp liền mạch (seamless tiling).
- **Audio & Input**: Quản lý State Controller tách biệt với Render Loop, xử lý touch/keyboard mapping chuẩn xác.

## Mobile Architecture & Store-Ready Standards (bắt buộc với dự án Mobile)
- **Clean Architecture Pattern**:
  - Expo / React Native: `src/app/` (Expo Router), `src/features/` (Domain modules), `src/components/` (UI & Modules), `src/services/` (Storage/API).
  - Flutter: `lib/features/` (Presentation/Domain/Data), `lib/core/` (Network/Storage), `lib/shared/` (Widgets).
  - Kotlin Compose: `presentation/` (MVI/MVVM), `domain/` (UseCases), `data/` (Repository/Room), `ui/theme/`.
- **Google Play & App Store Compliance Gates**:
  - Safe Area handling trên 100% màn hình (`SafeAreaView` / `Scaffold` / `safeDrawingPadding`).
  - Minimum touch target: tối thiểu 48x48dp (Android) / 44x44pt (iOS).
  - Quyền truy cập (*Permissions*): Giải thích lý do rõ ràng trước khi hiển thị dialog hệ thống.
  - An toàn dữ liệu: Token và khóa nhạy cảm bắt buộc lưu trong `SecureStore` / `FlutterSecureStorage` / `EncryptedSharedPreferences` (Keychain/Keystore).
  - Offline & Error State: Ứng dụng phải có màn hình chờ mạng và fallback êm ái khi mất kết nối.

## Security requirements
## Testing standards
## Quality gates (what blocks a merge)
## Governance
How this document itself gets amended (who approves, version-bump rules).
```

## How downstream skills MUST use this file
- `sdd-plan` must check the draft plan against every principle before finalizing,
  and must call out any conflict explicitly rather than silently ignoring it.
- `sdd-build` must treat a constitution violation the same as a failing test — stop
  and flag it, don't route around it.
- `sdd-review-code` must include a full constitution-compliance pass in its report.

If a case comes up that the constitution doesn't cover, don't guess silently —
surface it, and if it's a recurring class of case, suggest amending the constitution.
