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

3. **Asset Preparation (auto, if UI design exists).**
   If `plan.md` contains a `## Design Template` section:

   a. **Auto-invoke `sdd-asset-generator`**: Read the `Required Assets` list from
      the Design Template section. Generate all images using the `generate_image`
      tool, following the template's color palette and style specifications.
      Output to `public/assets/generated/`.

   b. **Auto-invoke `sdd-bg-remover`** (conditional): Check if the chosen template
      has `requires_transparent_images: true` in its frontmatter. If yes:
      - Read each asset's description from the `sdd-asset-generator` inventory to
        choose the starting `--tier` (see `sdd-bg-remover` SKILL.md step 3 for
        the tier selection table: `standard` for smooth/simple edges, `high` for
        multi-object scenes, `fine-detail` for spiky/furry/lacy subjects). Default
        to `standard` if unsure — auto-escalation will handle the rest.
      - Run `remove_bg.py` using `--files` to target **only** those listed as
        `Needs BG Removal? = Yes` in the asset inventory — do not process hero
        banners, icons, scene photos, or background textures.
      - Handle exit codes:
        - `0` → all clean, proceed to next step.
        - `2` → some files flagged "NEEDS REVIEW" after max escalation — log them,
          surface to user, but continue the build (note files may need manual
          touch-up later).
        - `1` → hard failure — surface error to user, ask how to proceed.
      - Output to `public/assets/no-bg/`.

   c. **Copy ReactBits components**: If the template lists ReactBits components:
      - Visit each component's URL on `reactbits.dev`.
      - Copy the component source code (TypeScript + Tailwind CSS version).
      - Save to `src/components/reactbits/` (or similar).
      - Install any peer dependencies required.
      - Configure the component with the template's color palette.

   c2. **Auto-invoke `sdd-video-generator`** (conditional): Check if `plan.md`
       contains a video asset requirement — either from the template's
       `Required Assets` listing `.mp4` files, or from a selected module like
       `scroll-scrubbing-video` that needs a source video. If yes:
       - Read the asset description to compose the Veo prompt (following
         `sdd-video-generator` SKILL.md step 3 prompt framework, using
         `brainstorm.md` + `constitution.md` for tone/palette context).
       - Choose `--tier` based on importance: `fast` for most cases,
         `standard` for hero/key cinematic video.
       - If the module `scroll-scrubbing-video` was selected with canvas
         frame-sequence approach (Cách B), also run `extract_frames.py`
         after the video is generated to produce WebP frame sequence.
       - Output to `public/assets/video/`.

   d. Only after all assets (images, backgrounds, **videos**) and components
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
