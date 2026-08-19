---
name: sdd-brainstorm
description: Use when the user proposes a new feature, product, or project idea and no docs/sdd/<feature>/brainstorm.md exists yet for it. Refines a rough idea into a validated problem statement and approach through Socratic questioning, enhanced by automatic deep research (market, competitors, UX trends). This is step 1 of 6 in the SDD-Hybrid workflow (Brainstorm -> Constitution -> Plan -> Build -> Review -> Security). Do not use for bug fixes (use systematic-debugging) or for small, already fully-specified tasks.
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
1. **Deep Research (auto).** Before asking the user anything, automatically invoke
   the `sdd-deep-research` sub-skill:
   - Read the user's initial idea description.
   - Run structured research: market analysis, competitor landscape, UX/design
     trends in the domain, and technical feasibility notes.
   - The research output informs your Socratic questions — making them sharper
     and more relevant than generic brainstorming prompts.
   - The research findings will be included in the final brainstorm.md as a
     dedicated `## Research Findings` section.
2. **Do not propose solutions yet.** Using insights from the research, ask about
   one topic at a time (don't dump all questions at once):
   - **Domain & Platform**: Web App, Mobile App (iOS/Android), or 2D/2.5D Game (WebGL/Canvas, Phaser, PixiJS, Godot/Unity assets)?
   - What problem/pain does this solve, and for whom?
   - What does success look like? How will we know it worked?
   - What's explicitly OUT of scope for this iteration?
   - What constraints already exist (deadline, existing systems, target FPS/devices, data, users)?
   - If this is a **Game Project**:
     - Gameplay mechanics & camera perspective (side-scroller, isometric, top-down, fixed scene).
     - Art style archetype (pixel art, flat vector, painterly with silhouettes).
     - Environmental depth (parallax composite layers, tileable ground/walls, character animation states).
   - What alternatives or prior art did the user already consider or reject, and why?
   - (Reference specific competitors or trends from the research to prompt deeper
     thinking, e.g., "Competitor X does this differently — is that relevant?")
3. Once the shape is clear, draft 2-3 candidate approaches at a high level (not
   implementation detail) and lay out trade-offs.
4. Present the draft **in short sections**, not one giant wall of text. Get explicit
   sign-off section by section — don't assume silence means agreement.
5. Iterate until the user confirms the document is accurate.

## Output
Write to: `docs/sdd/<feature-slug>/brainstorm.md`

```markdown
# Brainstorm: <Feature Name>

## Problem
## Goals
## Non-goals (explicitly out of scope)
## Users / context
## Constraints

## Research Findings
### Market Overview
### Competitor Landscape
| Competitor | Value Prop | Strengths | Gaps | Pricing |
|---|---|---|---|---|
### UX/Design Trends in [Industry]
### Technical Notes

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
