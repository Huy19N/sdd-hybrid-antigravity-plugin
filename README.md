# sdd-hybrid

Spec-driven development workflow for AI coding agents, built as an **Antigravity
plugin**: `Brainstorm → Constitution → Plan → Build → Review → Security`.

Combines:
- **[obra/superpowers](https://github.com/obra/superpowers)**-style engineering
  discipline — bite-sized tasks, TDD, code review, subagent execution.
- **[github/spec-kit](https://github.com/github/spec-kit)**-style constitution —
  a project-wide, binding rule set every step must respect.
- An **OWASP Top 10:2025** security gate that must pass before anything is
  pushed, PR'd, or sent to CI/CD.

Install this plugin once, and every new project you start gets the same
disciplined flow — no copy-pasting prompts between projects.

## The workflow

```
1. sdd-brainstorm       docs/sdd/<feature>/brainstorm.md
2. sdd-constitution     docs/sdd/constitution.md            (once per project)
3. sdd-plan             docs/sdd/<feature>/plan.md
4. sdd-build            code, plan.md tasks checked off
5. sdd-review-code      docs/sdd/<feature>/review-report.md   (correctness)
6. sdd-security-review  docs/sdd/<feature>/security-report.md (OWASP Top 10:2025)
                         -> only a "Cleared" verdict here unlocks push/PR/CI-CD
```

Each skill is a `SKILL.md` under `skills/`. The agent picks the right one
automatically based on its `description` — you don't need slash commands, just
describe what you want ("I want to build X", "ready to start building",
"review this before I push").

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

## Using it in a new project

1. Open the project in Antigravity (CLI or IDE) with the plugin installed.
2. Just describe the idea: *"I want to build a notification system for..."*
   → `sdd-brainstorm` kicks in and asks clarifying questions.
3. First time in this project? Right after brainstorm is approved, run the
   constitution step once: *"let's set up the project constitution."*
4. Approve `brainstorm.md` → plan → build → review → security, in order. Each
   skill tells you explicitly what the next one is when it finishes.
5. Only after `sdd-security-review` says **Cleared** should you push or open a PR.

## Repo layout

```
sdd-hybrid/
├── plugin.json                     # Antigravity plugin manifest
├── rules/
│   └── sdd-workflow.md             # always-loaded: step order + hard gates
├── skills/
│   ├── sdd-brainstorm/SKILL.md
│   ├── sdd-constitution/SKILL.md
│   ├── sdd-plan/SKILL.md
│   ├── sdd-build/SKILL.md
│   ├── sdd-review-code/SKILL.md
│   └── sdd-security-review/SKILL.md
├── LICENSE
└── README.md
```

## Why a constitution as well as a brainstorm

Superpowers has brainstorming but nothing binding downstream of it. Spec-kit has
a constitution but no equivalent brainstorming step. Here:

- `brainstorm.md` is **per feature** — the idea, scope, and approach for one
  piece of work.
- `constitution.md` is **per project, created once** — non-negotiable rules
  (testing standards, tech constraints, security requirements, architecture
  principles) that every later step must be checked against. `sdd-plan` checks
  a draft plan against it, `sdd-build` stops on any violation instead of routing
  around it, and `sdd-review-code` / `sdd-security-review` check the final code
  against it again, since small violations can drift in across several tasks
  even if each one individually passed its own check.

## Why OWASP Top 10:2025 as a hard gate before CI/CD

Neither superpowers nor spec-kit has a dedicated security step — code review
checks logic, not exploitability. `sdd-security-review` runs after
`sdd-review-code` and walks the diff against the current OWASP Top 10:2025
list (SSRF folded into Broken Access Control; Software Supply Chain Failures
and Mishandling of Exceptional Conditions are new since the 2021 list), plus
whatever your `constitution.md` states under "Security requirements". A
Critical or High finding blocks the branch from being pushed — `sdd-review-code`
is explicitly not allowed to offer merge/PR/push options itself, only
`sdd-security-review` can, and only after a clean or explicitly-accepted verdict.

## Customizing

- Add or edit skills under `skills/<name>/SKILL.md` — the `description` field in
  the frontmatter controls when the agent picks it up, so keep it specific.
- Edit `rules/sdd-workflow.md` to change the step order or add project-specific
  hard rules that should apply to every session, not just when a skill triggers.
- If you rely on other superpowers skills too (`test-driven-development`,
  `systematic-debugging`, `using-git-worktrees`, `subagent-driven-development`),
  install that plugin alongside this one — `sdd-build` and `sdd-review-code`
  reference them as optional sub-steps when available.
