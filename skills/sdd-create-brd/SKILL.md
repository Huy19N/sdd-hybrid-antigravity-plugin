---
name: sdd-create-brd
description: "Use when the user wants to start a new project and no docs/sdd/BRD.md exists yet, or when they say 'tạo BRD', 'business requirements', 'phân tích yêu cầu kinh doanh', or 'bắt đầu dự án mới'. Guides the user through structured Socratic questioning across 6 sections (Problem Statement, Vision & Objectives, Stakeholder Register, Scope & Capabilities, Business Rules, Constraints/Assumptions/Risks) to produce a comprehensive Business Requirements Document. This is the first step in the BA/SA document chain: BRD → PRD → ES → ADD, which feeds into the existing 6-step SDD-Hybrid workflow."
---

# SDD Create BRD (Business Requirements Document)

## Purpose
Guide the user through a structured discovery process to produce a comprehensive
Business Requirements Document (BRD). This document captures the **business context,
stakeholders, scope, rules, and constraints** before any product or technical design
begins. The BRD is the foundation for all downstream documents (PRD, ES, ADD).

## When NOT to use
- A `docs/sdd/BRD.md` for this project already exists → read and amend it, don't
  start from scratch.
- The user already has a fully-specified BRD from another source → import and
  validate it instead.
- The user wants to jump straight to feature-level work → point them to
  `sdd-brainstorm` for per-feature exploration, but recommend BRD first for
  new projects.

## Process

### Phase 0: Check existing state
- Does `docs/sdd/BRD.md` already exist?
  - **Yes** → Read it, show summary, ask if this is an amendment or restart.
  - **No** → Proceed with full creation below.

### Phase 1: Problem Statement
Ask one topic at a time. Do not dump all questions at once.

Questions to cover:
1. "Hệ thống này giải quyết **vấn đề kinh doanh** cụ thể nào?"
2. "Hiện tại, vấn đề này đang được xử lý bằng cách nào? (manual, Excel, hệ thống cũ…)"
3. "Điều gì khiến cách làm hiện tại **không còn đáp ứng** được?"
4. "Nếu không xây dựng hệ thống này, **hậu quả kinh doanh** sẽ là gì trong 6-12 tháng?"
5. "**Ai** bị ảnh hưởng trực tiếp bởi vấn đề này? Tần suất gặp phải?"

From the answers, synthesize:
- **Affected Audience**: Who suffers from the problem
- **Obstacle**: What blocks them
- **Root Cause**: Why the obstacle exists
- **Frequency**: How often it occurs
- **Impact**: Business cost (time, money, risk, reputation)

### Phase 2: Vision and Objectives
Questions to cover:
1. "Hệ thống này nằm trong **chiến lược dài hạn** nào của tổ chức?"
2. "Hãy mô tả **trạng thái lý tưởng** sau khi hệ thống đi vào hoạt động?"
3. "Có **hệ thống tương tự** nào trên thị trường mà anh/chị tham khảo chưa?"
4. "**Ngân sách** và **timeline** dự kiến?"
5. "Làm sao chúng ta **đo lường** thành công? KPI nào?"

From the answers, synthesize:
- **Product Vision**: One sentence describing the desired future state
- **Measurable Objectives**: 3-5 SMART objectives
- **Success Metrics**: Specific KPIs with targets and timeframes

### Phase 3: Stakeholder Register
Questions to cover:
1. "Ai là **sponsor** (người tài trợ) và **decision maker** cuối cùng?"
2. "Hệ thống phục vụ **những nhóm người dùng** nào?"
3. "Ai sẽ **quản trị** hệ thống hàng ngày?"
4. "Bộ phận/phòng ban nào **bị ảnh hưởng** bởi hệ thống mới?"
5. "Có **khách hàng bên ngoài** hoặc **đối tác** nào tương tác với hệ thống?"

From the answers, build a stakeholder table with:
- Name/Role, Category (User/Stakeholder/Decision-maker/Operator),
  Responsibilities, Key Concerns

### Phase 4: Scope and Capabilities
Questions to cover:
1. "Hãy liệt kê **5 tính năng quan trọng nhất** theo thứ tự ưu tiên?"
2. "Những gì **KHÔNG NẰM TRONG** phạm vi dự án này?"
3. "Có phụ thuộc nào với dự án hoặc hệ thống khác?"
4. "Hệ thống cần tích hợp với những hệ thống nào?"

From the answers, build:
- **In-Scope Capabilities**: Capability, Priority (MoSCoW), Rationale, Dependencies
- **Out-of-Scope**: Capability, Rationale for exclusion, Planned phase (if any)

### Phase 5: Business Rules
Questions to cover:
1. "Có những **quy tắc nghiệp vụ** nào hệ thống phải tuân theo?"
2. "Có quy trình **phê duyệt** nào cần được tự động hóa?"
3. "Khi xảy ra **ngoại lệ**, hệ thống nên xử lý thế nào?"
4. "Có **quy định pháp lý** nào ảnh hưởng đến logic nghiệp vụ?"

Each rule must be:
- **Testable**: Can be verified as true/false
- **Structured**: ID, Description, Condition/Trigger, Expected Outcome, Scope, Exceptions

### Phase 6: Constraints, Assumptions and Risks
Questions to cover:
1. "Có **ràng buộc kỹ thuật** nào bắt buộc? (tech stack, platform, compliance…)"
2. "Có **ràng buộc pháp lý** nào? (GDPR, NĐ 13/2023, PCI-DSS…)"
3. "Những **giả định** nào chúng ta đang đặt ra cần được xác nhận?"
4. "Có **rủi ro** nào anh/chị thấy trước cho dự án này?"
5. "Kế hoạch **giảm thiểu** rủi ro?"

Capture:
- **Hard Constraints**: Constraint, Type (Technical/Legal/Budget/Time), Impact
- **Assumptions to Validate**: Assumption, Validation Method, Owner, Deadline
- **Dependencies**: Dependency, Owner, Expected Date, Fallback
- **Risks**: Risk, Probability (H/M/L), Impact (H/M/L), Mitigation, Owner

## Interaction Rules
- Ask about **one section at a time** — never dump all questions at once.
- Present each completed section for review before moving to the next.
- Use the user's **own words** in the document — do not over-formalize their language.
- If the user's answer is vague, apply the **5 Whys technique** to dig deeper.
- Reference specific examples or industry context to prompt deeper thinking.
- Mark any gaps or unresolved items explicitly as `[TBD]` with a note on who owns resolution.

## Output
Write to: `docs/sdd/BRD.md`

```markdown
# Business Requirements Document (BRD)

Version: <semver> | Created: <date> | Last updated: <date>
Project: <project name>

---

## 1. Problem Statement

### Affected Audience
<who suffers from this problem>

### Obstacle
<what blocks them>

### Root Cause
<why the obstacle exists>

### Frequency
<how often it occurs — daily/weekly/per-transaction>

### Impact
| Impact Type | Description | Estimated Cost |
|-------------|-------------|----------------|
| Financial   | ...         | ...            |
| Time        | ...         | ...            |
| Risk        | ...         | ...            |
| Reputation  | ...         | ...            |

---

## 2. Vision and Objectives

### Product Vision
> <One sentence describing the desired future state>

### Measurable Objectives
| # | Objective | Success Metric | Target | Timeframe |
|---|-----------|----------------|--------|-----------|
| 1 | ...       | ...            | ...    | ...       |

---

## 3. Stakeholder Register

| Name / Role | Category | Responsibilities | Key Concerns |
|-------------|----------|------------------|--------------|
| ...         | Decision-maker | ...        | ...          |
| ...         | User     | ...              | ...          |
| ...         | Operator | ...              | ...          |

---

## 4. Scope and Capabilities

### In-Scope
| # | Capability | Priority | Rationale | Dependencies |
|---|------------|----------|-----------|--------------|
| 1 | ...        | Must     | ...       | ...          |

### Out-of-Scope
| # | Capability | Rationale | Planned Phase |
|---|------------|-----------|---------------|
| 1 | ...        | ...       | Phase 2       |

---

## 5. Business Rules

| Rule ID | Description | Condition / Trigger | Expected Outcome | Scope | Exceptions |
|---------|-------------|---------------------|-------------------|-------|------------|
| BR-001  | ...         | ...                 | ...               | ...   | ...        |

---

## 6. Constraints, Assumptions and Risks

### Hard Constraints
| # | Constraint | Type | Impact |
|---|------------|------|--------|
| 1 | ...        | Technical | ... |

### Assumptions to Validate
| # | Assumption | Validation Method | Owner | Deadline |
|---|------------|-------------------|-------|----------|
| 1 | ...        | ...               | ...   | ...      |

### Dependencies
| # | Dependency | Owner | Expected Date | Fallback |
|---|------------|-------|---------------|----------|
| 1 | ...        | ...   | ...           | ...      |

### Risks
| # | Risk | Probability | Impact | Mitigation | Owner |
|---|------|-------------|--------|------------|-------|
| 1 | ...  | H/M/L       | H/M/L  | ...        | ...   |
```

## Handoff
Once the user confirms the BRD is complete and accurate, say:

> "BRD đã hoàn thành. Bước tiếp theo là **sdd-create-prd** để chuyển yêu cầu kinh doanh
> thành yêu cầu sản phẩm chi tiết (Product Requirements Document)."

Do not auto-proceed to PRD — wait for the user to say go.
