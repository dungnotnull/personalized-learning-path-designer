---
name: sub-scoring-engine
description: Score a draft curriculum against learning-science criteria with framework-mapped evidence. Ensures all learning paths meet evidence-based quality standards before implementation.
---

## Purpose
Evaluate curriculum design quality using evidence-based learning science criteria. Every scoring decision must be grounded in a named framework and cited from SECOND-KNOWLEDGE-BRAIN.md. This gate prevents poor curriculum designs from reaching learners.

## Required Inputs

### From Previous Sub-skills
- **Draft Path**: Proposed curriculum structure from research phase
- **Learner Profile**: Goal, time budget, current level from `sub-profile-intake`
- **Selected Frameworks**: Framework set from `sub-framework-selector`
- **Available Resources**: High-quality materials identified in research phase

### Scoring Context
- Goal complexity and domain
- Timeline constraints
- Learner characteristics
- Resource availability

## Scoring Criteria & Frameworks

### Criterion 1: Objective–Assessment Alignment (Weight: 25%)
**Framework Reference**: Backward Design (Wiggins & McTighe), Bloom's Taxonomy

**What to Evaluate:**
- Are learning objectives clearly defined and measurable?
- Are objectives classified at appropriate Bloom's levels?
- Does each objective have corresponding assessment evidence?
- Are assessments aligned to measure the stated objective?
- Is there a clear path from objective → assessment → activity?

**Scoring Rubric:**
| Score | Criteria |
|-------|-----------|
| 4 (Excellent) | All objectives are measurable, classified at appropriate Bloom's levels, and have directly aligned assessments with clear mastery criteria |
| 3 (Good) | Most objectives are measurable and aligned, minor gaps in assessment specificity |
| 2 (Fair) | Objectives exist but lack Bloom's classification or assessments are generic |
| 1 (Poor) | Objectives are vague, missing assessments, or misaligned |

**Evaluation Questions:**
1. Can you observe whether the objective was achieved?
2. Does the assessment actually measure the objective?
3. Are the learning activities likely to achieve the objective?

**Framework Citation**: SECOND-KNOWLEDGE-BRAIN.md — Backward Design, Bloom's Taxonomy sections

---

### Criterion 2: Sequencing & Prerequisites (Weight: 20%)
**Framework Reference**: Mastery Learning (Bloom), Zone of Proximal Development (Vygotsky)

**What to Evaluate:**
- Is content sequenced logically from simple to complex?
- Are prerequisites identified and addressed before dependent topics?
- Does the sequence respect the ZPD (challenging but achievable)?
- Are there clear milestones for progression?
- Is mastery required before advancing (not just time)?

**Scoring Rubric:**
| Score | Criteria |
|-------|-----------|
| 4 (Excellent) | Logical prerequisite sequence, ZPD-aligned challenges, mastery-based progression gates |
| 3 (Good) | Logical sequence with appropriate challenges, minor gaps in prerequisite checks |
| 2 (Fair) | Generally logical but some prerequisites missed or sequencing issues |
| 1 (Poor) | Illogical sequence, prerequisite gaps, or inappropriate difficulty jumps |

**Evaluation Questions:**
1. Will learners have the required knowledge before each topic?
2. Is each step challenging but achievable?
3. Are there opportunities to demonstrate mastery before advancing?

**Framework Citation**: SECOND-KNOWLEDGE-BRAIN.md — Mastery Learning, ZPD sections

---

### Criterion 3: Retention Design (Weight: 20%)
**Framework Reference**: Spaced Repetition, Retrieval Practice (Bjork, Roediger)

**What to Evaluate:**
- Is there an explicit spaced-repetition schedule (not optional suggestions)?
- Are retrieval practice activities included (beyond passive review)?
- Is repetition appropriately spaced (expanding intervals)?
- Is there interleaving of topics for durable learning?
- Are review activities connected to original learning context?

**Scoring Rubric:**
| Score | Criteria |
|-------|-----------|
| 4 (Excellent) | Comprehensive spaced-repetition schedule with expanding intervals, active retrieval practice, topic interleaving |
| 3 (Good) | Spaced-repetition schedule present, some retrieval practice, minor gaps in spacing optimization |
| 2 (Fair) | Review reminders present but not scheduled, limited retrieval practice |
| 1 (Poor) | No spaced repetition, only passive review, or completely missing |

**Evaluation Questions:**
1. When will learners review each topic?
2. Are they practicing retrieval or just rereading?
3. Is spacing following research-based intervals?

**Framework Citation**: SECOND-KNOWLEDGE-BRAIN.md — Spaced Repetition section

---

### Criterion 4: Cognitive Load Management (Weight: 15%)
**Framework Reference**: Cognitive Load Theory (Sweller)

**What to Evaluate:**
- Is intrinsic load managed (complexity broken into steps)?
- Is extraneous load minimized (no distractions, clear presentation)?
- Is germane load optimized (activities build schemas)?
- Are working memory limits respected?
- Is scaffolding provided and gradually removed?

**Scoring Rubric:**
| Score | Criteria |
|-------|-----------|
| 4 (Excellent) | Complexity well-scaffolded, presentation optimized, activities build mental models, scaffolding fades appropriately |
| 3 (Good) | Generally well-managed load, minor issues with presentation or scaffolding |
| 2 (Fair) | Some awareness of load, but overwhelms at points or misses scaffolding opportunities |
| 1 (Poor) | No load management, overwhelms working memory, or no scaffolding |

**Evaluation Questions:**
1. Is the learner's working memory respected?
2. Are complex topics broken into manageable chunks?
3. Is scaffolding provided where needed?

**Framework Citation**: SECOND-KNOWLEDGE-BRAIN.md — Cognitive Load Theory section

---

### Criterion 5: Motivation & Feasibility (Weight: 10%)
**Framework Reference**: Self-Determination Theory (Deci & Ryan), realistic time estimation

**What to Evaluate:**
- Are autonomy, competence, and relatedness supported?
- Is the timeline realistic for the goal and time budget?
- Is the workload sustainable across the timeline?
- Are there motivation checkpoints and supports?
- Is the goal achievable within the given constraints?

**Scoring Rubric:**
| Score | Criteria |
|-------|-----------|
| 4 (Excellent) | Clear timeline validation, autonomy supported, regular motivation checkpoints, sustainable workload |
| 3 (Good) | Timeline validated, basic motivation elements, generally sustainable |
| 2 (Fair) | Timeline questionably realistic, limited motivation support |
| 1 (Poor) | Unrealistic timeline, no motivation consideration, or burnout risk |

**Evaluation Questions:**
1. Can this goal realistically be achieved in the available time?
2. Will the learner maintain motivation throughout?
3. Is the workload sustainable?

**Framework Citation**: SECOND-KNOWLEDGE-BRAIN.md (if available) or external SDT reference

---

### Criterion 6: Practice & Feedback Loops (Weight: 10%)
**Framework Reference**: Deliberate Practice (Ericsson)

**What to Evaluate:**
- Are there focused practice activities at ability boundaries?
- Is immediate, specific feedback provided?
- Is there opportunity for iteration and improvement?
- Are practice activities appropriately challenging?
- Is feedback actionable and specific?

**Scoring Rubric:**
| Score | Criteria |
|-------|-----------|
| 4 (Excellent) | Well-designed practice at challenge edge, immediate specific feedback, iteration cycles, measurable improvement |
| 3 (Good) | Practice activities present with feedback, some iteration opportunities |
| 2 (Fair) | Basic practice included, but limited feedback or iteration |
| 1 (Poor) | No practice activities, no feedback, or practice not challenging |

**Evaluation Questions:**
1. Are learners practicing the right things at the right difficulty?
2. Do they get feedback on their practice?
3. Can they iterate and improve?

**Framework Citation**: SECOND-KNOWLEDGE-BRAIN.md — Deliberate Practice section

---

## Time-Budget Feasibility Analysis

### Calculation Method

**Step 1: Estimate Topic Hours**
For each topic/module, estimate total learning hours including:
- Initial learning (videos, reading, instruction)
- Practice activities
- Assessment completion
- Review and spaced repetition

**Step 2: Calculate Total Required Hours**
```
Total Hours = Sum of all topic hours + buffer (20%)
```

**Step 3: Compare with Available Time**
```
Available Hours = weekly_hours × total_weeks
Feasibility Ratio = Total Hours / Available Hours
```

**Step 4: Determine Feasibility Verdict**
| Ratio | Verdict | Action |
|-------|---------|--------|
| ≤ 1.0 | CONFIRMED | Proceed with current path |
| 1.01-1.2 | CAUTION | Minor adjustments recommended |
| 1.21-1.5 | RESCOPE NEEDED | Significant scope reduction required |
| > 1.5 | INFEASIBLE | Goal unrealistic for time budget |

## Output Structure

```markdown
## Curriculum Quality Score

### Detailed Scoring

| Criterion | Weight | Score (1-4) | Weighted Score | Framework | Rationale |
|-----------|--------|-------------|----------------|-----------|-----------|
| Objective–Assessment Alignment | 25% | X/4 | X.XX | Backward Design, Bloom's | [Specific rationale] |
| Sequencing & Prerequisites | 20% | X/4 | X.XX | Mastery Learning, ZPD | [Specific rationale] |
| Retention Design | 20% | X/4 | X.XX | Spaced Repetition | [Specific rationale] |
| Cognitive Load Management | 15% | X/4 | X.XX | Cognitive Load Theory | [Specific rationale] |
| Motivation & Feasibility | 10% | X/4 | X.XX | SDT | [Specific rationale] |
| Practice & Feedback Loops | 10% | X/4 | X.XX | Deliberate Practice | [Specific rationale] |
| **TOTAL** | **100%** | **X.XX/4** | **XX.XX/100** | | |

### Quality Band
- **90-100**: Excellent — Ready to implement with confidence
- **75-89**: Good — Minor improvements recommended
- **60-74**: Fair — Significant improvements needed before implementation
- **< 60**: Poor — Major redesign required

### Time-Budget Feasibility Analysis
- **Total Required Hours**: XX hours (including 20% buffer)
- **Available Hours**: XX hours (X hrs/week × X weeks)
- **Feasibility Ratio**: X.XX
- **Verdict**: [CONFIRMED / CAUTION / RESCOPE NEEDED / INFEASIBLE]

### Recommended Improvements
| Priority | Criterion | Action | Expected Impact |
|----------|-----------|--------|-----------------|
| [Priority] | [Criterion] | [Specific action] | [Score improvement] |
```

## Quality Gates

Before completing scoring, verify:

- [ ] All 6 criteria have been scored (1-4 scale)
- [ ] Each criterion score is backed by framework rationale
- [ ] Each framework is cited from SECOND-KNOWLEDGE-BRAIN.md
- [ ] Weighted total is calculated correctly
- [ ] Time-budget feasibility has been explicitly analyzed
- [ ] Feasibility verdict is provided with action guidance
- [ ] Recommended improvements are specific and actionable

## Error Handling

### Missing Framework Citation
**Condition**: Framework not found in SECOND-KNOWLEDGE-BRAIN.md
**Action**: Use external citation, add to knowledge base for future reference

### Unclear Scoring Rationale
**Condition**: Score given without framework-based rationale
**Action**: Re-evaluate criterion using framework principles, document reasoning

### Feasibility Calculation Issues
**Condition**: Cannot estimate hours or validate feasibility
**Action**: Use conservative estimates, flag uncertainty, recommend pilot testing

## Integration Notes

This sub-skill receives:
- Draft path from research phase
- Learner profile from `sub-profile-intake`
- Frameworks from `sub-framework-selector`

It provides:
- Quality assessment to `sub-improvement-roadmap`
- Feasibility validation for final roadmap
- Improvement priorities for optimization

## Tools Required
- Read — Access SECOND-KNOWLEDGE-BRAIN.md for framework citations
- Write — Generate scoring documentation and recommendations
