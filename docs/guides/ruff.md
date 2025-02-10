# Ruff

Ruff is an extremely fast Python linter, formatter, and code assistant. It's written in Rust and is designed to be a drop-in replacement for tools like Flake8, pycodestyle, pyupgrade, isort, and others.

- [Ruff](#ruff)
  - [Key Features](#key-features)
  - [Ruff in this Project](#ruff-in-this-project)
    - [Configuration (`ruff.toml`)](#configuration-rufftoml)
    - [Usage](#usage)
      - [Pre-commit Hooks](#pre-commit-hooks)
      - [Command Line](#command-line)
    - [Integrating with Editors](#integrating-with-editors)
    - [Customizing Ruff](#customizing-ruff)
    - [Pydocstyle Convention](#pydocstyle-convention)

## Key Features

- **Extremely Fast**: Written in Rust, Ruff is significantly faster than traditional Python linters.
- **Comprehensive**: Combines the functionality of multiple tools, including linters, formatters, and code fixers.
- **Configurable**: Highly customizable through the `ruff.toml` configuration file.
- **Easy to Integrate**: Integrates well with popular editors and CI/CD systems.
- **Automatic Fixes**: Can automatically fix many common linting errors.

## Ruff in this Project

This project uses Ruff for linting, formatting, and ensuring code quality. The configuration is managed through the `ruff.toml` file located in the root directory of the project.

### Configuration (`ruff.toml`)

The `ruff.toml` file specifies the settings for Ruff. Here's a breakdown of the key configurations:

- `exclude`: Specifies directories that Ruff should ignore, such as `.git`, `.venv`, `dist`, etc.
- `line-length`: Sets the maximum line length for the project (currently 99 characters).
- `target-version`: Specifies the target Python version (currently Python 3.12).
- `lint.select`: Defines the set of rules that Ruff should enforce. This includes:
    - `E`: pycodestyle errors
    - `N`: pep8-naming conventions
    - `F`: pyflakes
    - `D`: pydocstyle
- `lint.ignore`: Specifies rules that should be ignored. This project ignores several pydocstyle rules related to missing docstrings in certain contexts.
- `fixable`: Specifies rules that Ruff can automatically fix.
- `dummy-variable-rgx`: Configures the regular expression for dummy variable names.
- `format`: Configures code formatting options such as quote style, indentation, etc.
- `per-file-ignores`: Allows specifying different configurations for different files or directories.  Tests directory ignores missing docstrings.

### Usage

Ruff is integrated into the development workflow using pre-commit hooks, the CI/CD pipelines and will be applied in auto save mode when using VS Code.

#### Pre-commit Hooks

Ruff is configured as a pre-commit hook to automatically lint and format code before each commit. This helps ensure that all code meets the project's quality standards. To use the pre-commit hooks, make sure you have pre-commit installed and configured in your local environment.

#### Command Line

Ruff can also be run from the command line:

```bash
uv run ruff check .
uv run ruff format .
```

These commands will check and format the code in the current directory, respectively.

### Integrating with Editors

Ruff integrates with many popular code editors, such as VS Code, Sublime Text, and others. Refer to the Ruff documentation for editor-specific instructions.

### Customizing Ruff

The `ruff.toml` file can be customized to suit the specific needs of the project.  Refer to the Ruff documentation for a complete list of available options.

### Pydocstyle Convention

The `pydocstyle` section specifies the convention for docstrings. This project uses the "google" convention.
