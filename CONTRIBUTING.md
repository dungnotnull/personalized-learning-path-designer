# Contributing to Personalized Learning Path Designer

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

Before creating bug reports or feature requests, please check existing issues to avoid duplicates.

When creating an issue, include:

- **Clear title and description**: What you're trying to do and what happened
- **Steps to reproduce**: Minimal reproduction steps
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Environment**: OS, Python version, relevant configurations
- **Screenshots/logs**: If applicable

### Submitting Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** with clear, focused commits
3. **Write tests** for new functionality (see `tests/test_scenarios.py` for examples)
4. **Ensure all tests pass** locally
5. **Update documentation** if you've changed functionality
6. **Submit your pull request** with a clear description of changes

## Development Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Installation

```bash
# Clone your fork
git clone https://github.com/your-username/personalized-learning-path-designer.git
cd personalized-learning-path-designer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Run tests with coverage
pytest --cov=tests tests/
```

## Project Structure

```
personalized-learning-path-designer/
├── CLAUDE.md                    # Project instructions
├── README.md                    # Project overview
├── CONTRIBUTING.md             # This file
├── LICENSE                     # MIT License
├── SECOND-KNOWLEDGE-BRAIN.md   # Knowledge base
├── PROJECT-detail.md           # Detailed project documentation
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Development progress
├── skills/                     # Claude skill files
│   ├── main.md                 # Main skill orchestration
│   ├── sub-profile-intake.md
│   ├── sub-framework-selector.md
│   ├── sub-scoring-engine.md
│   └── sub-improvement-roadmap.md
├── tools/                      # Supporting tools
│   └── knowledge_updater.py    # Knowledge base updater
├── tests/                      # Test suite
│   ├── test-scenarios.md       # Scenario documentation
│   └── test_scenarios.py       # Executable test implementation
├── examples/                   # Usage examples
│   ├── exam_preparation.md
│   └── professional_transition.md
├── config/                     # Configuration (gitignored)
└── pyproject.toml             # Project configuration
```

## Coding Standards

### Python Code
- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Include docstrings for functions and classes
- Write tests for new functionality
- Keep functions focused and modular

Example:
```python
def validate_learner_profile(profile: Dict[str, Any]) -> List[str]:
    """
    Validate learner profile completeness.

    Args:
        profile: Dictionary containing learner information

    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    if not profile.get("goal"):
        errors.append("Missing required field: goal")
    return errors
```

### Skill Files (Markdown)
- Use clear section headers (##, ###)
- Include examples for complex concepts
- Reference frameworks with citations
- Maintain consistent structure across files

### Documentation
- Use clear, concise language
- Include examples where helpful
- Update relevant sections when making changes
- Maintain consistent formatting

## Testing

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific scenario
pytest tests/test_scenarios.py::test_scenario_1

# Run with verbose output
pytest tests/ -v

# Generate coverage report
pytest --cov=tests tests/ --cov-report=html
```

### Writing Tests

When adding new functionality, write tests that:

1. **Cover normal cases**: Expected usage scenarios
2. **Cover edge cases**: Boundary conditions and unusual inputs
3. **Test error handling**: Invalid inputs and error conditions
4. **Are maintainable**: Clear test names and assertions

Example test structure:
```python
def test_specific_functionality():
    # Arrange
    input_data = {...}

    # Act
    result = function_under_test(input_data)

    # Assert
    assert result["expected_field"] == expected_value
```

## Areas for Contribution

We welcome contributions in these areas:

### 1. Additional Learning Frameworks
- Implement new evidence-based pedagogical frameworks
- Add framework citations to SECOND-KNOWLEDGE-BRAIN.md
- Update scoring criteria appropriately

### 2. Domain-Specific Paths
- Create specialized paths for specific domains (e.g., language learning, music)
- Add domain-appropriate assessment strategies
- Identify domain-specific resources

### 3. Knowledge Base Expansion
- Add authoritative sources to SECOND-KNOWLEDGE-BRAIN.md
- Improve crawler sources in knowledge_updater.py
- Add recent research findings

### 4. Testing
- Create additional test scenarios
- Improve test coverage
- Add integration tests

### 5. Documentation
- Improve existing documentation clarity
- Add more usage examples
- Translate documentation to other languages

### 6. Tools and Utilities
- Improve knowledge_updater.py functionality
- Add new supporting tools
- Create visualization tools for learning paths

## Commit Messages

Use clear, descriptive commit messages:

```
# Good
Add spaced-repetition validation to scoring engine
Fix prerequisite gap detection in roadmap generation
Update framework citations for Cognitive Load Theory

# Avoid
Fix bug
Update stuff
Make changes
```

## Release Process

Releases are managed by project maintainers:

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md (if applicable)
3. Create git tag
4. Publish release notes

## Code Review

All pull requests require review. Reviewers check:

- Code follows project standards
- Tests are included and passing
- Documentation is updated
- Changes align with project goals

## Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and ideas
- **Existing Documentation**: Check README and skill files first

## License

Contributions are accepted under the MIT License. By submitting, you agree that your contributions will be licensed under the same license.

## Code of Conduct

Be respectful, constructive, and inclusive. We welcome contributors from all backgrounds and experience levels.
