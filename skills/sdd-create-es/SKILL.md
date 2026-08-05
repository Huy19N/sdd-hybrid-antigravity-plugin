---
name: sdd-create-es
description: "Use when docs/sdd/BRD.md and docs/sdd/PRD.md both exist and are approved, and the user wants to create an Event Storming Canvas. Analyzes the BRD and PRD to discover Domain Events, Actors & Commands, Policies, and Aggregates using an interactive workshop-style approach. This is step 3 in the BA/SA document chain: BRD → PRD → ES → ADD. Do not use before BRD and PRD exist — redirect to the missing step first."
---

# SDD Create ES (Event Storming Canvas)

## Purpose
Conduct a structured Event Storming workshop to discover the system's domain model
by mapping **events, commands, actors, policies, and aggregates**. This document
bridges the gap between product requirements (PRD) and architecture design (ADD)
by revealing the true domain complexity, bounded contexts, and integration points.

## When NOT to use
- `docs/sdd/BRD.md` does not exist → redirect to `sdd-create-brd`.
- `docs/sdd/PRD.md` does not exist → redirect to `sdd-create-prd`.
- A `docs/sdd/ES.md` already exists → read and amend it.

## Preconditions — check before starting
- `docs/sdd/BRD.md` exists. If not, stop and redirect.
- `docs/sdd/PRD.md` exists. If not, stop and redirect.
- Both documents have been confirmed/approved by the user.

## Process

### Step 1: Read and Prepare
Read both `docs/sdd/BRD.md` and `docs/sdd/PRD.md` in full. Extract:
- Business Capabilities (PRD Section 1) → these become **business flows**
- Functional Requirements (PRD Section 2) → these hint at **commands and events**
- Business Rules (BRD Section 5) → these become **policies**
- Stakeholder Register (BRD Section 3) → these become **actors**

Present a brief summary of what you've extracted and confirm with the user.

### Step 2: Domain Events
Walk through each Business Capability and ask:

1. "Trong flow [X], những **sự kiện quan trọng** nào xảy ra? (dùng thì quá khứ:
   'Đơn hàng đã được tạo', 'Thanh toán đã thành công'...)"
2. "Sự kiện nào **kích hoạt** sự kiện này? (user action, system timer, external event)"
3. "Sau khi sự kiện này xảy ra, **hệ thống downstream** nào cần biết?"
4. "Có **hotspot** nào không? (điểm tranh cãi, logic phức tạp, performance concern)"

For each domain event, capture:
- **ID**: DE-001, DE-002, ...
- **Name**: Past-tense domain fact (e.g., "OrderPlaced", "PaymentConfirmed")
- **Business Flow**: Which BC this belongs to
- **Trigger**: What causes this event (User action / System / External / Time-based)
- **Downstream Effects**: What happens next
- **Hotspot**: Any concerns or complexity flags (mark with 🔥)

Group events by business flow and present in **timeline order** within each flow.

### Step 3: Actors and Commands
For each domain event, work backwards to identify:

1. "**Ai** (actor) thực hiện hành động gây ra sự kiện [X]?"
2. "Hành động đó (command) cụ thể là gì?"
3. "**Điều kiện tiên quyết** (precondition) để actor có thể thực hiện command?"
4. "Command này thuộc **business flow** nào?"

For each actor-command pair, capture:
- **Actor**: Who performs the command (from Stakeholder Register)
- **Command**: Present-tense imperative (e.g., "PlaceOrder", "ApprovePayment")
- **Preconditions**: What must be true before this command can execute
- **Resulting Event(s)**: Which domain event(s) this command produces
- **Business Flow**: Which BC this belongs to

### Step 4: Policies
Analyze BRD Business Rules and PRD functional requirements to identify **reactive
policies** — automated reactions triggered by events.

1. "Khi sự kiện [X] xảy ra, có **phản ứng tự động** nào cần kích hoạt?"
2. "Policy này tạo ra **command mới** hay **event mới**?"
3. "Policy này có **vượt qua ranh giới** giữa các domain không?"

For each policy, capture:
- **ID**: PL-001, PL-002, ...
- **Name**: Descriptive policy name
- **Triggering Event**: Which domain event activates this policy
- **Resulting Action**: Command triggered or event emitted
- **Cross-boundary?**: Does this cross aggregate or domain boundaries?
- **BRD Rule Ref**: Which business rule(s) this implements

### Step 5: Aggregates
Based on the events, commands, and policies discovered, identify **consistency
boundaries** (aggregates).

1. "Những **commands và events** nào phải xảy ra trong cùng một transaction?"
2. "Ranh giới nhất quán (consistency boundary) nằm ở đâu?"
3. "**Invariant** nào aggregate này phải bảo vệ? (VD: 'Số dư không được âm')"

For each aggregate, capture:
- **ID**: AGG-001, AGG-002, ...
- **Name**: Aggregate name
- **Responsibility**: What this aggregate is responsible for
- **Handled Commands**: Which commands this aggregate processes
- **Emitted Events**: Which events this aggregate produces
- **Invariants**: Business rules this aggregate must enforce
- **Business Flow(s)**: Which BCs this aggregate participates in

## Interaction Rules
- Walk through events **one business flow at a time**.
- Use **visual language**: refer to event storming colors (orange = event,
  blue = command, yellow = actor, pink/lilac = policy, green = aggregate).
- Validate each section before moving to the next.
- If the user identifies a new event not covered in the PRD, flag it as a
  **gap** that may need PRD amendment.
- Present aggregates as a summary view connecting all previous discoveries.

## Output
Write to: `docs/sdd/ES.md`

```markdown
# Event Storming Canvas

Version: <semver> | Created: <date> | Last updated: <date>
Source: BRD.md (v<version>), PRD.md (v<version>)

---

## 1. Domain Events

### Flow: <BC-001 Name>

| ID | Event Name | Trigger | Downstream Effects | Hotspot |
|----|------------|---------|--------------------|---------| 
| DE-001 | OrderPlaced | User: PlaceOrder | → Inventory check, → Payment initiation | - |
| DE-002 | PaymentConfirmed | System: Payment Gateway callback | → Order fulfillment | 🔥 Timeout handling |

### Flow: <BC-002 Name>
...

---

## 2. Actors and Commands

| Actor | Command | Preconditions | Resulting Event(s) | Business Flow |
|-------|---------|---------------|--------------------|---------| 
| Customer | PlaceOrder | Cart not empty, user authenticated | OrderPlaced | BC-001 |
| Admin | ApproveRefund | Refund request exists | RefundApproved | BC-003 |

---

## 3. Policies

| ID | Policy Name | Triggering Event | Resulting Action | Cross-boundary? | BRD Rule Ref |
|----|-------------|------------------|------------------|-----------------|--------------|
| PL-001 | Auto-confirm small orders | OrderPlaced | → ConfirmOrder (if amount < threshold) | No | BR-003 |
| PL-002 | Send notification on payment | PaymentConfirmed | → SendConfirmationEmail | Yes (Notification domain) | BR-005 |

---

## 4. Aggregates

| ID | Aggregate | Responsibility | Handled Commands | Emitted Events | Invariants | Flows |
|----|-----------|----------------|------------------|----------------|------------|-------|
| AGG-001 | Order | Manages order lifecycle | PlaceOrder, CancelOrder | OrderPlaced, OrderCancelled | Order total must be > 0 | BC-001 |
| AGG-002 | Payment | Manages payment processing | InitiatePayment, ConfirmPayment | PaymentInitiated, PaymentConfirmed | Payment amount = Order total | BC-001, BC-003 |

---

## Event Flow Diagram

​```mermaid
graph LR
    subgraph "BC-001: Order Management"
        A["👤 Customer"] -->|PlaceOrder| B["🟧 OrderPlaced"]
        B -->|Policy: Auto-confirm| C["🔵 ConfirmOrder"]
        C --> D["🟧 OrderConfirmed"]
    end

    subgraph "BC-002: Payment"
        D -->|Policy: Initiate payment| E["🔵 InitiatePayment"]
        E --> F["🟧 PaymentInitiated"]
        F -->|External: Gateway| G["🟧 PaymentConfirmed"]
    end

    G -->|Policy: Send notification| H["📧 Notification"]
​```

## Hotspots & Open Questions
| # | Hotspot | Location | Concern | Resolution |
|---|---------|----------|---------|------------|
| 1 | ... | DE-xxx | ... | [TBD] |
```

## Handoff
Once the user confirms the ES is complete, say:

> "Event Storming Canvas đã hoàn thành. Bước tiếp theo là **sdd-create-add** để
> thiết kế kiến trúc hệ thống (Architecture Design Document) dựa trên domain model vừa khám phá."

Do not auto-proceed — wait for the user to say go.
