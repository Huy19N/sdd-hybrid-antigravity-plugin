# SDD-Hybrid workflow

This project uses the **sdd-hybrid** plugin. Any time you are about to start a new
feature, write a plan, write code, or finish a change, check whether one of the
skills below applies before doing anything else — including before asking
clarifying questions or exploring the codebase. If there is even a small chance a
step applies, use it. This is not optional.

## The six steps, in order

1. **sdd-brainstorm** — turn a rough idea into `docs/sdd/<feature-slug>/brainstorm.md`.
2. **sdd-constitution** — project-wide binding rules in `docs/sdd/constitution.md`
   (created once, amended over time — not per feature).
3. **sdd-plan** — turn an approved brainstorm into `docs/sdd/<feature-slug>/plan.md`
   (spec + constitution compliance check + bite-sized tasks).
4. **sdd-build** — execute the plan task-by-task under TDD, gated by the constitution.
5. **sdd-review-code** — full correctness/logic review after all tasks are done.
6. **sdd-security-review** — OWASP Top 10:2025 gate. **Nothing gets pushed, PR'd,
   or sent to CI/CD before this step returns a "Cleared" verdict.**

## Hard rules

- Never skip straight to writing code for a new feature without brainstorm + plan.
- Never treat `constitution.md` as optional reading — `sdd-build` must stop on any
  violation instead of routing around it.
- Never let `sdd-review-code` offer to merge/PR/push directly — that decision only
  happens after `sdd-security-review` clears the branch.
- `constitution.md` is project-wide (one file, amended over time). `brainstorm.md`,
  `plan.md`, `review-report.md`, and `security-report.md` are per-feature, under
  `docs/sdd/<feature-slug>/`.

## Small tasks and bug fixes

For a small, already fully-specified task, or for a bug fix, the full six-step
flow is overkill — use judgment. Bug fixes should still go through systematic
debugging if that skill is available, and any code change should still pass
`sdd-review-code` and `sdd-security-review` before it's pushed.
