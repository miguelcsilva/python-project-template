# Python Project Template

A **modern Python project template** with best practices and tooling configured out of the box.
*Get up and running in minutes, not hours!*

## Features

- 🚀 **CI/CD**: [GitHub Actions](https://github.com/features/actions) workflow with dependency caching
- 🔍 **Code Quality**: [Pre-commit](https://pre-commit.com/) hooks for automated code quality checks
- ⚙️ **Configuration**: [Pydantic](https://docs.pydantic.dev/latest/) for type-safe settings management
- 📝 **Logging**: [Structlog](https://www.structlog.org/en/stable/index.html) for structured logging
- ⚡ **Dependencies**: [UV](https://docs.astral.sh/uv/) for fast dependency and virtual environment management
- 🎨 **Formatting & Linting**: [Ruff](https://github.com/astral-sh/ruff) for code formatting and linting
- 🔒 **Type Checking**: [Mypy](https://mypy.readthedocs.io/en/stable/) for static type checking
- 🧪 **Testing**: [Pytest](https://docs.pytest.org/) with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) for coverage

## Example Output

When you run the project, you'll see different logging formats depending on your configuration:

### Textual Logs (Human-Readable)
![Untitled design](https://github.com/user-attachments/assets/a0276a80-f405-4ebc-93b6-4e36b798ee58)

### JSON Structured Logging (Machine-Readable)
```json
{"timestamp": "2025-09-27 16:36:15", "level": "info", "logger": "project_name", "filename": "__main__.py", "lineno": 7, "func_name": "main", "message": "Program started."}
{"exc_info": true, "timestamp": "2025-09-27 16:36:15", "level": "error", "logger": "project_name", "filename": "__main__.py", "lineno": 12, "func_name": "main", "message": "Cannot divide by 0."}
{"timestamp": "2025-09-27 16:36:15", "level": "info", "logger": "project_name", "filename": "__main__.py", "lineno": 13, "func_name": "main", "message": "Program finished."}
```

## Quick Start

To use this template:

1. **Click** "Use this template" → "Create a new repository" on GitHub
2. **Clone** your new repository locally
3. **Customize** the project:
   ```bash
   # Give execute permissions to the rename script
   chmod 700 ./rename.sh

   # Rename the project (e.g., from 'project_name' to 'my_project')
   ./rename.sh my_project

   # Clean up the rename script
   rm rename.sh
   ```

4. **Install** dependencies and set up development environment:
   ```bash
   # Install dependencies
   uv sync

   # Install pre-commit hooks
   uv run pre-commit install
   ```

## Development

### Key Commands

```bash
# Testing
uv run pytest
uv run pytest --cov

# Code Quality
uv run ruff format          # Format code
uv run ruff check --fix     # Lint and fix issues
uv run mypy .              # Type checking

# Dependencies
uv sync                    # Install/update dependencies
```

### Configuration

The template includes **flexible configuration management**:

- **Environment Support**: Handle multiple environments (`production`, `local`, etc.)
- **Logging Control**: Configurable logging levels and formats (plain text or JSON)
- **Third-party Libraries**: Control logging levels for external dependencies

## Project Structure
```shell
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│  └── project_name
│     ├── __init__.py
│     ├── __main__.py
│     ├── log.py
│     └── settings.py
└── tests
   ├── __init__.py
   ├── test_log.py
   └── test_settings.py
```
