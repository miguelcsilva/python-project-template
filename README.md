# Python project template

💻 A simple template to get you started with your next Python project.

## ✨ Main Features
- 🔨 [Github Actions](https://github.com/features/actions): ready to use github CI action (with dependency caching included).
- ⚡️ [Pre-commit](https://pre-commit.com/): comprehensive set pre-commit hooks already defined.
- 🔧 [Pydantic](https://docs.pydantic.dev/latest/): for settings management.
- 🔊 [Structlog](https://www.structlog.org/en/stable/index.html): for structured logging.
- 📌 [Poetry](https://python-poetry.org/): for dependency and virtual environment management.
- 📝 [Ruff](https://github.com/astral-sh/ruff): for formatting and linting.
- 🏷️ [Mypy](https://mypy.readthedocs.io/en/stable/): for type checking.
- 🧪 [Pytest](https://docs.pytest.org/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/): for testing.


## 💥 When you run it
![Untitled design](https://github.com/user-attachments/assets/a0276a80-f405-4ebc-93b6-4e36b798ee58)

## 📦️ Usage
-  On the top right corner of the github page click: "Use this template" -> "Create a new repository"
- Create your new repository as desired.
- Clone the newly created repository to your local machine.
- Give execute permissions to the rename script:
```shell
chmod 700 ./rename.sh
```
- Execute the rename script to rename the project to your desired new name. For example, to rename from "project_name" to "my_project" do:
```shell
./rename.sh my_project
```
- Delete the `rename.sh` script:
```shell
rm rename.sh
```
- Enjoy!

## Adaptable settings
Allows for the following out of the box:
- Handle multiple running environments (`production`, `local`, etc.)
- Easily control the logging level.
- Log in either plain text or json.
- Control the logging level of third-party libraries.

## 🏗️ Folder structure
Simple and standardized folder structure so that you can start coding immediately.
```shell
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│  └── project_name
│     ├── \_\_init\_\_.py
│     ├── \_\_main\_\_.py
│     ├── log.py
│     └── settings.py
└── tests
   ├── \_\_init\_\_.py
   ├── test_log.py
   └── test_settings.py
```
