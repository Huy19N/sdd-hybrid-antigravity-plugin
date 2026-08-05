---
name: sdd-build
description: Use when the user has approved docs/sdd/<feature>/plan.md and says to start building or implementing. Executes the plan task-by-task under strict TDD, checks every task against docs/sdd/constitution.md and business rules from docs/sdd/BRD.md (if exists), tracks functional requirement completion from docs/sdd/PRD.md (if exists), auto-generates visual assets if a design template was selected, and updates plan.md as tasks complete. This is step 4 of 6 in the SDD-Hybrid workflow. Do not use to start work with no approved plan.md — redirect to sdd-plan first.
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
   - Also read `docs/sdd/BRD.md` (Section 5: Business Rules) and
     `docs/sdd/PRD.md` (Section 2: Functional Requirements) **if they exist**.
     These enable business rule compliance checking and requirement tracking
     during the build. If they don't exist, skip these checks — the build
     works fine without them.

3. **Asset Preparation (auto, if UI design exists).**
   If `plan.md` contains a `## Design Template` section:

   a. **Auto-invoke `sdd-asset-generator`**: Read the `Required Assets` list from
      the Design Template section. Generate all images using the `generate_image`
      tool, following the template's color palette and style specifications.
      Output to `public/assets/generated/`.

   b. **Auto-invoke `sdd-bg-remover`** (conditional): Check if the chosen template
      has `requires_transparent_images: true` in its frontmatter. If yes, run the
      background removal script on all product/item images that need it.
      Output to `public/assets/no-bg/`.

   c. **Copy ReactBits components**: If the template lists ReactBits components:
      - Visit each component's URL on `reactbits.dev`.
      - Copy the component source code (TypeScript + Tailwind CSS version).
      - Save to `src/components/reactbits/` (or similar).
      - Install any peer dependencies required.
      - Configure the component with the template's color palette.

   d. Only after all assets and components are ready, proceed to build tasks.

4. **For every task, in order:**
   a. Write the failing test first (RED). Run it — confirm it fails for the
      expected reason, not by accident.
   b. Write the minimal code to make it pass (GREEN). Run it — confirm it passes.
   c. Refactor if needed, re-run tests.
   d. **Constitution check**: does this task's implementation violate any principle
      in `constitution.md`? If yes, stop — do not route around it silently. Surface
      it to the user, citing the specific principle.
   e. **Business Rule compliance check** (only when BRD.md exists): does this
      task's code violate any BR-xxx from BRD Section 5? Check the specific
      business rules mapped to this task (from the Requirement Traceability
      section). If violated, stop — treat it the same as a constitution
      violation. Report:
      > "⚠️ Task N vi phạm **BR-xxx**: [rule description]. Code hiện tại
      > [specific violation]. Cần fix trước khi tiếp tục."
   f. Mark the task `[x]` in `plan.md` and commit, referencing the task in the
      commit message.
   g. **Update Requirement Traceability** (only when plan.md has the section):
      update the status of FR-xxx/BR-xxx IDs mapped to this task from
      `⬜ Pending` to `✅ Done`.
   h. **Show progress** after each task:
      ```
      📊 Progress: Task N/M done
         FR Coverage: X/Y (Z%) — ✅ FR-001, FR-002 | ⬜ FR-003, FR-004
         BR Compliance: X/Y checked, 0 violations
      ```
      Skip this output if BRD/PRD don't exist.
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
- No business rule violation is "fixed later" — it blocks that task, same as constitution.
- Asset generation and ReactBits setup must complete before UI build tasks begin.
- If Requirement Traceability section exists in plan.md, FR/BR status must be
  updated after every task completion — don't leave it stale.

## Handoff
When all tasks in `plan.md` are checked off and tests are green, say:

> "Tất cả task đã build xong và pass test. Bước tiếp theo là **sdd-review-code**
> trước khi merge/finish."
