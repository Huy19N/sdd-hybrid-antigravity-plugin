---
name: sdd-help
description: "Use when the user asks for help, guidance, or how to use the SDD-Hybrid workflow. Responds to triggers like 'help', 'hướng dẫn', 'cách dùng', 'workflow là gì', 'bắt đầu từ đâu', 'next step', or 'bước tiếp theo'. Shows the complete workflow (BA/SA document chain + 6-step development cycle), checks the current state of existing documents, and recommends the next step. Does not create any files."
---

# SDD Help (Workflow Guide)

## Purpose
Help the user understand and navigate the full SDD-Hybrid workflow. This skill
does NOT create any files — it only provides guidance, checks document status,
and recommends the next step.

## When to use
- User says "help", "hướng dẫn", "cách dùng", "làm sao", "bắt đầu từ đâu"
- User asks "bước tiếp theo là gì?", "next step?", "what should I do next?"
- User seems confused about the workflow order
- User is new to the SDD-Hybrid plugin

## Process

### Step 1: Show the Complete Workflow

Display the full workflow in two phases:

```
╔══════════════════════════════════════════════════════════════════╗
║                    SDD-HYBRID WORKFLOW                          ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  📋 PHASE A: BA/SA Document Chain (project-level, done once)     ║
║  ─────────────────────────────────────────────────────────────    ║
║  A1. sdd-create-brd    → docs/sdd/BRD.md                        ║
║      Business Requirements Document                              ║
║      (Problem, Vision, Stakeholders, Scope, Rules, Risks)        ║
║                          ↓                                       ║
║  A2. sdd-create-prd    → docs/sdd/PRD.md                        ║
║      Product Requirements Document                               ║
║      (Business Capabilities, Functional Reqs, NFRs)              ║
║                          ↓                                       ║
║  A3. sdd-create-es     → docs/sdd/ES.md                         ║
║      Event Storming Canvas                                       ║
║      (Domain Events, Commands, Policies, Aggregates)             ║
║                          ↓                                       ║
║  A4. sdd-create-add    → docs/sdd/ADD.md                        ║
║      Architecture Design Document                                ║
║      (Tech Stack, Entities, Components, Contracts, ADRs)         ║
║                                                                  ║
║  ⚙️ PHASE B: Feature Development Cycle (per feature)             ║
║  ─────────────────────────────────────────────────────────────    ║
║  B1. sdd-brainstorm    → docs/sdd/<feature>/brainstorm.md       ║
║      (auto: sdd-deep-research)                                   ║
║                          ↓                                       ║
║  B2. sdd-constitution  → docs/sdd/constitution.md (once)         ║
║                          ↓                                       ║
║  B3. sdd-plan          → docs/sdd/<feature>/plan.md             ║
║      (auto: Design Template Selection + FR/BR Traceability)     ║
║                          ↓                                       ║
║  B4. sdd-build         → code + tests                           ║
║      (auto: assets, bg-remover, ReactBits, BR/FR tracking)      ║
║                          ↓                                       ║
║  B5. sdd-review-code   → docs/sdd/<feature>/review-report.md   ║
║      (includes: BR Compliance + FR Coverage analysis)            ║
║                          ↓                                       ║
║  B6. sdd-security-review → docs/sdd/<feature>/security-report.md║
║      🔒 Only "Cleared" unlocks push/PR/CI-CD                    ║
║                                                                  ║
║  ❓ sdd-help — Show this guide anytime                           ║
║  📊 sdd-traceability-report — FR/BR coverage dashboard           ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

### Step 2: Check Current Document Status
Scan the project for existing SDD documents and report their status:

```
📊 Document Status:
  Phase A (BA/SA):
    BRD.md:          ✅ exists / ❌ missing
    PRD.md:          ✅ exists / ❌ missing
    ES.md:           ✅ exists / ❌ missing
    ADD.md:          ✅ exists / ❌ missing

  Phase B (Project-wide):
    constitution.md: ✅ exists / ❌ missing

  Phase B (Per-feature):
    <feature-1>/brainstorm.md: ✅ / ❌
    <feature-1>/plan.md:       ✅ / ❌
    ...
```

Check for these files:
- `docs/sdd/BRD.md`
- `docs/sdd/PRD.md`
- `docs/sdd/ES.md`
- `docs/sdd/ADD.md`
- `docs/sdd/constitution.md`
- `docs/sdd/*/brainstorm.md` (glob for all features)
- `docs/sdd/*/plan.md`
- `docs/sdd/*/review-report.md`
- `docs/sdd/*/security-report.md`

### Step 3: Recommend Next Step
Based on the document status, recommend the logical next step:

**Decision tree:**
1. No BRD.md → "Bắt đầu với **sdd-create-brd** để tạo Business Requirements Document."
2. BRD exists, no PRD → "BRD đã có. Tiếp theo: **sdd-create-prd** để tạo Product Requirements."
3. BRD + PRD exist, no ES → "Tiếp theo: **sdd-create-es** để tạo Event Storming Canvas."
4. BRD + PRD + ES exist, no ADD → "Tiếp theo: **sdd-create-add** để thiết kế kiến trúc."
5. All Phase A done, no constitution → "Phase A hoàn tất! Tiếp: **sdd-constitution** để thiết lập quy tắc dự án."
6. Constitution exists, no feature brainstorms → "Sẵn sàng phát triển feature! Mô tả ý tưởng feature để **sdd-brainstorm** bắt đầu."
7. Feature has brainstorm, no plan → "Brainstorm xong. Tiếp: **sdd-plan** cho feature [name]."
8. Feature has plan, not built → "Plan đã sẵn sàng. Tiếp: **sdd-build** để bắt đầu code."
9. Feature built, no review → "Code xong. Tiếp: **sdd-review-code** để kiểm tra chất lượng."
10. Feature reviewed, no security → "Review xong. Tiếp: **sdd-security-review** — bước cuối trước khi push."

### Step 4: Answer Specific Questions
If the user has a specific question, answer it:

- **"Skill X làm gì?"** → Explain the skill's purpose and when to use it.
- **"Tôi có thể bỏ qua bước X không?"** → Explain why the step is important, but
  note that Phase A (BA/SA) is recommended but not hard-gated — users can start
  from Phase B if they prefer. Phase B steps have hard gates.
- **"Sự khác biệt giữa BRD và PRD?"** → BRD = business needs (WHY),
  PRD = product behaviors (WHAT the system does).
- **"Event Storming là gì?"** → A collaborative modeling technique that discovers
  domain complexity by mapping events, commands, and policies.

## Interaction Rules
- Always be concise — this is a help guide, not a lecture.
- Use Vietnamese for explanations, English for technical terms.
- After showing the guide, ask: "Bạn muốn bắt đầu bước nào?"
- If the user is overwhelmed, suggest starting with just Phase A, step 1.

## Output
This skill does NOT create any files. It only displays information and guidance
in the chat.
