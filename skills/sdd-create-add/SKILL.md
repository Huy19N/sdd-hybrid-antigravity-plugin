---
name: sdd-create-add
description: "Use when docs/sdd/BRD.md, docs/sdd/PRD.md, and docs/sdd/ES.md all exist and are approved, and the user wants to create an Architecture Design Document. Synthesizes all previous documents into technology stack decisions, domain entity definitions, architecture component design, interface contracts, and ADR-style architecture decisions. This is step 4 (final) in the BA/SA document chain: BRD → PRD → ES → ADD. Do not use before BRD, PRD, and ES exist — redirect to the missing step first."
---

# SDD Create ADD (Architecture Design Document)

## Purpose
Synthesize all upstream documents (BRD, PRD, ES) into a comprehensive Architecture
Design Document (ADD). This document makes **binding technology and design decisions**
that guide all implementation work. It serves as the architectural blueprint that
the `sdd-constitution` and `sdd-plan` steps will reference.

## When NOT to use
- Any of `docs/sdd/BRD.md`, `docs/sdd/PRD.md`, `docs/sdd/ES.md` is missing →
  redirect to the missing step.
- A `docs/sdd/ADD.md` already exists → read and amend it.

## Preconditions — check before starting
- `docs/sdd/BRD.md` exists and is approved.
- `docs/sdd/PRD.md` exists and is approved.
- `docs/sdd/ES.md` exists and is approved.

If any is missing, stop and redirect:
> "Chưa đủ tài liệu. Cần có BRD → PRD → ES trước khi tạo ADD.
> Thiếu: **[tên tài liệu]**. Hãy chạy **[skill tương ứng]** trước."

## Process

### Step 1: Read and Synthesize All Documents
Read all three documents in full. Extract and cross-reference:
- From **BRD**: Constraints (technical, legal, budget), assumptions, risks
- From **PRD**: Business capabilities, functional requirements, NFRs
- From **ES**: Domain events, aggregates, policies, bounded contexts, hotspots

Present a brief architecture-relevant summary and confirm understanding.

### Step 2: Technology Stack
Questions to ask:
1. "Có **ràng buộc tech stack** nào từ tổ chức? (ngôn ngữ, framework, cloud provider…)"
2. "Team hiện tại có **kinh nghiệm** với tech stack nào?"
3. "Có yêu cầu **licensing** nào? (open-source only, enterprise licenses available…)"
4. "**Database**: relational, NoSQL, hay hybrid? Lý do?"
5. "**Hosting**: on-premise, cloud (AWS/Azure/GCP), hay hybrid?"
6. "Có yêu cầu **CI/CD** cụ thể không?"

For each technology decision, capture:
- **Category**: Language, Framework, Database, Infrastructure, CI/CD, Monitoring, etc.
- **Selected**: The chosen technology
- **Version**: Pinned version (if applicable)
- **Alternatives Considered**: What else was evaluated
- **Rationale**: Why this was chosen over alternatives
- **BRD/PRD Ref**: Which constraint or requirement drives this decision

### Step 3: Domain Entities
Derive from ES aggregates and PRD functional requirements:

1. "Dựa trên Event Storming, tôi xác định các **domain entity** chính: [list]. Đúng không?"
2. "Mỗi entity có những **attribute** và **relationship** nào?"
3. "**Lifecycle** của entity này ra sao? (created → active → archived → deleted)"

For each entity, capture:
- **Name**: Entity name
- **Responsibility**: What this entity represents and manages
- **Key Attributes**: Core data fields (not exhaustive — focus on domain-significant ones)
- **Relationships**: How it connects to other entities (1:1, 1:N, M:N)
- **Lifecycle States**: State transitions
- **ES Aggregate Ref**: Which aggregate this maps to

### Step 4: Architecture Components
Design the system's deployable or logical components:

1. "Hệ thống nên chia thành **bao nhiêu services/modules**?"
2. "Mỗi component **trách nhiệm** chính là gì?"
3. "Component nào **giao tiếp** với component nào? Qua protocol nào?"
4. "Có **cross-cutting concerns** nào? (logging, auth, caching, rate limiting…)"

For each component, capture:
- **ID**: COMP-001, COMP-002, ...
- **Name**: Component name
- **Type**: Service / Module / Library / Infrastructure
- **Responsibility**: What it does
- **Interfaces Exposed**: APIs or events it produces
- **Dependencies**: Other components it consumes
- **Constraints**: Performance, scaling, security requirements
- **ES Mapping**: Which aggregates/bounded contexts this implements

### Step 5: Interface Contracts
Define the contracts between components:

1. "Giữa component [A] và [B], **dữ liệu** nào được trao đổi?"
2. "**Format** dữ liệu? (JSON, Protobuf, GraphQL, events…)"
3. "Xử lý **lỗi** thế nào? (retry, circuit breaker, dead letter…)"
4. "Có yêu cầu **backward compatibility** không?"

For each contract, capture:
- **ID**: IC-001, IC-002, ...
- **Provider**: Component that exposes the interface
- **Consumer(s)**: Component(s) that consume it
- **Protocol**: REST / gRPC / GraphQL / Event / Message Queue
- **Data Exchanged**: Key fields and types
- **Error Cases**: Expected errors and handling
- **Compatibility Notes**: Versioning strategy, breaking change policy

### Step 6: Architecture Decisions (ADR Format)
Document key architectural decisions in ADR (Architecture Decision Record) format:

1. "Những **quyết định kiến trúc quan trọng** nào chúng ta vừa đưa ra?"
2. "Cho mỗi quyết định, **bối cảnh** (context) dẫn đến quyết định là gì?"
3. "Có **options** nào khác đã xem xét?"
4. "**Hậu quả** (consequences) của quyết định này?"

For each ADR, capture:
- **ID**: ADR-001, ADR-002, ...
- **Title**: Decision title
- **Status**: Proposed / Accepted / Deprecated / Superseded
- **Context**: What situation or requirement drives this decision
- **Options Considered**: Alternatives and their trade-offs
- **Decision**: What was decided
- **Rationale**: Why this option was chosen
- **Consequences**: Positive and negative effects
- **ES Reference**: Which ES hotspot, aggregate, or policy this addresses

## Interaction Rules
- Present each section one at a time for review.
- Architecture decisions must be **justified**, not just stated.
- Every component must trace back to at least one ES aggregate or PRD capability.
- Flag any **architectural risks** discovered during this process.
- If a decision conflicts with BRD constraints, stop and surface the conflict.

## Output
Write to: `docs/sdd/ADD.md`

```markdown
# Architecture Design Document (ADD)

Version: <semver> | Created: <date> | Last updated: <date>
Source: BRD.md (v<ver>), PRD.md (v<ver>), ES.md (v<ver>)

---

## 1. Technology Stack

| Category | Selected | Version | Alternatives Considered | Rationale | Ref |
|----------|----------|---------|-------------------------|-----------|-----|
| Language | ... | ... | ... | ... | BRD Constraint #x |
| Framework | ... | ... | ... | ... | PRD NFR-xxx |
| Database | ... | ... | ... | ... | ... |
| Infrastructure | ... | ... | ... | ... | ... |
| CI/CD | ... | ... | ... | ... | ... |
| Monitoring | ... | ... | ... | ... | ... |

---

## 2. Domain Entities

### <Entity Name>

| Attribute | Detail |
|-----------|--------|
| **Responsibility** | ... |
| **Key Attributes** | attr1 (type), attr2 (type), ... |
| **Relationships** | Entity A (1:N), Entity B (M:N) |
| **Lifecycle** | Created → Active → Archived → Deleted |
| **ES Aggregate Ref** | AGG-xxx |

---

## 3. Architecture Components

| ID | Component | Type | Responsibility | Interfaces | Dependencies | Constraints | ES Mapping |
|----|-----------|------|----------------|------------|--------------|-------------|------------|
| COMP-001 | ... | Service | ... | REST API | COMP-002 | ... | AGG-001 |

### Component Diagram

​```mermaid
graph TB
    subgraph "Frontend"
        WEB["Web App"]
        MOB["Mobile App"]
    end

    subgraph "Backend Services"
        API["API Gateway"]
        SVC1["Service A"]
        SVC2["Service B"]
    end

    subgraph "Data Layer"
        DB["Database"]
        CACHE["Cache"]
        MQ["Message Queue"]
    end

    WEB --> API
    MOB --> API
    API --> SVC1
    API --> SVC2
    SVC1 --> DB
    SVC1 --> CACHE
    SVC1 --> MQ
    SVC2 --> DB
    MQ --> SVC2
​```

---

## 4. Interface Contracts

| ID | Provider | Consumer(s) | Protocol | Data Exchanged | Error Cases | Compatibility |
|----|----------|-------------|----------|----------------|-------------|---------------|
| IC-001 | COMP-001 | COMP-002 | REST | OrderDTO: {id, items, total} | 400, 404, 500 + retry 3x | Semantic versioning |

---

## 5. Architecture Decisions

### ADR-001: <Decision Title>

| Attribute | Detail |
|-----------|--------|
| **Status** | Accepted |
| **Context** | ... |
| **Options** | 1. ... (pros/cons) 2. ... (pros/cons) |
| **Decision** | Option 1 |
| **Rationale** | ... |
| **Consequences** | + ... / - ... |
| **ES Reference** | Hotspot at DE-xxx, AGG-xxx |

---

## Cross-Reference Matrix

| ES Item | Domain Entity | Component | Interface | ADR |
|---------|---------------|-----------|-----------|-----|
| AGG-001 | Order | COMP-001 | IC-001 | ADR-001 |
```

## Handoff
Once the user confirms the ADD is complete, say:

> "Architecture Design Document đã hoàn thành. Chuỗi tài liệu BA/SA đã đầy đủ:
> BRD ✅ → PRD ✅ → ES ✅ → ADD ✅.
>
> Bây giờ có thể bắt đầu workflow phát triển cho từng feature:
> **sdd-brainstorm** → **sdd-constitution** → **sdd-plan** → **sdd-build** → **sdd-review-code** → **sdd-security-review**.
>
> Gõ `sdd-help` bất kỳ lúc nào để xem hướng dẫn chi tiết."

Do not auto-proceed — wait for the user to choose which feature to brainstorm first.
