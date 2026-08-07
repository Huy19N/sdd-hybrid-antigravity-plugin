---
name: sdd-plan
description: Use when both docs/sdd/constitution.md and a feature's docs/sdd/<feature>/brainstorm.md exist and are approved, and the user is ready to move from idea to an executable engineering plan. Produces plan.md with a short spec, constitution-compliance check, UI/UX design template selection (if applicable), and a bite-sized task breakdown. This is step 3 of 6 in the SDD-Hybrid workflow. Do not use before brainstorm and constitution exist — redirect to those first.
---

# SDD Plan (step 3 of 6)

## Purpose
Turn an approved brainstorm into a plan detailed enough that a capable-but-context-free
engineer (or subagent) could execute each task without guessing. Includes design
template selection for UI-focused projects. Folds spec-kit's `/specify` + `/plan` +
`/tasks` into a single pass, but uses superpowers-style bite-sized tasks (2-5 min each,
exact files, explicit verification) instead of loose task lists.

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

3. **Design Template Selection** (only when the project has UI components):
   a. Read `skills/sdd-plan/templates/template-index.md` to get an overview of all
      22 available design templates.
   b. Analyze `brainstorm.md` to extract: project type, industry/domain, target
      audience, mood/tone, and any visual preferences mentioned.
   c. **Scoring**: Match keywords from the brainstorm against each template's
      `category`, `tags`, and `best_for` fields. Score: +3 for category match,
      +2 for each tag match, +1 for partial `best_for` keyword overlap.
   d. Select the **top 2-3 templates** with highest scores and present them to
      the user:
      - Template name + preview description (1-2 sentences)
      - Why it matches (which keywords/themes aligned)
      - Color palette preview (hex codes)
      - ReactBits components it uses
   e. **Wait for user to choose 1 template** before proceeding.
   f. Once chosen, read the full template file from `templates/<file>.md` and
      incorporate the design specification into the plan.
   f2. If the chosen template has a `uses_shared_interactions` field in its
       frontmatter, also read each referenced file from
       `templates/_shared/interactions/<name>.md` — these contain reusable
       interaction specs (SVG animations, hotspot logic) that the template
       depends on but does not duplicate inline. These are **mandatory** —
       the template does not fully work without them.
   f3. **Distinctive modules (optional, for visual differentiation)**: Read
       `templates/_shared/module-index.md`. Cross-reference `brainstorm.md`
       (product type, mood, any reference sites mentioned) against the module
       catalog. Build **2-3 different module combinations** (1-3 modules
       each, each combination with a distinct "personality" — not small
       variations of the same idea) and present them to the user with a short
       reason each fits. **Do not silently auto-apply a single "best"
       combination** — two different projects on the same base template
       should not converge on the same look, which is the entire point of
       this step. Wait for the user to pick one, mix their own, or skip
       module selection entirely (a template alone is a valid choice too).
       Once chosen, read the full file for each selected module and fold its
       spec into the plan.
   g. **Tech stack check against constitution**:
      - If `constitution.md` allows React + TypeScript + Vite + Tailwind CSS
        → plan includes full code generation from the template prompt.
      - If `constitution.md` requires a different stack (e.g., Next.js, Vue,
        vanilla JS, or any non-React stack) → plan includes **design-only
        output**: layout structure, color palette, typography, interactions, and
        assets. The template prompt is provided as a reference but the actual
        code tasks use the constitution's mandated stack.
   h. If the project has **no UI component** (CLI tool, API, library, etc.)
      → **skip this step entirely**.

4. **Draft a short spec section** (what/why, not how): one short paragraph plus a
   bullet list of functional requirements and acceptance criteria. Keep it
   high-level; implementation detail belongs in the task breakdown.
5. **Constitution compliance check** — walk every principle in constitution.md and
   mark: complies / needs a documented exception (with justification) / not
   applicable. A plan with an unresolved conflict is not done.
6. **Technical approach** — architecture and tech choices for this feature,
   consistent with the constitution's technology constraints.
7. **Task breakdown** — split the approach into tasks that each:
   - Take about 2-5 minutes of focused work.
   - Name the exact file path(s) touched.
   - State the test that proves the task is done (TDD-first: the test-writing task
     comes before the implementation task).
   - Leave the codebase in a working, testable state when done.
   - If a design template was selected, include tasks for:
     - Setting up the template's fonts (Google Fonts links in index.html)
     - Installing/copying ReactBits components from reactbits.dev
     - Building each layout section defined in the template
     - Integrating generated assets (these will be created by `sdd-asset-generator`
       during build)
   - If distinctive modules were selected, include a separate task per module
     for implementing its spec (each module file has its own condensed
     "Prompt" section ready to hand to a subagent) — keep module tasks
     separate from base-template section tasks so they can be reviewed
     independently.
8. Present the draft **in sections** (spec -> template -> compliance check -> tasks)
   for the user to validate — don't dump the whole thing and assume approval.

## Output
Write to: `docs/sdd/<feature-slug>/plan.md`

```markdown
# Plan: <Feature Name>

Source: brainstorm.md (v?), constitution.md (v?)

## Spec summary
### Functional requirements
### Acceptance criteria

## Design Template
- Template: `<chosen template name>`
- Source: `templates/<file>.md`
- Color Palette:
  - Primary: `#hex` — usage
  - Secondary: `#hex` — usage
  - Accent: `#hex` — usage
  - Background: `#hex`
  - Text: `#hex`
- Fonts:
  - Display: `<font name>` — headings, hero text
  - Body: `<font name>` — paragraphs, labels
- ReactBits Components:
  - `<Component>` — `<url>` — `<where used>`
- Required Assets:
  - `<asset-name>` — `<description>` — `<needs bg removal?>`
- Stack Note: `<"Full code generation" or "Design-only (stack outside React/TS/Vite/Tailwind)">`

## Distinctive Modules (optional)
- Combination presented: `<A / B / C>` — chosen: `<which one, or "custom mix", or "none">`
- Modules:
  - `<module id>` — `templates/_shared/<category>/<file>.md` — `<where applied in this project>`

## Constitution compliance check
| Principle | Status | Notes |
|---|---|---|

## Technical approach

## Tasks
- [ ] Task 1 — <file path(s)> — <test that proves this is done> — <exact steps>
- [ ] Task 2 — ...
```

If no design template was selected (non-UI project), omit the `## Design Template`
section entirely.

## Handoff
When the user approves the plan, say:

> "Plan đã được duyệt. Bước tiếp theo là **sdd-build** để bắt đầu thực thi."
