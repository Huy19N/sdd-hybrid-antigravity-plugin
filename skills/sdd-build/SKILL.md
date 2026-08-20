---
name: sdd-build
description: Use when the user has approved docs/sdd/<feature>/plan.md and says to start building or implementing. Executes the plan task-by-task under strict TDD, checks every task against docs/sdd/constitution.md, auto-generates visual assets if a design template was selected, and updates plan.md as tasks complete. This is step 4 of 6 in the SDD-Hybrid workflow. Do not use to start work with no approved plan.md — redirect to sdd-plan first.
---

# SDD Build (step 4 of 6)

## Purpose
Execute an approved plan with discipline: real TDD, one task at a time, and the
constitution treated as a live gate, not just a document to skim. When the plan
includes a Design Template, automatically prepare all visual assets and ReactBits
components before building UI code.

## Preconditions
- `docs/sdd/<feature-slug>/plan.md` exists and its tasks were approved.
- `docs/sdd/constitution.md` exists.

If either is missing, stop and point the user to `sdd-plan` / `sdd-constitution`.

## Process
1. **Isolate the work.** If not already on a dedicated branch/worktree for this
   feature, create one and confirm the test baseline is currently green before
   touching anything. (If the superpowers `using-git-worktrees` skill is installed,
   use it here.)
2. Read `plan.md` and `constitution.md` fully before starting task 1.

3. **Asset Preparation (auto, if UI design or Game assets exist).**

   **Trường hợp A: Dự án Web / Mobile UI (`plan.md` có `## Design Template`)**:
   a. **Auto-invoke `sdd-asset-generator` (Web mode)**: Read the `Required Assets` list from
      the Design Template section. Generate all images using the `generate_image`
      tool (Antigravity IDE native quota). If quota is exhausted (429), automatically
      run `python skills/sdd-asset-generator/scripts/generate_image_fallback.py` to seamlessly fallback.
      Output to `public/assets/generated/`.

   b. **Auto-invoke `sdd-bg-remover` Mode 1** (`remove_bg.py`, conditional): Check if the chosen template
      has `requires_transparent_images: true` in its frontmatter. If yes:
      - Read each asset's description from the `sdd-asset-generator` inventory to
        choose the starting `--tier` (`standard`, `high`, `fine-detail`).
      - Run `remove_bg.py` on items marked `Needs BG Removal? = Yes`.
      - Output to `public/assets/no-bg/`.

   c. **Copy ReactBits / Mobile components**: If the template lists ReactBits or Mobile shared modules,
      copy and configure component source code into project design system.

   c2. **Auto-invoke `sdd-video-generator`** (conditional): Check if `plan.md`
       contains a video asset requirement. If yes, generate video via Veo 3.1
       and output to `public/assets/video/`.

   **Trường hợp B: Dự án Game 2D / 2.5D (`plan.md` có `## Game Asset Requirements`)**:
   a. **Auto-invoke `sdd-asset-generator` (Game mode)**: Read the Game Asset manifest
      (Parallax Composite Scenes, Character Sprites, Tileable Textures). Generate all assets
      with clean silhouettes, character consistency sheets, and depth cues.
      Output to `public/assets/generated/`.

   b. **Auto-invoke `sdd-bg-remover` Mode 2** (`segment_layers.py`, cho Parallax Composite Scenes):
      - For each asset with type `parallax-composite`:
        - Extract its `Decomposition Labels` from the manifest.
        - Run:
          ```bash
          python skills/sdd-bg-remover/scripts/segment_layers.py \
            --input public/assets/generated/<scene-file>.webp \
            --output public/assets/game-layers/<scene-name>/ \
            --labels <labels from manifest>
          ```
        - Verifies that layer area percentages are valid and transparent PNG layers are created.

   c. **Auto-run `make_tileable.py`** (cho Tileable Textures):
      - For each asset with type `tileable-texture`:
        - Run:
          ```bash
          python skills/sdd-asset-generator/scripts/make_tileable.py \
            --input public/assets/generated/<texture-file>-raw.webp \
            --output public/assets/game-textures/<texture-file>.png \
            --blend-width 48
          ```

   d. **Auto-invoke `sdd-bg-remover` Mode 1** (`remove_bg.py`, cho Character Sprites):
      - Run `remove_bg.py` on any character sprites needing isolated transparent backgrounds.
      - Output to `public/assets/game-sprites/`.

   e. Only after all assets (UI/Game images, layers, textures, **videos**) and components
      are ready, proceed to build tasks.

4. **For every task, in order:**
   a. Write the failing test first (RED). Run it — confirm it fails for the
      expected reason, not by accident.
   b. Write the minimal code to make it pass (GREEN). Run it — confirm it passes.
   c. Refactor if needed, re-run tests.
   d. **Constitution check**: does this task's implementation violate any principle
      in `constitution.md`? If yes, stop — do not route around it silently. Surface
      it to the user, citing the specific principle.
   e. Mark the task `[x]` in `plan.md` and commit, referencing the task in the
      commit message.
5. If a task turns out to need something the plan didn't anticipate, stop and
   re-plan that task with the user rather than improvising silently.
6. Prefer dispatching each task to a fresh subagent with a two-stage review (spec
   compliance, then code quality) when the harness supports it — this keeps the
   coordinating context clean. (If the superpowers `subagent-driven-development`
   skill is installed, use it here.) Fall back to direct execution with checkpoints
   for small plans or harnesses without subagent support.

## Non-negotiables
- No task's implementation code is written before its test.
- No task is marked done without actually running its verification step.
- No constitution violation is "fixed later" — it blocks that task, full stop.
- Asset generation and ReactBits setup must complete before UI build tasks begin.

## Handoff
When all tasks in `plan.md` are checked off and tests are green, say:

> "Tất cả task đã build xong và pass test. Bước tiếp theo là **sdd-review-code**
> trước khi merge/finish."
