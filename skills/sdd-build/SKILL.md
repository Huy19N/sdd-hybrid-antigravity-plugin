---
name: sdd-build
description: Use when the user has approved docs/sdd/<feature>/plan.md and says to start building or implementing. Executes the plan task-by-task under strict TDD, checks every task against docs/sdd/constitution.md, and updates plan.md as tasks complete. This is step 4 of 6 in the SDD-Hybrid workflow. Do not use to start work with no approved plan.md — redirect to sdd-plan first.
---

# SDD Build (step 4 of 6)

## Purpose
Execute an approved plan with discipline: real TDD, one task at a time, and the
constitution treated as a live gate, not just a document to skim.

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
3. **For every task, in order:**
   a. Write the failing test first (RED). Run it — confirm it fails for the
      expected reason, not by accident.
   b. Write the minimal code to make it pass (GREEN). Run it — confirm it passes.
   c. Refactor if needed, re-run tests.
   d. **Constitution check**: does this task's implementation violate any principle
      in `constitution.md`? If yes, stop — do not route around it silently. Surface
      it to the user, citing the specific principle.
   e. Mark the task `[x]` in `plan.md` and commit, referencing the task in the
      commit message.
4. If a task turns out to need something the plan didn't anticipate, stop and
   re-plan that task with the user rather than improvising silently.
5. Prefer dispatching each task to a fresh subagent with a two-stage review (spec
   compliance, then code quality) when the harness supports it — this keeps the
   coordinating context clean. (If the superpowers `subagent-driven-development`
   skill is installed, use it here.) Fall back to direct execution with checkpoints
   for small plans or harnesses without subagent support.

## Non-negotiables
- No task's implementation code is written before its test.
- No task is marked done without actually running its verification step.
- No constitution violation is "fixed later" — it blocks that task, full stop.

## Handoff
When all tasks in `plan.md` are checked off and tests are green, say:

> "Tất cả task đã build xong và pass test. Bước tiếp theo là **sdd-review-code**
> trước khi merge/finish."
