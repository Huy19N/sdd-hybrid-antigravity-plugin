---
name: sdd-traceability-report
description: "Use when the user asks about progress, coverage, traceability, or which functional requirements are done. Triggers include 'tiến độ', 'coverage', 'traceability', 'FR nào xong rồi', 'progress', 'requirement status', or 'báo cáo tiến độ'. Reads BRD.md, PRD.md, and all feature plan.md files to generate an on-demand traceability dashboard showing Business Rule compliance, Functional Requirement coverage, and per-feature progress. Does not create files — displays results in chat only. Requires at least docs/sdd/PRD.md to produce useful output."
---

# SDD Traceability Report (on-demand dashboard)

## Purpose
Generate an on-demand dashboard showing the current status of Business Rule
compliance and Functional Requirement coverage across all features. This is a
read-only, non-destructive skill — it only reads existing documents and reports
status, never modifies anything.

## When to use
- User asks about progress: "tiến độ", "progress", "how much is done"
- User asks about coverage: "FR nào xong rồi", "requirement status", "coverage"
- User asks about traceability: "traceability", "mapping", "gap analysis"
- User wants a quick status check before a meeting or report

## When NOT to use
- No `docs/sdd/PRD.md` exists → inform the user there's nothing to trace.
  Recommend `sdd-create-prd` if they want traceability features.
- User wants to modify requirements → redirect to `sdd-create-brd` or
  `sdd-create-prd`.

## Process

### Step 1: Scan for documents
Check for existence of:
- `docs/sdd/BRD.md` → extract Business Rules (BR-xxx) from Section 5
- `docs/sdd/PRD.md` → extract Functional Requirements (FR-xxx) from Section 2,
  NFRs (NFR-xxx) from Section 3
- `docs/sdd/*/plan.md` → scan all feature plan.md files for:
  - Task completion status (`[x]` vs `[ ]`)
  - Requirement Traceability section (FR/BR → task mapping with status)
- `docs/sdd/*/review-report.md` → check for BR Compliance and FR Coverage results

If PRD.md doesn't exist, say:
> "Chưa có PRD.md nên không có dữ liệu traceability. Chạy **sdd-create-prd** để
> tạo Product Requirements Document, sau đó traceability sẽ tự động hoạt động."

### Step 2: Aggregate status
For each FR-xxx from PRD:
- Check all plan.md files → is this FR mapped to any task?
- If mapped, what's the task status? (`⬜ Pending` / `✅ Done`)
- If a review-report.md exists, use its FR Coverage table as the definitive status
- Final status per FR:
  - ✅ **Implemented & Tested** — code + test exist, review confirmed
  - ⚠️ **Implemented, No Test** — code exists but test missing
  - 🔄 **In Progress** — task mapped but not yet completed
  - 🔲 **Not Started** — task mapped but pending
  - ❌ **Not Planned** — no task maps to this FR in any plan.md
  - 🔳 **Deferred** — explicitly marked out-of-scope with justification

For each BR-xxx from BRD:
- Check review-report.md for compliance status
- If no review exists, check plan.md Requirement Traceability section
- Final status:
  - ✅ **Compliant** — review confirmed
  - ❌ **Violated** — review found violation
  - ⚠️ **Partially** — partially implemented
  - 🔲 **Not Checked** — no review has verified this yet

### Step 3: Display dashboard
Present the dashboard in chat (do NOT create a file):

```
╔══════════════════════════════════════════════════════════════╗
║                  TRACEABILITY DASHBOARD                      ║
║                  Generated: <timestamp>                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📋 Business Rules (from BRD.md)                             ║
║  Total: X rules                                              ║
║  ├── ✅ Compliant:    X                                      ║
║  ├── ❌ Violated:     X                                      ║
║  ├── ⚠️ Partial:      X                                      ║
║  └── 🔲 Not Checked:  X                                      ║
║                                                              ║
║  ⚙️ Functional Requirements (from PRD.md)                    ║
║  Total: X requirements                                       ║
║  ├── ✅ Implemented & Tested:  X (Z%)                        ║
║  ├── ⚠️ Implemented, No Test:  X (Z%)                        ║
║  ├── 🔄 In Progress:           X (Z%)                        ║
║  ├── 🔲 Not Started:           X (Z%)                        ║
║  ├── ❌ Not Planned:           X (Z%)                        ║
║  └── 🔳 Deferred:              X (Z%)                        ║
║                                                              ║
║  📊 Per-Feature Breakdown                                    ║
║  ├── <feature-1>: Tasks X/Y done                             ║
║  │   FRs: FR-001 ✅, FR-002 ✅, FR-003 🔄                   ║
║  ├── <feature-2>: Tasks X/Y done                             ║
║  │   FRs: FR-005 🔲, FR-006 🔲                               ║
║  └── <not-in-any-feature>:                                   ║
║      FRs: FR-010 ❌, FR-011 ❌ (not planned yet)             ║
║                                                              ║
║  📊 NFR Status (from PRD.md Section 3)                       ║
║  ├── Performance:  ✅ / ⚠️ / 🔲                              ║
║  ├── Security:     ✅ / ⚠️ / 🔲                              ║
║  ├── Availability: ✅ / ⚠️ / 🔲                              ║
║  └── ...                                                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### Step 4: Highlight gaps and recommend actions
After the dashboard, provide actionable recommendations:

- **If FRs are ❌ Not Planned**: "FR-010, FR-011 chưa được plan vào feature nào.
  Cần tạo feature mới hoặc thêm vào feature hiện có."
- **If BRs are ❌ Violated**: "BR-002 bị vi phạm trong feature-order. Cần fix
  trước khi push."
- **If FRs are ⚠️ No Test**: "FR-003, FR-007 đã implement nhưng thiếu test.
  Cần bổ sung test trước review."
- **If all good**: "🎉 Tất cả Business Rules compliant và Functional Requirements
  đã covered. Sẵn sàng cho review/security gate."

## Output
This skill does NOT create any files. It only displays the dashboard and
recommendations in chat. The data source is always the latest state of the
existing documents — it's always fresh.

## Interaction Rules
- Keep the dashboard concise — focus on status, not re-listing requirement details.
- Use color-coded status icons consistently.
- If the user asks to drill into a specific FR or BR, show the detail from the
  source document (PRD or BRD) and the implementation evidence.
- If asked "what should I work on next?", prioritize: ❌ Violated BRs first,
  then ❌ Not Planned FRs, then ⚠️ No Test FRs.
