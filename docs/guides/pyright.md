# Pyright Usage Guide

Pyright is a static type checker for Python. It helps you catch type-related errors early in the development process, improving the reliability and maintainability of your code. This guide explains how to use Pyright in this project, including configuration and best practices.

- [Pyright Usage Guide](#pyright-usage-guide)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [VS Code Integration](#vs-code-integration)
    - [Command-Line Usage](#command-line-usage)
    - [Ignoring Errors](#ignoring-errors)
  - [Integration with Ruff](#integration-with-ruff)
  - [Best Practices](#best-practices)

## Installation

Pyright is included as a development dependency in this project. You can install it using `uv`:

```bash
uv add pyright
```

## Configuration

Pyright is configured using the `pyrightconfig.json` file in the root of the project. Here's a breakdown of the configuration options:

- `pythonVersion`: Specifies the Python version used for type checking.
- `pythonPlatform`: Specifies the target platform.
- `venvPath`: Specifies the path to the virtual environment.
- `typeCheckingMode`: Specifies the type checking mode. Options include `"basic"`, `"strict"`, and `"standard"`.
- `include`: A list of directories to include in type checking.
- `exclude`: A list of directories to exclude from type checking.

```json
{
    "pythonVersion": "3.12",
    "pythonPlatform": "All",
    "venvPath": "./.venv",
    "typeCheckingMode": "standard",
    "include": [
        "src/",
        "tests/"
    ],
    "exclude": [
        "**/__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        ".venv"
    ]
}
```

## Usage

To run Pyright, use the following command:

```bash
uv run pyright
```

This will analyze the code in the `src/` and `tests/` directories based on the configuration in `pyrightconfig.json`.

### VS Code Integration

For VS Code, the [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension provides excellent integration with Pyright. It offers real-time type checking and code completion as you type.

To enable Pylance, install the extension and ensure that it is configured to use the project's Python environment.

### Command-Line Usage

You can also run Pyright from the command line using the `pyright` command. This is useful for CI/CD pipelines and pre-commit hooks.

```bash
uv run pyright
```

### Ignoring Errors

Sometimes, you may want to ignore specific Pyright errors. You can do this using the `# pyright: ignore` comment.

```python
x = 1  # pyright: ignore
```

You can also ignore specific error codes:

```python
x = 1  # pyright: ignore[reportGeneralTypeIssues]
```

## Integration with Ruff

This project uses [Ruff](https://github.com/charliermarsh/ruff) for linting and formatting. Ruff can also run Pyright as part of its checks. To enable this, configure Ruff to include Pyright rules. However, in this project, we run pyright separately.

## Best Practices

- Write type hints for all functions and variables.
- Use the `typing` module for advanced type hinting.
- Run Pyright regularly to catch errors early.
- Configure your editor to use Pylance for real-time type checking.

By following these guidelines, you can ensure that your code is well-typed and maintainable.
