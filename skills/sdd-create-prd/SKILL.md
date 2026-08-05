---
name: sdd-create-prd
description: "Use when docs/sdd/BRD.md exists and is approved, and the user wants to create a Product Requirements Document. Transforms business requirements into testable product behaviors organized by Business Capabilities, Functional Requirements (with Gherkin acceptance criteria), and Non-Functional Requirements. This is step 2 in the BA/SA document chain: BRD → PRD → ES → ADD. Do not use before BRD exists — redirect to sdd-create-brd first."
---

# SDD Create PRD (Product Requirements Document)

## Purpose
Transform approved business requirements (BRD) into a detailed, testable Product
Requirements Document (PRD). While the BRD describes **what the business needs**,
the PRD describes **what the product must do** — specific, measurable behaviors
that can be verified by QA and implemented by developers.

## When NOT to use
- `docs/sdd/BRD.md` does not exist → redirect to `sdd-create-brd`.
- A `docs/sdd/PRD.md` already exists → read and amend it.
- The user only wants feature-level work → point to `sdd-brainstorm`.

## Preconditions — check before starting
- `docs/sdd/BRD.md` exists and was confirmed by the user. If not, stop and say:
  > "Chưa có BRD. Hãy chạy **sdd-create-brd** trước để tạo Business Requirements Document."

## Process

### Step 1: Read and Internalize BRD
Read `docs/sdd/BRD.md` in full. Extract:
- In-scope capabilities (Section 4)
- Business rules (Section 5)
- Constraints and assumptions (Section 6)
- Stakeholder concerns (Section 3)

Summarize your understanding to the user and confirm before proceeding.

### Step 2: Business Capabilities
Group the BRD's in-scope capabilities into **business capability domains** — these
are high-level domain boundaries or major business flows.

Questions to ask:
1. "Dựa trên BRD, tôi nhóm các tính năng thành [X] domain chính: [list]. Đúng không?"
2. "Có business flow nào tôi bỏ sót không?"
3. "Thứ tự ưu tiên giữa các domain?"

For each capability, define:
- **ID**: BC-001, BC-002, ...
- **Name**: Business capability name
- **Description**: What this domain covers
- **Key Flows**: Major business processes within this domain
- **BRD Traceability**: Which BRD scope items map here

### Step 3: Functional Requirements
For each Business Capability, derive specific functional requirements.

Questions to ask (per capability domain):
1. "Trong domain [X], hệ thống cần thực hiện cụ thể những hành vi nào?"
2. "Input và output mong muốn cho mỗi hành vi?"
3. "Khi xảy ra lỗi hoặc ngoại lệ, hệ thống phản ứng thế nào?"
4. "Có cần notification/reporting gì không?"

Each functional requirement must have:
- **ID**: FR-001, FR-002, ...
- **Title**: Short descriptive name
- **Description**: Detailed behavior description
- **Inputs**: What data/actions trigger this behavior
- **Outputs / Observable Results**: What the user sees or system produces
- **Acceptance Signal**: How to verify this works (Gherkin format)
- **Priority**: Must / Should / Could / Won't (MoSCoW)
- **Dependencies**: Other FRs or BCs this depends on
- **BRD Traceability**: Which BRD items this fulfills

Write acceptance criteria in **Gherkin format**:
```gherkin
Scenario: <descriptive name>
  Given <precondition>
  When  <action>
  Then  <expected result>
```

### Step 4: Non-Functional Requirements
Derive NFRs from BRD constraints and stakeholder concerns.

Questions to ask:
1. "Về **hiệu năng**: bao nhiêu người dùng đồng thời? Thời gian phản hồi tối đa?"
2. "Về **bảo mật**: xác thực thế nào? Dữ liệu nhạy cảm nào cần mã hóa?"
3. "Về **khả dụng**: uptime SLA? Backup/recovery?"
4. "Về **khả năng mở rộng**: dự kiến tăng trưởng 3-5 năm?"
5. "Về **khả năng sử dụng**: training time? Accessibility?"
6. "Về **tuân thủ**: quy định nào áp dụng?"

Each NFR must have:
- **ID**: NFR-001, NFR-002, ...
- **Category**: Performance / Security / Availability / Scalability / Usability / Compliance
- **Attribute**: Specific quality attribute
- **Measure**: How to measure it
- **Target**: Quantitative target value
- **Constraint**: Hard limit (if any)
- **Verification Method**: How to test/verify this NFR
- **BRD Traceability**: Which BRD constraint/assumption this addresses

## Interaction Rules
- Present each section (Business Capabilities → Functional Requirements → NFRs)
  **one at a time** for user review.
- Every functional requirement MUST have at least one Gherkin acceptance criterion.
- Cross-reference every PRD item back to BRD items — no orphan requirements.
- If a BRD item cannot be mapped to a PRD requirement, flag it explicitly.
- Mark unresolved items as `[TBD]`.

## Output
Write to: `docs/sdd/PRD.md`

```markdown
# Product Requirements Document (PRD)

Version: <semver> | Created: <date> | Last updated: <date>
Source: BRD.md (v<version>)

---

## 1. Business Capabilities

| ID | Capability | Description | Key Flows | BRD Ref |
|----|------------|-------------|-----------|---------|
| BC-001 | ... | ... | ... | Scope #1, #2 |

---

## 2. Functional Requirements

### BC-001: <Capability Name>

#### FR-001: <Requirement Title>

| Attribute | Detail |
|-----------|--------|
| **Description** | ... |
| **Inputs** | ... |
| **Outputs** | ... |
| **Priority** | Must / Should / Could |
| **Dependencies** | FR-xxx, BC-xxx |
| **BRD Ref** | Scope #x, BR-xxx |

**Acceptance Criteria:**

​```gherkin
Scenario: <happy path>
  Given <precondition>
  When  <action>
  Then  <expected result>

Scenario: <error case>
  Given <precondition>
  When  <invalid action>
  Then  <error handling>
​```

#### FR-002: <Next Requirement>
...

---

## 3. Non-Functional Requirements

| ID | Category | Attribute | Measure | Target | Constraint | Verification | BRD Ref |
|----|----------|-----------|---------|--------|------------|--------------|---------|
| NFR-001 | Performance | Response Time | P95 latency | ≤ 2s | - | Load test | Constraint #x |
| NFR-002 | Security | Authentication | Auth method | MFA | - | Pen test | Constraint #x |

---

## Traceability Matrix

| BRD Item | PRD Item(s) | Status |
|----------|-------------|--------|
| Scope #1 | BC-001, FR-001, FR-002 | ✅ Covered |
| BR-001   | FR-003 | ✅ Covered |
| Constraint #1 | NFR-001 | ✅ Covered |
```

## Handoff
Once the user confirms the PRD is complete, say:

> "PRD đã hoàn thành. Bước tiếp theo là **sdd-create-es** để phân tích domain events
> và xây dựng Event Storming Canvas."

Do not auto-proceed — wait for the user to say go.
