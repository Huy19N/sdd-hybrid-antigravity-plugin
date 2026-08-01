---
name: sdd-plan
description: Use when both docs/sdd/constitution.md and a feature's docs/sdd/<feature>/brainstorm.md exist and are approved, and the user is ready to move from idea to an executable engineering plan. Produces plan.md with a short spec, an explicit constitution-compliance check, and a bite-sized task breakdown. This is step 3 of 6 in the SDD-Hybrid workflow. Do not use before brainstorm and constitution exist — redirect to those first.
---

# SDD Plan (step 3 of 6)

## Purpose
Turn an approved brainstorm into a plan detailed enough that a capable-but-context-free
engineer (or subagent) could execute each task without guessing. Folds spec-kit's
`/specify` + `/plan` + `/tasks` into a single pass, but uses superpowers-style
bite-sized tasks (2-5 min each, exact files, explicit verification) instead of loose
task lists.

## Preconditions — check before starting
- `docs/sdd/constitution.md` exists. If not, stop and point the user to
  `sdd-constitution`.
- `docs/sdd/<feature-slug>/brainstorm.md` exists and was confirmed by the user. If
  not, point the user to `sdd-brainstorm`.

## Process
1. **Read both files in full**: `constitution.md` and the feature's `brainstorm.md`.
2. **Clarify before planning.** If brainstorm.md has open questions, or there's
   ambiguity that would force you to guess at implementation, ask the user now —
   numbered, specific questions. Never silently assume.
3. **Draft a short spec section** (what/why, not how): one short paragraph plus a
   bullet list of functional requirements and acceptance criteria. Keep it
   high-level; implementation detail belongs in the task breakdown.
4. **Constitution compliance check** — walk every principle in constitution.md and
   mark: complies / needs a documented exception (with justification) / not
   applicable. A plan with an unresolved conflict is not done.
5. **Technical approach** — architecture and tech choices for this feature,
   consistent with the constitution's technology constraints.
6. **Task breakdown** — split the approach into tasks that each:
   - Take about 2-5 minutes of focused work.
   - Name the exact file path(s) touched.
   - State the test that proves the task is done (TDD-first: the test-writing task
     comes before the implementation task).
   - Leave the codebase in a working, testable state when done.
7. Present the draft **in sections** (spec -> compliance check -> tasks) for the
   user to validate — don't dump the whole thing and assume approval.

## Output
Write to: `docs/sdd/<feature-slug>/plan.md`

```markdown
# Plan: <Feature Name>

Source: brainstorm.md (v?), constitution.md (v?)

## Spec summary
### Functional requirements
### Acceptance criteria

## Constitution compliance check
| Principle | Status | Notes |
|---|---|---|

## Technical approach

## Tasks
- [ ] Task 1 — <file path(s)> — <test that proves this is done> — <exact steps>
- [ ] Task 2 — ...
```

## Handoff
When the user approves the plan, say:

> "Plan đã được duyệt. Bước tiếp theo là **sdd-build** để bắt đầu thực thi."
