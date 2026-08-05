---
name: sdd-review-code
description: Use when all tasks in docs/sdd/<feature>/plan.md are marked complete and the user wants a final correctness/quality check before the security gate. Verifies tests actually pass, checks for bugs, logic errors, and flow issues across the whole change, cross-checks against plan.md and docs/sdd/constitution.md, and performs Business Rule compliance and Functional Requirement coverage analysis against docs/sdd/BRD.md and docs/sdd/PRD.md (if they exist). This is step 5 of 6 in the SDD-Hybrid workflow — a full verification pass, not a quick glance at the diff. Handles correctness only; security is sdd-security-review's job (step 6), which runs next, before anything is pushed to CI/CD.
---

# SDD Review Code (step 5 of 6)

## Purpose
Prove the feature actually works, actually matches the plan, actually respects
the constitution, and actually implements the required business rules and functional
requirements — before it moves on to the security gate. This is *not* the last
checkpoint before CI/CD; `sdd-security-review` runs after this one and has the
final say on whether the branch is safe to push.

## Process
1. **Run everything for real.** Full test suite, linter, build/typecheck. Don't
   infer results from reading code — execute and read the actual output.
2. **Diff vs plan.md** — for each task, does the resulting code do what the task
   said? Flag scope drift (unplanned extra changes) and any missed acceptance
   criteria.
3. **Diff vs constitution.md** — walk every principle again against the *final*
   code, not just what was checked mid-build. Small drifts across several tasks can
   add up even if each task individually passed its own check.
4. **Business Rule Compliance Check** (only when `docs/sdd/BRD.md` exists):
   - Read BRD.md Section 5 (Business Rules).
   - For each BR-xxx: verify the final code correctly implements the rule.
   - Categorize each: ✅ Compliant / ❌ Violated / ⚠️ Partially implemented / N/A.
   - A BR ❌ Violated is a **Critical** finding — blocks merge.
   - If BRD.md doesn't exist, skip this step entirely.
5. **Functional Requirement Coverage Analysis** (only when `docs/sdd/PRD.md` exists):
   - Read PRD.md Section 2 (Functional Requirements).
   - For each FR-xxx relevant to this feature: check if code + test exist.
   - Categorize each:
     ✅ Implemented & Tested /
     ⚠️ Implemented, No Test /
     ❌ Missing (not implemented) /
     🔲 Out of scope for this feature.
   - An FR ❌ Missing that was mapped to a task in plan.md is a **Critical** finding.
   - An FR ⚠️ Implemented, No Test is an **Important** finding.
   - If PRD.md doesn't exist, skip this step entirely.
6. **Systematic code read** — beyond style, look specifically for:
   - Logic errors, off-by-one mistakes, wrong conditionals.
   - Unhandled edge cases (empty input, nulls, concurrency, error paths).
   - Broken or missing error handling.
   - Dead code, leftover debug statements, TODOs that should actually block.
   - Anything that silently swallows a failure instead of surfacing it.
7. **Categorize every finding**: Critical (blocks completion) / Important (should
   fix before merge) / Minor / Nit. A Critical finding is a hard stop.
8. If Critical or Important issues are found, send the specific task(s) back to
   `sdd-build` to fix, then re-run this review. Never approve with known Critical
   issues "to fix later."
9. If clean, summarize the review. **Do not offer to push, open a PR, or trigger
   CI/CD yet** — hand off to `sdd-security-review` first.

## Output
Write a report to: `docs/sdd/<feature-slug>/review-report.md`

The report must include standard findings, plus (when BRD/PRD exist):

```markdown
# Code Review: <Feature Name>

Source: plan.md, constitution.md, BRD.md (if exists), PRD.md (if exists)

## Code Quality Findings
| # | Severity | File/Location | Description | Status |
|---|----------|---------------|-------------|--------|

## Business Rule Compliance
| Rule ID | Description | Status | Evidence |
|---------|-------------|--------|----------|
| BR-001  | ...         | ✅ Compliant | file.ts:L45 validates |
| BR-002  | ...         | ❌ Violated  | No validation found |

## Functional Requirement Coverage
| FR ID | Title | Implementation | Test | Status |
|-------|-------|----------------|------|--------|
| FR-001 | ...  | file.ts        | file.spec.ts | ✅ Complete |
| FR-002 | ...  | file.ts        | ❌ Missing   | ⚠️ Needs test |

## Coverage Summary
- Business Rules: X/Y compliant (Z%)
- Functional Requirements: X/Y implemented (Z%), X/Y tested (Z%)
- ⚠️ Gaps: <list or "None">

## Verdict
- [ ] Blocked — Critical/Important findings
- [ ] Passed — ready for security review
```

If BRD/PRD don't exist, omit the Business Rule Compliance, Functional Requirement
Coverage, and Coverage Summary sections — just report standard code quality findings.

## Non-negotiables
- Never report "all good" without having actually run the tests in this pass.
- Never silently downgrade a Critical finding just to reach "done" faster.
- Never present merge/PR/push options directly from this skill — that decision
  belongs after `sdd-security-review` clears the branch.

## Handoff
When the review is clean, say:

> "Code review sạch. Bước tiếp theo là **sdd-security-review** (kiểm tra OWASP
> Top 10) trước khi push lên CI/CD."
