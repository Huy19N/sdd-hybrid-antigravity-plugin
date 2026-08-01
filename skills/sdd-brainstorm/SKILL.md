---
name: sdd-brainstorm
description: Use when the user proposes a new feature, product, or project idea and no docs/sdd/<feature>/brainstorm.md exists yet for it. Refines a rough idea into a validated problem statement and approach through Socratic questioning, before any constitution, spec, or planning work begins. This is step 1 of 6 in the SDD-Hybrid workflow (Brainstorm -> Constitution -> Plan -> Build -> Review -> Security). Do not use for bug fixes (use systematic-debugging) or for small, already fully-specified tasks.
---

# SDD Brainstorm (step 1 of 6)

## Purpose
Turn a rough idea into a written, human-validated understanding of *what* problem is
being solved and *why* — before anything gets constrained (constitution) or planned
(plan.md). Nothing gets built from this step; it only produces a document.

## When NOT to use
- Bug fixes -> use `systematic-debugging` (superpowers).
- The user already gave a fully-specified, unambiguous small task.
- A `brainstorm.md` for this exact feature already exists -> read and amend it,
  don't start from scratch.

## Process
1. **Do not propose solutions yet.** Ask about, one topic at a time (don't dump all
   questions at once):
   - What problem/pain does this solve, and for whom?
   - What does success look like? How will we know it worked?
   - What's explicitly OUT of scope for this iteration?
   - What constraints already exist (deadline, existing systems, data, users)?
   - What alternatives or prior art did the user already consider or reject, and why?
2. Once the shape is clear, draft 2-3 candidate approaches at a high level (not
   implementation detail) and lay out trade-offs.
3. Present the draft **in short sections**, not one giant wall of text. Get explicit
   sign-off section by section — don't assume silence means agreement.
4. Iterate until the user confirms the document is accurate.

## Output
Write to: `docs/sdd/<feature-slug>/brainstorm.md`

```markdown
# Brainstorm: <Feature Name>

## Problem
## Goals
## Non-goals (explicitly out of scope)
## Users / context
## Constraints
## Approaches considered
| Approach | Pros | Cons | Chosen? |
|---|---|---|---|

## Decision & rationale
## Open questions (unresolved, carried into planning)
```

## Handoff
Once the user confirms this document, say explicitly:

> "Brainstorm xong. Nếu dự án chưa có `docs/sdd/constitution.md`, bước tiếp theo là
> **sdd-constitution**. Nếu đã có rồi, có thể chạy thẳng **sdd-plan**."

Do not auto-proceed to constitution or plan — wait for the user to say go.
