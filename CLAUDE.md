# Claude Code Configuration

## Project Overview

Python project template with modern tooling and best practices.

**Stack:** Python 3.12+, UV, Pydantic, Structlog, Ruff, Mypy, Pytest

## Key Commands

```bash
# Testing
uv run pytest
uv run pytest --cov

# Code Quality
uv run ruff format
uv run ruff check --fix
uv run mypy .

# Setup
uv sync
uv run pre-commit install
```

## Structure

- `src/` - Source code
- `tests/` - Test files
- `pyproject.toml` - Project config

## Notes

- Uses UV for dependency management
- Follows strict type checking and linting
- Run tests and type checks after changes
- Environment config via `.env` file
