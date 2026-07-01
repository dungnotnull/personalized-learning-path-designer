---
name: sub-profile-intake
description: Profile a learner — goal, prior knowledge, time budget, modality preference, constraints — before path design. Ensures all required information is captured for effective learning path design.
---

## Purpose
Build a comprehensive, structured learner profile that serves as the foundation for personalized curriculum design. This sub-skill conducts a thorough intake process, including goal clarification, prior-knowledge assessment, and constraint identification.

## Required Inputs

### 1. Learning Goal (Required)
The learner must articulate what they want to achieve in specific terms.

**Acceptable Goals:**
- "Learn calculus to pass AP Calculus exam"
- "Build a web application using React"
- "Transition from marketing to UX design"
- "Learn conversational Spanish for travel"

**Unacceptable Goals (require refinement):**
- "Learn programming" (too vague)
- "Get better at math" (not specific)
- "Learn coding" (no clear outcome)

### 2. Deadline (Optional but Recommended)
- Target date for completion
- Helps determine pacing and feasibility
- If no deadline, assume ongoing learning

### 3. Prior Experience (Required)
- Current level relative to the goal
- Related knowledge or skills
- Self-assessment of proficiency

### 4. Weekly Time Budget (Required)
- Hours per week available for study
- Must be realistic and sustainable
- Minimum 2 hours/week for meaningful progress

### 5. Preferred Learning Modality (Required)
Options:
- **Visual**: Video lectures, diagrams, visual demonstrations
- **Reading**: Text-based content, articles, books
- **Hands-on**: Projects, exercises, practical applications
- **Mixed**: Combination of approaches

### 6. Constraints (Optional)
- Budget limitations for paid resources
- Accessibility needs
- Schedule restrictions
- Equipment/software requirements

## Intake Process

### Step 1: Goal Clarification
Transform vague goals into measurable objectives using SMART framework.

**Questions to Ask:**
- "What specific outcome do you want to achieve?"
- "How will you know when you've reached your goal?"
- "Can you measure your success?"

**Transformation Examples:**
| Vague Goal | Refined Goal |
|------------|--------------|
| "Learn Python" | "Build a data analysis dashboard using Python pandas" |
| "Get better at math" | "Master algebra to prepare for calculus" |
| "Learn design" | "Create a professional portfolio website using UI/UX principles" |

### Step 2: Prior-Knowledge Diagnostic
Assess current level to determine starting point and prerequisites.

**Diagnostic Approach:**
1. **Self-Assessment Questions** (3-5 targeted questions)
   - "What related experience do you have?"
   - "What concepts are you already familiar with?"
   - "What have you tried before?"

2. **Checkpoint Questions** (topic-specific)
   - For programming: "Do you know what a variable is?"
   - For math: "Can you solve basic equations?"
   - For languages: "Can you introduce yourself in the target language?"

3. **Prerequisite Mapping**
   - Identify gaps between current and required knowledge
   - Determine if remediation is needed
   - Estimate time to close gaps

### Step 3: Time Budget Assessment
Capture realistic time commitment and validate feasibility.

**Time Categories:**
- **Light** (2-4 hrs/week): Casual learning, longer timeline
- **Moderate** (5-8 hrs/week): Steady progress, common schedule
- **Intensive** (9-15 hrs/week): Accelerated learning, significant commitment
- **Immersion** (16+ hrs/week): Full-time focus, bootcamp-style

**Validation Rules:**
- Minimum 2 hours/week for meaningful progress
- If goal requires extensive time, verify commitment
- Flag if time budget seems unrealistic for goal

### Step 4: Modality Identification
Determine learning preferences for optimal engagement.

**Modality Assessment:**
- Ask: "How do you prefer to learn new information?"
- Present options: video, reading, hands-on, mixed
- Note: Mixed modality often produces best retention

### Step 5: Constraint Capture
Identify any limitations that affect path design.

**Common Constraints:**
- **Financial**: Free resources only, budget ceiling
- **Time**: Only available on weekends, study hours restricted
- **Access**: No high-speed internet, specific device limitations
- **Accessibility**: Screen reader needed, caption requirements
- **Schedule**: Can only study mornings, limited days per week

## Blocking Conditions

Do NOT proceed to curriculum design if:

1. **Goal is Undefined**
   - Learner cannot articulate what they want to achieve
   - Goal is too vague to design objectives
   - **Action**: Ask clarifying questions until goal is specific

2. **Time Budget is Absent**
   - Learner cannot commit to weekly hours
   - Time budget is unrealistic (< 2 hrs/week for most goals)
   - **Action**: Confirm time commitment or adjust goal scope

3. **Critical Information Missing**
   - Prior knowledge completely unknown
   - Essential constraints undisclosed
   - **Action**: Request missing information before proceeding

## Output Structure

```json
{
  "learner_profile": {
    "goal": {
      "original_input": "string",
      "refined_goal": "Specific, measurable objective",
      "bloom_level": "Apply/Analyze/Create/etc",
      "measurable_outcome": "Observable result"
    },
    "current_level": {
      "self_assessment": "Beginner/Intermediate/Advanced",
      "prior_knowledge": ["List of related knowledge"],
      "prerequisite_gaps": ["Missing prerequisites"],
      "diagnostic_results": {
        "checkpoint_questions": ["Question 1", "Question 2"],
        "responses": ["Answer 1", "Answer 2"],
        "estimated_level": "quantitative assessment"
      }
    },
    "time_budget": {
      "weekly_hours": number,
      "total_weeks": number,
      "category": "Light/Moderate/Intensive/Immersion",
      "deadline": "YYYY-MM-DD or null"
    },
    "modality": {
      "primary": "video/reading/hands-on/mixed",
      "secondary": "backup preference",
      "accessibility_needs": ["any specific requirements"]
    },
    "constraints": {
      "budget": "limitation or none",
      "schedule": "restrictions",
      "equipment": "required resources",
      "other": "additional limitations"
    }
  }
}
```

## Error Handling

### Goal Too Vague
**Response Template:**
```
I'd like to help you design a learning path, but I need to understand your goal more specifically. 

Instead of "learn [topic]", could you tell me:
- What specific outcome do you want to achieve?
- How will you use what you learn?
- What does success look like to you?

For example: "Build a personal blog using React" or "Pass the AWS certification exam"
```

### Time Budget Uncertain
**Response Template:**
```
To design an effective learning path, I need to understand your time commitment. 

How many hours per week can you realistically dedicate to learning?
- Light: 2-4 hours/week (casual learning, longer timeline)
- Moderate: 5-8 hours/week (steady progress)
- Intensive: 9-15 hours/week (accelerated learning)

If you're unsure, start with a conservative estimate—we can always adjust later.
```

### Prior Knowledge Unknown
**Response Template:**
```
To design an appropriate starting point, I'd like to assess your current level. 

Quick questions:
1. What experience do you have with [topic]?
2. What concepts are you already familiar with?
3. Have you tried to learn this before? If so, how did it go?

This helps me place you at the right level and identify any prerequisites you might need.
```

## Quality Gates

Before completing the intake, verify:

- [ ] Goal is specific and measurable
- [ ] Goal can be expressed as a Bloom's-level objective
- [ ] Prior knowledge has been assessed
- [ ] Prerequisite gaps are identified
- [ ] Weekly time budget is defined and ≥ 2 hours
- [ ] Learning modality preference is captured
- [ ] Constraints are documented
- [ ] All blocking conditions have been resolved

## Integration Notes

This sub-skill is the entry point for the personalized learning path designer. It must complete successfully before any framework selection or curriculum design can proceed. The learner profile object produced here is consumed by:

- `sub-framework-selector` — Uses goal type and learner characteristics
- `sub-scoring-engine` — Uses time budget for feasibility assessment
- `sub-improvement-roadmap` — Uses modality and constraints for path customization

## Tools Required
- Read — Access intake templates and question banks
- Write — Generate learner profile documentation
