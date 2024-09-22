# Python project template

A simple template to get you started with your next Python project.

## Usage
1. On the top right corner of the github page click: "Use this template" -> "Create a new repository"
1. Create your new repository as desired.
1. Clone the newly created repository to your local machine.
1. Give execute permissions to the rename script:
```shell
chmod 700 ./rename.sh
```
1. Execute the rename script to rename the project to your desired new name. For example, to rename from "project_name" to "my_project" do:
```shell
./rename.sh my_project
```
1. Delete the `rename.sh` script:
```shell
rm rename.sh
```
1. Enjoy!


## Includes
- [Github Actions](https://github.com/features/actions): ready to use github CI action (with dependency caching included).
- [Pre-commit](https://pre-commit.com/): comprehensive set pre-commit hooks already defined.
- [Pydantic](https://docs.pydantic.dev/latest/): for settings management.
- [Structlog](https://www.structlog.org/en/stable/index.html): for structured logging.
- [Poetry](https://python-poetry.org/): for dependency and virtual environment management.
- [Ruff](https://github.com/astral-sh/ruff): for formatting and linting.
- [Mypy](https://mypy.readthedocs.io/en/stable/): for type checking.
- [Pytest](https://docs.pytest.org/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/): for testing.
