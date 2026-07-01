# Personalized Learning Path Designer

<div align="center">

**Evidence-based curriculum design grounded in learning science**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-purple.svg)](https://claude.ai/claude-code)

</div>

## Overview

The Personalized Learning Path Designer is a Claude Code skill that profiles learners and creates customized, sequenced learning paths grounded in evidence-based pedagogical frameworks. Unlike generic course recommendations, this skill designs complete curricula with explicit spaced-repetition schedules, mastery checkpoints, and continuous improvement mechanisms.

### What It Does

- **Profile Learners**: Captures goals, prior knowledge, time constraints, and learning preferences
- **Apply Learning Science**: Uses frameworks like Backward Design, Bloom's Taxonomy, Spaced Repetition, and Cognitive Load Theory
- **Design Curricula**: Creates week-by-week learning paths with objectives, activities, and assessments
- **Score Quality**: Evaluates curriculum designs against evidence-based criteria
- **Ensure Retention**: Includes explicit spaced-repetition schedules (not optional suggestions)
- **Provide Roadmaps**: Delivers actionable improvement plans for both the curriculum and the learning process

### Ideal For

- **Students**: "Learn calculus for my exam in 8 weeks, 10 hrs/week"
- **Working Professionals**: "Learn data engineering, 5 hrs/week, 6 months"
- **Career Switchers**: "Transition from marketing to UX design"
- **Lifelong Learners**: Anyone wanting structured, evidence-based learning paths

## Quick Start

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/personalized-learning-path-designer.git
   cd personalized-learning-path-designer
   ```

2. **Install dependencies** (optional, for knowledge updater):
   ```bash
   pip install -r requirements.txt
   ```

3. **Use with Claude Code**:
   - Ensure this skill is in your Claude skills directory
   - Invoke the skill when you need a personalized learning path

### Basic Usage

Once installed, simply describe your learning goal to Claude:

```
I want to learn Python for data analysis. I can study 6 hours per week
and have 12 weeks before I need to use it for a project. I prefer
hands-on learning.
```

The skill will guide you through:

1. **Goal Clarification**: Making your objective specific and measurable
2. **Framework Selection**: Choosing appropriate pedagogical frameworks
3. **Curriculum Design**: Creating a sequenced learning path
4. **Quality Scoring**: Evaluating the design against learning science
5. **Roadmap Generation**: Producing an actionable plan with assessments and schedules

## Architecture

### Harness Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Personalized Learning Path Designer               │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
            ┌───────▼────────┐          ┌────────▼────────┐
            │  Intake Phase  │          │  Knowledge Base │
            │  (Profile      │          │  (SECOND-KNOW-  │
            │   Learner)      │          │   LEDGE-BRAIN)  │
            └───────┬────────┘          └─────────────────┘
                    │
                    └──────────────┐
                                   │
                    ┌──────────────▼──────────────┐
                    │   Framework Selection Phase  │
                    │   (Backward Design, Bloom's, │
                    │    Spaced Repetition, etc.)   │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │      Research Phase         │
                    │  (Current resources, best    │
                    │   practices, comparisons)    │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │     Scoring Phase           │
                    │  (Quality assessment,       │
                    │   feasibility analysis)      │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │    Roadmap Generation       │
                    │  (Week-by-week path,         │
                    │   assessments, schedules)    │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │      Synthesis Phase        │
                    │  (Complete learning path    │
                    │   with improvements)         │
                    └─────────────────────────────┘
```

### Sub-Skills

| Sub-Skill | Purpose | Key Output |
|-----------|---------|------------|
| `sub-profile-intake` | Profile learner and capture constraints | Learner profile object |
| `sub-framework-selector` | Select evidence-based pedagogical frameworks | Framework set with rationale |
| `sub-scoring-engine` | Score curriculum quality | Quality assessment with recommendations |
| `sub-improvement-roadmap` | Generate actionable learning path | Complete roadmap with schedules |

## Learning Science Frameworks

This skill is grounded in well-established pedagogical frameworks:

- **Backward Design (UbD)**: Design from objectives → assessments → activities
- **Bloom's Taxonomy**: Classify objectives at appropriate cognitive levels
- **Spaced Repetition**: Schedule reviews at expanding intervals for retention
- **Cognitive Load Theory**: Manage intrinsic, extraneous, and germane load
- **Deliberate Practice**: Focused practice at ability boundaries with feedback
- **Zone of Proximal Development**: Target learning just beyond current ability
- **Mastery Learning**: Advance based on demonstrated mastery, not time

Each framework is cited from our knowledge base ([`SECOND-KNOWLEDGE-BRAIN.md`](SECOND-KNOWLEDGE-BRAIN.md)), which is continuously updated with current research.

## Example Output

```markdown
# Personalized Learning Path — Python for Data Analysis

## 1. Learner Profile Summary
- **Goal**: Learn Python for data analysis project
- **Current Level**: Novice programmer, some statistics background
- **Time Budget**: 6 hours/week for 12 weeks (72 hours total)
- **Modality**: Hands-on with visual supplements
- **Deadline**: 12 weeks from start

## 2. Learning Frameworks Applied
- **Backward Design**: Structure and alignment
- **Bloom's Taxonomy**: Objective classification
- **Spaced Repetition**: Retention optimization
- **Cognitive Load Theory**: Manage complexity
- **Deliberate Practice**: Build coding skills

## 3. Week-by-Week Learning Path

### Week 1-2: Python Fundamentals
**Learning Objective**: Apply (Apply) Write basic Python programs using variables, data types, and control structures.

**Activities**:
- Interactive Python tutorial (4 hours)
- Practice exercises (6 hours)
- Mini-project: Simple calculator (2 hours)

**Resources**:
- Python Official Tutorial
- Real Python: Python Basics

**Formative Assessment**: Complete 10 coding problems with 80% accuracy
**Hours**: 12/12

### Week 3-4: Data Structures and Functions
[Continue pattern...]

## 4. Assessment Structure

### Formative Assessments
- Week 2: Python basics quiz
- Week 4: Data structures implementation
- Week 6: Data manipulation challenge
- Week 8: Analysis project component
- Week 10: Visualization task

### Summative Milestones

#### Milestone 1: Core Python Competence — Week 6
- **Objectives Assessed**: Weeks 1-6
- **Assessment Task**: Build a data processing script
- **Mastery Criteria**: Script runs without errors, handles edge cases
- **Progression Gate**: Must achieve mastery to continue

## 5. Spaced Repetition Schedule

| Topic | Initial | Review 1 | Review 2 | Review 3 | Review 4 |
|-------|---------|----------|----------|----------|----------|
| Variables | Week 1 | Week 2 | Week 4 | Week 8 | Week 12 |
| Data Types | Week 1 | Week 2 | Week 4 | Week 8 | Week 12 |
| Control Flow | Week 2 | Week 3 | Week 5 | Week 9 | Week 12 |

## 6. Improvement Actions

| Priority | Criterion | Current | Target | Action | Effort | Impact |
|----------|-----------|---------|--------|--------|--------|--------|
| High | Retention Design | 2.5/4 | 3.5/4 | Add retrieval practice to reviews | 2 hrs | +10 points |
```

## Knowledge Base

The [`SECOND-KNOWLEDGE-BRAIN.md`](SECOND-KNOWLEDGE-BRAIN.md) file contains:

- Core learning science frameworks and their applications
- Scoring criteria mapped to frameworks
- Key research papers and findings
- State-of-the-art methods and tools
- Authoritative data sources
- Auto-update protocol and logs

This knowledge base is continuously updated through automated crawling of:
- ERIC (Education Resources Information Center)
- ArXiv cs.CY (Computers and Society category)
- OECD Education reports

## Knowledge Updater

The [`tools/knowledge_updater.py`](tools/knowledge_updater.py) script maintains the knowledge base:

```bash
# Dry run to see what would be added
python tools/knowledge_updater.py --dry-run

# Update knowledge base
python tools/knowledge_updater.py
```

**Schedule**: Run weekly (recommended via cron)

**Dependencies**: 
- Optional: `crawl4ai` for web crawling (degrades gracefully without it)

## Testing

Test scenarios are documented in [`tests/test-scenarios.md`](tests/test-scenarios.md):

1. **Exam-deadline student**: Time-constrained, outcome-focused
2. **Time-constrained professional**: Limited hours, long timeline
3. **Career switcher**: Prerequisite gaps, portfolio needs
4. **Unrealistic goal/time**: Feasibility validation and rescope
5. **Child learner**: Age-appropriate design considerations
6. **Offline mode**: Degraded operation without web access

## Contributing

We welcome contributions! Areas of particular interest:

1. **Additional Frameworks**: Implement new evidence-based pedagogical frameworks
2. **Domain-Specific Paths**: Specialized paths for specific domains
3. **Knowledge Expansion**: Add sources and improve the knowledge base
4. **Testing**: Create additional test scenarios and validation

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch
3. Make your changes with clear commit messages
4. Ensure all quality gates pass
5. Submit a pull request with description

### Code Standards

- Python: Follow PEP 8 style guidelines
- Documentation: Use clear, concise English
- Skills: Follow Claude skill format specifications
- Citations: Always cite framework sources from knowledge base

## Quality Assurance

All curriculum designs must pass these quality gates:

- [ ] Goal is specific and measurable
- [ ] Weekly time budget is defined and feasible
- [ ] Backward Design structure is evident
- [ ] Each scoring criterion maps to a named framework
- [ ] Spaced-repetition schedule is explicit
- [ ] Milestone assessments are defined with mastery criteria
- [ ] Cognitive load is managed
- [ ] Feasibility has been validated
- [ ] Offline limitations are flagged if applicable

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Built on the foundational work of learning science researchers:

- **Grant Wiggins and Jay McTighe** — Backward Design / Understanding by Design
- **Benjamin Bloom** — Bloom's Taxonomy, Mastery Learning
- **Robert Bjork** — Spaced Repetition, Desirable Difficulties
- **John Sweller** — Cognitive Load Theory
- **Lev Vygotsky** — Zone of Proximal Development
- **Anders Ericsson** — Deliberate Practice
- **Deci and Ryan** — Self-Determination Theory

## Contact & Support

- **Issues**: Report bugs and feature requests via GitHub Issues
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Documentation**: See inline documentation in skill files

## Roadmap

### Current Version: 1.0.0

**Completed Features:**
- ✅ Core sub-skills implemented
- ✅ Learning science frameworks documented
- ✅ Quality gates and scoring system
- ✅ Knowledge updater tool
- ✅ Comprehensive test scenarios

**Planned Enhancements:**
- 🔲 Domain-specific skill trees
- 🔲 Progress tracking dashboard
- 🔲 Collaborative learning paths
- 🔲 Integration with learning platforms
- 🔲 Mobile app interface

---

<div align="center">

**Built with 🧠 for evidence-based learning**

[⭐ Star us on GitHub](https://github.com/your-username/personalized-learning-path-designer)

</div>
