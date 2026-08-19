# SDD-Hybrid workflow

This project uses the **sdd-hybrid** plugin. Any time you are about to start a new
feature, write a plan, write code, or finish a change, check whether one of the
skills below applies before doing anything else — including before asking
clarifying questions or exploring the codebase. If there is even a small chance a
step applies, use it. This is not optional.

## The six steps, in order

1. **sdd-brainstorm** — turn a rough idea into `docs/sdd/<feature-slug>/brainstorm.md`.
   - Auto-invokes: **sdd-deep-research** (market/competitor/UX research) before
     Socratic questioning begins.
2. **sdd-constitution** — project-wide binding rules in `docs/sdd/constitution.md`
   (created once, amended over time — not per feature).
3. **sdd-plan** — turn an approved brainstorm into `docs/sdd/<feature-slug>/plan.md`
   (spec + platform/architecture selection + constitution compliance check + bite-sized tasks).
   - Includes: **Platform & Stack Selection** (Web React, Mobile Expo/Flutter/Kotlin, or 2D/2.5D Game).
   - Includes: **Design Template & Module Selection** (22 UI/UX templates + 18 shared modules for UI projects) OR **Game Asset Requirements** (parallax composite scenes, character sprites, tileable textures for game projects).
4. **sdd-build** — execute the plan task-by-task under TDD, gated by the constitution.
   - Auto-invokes (when plan.md has `## Design Template` or `## Game Asset Requirements`):
     → **sdd-asset-generator** — creates visual assets (Web/Mobile UI assets OR Game parallax scenes, sprites, textures) via `generate_image` tool.
     → **sdd-bg-remover** — Mode 1 (`remove_bg.py`): removes backgrounds for cutouts; Mode 2 (`segment_layers.py`): multi-layer CLIPSeg segmentation for game parallax composite scenes into separate transparent PNG layers.
     → **`make_tileable.py`** — seamless seam-offset post-processing for game textures.
     → **sdd-video-generator** — generates video assets via Gemini API + Veo 3.1
       (only when plan.md has video asset requirements).
     → **ReactBits / Mobile / Game Component copy** — copies and configures UI/Game components in project.
5. **sdd-review-code** — full correctness/logic review after all tasks are done.
6. **sdd-security-review** — OWASP Top 10:2025 (Web) & OWASP Mobile Top 10 gate. **Nothing gets pushed, PR'd,
   or sent to CI/CD/Store before this step returns a "Cleared" verdict.**

## Sub-skills (auto-invoked, never trigger manually)

These skills are called automatically by their parent skills. Do not trigger them
directly — they have no standalone use:

| Sub-skill | Called by | When |
|---|---|---|
| `sdd-deep-research` | `sdd-brainstorm` | Always — first step of brainstorming |
| `sdd-asset-generator` | `sdd-build` | When plan.md has `## Design Template` (web/mobile) OR `## Game Asset Requirements` (2D/2.5D game) |
| `sdd-bg-remover` | `sdd-build` | Mode 1 (`remove_bg.py`): when template has `requires_transparent_images: true` or sprite cutout. Mode 2 (`segment_layers.py`): when game plan has parallax composite scenes with decomposition labels |
| `sdd-video-generator` | `sdd-build` | When plan.md has video asset requirements |

## Hard rules

- Never skip straight to writing code for a new feature without brainstorm + plan.
- Never treat `constitution.md` as optional reading — `sdd-build` must stop on any
  violation instead of routing around it.
- Never let `sdd-review-code` offer to merge/PR/push directly — that decision only
  happens after `sdd-security-review` clears the branch.
- `constitution.md` is project-wide (one file, amended over time). `brainstorm.md`,
  `plan.md`, `review-report.md`, and `security-report.md` are per-feature, under
  `docs/sdd/<feature-slug>/`.
- Design template selection is mandatory for UI-focused projects. For non-UI projects
  (CLI, API, library), skip template selection entirely.
- When template selection suggests 2-3 templates, always wait for the user to choose
  one — never auto-select.

## Small tasks and bug fixes

For a small, already fully-specified task, or for a bug fix, the full six-step
flow is overkill — use judgment. Bug fixes should still go through systematic
debugging if that skill is available, and any code change should still pass
`sdd-review-code` and `sdd-security-review` before it's pushed.
