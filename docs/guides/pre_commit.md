# Using Pre-Commit Hooks

Pre-commit hooks are scripts that run automatically before each commit. They help to identify and fix issues before they are integrated into the codebase, ensuring code quality and consistency.

- [Using Pre-Commit Hooks](#using-pre-commit-hooks)
  - [Benefits of Using Pre-Commit Hooks?](#benefits-of-using-pre-commit-hooks)
  - [How to Use Pre-Commit Hooks in This Project](#how-to-use-pre-commit-hooks-in-this-project)
    - [1. Installation](#1-installation)
    - [2. Install Pre-Commit Hooks and/or Running Hooks Manually](#2-install-pre-commit-hooks-andor-running-hooks-manually)
    - [3. Configuring Hooks](#3-configuring-hooks)
    - [4. Customizing Hooks](#4-customizing-hooks)

## Benefits of Using Pre-Commit Hooks?

Pre-commit hooks automate code checks, formatting, and other tasks, saving time and effort during code reviews. They catch common problems early, preventing them from becoming bigger issues later.

## How to Use Pre-Commit Hooks in This Project

This project uses [pre-commit](https://pre-commit.com/) to manage pre-commit hooks. Here's how to get started:

### 1. Installation

Make sure you have `uv` installed. If not, refer to the [installation guide](./uv.md).

### 2. Install Pre-Commit Hooks and/or Running Hooks Manually

- Install Pre-Commit Hooks to automatically when you commit changes.
Run the following command to install the pre-commit hooks:

    ```Bash
    uv run pre-commit install
    ```

- Running Hooks Manually
If you want to run the hooks manually, use the following command:

    ```Bash
    uv run pre-commit run --all-files
    ```

### 3. Configuring Hooks

The pre-commit hooks are configured in the `.pre-commit-config.yaml` file. This file specifies the hooks to use, their settings, and other options.

Here's a breakdown of the hooks used in this project:

- **Ruff**: A fast Python linter and formatter. It checks for code style issues and automatically fixes them. Refer to the `ruff.toml` file for the configurations.
    - **Ruff Check**: Runs the Ruff linter to identify issues. The `--fix` argument automatically fixes fixable issues. `--exit-non-zero-after-fix` will cause the hook to fail if ruff makes changes.
    - **Ruff Format**: Runs the Ruff formatter to format the code. The `--diff` argument displays a diff of the changes instead of applying them directly.
- **Pyright**: A static type checker for Python. It checks for type errors in the code. Refer to the `pyrightconfig.json` file for the configurations.
- **Hadolint**: A linter for Dockerfiles. It checks for common issues and best practices in Dockerfiles. The `--config .hadolint.yaml` argument specifies a configuration file for Hadolint.

### 4. Customizing Hooks

You can customize the pre-commit hooks by modifying the `.pre-commit-config.yaml` file. You can add new hooks, remove existing hooks, or change the settings of existing hooks.

For more information on how to configure pre-commit hooks, see the [pre-commit documentation](https://pre-commit.com/index.html).
