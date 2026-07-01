# CLAUDE.md — Personalized Learning Path Designer Skill (Idea 52)

**Skill name:** `personalized-learning-path-designer`
**Tagline:** Learner-tailored curriculum & study path graded against learning-science frameworks.
**Current phase:** Scaffold complete (Phases 0–5).
**Source idea:** 52 — *Design & evaluate a personalized curriculum/learning path for any learner type (students, working professionals, career switchers), grounded in world-renowned pedagogy & learning science, with improvement recommendations; continuously crawl papers/docs to stay current.*
**Cluster:** `career-education`

## Problem This Skill Solves
Generic courses ignore prior knowledge, goals, and time budget. This skill profiles the learner, designs a sequenced path using named learning-science frameworks (Bloom's taxonomy, Backward Design/UbD, spaced repetition, deliberate practice, cognitive load theory, ZPD), scores the design, and emits an improvement roadmap.

## Harness Flow Summary
1. **Intake** (`sub-profile-intake`) — goals, prior knowledge, time budget, learning preferences, constraints.
2. **Framework selection** (`sub-framework-selector`) — pedagogy by learner type/goal.
3. **Research** (main) — verify current best practices/resources vs SECOND-KNOWLEDGE-BRAIN.md.
4. **Scoring** (`sub-scoring-engine`) — curriculum quality score vs frameworks.
5. **Roadmap** (`sub-improvement-roadmap`) — sequenced path + improvement actions.

## Sub-skills
- `sub-profile-intake.md` · `sub-framework-selector.md` · `sub-scoring-engine.md` · `sub-improvement-roadmap.md`

## Tools Required
WebSearch, WebFetch, Read, Write, Bash.

## Knowledge Sources
ERIC, ArXiv cs.CY/stat.ML (learning analytics), learning-science literature (Bjork, Sweller, Wiggins & McTighe), OECD education reports.

## Supporting Python Tools
`tools/knowledge_updater.py` — crawl → SECOND-KNOWLEDGE-BRAIN.md.

## Active Development Tasks
- [x] Scaffold deliverables.
- [ ] Add domain-specific skill trees.

## Reference Docs
PROJECT-detail.md · PROJECT-DEVELOPMENT-PHASE-TRACKING.md · SECOND-KNOWLEDGE-BRAIN.md
