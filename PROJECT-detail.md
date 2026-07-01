# PROJECT-detail.md — Personalized Learning Path Designer (Idea 52)

## Executive Summary
A harness that profiles a learner and designs a sequenced, learning-science-grounded curriculum, scores its quality, and emits an improvement roadmap with milestones and assessments.

## Problem Statement
Off-the-shelf courses ignore prior knowledge, goals, and available time, producing poor retention and motivation. This skill builds an evidence-based personalized path.

## Target Users & Use Cases
- **Student:** "Help me learn calculus for an exam in 8 weeks" → sequenced path + spaced-repetition schedule.
- **Working professional:** "Learn data engineering, 5 hrs/week" → modular path fitting time budget.
- **Career switcher:** "From marketing to UX" → prerequisite-aware path + portfolio milestones.

## Harness Architecture
```
/personalized-learning-path-designer
  → sub-profile-intake      (goals, prior knowledge, time)   [gate: goal + time budget set]
  → sub-framework-selector  (pedagogy per learner type)      [gate: ≥2 named frameworks]
  → [main] research         (current resources/best practice) [gate: cited]
  → sub-scoring-engine      (curriculum quality score)        [gate: each criterion vs framework]
  → sub-improvement-roadmap (sequenced path + actions)        [gate: milestones + assessments]
  → [main] synthesize
```

## Full Sub-Skill Catalog
| Sub-skill | Purpose | Inputs | Outputs | Tools | Gate |
|-----------|---------|--------|---------|-------|------|
| sub-profile-intake | Profile learner | goals, prior knowledge, time | learner profile | Read | Goal + time budget present |
| sub-framework-selector | Pick pedagogy | learner type, goal | framework set | Read, WebSearch | ≥2 named frameworks |
| sub-scoring-engine | Score curriculum | draft path, frameworks | quality score | Read | Each criterion vs framework |
| sub-improvement-roadmap | Build path + improve | scores, profile | sequenced path | Write | Milestones + assessments |

## Skill File Format Specification
Per Claude skill standard; see skills/main.md.

## E2E Execution Flow
1. Intake captures goal, prior knowledge (diagnostic), time budget, modality preference. 2. Selector picks frameworks (Backward Design, Bloom's, spaced repetition, deliberate practice, cognitive load). 3. Research finds current high-quality resources. 4. Draft path scored on alignment, sequencing, assessment, load, motivation. 5. Roadmap produces a week-by-week plan with milestones and formative assessments. 6. Render.
Error handling: unrealistic time vs goal → flag + rescope; no clear goal → ask; offline → use brain + flag.

## SECOND-KNOWLEDGE-BRAIN Integration
Sources: ERIC, learning-science literature, OECD, ArXiv cs.CY. Weekly append.

## Supporting Tools Spec
`knowledge_updater.py`: queries on learning science/edtech; weekly cron; dedupe by hash.

## Quality Gates
- Path uses Backward Design: objectives → assessments → activities.
- Each scoring criterion maps to a named framework.
- Time budget feasibility validated.
- Milestones + formative assessments present; offline flagged.

## Test Scenarios (summary)
1. Exam-deadline student. 2. Time-constrained professional. 3. Career switcher with prerequisites. 4. Unrealistic goal/time (rescope). 5. Child learner (age-appropriate). (Full set in tests/.)

## Key Design Decisions
1. Backward Design is mandatory structure. 2. Spaced repetition scheduled, not suggested. 3. Time feasibility is a gate. 4. Assessments at every milestone. 5. Prior-knowledge diagnostic before sequencing.
