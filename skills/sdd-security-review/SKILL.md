---
name: sdd-security-review
description: Use when docs/sdd/<feature>/plan.md tasks are complete and sdd-review-code has already passed, and before the user pushes the branch, opens a PR, or triggers CI/CD. Runs a structured OWASP Top 10:2025 security check against the changed code plus the project's Security requirements section in docs/sdd/constitution.md. This is step 6 of 6 in the SDD-Hybrid workflow — a hard gate: code must pass this before it goes to CI/CD. Do not use this for general code-quality/logic review — that's sdd-review-code's job; this skill only covers security.
---

# SDD Security Review (step 6 of 6)

## Purpose
Final security gate before code leaves the local branch. Checks the change against
the OWASP Top 10:2025 categories and against any project-specific "Security
requirements" already defined in `constitution.md`. This step exists so code only
reaches CI/CD after a deliberate security pass, not as an afterthought caught later
in a pipeline scan (or not caught at all).

## Preconditions
- `sdd-review-code` has already run and reported no Critical/Important issues.
- All tasks in `docs/sdd/<feature-slug>/plan.md` are checked off.

If review-code hasn't run yet, run that first. This skill assumes the code is
already functionally correct and checks a different dimension (security) — it
does not re-litigate logic bugs that belong to `sdd-review-code`.

## Process
1. Read `docs/sdd/constitution.md` and pull out anything already stated under
   "Security requirements" (auth model, secrets handling, allowed dependencies,
   compliance constraints). Those are binding and project-specific; OWASP below is
   the general-purpose checklist on top of them.
2. Get the actual diff for this feature — everything since the branch/worktree was
   created, not just files that "look" security-relevant. Injection and
   access-control bugs commonly hide in ordinary CRUD/API code.
3. Walk every one of the 10 categories below against the diff. For each: state
   whether it applies, and if so whether the code passes or fails, with the
   specific file/line as evidence. Don't mark a category N/A without actually
   checking — most categories touch more code paths than expected.

   | # | Category (OWASP Top 10:2025 - Web / Backend) | Look for |
   |---|---|---|
   | A01 | Broken Access Control (now includes SSRF) | Missing authorization checks, IDOR (object reference not scoped to the requesting user), server-side calls to attacker-influenced URLs |
   | A02 | Security Misconfiguration | Default credentials, verbose error/debug output on prod paths, overly permissive CORS/headers, unnecessary features left enabled |
   | A03 | Software Supply Chain Failures | New/updated dependencies from untrusted sources, unpinned versions, no integrity check, CI/CD pipeline changes that widen trust |
   | A04 | Cryptographic Failures | Sensitive data stored/transmitted unencrypted, weak or custom crypto, hardcoded keys/secrets in code |
   | A05 | Injection | Unsanitized input reaching SQL/NoSQL/OS commands/templates, string-concatenated queries |
   | A06 | Insecure Design | Missing threat modeling for a new trust boundary, business logic that can be abused (e.g. no rate limit on a sensitive action) |
   | A07 | Authentication Failures | Weak session handling, missing MFA where the constitution requires it, predictable tokens, no lockout/backoff |
   | A08 | Software or Data Integrity Failures | Unsigned/unverified deserialization, auto-update or CI steps trusting unverified artifacts |
   | A09 | Security Logging & Alerting Failures | Security-relevant events not logged, logs containing secrets/PII, no alerting hook for events that matter |
   | A10 | Mishandling of Exceptional Conditions | Errors failing open instead of closed, stack traces or internal state leaked to the client, unhandled edge cases that crash into an insecure state |

   **Nếu là dự án Mobile App (React Native / Flutter / Kotlin), kiểm tra thêm OWASP Mobile Top 10**:
   | # | Mobile Category | Look for |
   |---|---|---|
   | M1 | Insecure Credential & Data Storage | Auth tokens / PII lưu trong plain `AsyncStorage` / `SharedPreferences` thay vì `SecureStore` (Keychain/Keystore) |
   | M2 | Insecure Communication | Gọi API HTTP không mã hóa, thiếu Certificate Pinning cho giao dịch tài chính nhạy cảm |
   | M3 | Insecure Authentication/Authorization | Xác thực sinh trắc học FaceID/Biometrics không có fallback an toàn hoặc xử lý client-side giả mạo |
   | M4 | Insufficient Input/Output Validation | Deep links (URL schemes) không validate param, nguy cơ injection qua WebView / Intents |
   | M5 | Insecure Code & Reverse Engineering | Thiếu obfuscation (ProGuard / R8 / Flutter obfuscate), lộ API key nhạy cảm trong client bundle |
   | M8 | Security Misconfiguration | Quyền AndroidManifest.xml / iOS Info.plist quá rộng, `android:exported="true"` không an toàn |

4. **Categorize every finding**: Critical (exploitable now, blocks push) / High
   (fix before merge) / Medium (track, fix soon) / Low (note for later).
5. If any Critical or High finding exists, **do not let the branch go to CI/CD.**
   Send the specific file/task back to `sdd-build` to fix, then re-run this review
   on the fix.
6. If clean — or only Medium/Low remain and the user explicitly accepts them —
   this is the true finish line. Present the options: merge to main / open a PR /
   push the branch (triggers CI/CD) / keep as-is / discard. Clean up the
   worktree/branch per the user's choice.

## Output
Write to: `docs/sdd/<feature-slug>/security-report.md`

```markdown
# Security Review: <Feature Name>

Reviewed against: OWASP Top 10:2025 + constitution.md Security requirements

## Findings
| Category | Severity | File/Location | Description | Status |
|---|---|---|---|---|

## Verdict
- [ ] Blocked — Critical/High findings open
- [ ] Cleared for CI/CD — <date>, reviewed by <who/what>
```

## Non-negotiables
- A Critical or High finding is a hard stop — never wave it through "CI/CD will
  catch it," that defeats the point of this gate existing.
- Don't mark a category N/A without evidence you actually checked it against the
  diff.
- If the user overrides a blocked verdict, record that explicitly in the report
  (who approved the override and why) rather than silently changing the status.

## Handoff
On a clean verdict, say:

> "Security review pass. An toàn để push lên CI/CD."

On a blocked verdict, state clearly which findings are blocking and send back to
`sdd-build`.
