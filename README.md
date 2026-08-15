# sdd-hybrid

Spec-driven development workflow for AI coding agents, built as an **Antigravity
plugin**: `Brainstorm → Constitution → Plan → Build → Review → Security`.

Now with **UI/UX design automation**: 22 design templates, 13 shared design
modules, automatic asset generation (Art Director v2), video generation (Veo 3.1),
background removal, and ReactBits component integration.

Combines:
- **[obra/superpowers](https://github.com/obra/superpowers)**-style engineering
  discipline — bite-sized tasks, TDD, code review, subagent execution.
- **[github/spec-kit](https://github.com/github/spec-kit)**-style constitution —
  a project-wide, binding rule set every step must respect.
- An **OWASP Top 10:2025** security gate that must pass before anything is
  pushed, PR'd, or sent to CI/CD.
- **22 UI/UX design templates** with auto-selection, 13 mixable design modules,
  asset generation (Art Director v2), video generation, and premium animated components from
  [ReactBits](https://www.reactbits.dev/).

Install this plugin once, and every new project you start gets the same
disciplined flow — no copy-pasting prompts between projects.

## The workflow

```
1. sdd-brainstorm       docs/sdd/<feature>/brainstorm.md
   └── sdd-deep-research   (auto: market/competitor/UX research)
2. sdd-constitution     docs/sdd/constitution.md            (once per project)
3. sdd-plan             docs/sdd/<feature>/plan.md
   └── Design Template Selection (auto: 2-3 suggestions from 22 templates)
       + Distinctive Module Selection (2-3 combos from 13 shared modules)
4. sdd-build            code, plan.md tasks checked off
   ├── sdd-asset-generator  (auto: generate images via generate_image tool)
   ├── sdd-bg-remover       (auto: remove backgrounds if template requires)
   ├── sdd-video-generator  (auto: generate video via Veo 3.1 if plan requires)
   └── ReactBits copy       (auto: copy components from reactbits.dev)
5. sdd-review-code      docs/sdd/<feature>/review-report.md   (correctness)
6. sdd-security-review  docs/sdd/<feature>/security-report.md (OWASP Top 10:2025)
                         -> only a "Cleared" verdict here unlocks push/PR/CI-CD
```

Each skill is a `SKILL.md` under `skills/`. The agent picks the right one
automatically based on its `description` — you don't need slash commands, just
describe what you want ("I want to build X", "ready to start building",
"review this before I push").

## Design Templates (22 available)

When planning a UI-focused project, the agent automatically scans your
`brainstorm.md` and suggests the **2-3 most relevant templates** from the library:

| # | Template | Category | Key Features |
|---|---|---|---|
| 1 | Product Carousel | product-store | Transparent cutout images, color-shifting bg, depth carousel |
| 2 | SaaS Landing | saas | Aurora gradient, shiny text, pricing toggle |
| 3 | Creative Portfolio | portfolio | Masonry grid, serif typography, blur text |
| 4 | Restaurant & Food | food-beverage | Parallax food gallery, circular gallery, menu tabs |
| 5 | Fashion E-Commerce | fashion | Morph slider, lookbook layout, quick-view cards |
| 6 | Tech / AI Startup | tech-startup | Dot field particles, glitch text, blob cursor |
| 7 | Real Estate | real-estate | Bento grid properties, search hero, grid distortion |
| 8 | Education / LMS | education | Progress rings, split flap counter, gamification |
| 9 | Healthcare & Clinic | healthcare | Color bends bg, glass icons, booking form |
| 10 | Event & Conference | event | Line waves bg, countdown, scrambled text |
| 11 | Fitness & Gym | fitness | Neon green, pixel trail, text pressure |
| 12 | Travel & Tourism | travel | Morph slider hero, ripple distortion, booking |
| 13 | Music & Streaming | music | Magic rings, particle text, mini player |
| 14 | Crypto & Fintech | crypto-fintech | Aurora bg, blob cursor, live data tables |
| 15 | Photography Studio | photography | Circular gallery, magnet lines, minimal |
| 16 | Automotive | automotive | Grid distortion, shiny text, transparent vehicles |
| 17 | Pet Care | pet-care | Sticker peel, animated list, rounded playful |
| 18 | Coworking Space | coworking | Magic bento, tilted cards, industrial warm |
| 19 | Wedding Planner | wedding | Falling text, circular gallery, romantic serif |
| 20 | News & Magazine | news-blog | Split flap ticker, infinite menu, editorial grid |
| 21 | Scene Doodle Annotation | lifestyle-scene | Hand-drawn SVG hover annotations on scene photo |
| 22 | Shoppable Lifestyle Scene | shoppable-scene | Shop-the-look hotspots, mini product cards on scene |

Each template includes:
- Full React + TypeScript + Vite + Tailwind CSS prompt
- Color palette (sourced from [Coolors](https://coolors.co/palettes/popular))
- Google Fonts configuration
- ReactBits component references
- Required assets list for auto-generation
- Responsive layout specifications (mobile/tablet/desktop)

**Hand-drawn button hover** (v2): Templates 04, 07, 16, 17, 18, 19, 21, 22 also
apply a wobbly hand-drawn SVG border to CTA buttons on hover/focus — pure CSS,
no JS state needed. The `button-hover` variant from
`_shared/interactions/hand-drawn-annotation.md` is compatible with **all**
templates' CTA buttons.

## Shared Design Modules (13 available)

After picking a template, the agent suggests **2-3 module combos** from 13
mixable design modules to differentiate your project visually:

| Module | Type | Purpose |
|---|---|---|
| Hand-Drawn Annotation (v2) | interaction | Scene hotspots + button hover border |
| 3D Motion Frame | surface | Tilt/parallax/glare on cards |
| Holographic Shimmer | surface | Iridescent rainbow chromatic foil on cards |
| Ambient Glow Cursor | surface | Radial spotlight follower & border glow |
| Circular Badge Stamp | interaction | Rotating kinetic SVG text stamp ("Artisanal Quality") |
| Interactive Split Slider | viewer | Dual-state before/after comparison drag slider |
| Glassmorphism | surface | Frosted glass overlays |
| 360° Drag-Rotate Viewer | viewer | Product 360° inspection |
| Magnetic Cursor | interaction | Cursor attracted to buttons |
| Scroll Velocity Marquee | interaction | Kinetic text strip |
| Grain & Noise Overlay | surface | Premium grain texture |
| Liquid Blob Background | surface | Organic blob morphing bg |
| Scroll-Scrubbing Video | viewer | Apple-style scroll-controlled video playback |

## Sub-skills (auto-invoked)

These skills are called automatically — you never need to trigger them manually:

| Sub-skill | Called by | Purpose |
|---|---|---|
| `sdd-deep-research` | `sdd-brainstorm` | Market analysis, competitor landscape, UX trends, technical feasibility |
| `sdd-asset-generator` | `sdd-build` | Art Director Edition (v2): Curate and generate high-artistry images (3D liquid chrome, editorial photography, tactile still life) across 22 design templates via `generate_image` tool |
| `sdd-bg-remover` | `sdd-build` | Remove image backgrounds using `rembg` with tiered model selection (isnet → birefnet), auto-escalation, and alpha cleanup |
| `sdd-video-generator` | `sdd-build` | Generate video assets using Gemini API + Veo 3.1 (tiered: lite/fast/standard) |

## Install

### Antigravity CLI (`agy`) — global, applies to every project (recommended)

```bash
agy plugin install https://github.com/Huy19N/sdd-hybrid-antigravity-plugin
```

This stages the plugin under `~/.gemini/antigravity-cli/plugins/sdd-hybrid/`.
Once installed, it's active in every project you open with `agy` — nothing to
repeat per project. To update after you push changes to this repo, just run
the same install command again.

### Antigravity CLI or IDE — per-project (if you want to pin a version per repo)

```bash
mkdir -p .agents/plugins
git clone https://github.com/Huy19N/sdd-hybrid-antigravity-plugin .agents/plugins/sdd-hybrid
```

Or as a submodule, so each project tracks a specific commit:

```bash
git submodule add https://github.com/Huy19N/sdd-hybrid-antigravity-plugin .agents/plugins/sdd-hybrid
```

### Antigravity IDE — global (applies to every workspace)

```bash
git clone https://github.com/Huy19N/sdd-hybrid-antigravity-plugin ~/.gemini/config/plugins/sdd-hybrid
```

> Note: the IDE's global path (`~/.gemini/config/plugins/`) is different from
> the CLI's global path (`~/.gemini/antigravity-cli/plugins/`, managed by
> `agy plugin install`). Pick the one matching whichever you actually use — if
> you use both, install both ways.

### Optional: Background removal dependency

If you plan to use templates that require transparent images (product stores,
food, fashion, automotive, pet care), install the Python dependencies:

```bash
pip install rembg Pillow numpy scipy
```

For GPU-accelerated processing:
```bash
pip install rembg[gpu] Pillow numpy scipy
```

> `numpy` is required; `scipy` is optional but strongly recommended — it enables
> connected-component alpha cleanup for cleaner edges.

### Optional: Video generation dependency

If you plan to use modules that require video assets (e.g., `scroll-scrubbing-video`),
install the Gemini API client:

```bash
pip install google-genai
```

You'll also need a `GEMINI_API_KEY` (get one at https://aistudio.google.com/apikey)
and optionally `ffmpeg` on PATH (for frame extraction in scroll-scrubbing mode).

## Using it in a new project

1. Open the project in Antigravity (CLI or IDE) with the plugin installed.
2. Just describe the idea: *"I want to build a notification system for..."*
   → `sdd-brainstorm` kicks in, runs deep research, then asks clarifying questions.
3. First time in this project? Right after brainstorm is approved, run the
   constitution step once: *"let's set up the project constitution."*
4. When planning, the agent will automatically suggest 2-3 design templates
   matching your project — pick one and it becomes part of the plan.
5. During build, assets are generated automatically, backgrounds removed if needed,
   and ReactBits components are copied and configured in your project.
6. Only after `sdd-security-review` says **Cleared** should you push or open a PR.

## Repo layout

```
sdd-hybrid/
├── plugin.json                            # Antigravity plugin manifest
├── rules/
│   └── sdd-workflow.md                    # always-loaded: step order + hard gates
├── skills/
│   ├── sdd-brainstorm/SKILL.md            # Step 1: idea → brainstorm.md
│   ├── sdd-constitution/SKILL.md          # Step 2: project-wide rules
│   ├── sdd-plan/
│   │   ├── SKILL.md                       # Step 3: brainstorm → plan.md
│   │   └── templates/                     # 22 UI/UX design templates
│   │       ├── template-index.md          # Quick-reference index
│   │       ├── _shared/                   # Shared design modules
│   │       │   ├── module-index.md         # Module catalog & selection guide
│   │       │   ├── interactions/           # Hover/scroll behaviors
│   │       │   │   ├── circular-badge-stamp.md   # Rotating kinetic SVG stamp
│   │       │   │   ├── hand-drawn-annotation.md  # v2: scene-hotspot + button-hover
│   │       │   │   ├── magnetic-cursor.md
│   │       │   │   └── scroll-velocity-marquee.md
│   │       │   ├── surfaces/              # Visual textures & materials
│   │       │   │   ├── 3d-motion-frame.md
│   │       │   │   ├── ambient-glow-cursor.md    # Spotlight cursor & border glow
│   │       │   │   ├── glassmorphism.md
│   │       │   │   ├── grain-noise-overlay.md
│   │       │   │   ├── holographic-shimmer.md    # Iridescent chromatic foil
│   │       │   │   └── liquid-blob-background.md
│   │       │   └── viewers/               # Complex interactive components
│   │       │       ├── interactive-split-slider.md # Dual-state comparison slider
│   │       │       ├── product-360-drag-rotate.md
│   │       │       └── scroll-scrubbing-video.md
│   │       ├── 01-product-carousel.md
│   │       ├── ...
│   │       ├── 20-news-magazine.md
│   │       ├── 21-scene-doodle-annotation.md
│   │       └── 22-shoppable-lifestyle-scene.md
│   ├── sdd-build/SKILL.md                 # Step 4: plan → code
│   ├── sdd-review-code/SKILL.md           # Step 5: correctness review
│   ├── sdd-security-review/SKILL.md       # Step 6: OWASP security gate
│   ├── sdd-deep-research/SKILL.md         # Sub-skill: market/UX research
│   ├── sdd-asset-generator/SKILL.md       # Sub-skill: image generation
│   ├── sdd-bg-remover/                    # Sub-skill: background removal
│   │   ├── SKILL.md
│   │   └── scripts/
│   │       └── remove_bg.py
│   └── sdd-video-generator/               # Sub-skill: video generation
│       ├── SKILL.md
│       └── scripts/
│           ├── generate_video.py
│           └── extract_frames.py
├── LICENSE
└── README.md
```

## Why a constitution as well as a brainstorm

Superpowers has brainstorming but nothing binding downstream of it. Spec-kit has
a constitution but no equivalent brainstorming step. Here:

- `brainstorm.md` is **per feature** — the idea, scope, and approach for one
  piece of work. Now enhanced with **automatic deep research** (market data,
  competitor analysis, UX trends).
- `constitution.md` is **per project, created once** — non-negotiable rules
  (testing standards, tech constraints, security requirements, architecture
  principles) that every later step must be checked against.

## Why design templates

AI coding agents often produce generic-looking UIs. By embedding 22 curated
design templates + 8 mixable design modules into the workflow:

- **Consistency**: Every project gets a premium, well-designed starting point.
- **Speed**: No time wasted debating colors, fonts, or layout — pick a template
  and build.
- **Quality**: Templates reference ReactBits components for professional-grade
  animations and interactions.
- **Automation**: Assets are generated, backgrounds removed, and components
  configured automatically during the build step.
- **Differentiation**: Shared modules (3D tilt, glassmorphism, 360° viewer,
  magnetic cursor, etc.) ensure two projects on the same base template still
  look distinctly different.

## Why OWASP Top 10:2025 as a hard gate before CI/CD

Neither superpowers nor spec-kit has a dedicated security step — code review
checks logic, not exploitability. `sdd-security-review` runs after
`sdd-review-code` and walks the diff against the current OWASP Top 10:2025
list, plus whatever your `constitution.md` states under "Security requirements".

## Customizing

- Add or edit skills under `skills/<name>/SKILL.md` — the `description` field in
  the frontmatter controls when the agent picks it up, so keep it specific.
- Edit `rules/sdd-workflow.md` to change the step order or add project-specific
  hard rules that should apply to every session, not just when a skill triggers.
- Add new design templates to `skills/sdd-plan/templates/` — follow the existing
  template format with YAML frontmatter (id, name, category, tags, color_palette,
  reactbits_components, best_for) and update `template-index.md`.
- If you rely on other superpowers skills too (`test-driven-development`,
  `systematic-debugging`, `using-git-worktrees`, `subagent-driven-development`),
  install that plugin alongside this one — `sdd-build` and `sdd-review-code`
  reference them as optional sub-steps when available.
