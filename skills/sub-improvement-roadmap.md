---
name: sub-improvement-roadmap
description: Produce the sequenced week-by-week learning path with milestones, assessments, and a spaced-repetition schedule, plus improvement actions. Transforms scored curriculum design into an actionable, implementation-ready learning plan.
---

## Purpose
Transform the scored curriculum design into an executable, week-by-week learning plan that respects all framework principles, includes explicit spaced-repetition schedules, defines mastery milestones, and provides specific improvement actions to enhance learning outcomes.

## Required Inputs

### From Previous Sub-skills
- **Scored Curriculum**: Quality assessment from `sub-scoring-engine`
- **Learner Profile**: Goal, time budget, modality, constraints from `sub-profile-intake`
- **Selected Frameworks**: Framework principles from `sub-framework-selector`
- **Research Results**: Current high-quality resources from research phase
- **Feasibility Analysis**: Time-budget validation from scoring phase

### Planning Constraints
- Available hours per week
- Total timeline (weeks or deadline)
- Learning modality preferences
- Resource accessibility
- Any learner constraints

## Roadmap Generation Process

### Phase 1: Module Sequencing

**Step 1.1: Identify All Learning Components**
List all topics, skills, and knowledge components required for the goal.

**Step 1.2: Establish Prerequisite Dependencies**
Map which components must come before others using prerequisite analysis.

**Step 1.3: Create Learning Modules**
Group related components into logical modules (typically 1-2 weeks each).

**Step 1.4: Sequence Modules**
Order modules by prerequisite dependencies and complexity progression.

**Step 1.5: Allocate Time Budget**
Distribute available hours across modules within the time constraints.

**Sequencing Principles:**
- Build from foundational to advanced concepts
- Respect prerequisite relationships
- Balance cognitive load across weeks
- Ensure mastery points before advancing
- Include buffer time for review and catch-up

---

### Phase 2: Module Design

For each module, specify:

**2.1 Learning Objective**
```markdown
### Week X-Y: [Module Name]

**Learning Objective**: [Bloom's Level] [Specific, measurable objective]
- **Bloom's Level**: [Remember/Understand/Apply/Analyze/Evaluate/Create]
- **Measurable Outcome**: [Observable result that demonstrates achievement]
```

**Objective Requirements:**
- Must be specific and measurable
- Must be classified at appropriate Bloom's level
- Must connect to the overall learning goal
- Must be achievable within module timeframe

**2.2 Learning Activities**
List specific activities that will achieve the objective:
- Primary learning activities (instruction, reading, videos)
- Practice activities (exercises, problems, applications)
- Exploration activities (experiments, projects, investigations)

**Activity Design Guidelines:**
- Respect cognitive load limits
- Provide appropriate scaffolding
- Include active learning (not just passive consumption)
- Offer variety to maintain engagement
- Align with modality preferences

**2.3 Resource Links**
Provide direct access to high-quality resources:
- Primary learning resources (courses, books, videos)
- Practice resources (exercises, problem sets)
- Assessment resources (quizzes, projects, rubrics)

**Resource Selection Criteria:**
- High quality based on research phase
- Appropriate difficulty level
- Align with learning modality
- Accessible within learner constraints
- Current and up-to-date

**2.4 Formative Assessment**
Specify how learning will be checked during the module:
```markdown
**Formative Assessment**: [Check for understanding]
- **Format**: [Quiz/exercise/reflection/application]
- **Mastery Criteria**: [What constitutes passing]
- **Feedback Mechanism**: [How learners receive feedback]
```

**2.5 Time Estimate**
Provide realistic hour estimate for the module:
- Primary learning: X hours
- Practice activities: X hours
- Assessment completion: X hours
- Review and preparation: X hours
- **Total Module Hours**: X hours

---

### Phase 3: Assessment Structure

**3.1 Formative Assessments**
After each module, check understanding:
- Quick checks (5-10 minutes)
- Practice problems (15-30 minutes)
- Mini-applications (30-60 minutes)
- Reflection activities (10-15 minutes)

**3.2 Summative Milestones**
At key progression points (typically every 4-8 weeks):
```markdown
### Milestone M: [Milestone Name]
**Week**: [Week number]
**Objectives Assessed**: [List of module objectives]
**Assessment Task**: [Description of summative assessment]
**Mastery Criteria**: [Passing standard]
**Progression Gate**: [Must demonstrate mastery to advance]
```

**Milestone Types:**
- Knowledge integration projects
- Performance demonstrations
- Comprehensive assessments
- Portfolio submissions
- Practical applications

**3.3 Mastery Standards**
Define clear mastery criteria:
- Quantitative thresholds (e.g., 80% on assessment)
- Qualitative standards (e.g., can explain concept to others)
- Performance criteria (e.g., completes task independently)
- Application requirements (e.g., applies concept to new situation)

---

### Phase 4: Spaced Repetition Schedule

**4.1 Design Principles**
- **Expanding Intervals**: Review at 1, 3, 7, 14, 30 days after initial learning
- **Active Retrieval**: Test rather than just review
- **Interleaving**: Mix topics in review sessions
- **Contextual Variation**: Review in different contexts

**4.2 Schedule Template**
```markdown
## Spaced Repetition Schedule

| Topic | Initial Learning | Review 1 | Review 2 | Review 3 | Review 4 | Review 5 |
|-------|------------------|----------|----------|----------|----------|----------|
| [Topic 1] | Week 1 Day 1 | Week 1 Day 3 | Week 2 Day 2 | Week 3 Day 5 | Week 5 Day 1 | Week 8 Day 3 |
| [Topic 2] | Week 1 Day 2 | Week 1 Day 4 | Week 2 Day 3 | Week 3 Day 6 | Week 5 Day 2 | Week 8 Day 4 |
```

**4.3 Review Activities**
For each review, specify the activity:
- Retrieval practice (test without materials)
- Application exercises (apply to new problems)
- Explanation tasks (teach to someone else)
- Connection mapping (relate to other topics)

---

### Phase 5: Improvement Actions

Based on scoring results, create specific improvement actions:

**5.1 Priority Framework**
| Priority Band | Score Range | Action Required |
|---------------|-------------|-----------------|
| Critical | < 2.0 on any criterion | Immediate redesign required |
| High | 2.0-2.9 on weighted criteria | Significant improvements recommended |
| Medium | 3.0-3.4 on weighted criteria | Minor enhancements suggested |
| Low | 3.5-4.0 on weighted criteria | Optional refinements |

**5.2 Action Template**
```markdown
## Improvement Actions

| Priority | Criterion | Current Score | Target Score | Action | Effort | Impact | Timeline |
|----------|-----------|---------------|--------------|--------|--------|--------|----------|
| [High] | [Criterion Name] | [X/4] | [X/4] | [Specific action to improve] | [Hours] | [Score improvement] | [When to implement] |
```

**5.3 Common Improvement Actions**

**For Objective–Assessment Alignment:**
- Add measurable outcomes to vague objectives
- Create specific assessments for each objective
- Define mastery criteria for all assessments
- Align activities to objectives

**For Sequencing & Prerequisites:**
- Add missing prerequisite modules
- Reorder topics for logical flow
- Add mastery gates before progression
- Include bridging activities

**For Retention Design:**
- Create explicit spaced-repetition schedule
- Add retrieval practice activities
- Implement expanding intervals
- Include interleaving sessions

**For Cognitive Load Management:**
- Break complex topics into smaller chunks
- Add scaffolding for difficult concepts
- Optimize presentation materials
- Remove extraneous content

**For Motivation & Feasibility:**
- Add autonomy-supporting choices
- Include motivation checkpoints
- Adjust timeline to realistic expectations
- Add progress visualization

**For Practice & Feedback Loops:**
- Add deliberate practice activities
- Create immediate feedback mechanisms
- Include iteration opportunities
- Design challenge-level practice

---

## Output Structure

```markdown
# Personalized Learning Path — [Goal]

## 1. Learner Profile Summary
[Concise profile overview]

## 2. Learning Frameworks Applied
[Framework list and rationale]

## 3. Week-by-Week Learning Path

### Week 1-2: [Module Name]
**Learning Objective**: [Bloom's Level] [Specific objective]
- **Activities**: 
  - [Activity 1 with hours]
  - [Activity 2 with hours]
- **Resources**: [Links/references]
- **Formative Assessment**: [Check and mastery criteria]
- **Hours**: [Total estimate]
- **Prerequisites**: [What comes before]

### Week 3-4: [Module Name]
[Continue pattern...]

### [Additional weeks...]

## 4. Assessment Structure

### Formative Assessments
- [After each module: format and criteria]

### Summative Milestones
#### Milestone 1: [Name] — Week [X]
- **Objectives Assessed**: [List]
- **Assessment Task**: [Description]
- **Mastery Criteria**: [Standard]
- **Progression Gate**: [Requirement to advance]

#### Milestone 2: [Name] — Week [Y]
[Continue pattern...]

## 5. Spaced Repetition Schedule

[Complete schedule table as shown in Phase 4.2]

### Review Activities
- **Retrieval Practice**: [How to implement]
- **Application Exercises**: [How to implement]
- **Explanation Tasks**: [How to implement]

## 6. Improvement Actions

[Action table as shown in Phase 5.2]

## 7. Progress Tracking

### Weekly Check-ins
- [What to review each week]
- [Adjustment points]
- [Success indicators]

### Mastery Tracker
- [How to track objective achievement]
- [When to move to next module]
- [What to do if mastery not achieved]

## 8. Success Criteria

### Completion Metrics
- [What constitutes path completion]
- [Final assessment or demonstration]
- [Mastery level required]

### Ongoing Metrics
- [Weekly progress indicators]
- [Engagement and motivation measures]
- [Learning efficiency metrics]

## 9. Resource Summary

### Primary Resources
[High-priority resources for core learning]

### Supplementary Resources
[Additional resources for enrichment]

### Practice Resources
[Resources for exercises and applications]
```

## Quality Gates

Before finalizing the roadmap, verify:

- [ ] All modules are sequenced by prerequisite order
- [ ] Every module has a clear objective at Bloom's level
- [ ] Every module has specific learning activities
- [ ] Every module has estimated hours (realistic for time budget)
- [ ] Every module has a formative assessment with mastery criteria
- [ ] Summative milestones are defined with progression gates
- [ ] Spaced-repetition schedule is explicit (not optional)
- [ ] Review activities include active retrieval
- [ ] Improvement actions address weak scoring criteria
- [ ] Total path hours align with feasibility analysis
- [ ] All constraints are respected (budget, accessibility, schedule)
- [ ] Modality preferences are reflected in activity choices

## Error Handling

### Time Budget Exceeded
**Condition**: Sum of module hours exceeds available time
**Action**: 
1. Re-evaluate module scope
2. Remove non-essential components
3. Extend timeline if possible
4. Flag trade-offs clearly

### Prerequisite Gap Identified
**Condition**: Module requires knowledge not covered earlier
**Action**:
1. Add prerequisite module
2. Provide bridging materials
3. Adjust sequencing

### Resource Access Issue
**Condition**: Required resource is inaccessible or too expensive
**Action**:
1. Find alternative resource
2. Adjust activities to work with available resources
3. Flag limitation clearly

### Assessment Missing
**Condition**: Module lacks formative assessment
**Action**:
1. Add appropriate assessment
2. Define mastery criteria
3. Specify feedback mechanism

## Integration Notes

This sub-skill receives:
- Scored curriculum from `sub-scoring-engine`
- Learner profile from `sub-profile-intake`
- Frameworks from `sub-framework-selector`
- Research results from main research phase

It produces:
- Complete, implementation-ready learning path
- All deliverables for main synthesis phase

## Tools Required
- Read — Access all previous outputs and SECOND-KNOWLEDGE-BRAIN.md
- Write — Generate comprehensive roadmap document
- WebSearch — Find additional resources if needed
