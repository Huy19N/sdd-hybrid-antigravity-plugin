---
name: sdd-deep-research
description: "Sub-skill automatically invoked by sdd-brainstorm. Do NOT trigger manually. Performs structured market and UX research using search_web and read_url_content tools to enrich brainstorm.md with data-driven insights before Socratic questioning begins. Outputs a Research Findings section that helps the brainstorm ask sharper questions and propose better approaches."
---

# SDD Deep Research (sub-skill of sdd-brainstorm)

## Purpose
Gather structured, data-driven context about the user's idea **before** the
Socratic questioning phase of brainstorming begins. The research output helps
`sdd-brainstorm` ask more precise questions and propose approaches grounded in
real market/competitor data rather than generic assumptions.

## Invocation
This skill is **automatically called** by `sdd-brainstorm` as its first step.
It should never be triggered directly by the user. If a user asks for research
separately, point them to `sdd-brainstorm` which will invoke this automatically.

## Process

### 1. Extract seed keywords
From the user's initial idea description, extract:
- **Industry/domain** (e.g., F&B, SaaS, education, healthcare)
- **Product type** (e.g., e-commerce, portfolio, booking platform)
- **Target audience** (e.g., students, small business owners, developers)
- **Geographic focus** if mentioned (e.g., Vietnam, global)

### 2. Market Analysis
Use `search_web` to research:
- Market size and growth trends for the domain
- Key players and market leaders
- Recent industry news or shifts (last 6-12 months)
- Common pricing models in this space

Capture 3-5 key data points with sources.

### 3. Competitor Analysis
Identify the **top 5 competitors or similar products**:
- Name + URL
- Core value proposition (1 sentence each)
- Strengths (what they do well)
- Weaknesses or gaps (opportunities for differentiation)
- Pricing tier (free/freemium/paid)

Use `read_url_content` to skim competitor landing pages when available.

### 4. UX/Design Trends
Research current design patterns in this domain:
- What layouts are commonly used? (hero sections, grids, dashboards)
- What design language dominates? (minimalist, bold, playful, corporate)
- Color palette trends in this industry
- Common UI patterns (onboarding flows, navigation styles, CTAs)
- Mobile-first vs desktop-first conventions

### 5. Technical Feasibility Notes
Brief assessment of:
- Commonly used tech stacks for this type of product
- Key APIs or third-party services typically integrated
- Known technical challenges in this domain
- Performance/scale considerations

## Output Format
Return a structured section to be appended to the brainstorm.md draft:

```markdown
## Research Findings

### Market Overview
- Market size: ...
- Growth trend: ...
- Key data points: ...
- Sources: [1] ..., [2] ...

### Competitor Landscape
| Competitor | Value Prop | Strengths | Gaps | Pricing |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

### UX/Design Trends in [Industry]
- Dominant layout patterns: ...
- Color/typography trends: ...
- Common UI patterns: ...
- Mobile considerations: ...

### Technical Notes
- Common stacks: ...
- Key integrations: ...
- Known challenges: ...
```

## Constraints
- Keep research focused — spend no more than 5-8 search queries total.
- Do not deep-dive into any single competitor; breadth over depth.
- All claims must have a source URL. No fabricated data.
- If search results are thin for a niche domain, note the gap honestly
  rather than padding with generic advice.
- This step produces **input for brainstorming**, not final decisions.
  The user will validate and refine during the Socratic phase.

## Handoff
Return the Research Findings block to `sdd-brainstorm`, which will incorporate
it into the brainstorm.md draft and then proceed to Socratic questioning.
Do not interact with the user directly from this sub-skill.
