---
name: sub-framework-selector
description: Select the learning-science frameworks appropriate to the learner type and goal. Ensures all curriculum design decisions are grounded in evidence-based pedagogy.
---

## Purpose
Select and apply evidence-based learning science frameworks to guide curriculum design decisions. Every framework selected must be cited from SECOND-KNOWLEDGE-BRAIN.md and matched to the specific learner characteristics and goal requirements.

## Required Inputs

### From Learner Profile
- **Learner Type**: student, professional, career-switcher, child, lifelong-learner
- **Goal Characteristics**: complexity, duration, skill type, assessment requirements
- **Time Constraints**: urgency, total timeline, weekly intensity
- **Modality Preference**: visual, reading, hands-on, mixed

### Framework Selection Criteria
- Goal complexity and domain
- Timeline urgency
- Skill acquisition requirements
- Assessment and evaluation needs
- Motivation and engagement requirements

## Framework Selection Logic

### Anchor Frameworks (Always Included)

**1. Backward Design / Understanding by Design (UbD)**
- **Authors**: Wiggins & McTighe
- **Purpose**: Provide structural foundation for curriculum design
- **Application**: All paths must follow objectives → assessments → activities
- **When**: Always, for every learner type and goal
- **Citation**: SECOND-KNOWLEDGE-BRAIN.md — Backward Design / UbD section

**2. Bloom's Taxonomy (Revised)**
- **Authors**: Anderson & Krathwohl (revision of Bloom)
- **Purpose**: Define and classify learning objectives at appropriate cognitive levels
- **Levels**: Remember → Understand → Apply → Analyze → Evaluate → Create
- **Application**: All objectives must be classified at appropriate Bloom's levels
- **When**: Always, for every learner type and goal
- **Citation**: SECOND-KNOWLEDGE-BRAIN.md — Bloom's Taxonomy section

### Conditional Frameworks

**3. Spaced Repetition & Retrieval Practice**
- **Researchers**: Bjork, Roediger, Karpicke
- **Purpose**: Optimize long-term retention and combat forgetting curve
- **Application**: Design explicit review schedules with distributed practice
- **When**:
  - Time-sensitive goals (< 8 weeks) — REQUIRE
  - Knowledge-intensive goals (facts, vocabulary, procedures) — REQUIRE
  - Long-term skill retention required — REQUIRE
  - Optional for short, performance-only goals
- **Citation**: SECOND-KNOWLEDGE-BRAIN.md — Spaced repetition section

**4. Cognitive Load Theory (CLT)**
- **Author**: Sweller
- **Purpose**: Manage intrinsic, extraneous, and germane cognitive load
- **Application**: Scaffold complexity, prevent overwhelming, optimize learning efficiency
- **When**:
  - Complex or technical goals — REQUIRE
  - Novice learners in domain — REQUIRE
  - Multi-component skills integration — REQUIRE
  - Optional for simple, familiar topics
- **Citation**: SECOND-KNOWLEDGE-BRAIN.md — Cognitive Load Theory section

**5. Zone of Proximal Development (ZPD)**
- **Author**: Vygotsky
- **Purpose**: Target learning at the edge of current ability with appropriate scaffolding
- **Application**: Design tasks that are challenging but achievable with support
- **When**:
  - Skill acquisition goals — REQUIRE
  - Progressive skill building — REQUIRE
  - Technical or physical skills — REQUIRE
  - Optional for pure knowledge goals
- **Citation**: SECOND-KNOWLEDGE-BRAIN.md — ZPD section

**6. Deliberate Practice**
- **Author**: Ericsson
- **Purpose**: Structure focused, feedback-rich practice at ability boundaries
- **Application**: Design practice activities with immediate feedback and iteration
- **When**:
  - Performance skill goals (music, sports, technical skills) — REQUIRE
  - Mastery-level outcomes required — REQUIRE
  - Long-term skill development — REQUIRE
  - Optional for conceptual understanding goals
- **Citation**: SECOND-KNOWLEDGE-BRAIN.md — Deliberate practice section

**7. Mastery Learning**
- **Author**: Bloom
- **Purpose**: Ensure learners advance based on demonstrated mastery, not time
- **Application**: Gate progression on mastery checks, not completion
- **When**:
  - Sequential skill building — REQUIRE
  - Cumulative knowledge domains (math, programming) — REQUIRE
  - Certification or performance outcomes — REQUIRE
  - Optional for exploration-based learning
- **Citation**: SECOND-KNOWLEDGE-BRAIN.md — Mastery learning section

**8. Self-Determination Theory (SDT)**
- **Authors**: Deci & Ryan
- **Purpose**: Support autonomy, competence, and relatedness for motivation
- **Application**: Design choices, challenge levels, and collaborative elements
- **When**:
  - Long-term self-paced goals (> 3 months) — REQUIRE
  - Motivation concerns identified — REQUIRE
  - Adult learner autonomy preferences — REQUIRE
  - Optional for short, externally-motivated goals
- **Citation**: SECOND-KNOWLEDGE-BRAIN.md (if available) or external reference

## Selection Decision Tree

```
START
  ↓
Always include: Backward Design + Bloom's
  ↓
Is goal time-sensitive (< 8 weeks)?
  YES → Add Spaced Repetition + Retrieval Practice
  NO  → Continue
  ↓
Is goal complex/technical or learner novice?
  YES → Add Cognitive Load Theory + ZPD
  NO  → Continue
  ↓
Is goal performance-based skill acquisition?
  YES → Add Deliberate Practice + Mastery Learning
  NO  → Continue
  ↓
Is goal long-term self-paced (> 3 months)?
  YES → Add Self-Determination Theory
  NO  → End
```

## Framework Application Guidelines

### Backward Design Application
1. **Stage 1 - Identify Desired Results**
   - Define learning goals (Bloom's classified)
   - Establish essential questions
   - Specify knowledge and skills

2. **Stage 2 - Determine Acceptable Evidence**
   - Design performance tasks
   - Create assessment criteria
   - Define mastery standards

3. **Stage 3 - Plan Learning Experiences**
   - Sequence instruction
   - Design learning activities
   - Select resources

### Bloom's Taxonomy Application
- **Remember**: Recall facts and basic concepts
- **Understand**: Explain ideas or concepts
- **Apply**: Use information in new situations
- **Analyze**: Draw connections among ideas
- **Evaluate**: Justify a stand or decision
- **Create**: Produce new or original work

### Spaced Repetition Application
- **Initial encoding**: Learn material
- **Review schedule**: 1 day, 3 days, 7 days, 14 days, 30 days
- **Retrieval practice**: Test, don't just restudy
- **Interleaving**: Mix topics in review sessions

### Cognitive Load Management
- **Intrinsic load**: Simplify complex concepts, use pre-training
- **Extraneous load**: Eliminate distractions, optimize presentation
- **Germane load**: Design activities that build schemas

## Output Structure

```markdown
## Selected Learning Frameworks

### Anchor Frameworks (Always Applied)

**1. Backward Design (Understanding by Design)**
- **Authors**: Wiggins & McTighe
- **Rationale**: Provides structured approach to curriculum design
- **Application**: [Specific application to this goal]
- **Citation**: SECOND-KNOWLEDGE-BRAIN.md

**2. Bloom's Taxonomy (Revised)**
- **Authors**: Anderson & Krathwohl
- **Rationale**: Ensures objectives at appropriate cognitive levels
- **Application**: [How objectives will be classified]
- **Citation**: SECOND-KNOWLEDGE-BRAIN.md

### Additional Frameworks (Selected for This Learner/Goal)

[Framework 3-8 with similar structure...]

## Framework Integration Plan

[How frameworks will work together to guide curriculum design]

## Critical Success Factors

[Key elements that must be present based on selected frameworks]
```

## Quality Gates

Before completing framework selection, verify:

- [ ] Backward Design is included (always required)
- [ ] Bloom's Taxonomy is included (always required)
- [ ] At least 2 additional frameworks selected for most goals
- [ ] Each framework has clear rationale for this specific learner/goal
- [ ] Each framework is cited from SECOND-KNOWLEDGE-BRAIN.md
- [ ] Framework selection follows decision tree logic
- [ ] Framework integration plan is defined
- [ ] Critical success factors are identified based on frameworks

## Error Handling

### Too Few Frameworks Selected
**Condition**: Only anchor frameworks selected for complex goal
**Action**: Review decision tree, add conditional frameworks based on goal characteristics

### Framework Mismatch
**Condition**: Selected frameworks don't align with goal requirements
**Action**: Re-evaluate goal characteristics, adjust framework selection

### Citation Missing
**Condition**: Framework not found in SECOND-KNOWLEDGE-BRAIN.md
**Action**: Use external citation, add to knowledge base for future reference

## Integration Notes

This sub-skill receives the learner profile from `sub-profile-intake` and provides the framework foundation for:
- `sub-scoring-engine` — Scoring criteria mapped to selected frameworks
- `sub-improvement-roadmap` — Curriculum design guided by framework principles

## Tools Required
- Read — Access SECOND-KNOWLEDGE-BRAIN.md for framework citations
- WebSearch — Look up framework details if not in knowledge base
