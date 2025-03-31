# Cookiecutter Guide

Cookiecutter is a command-line utility that creates projects from project templates. This guide explains how cookiecutter works and how it's used in this project.

## What is Cookiecutter?

Cookiecutter is a Python-based project templating tool that:

- Creates projects from templates
- Handles variable substitution
- Supports conditional file creation
- Allows for pre and post-generation hooks

## Project Configuration

The main configuration for cookiecutter is in `cookiecutter.json`. This file defines all variables that can be customized when creating a new project. Key options in this template include:

```json
{
    "project_name": "project-name",
    "project_description": "A short description of the project.",
    "author_name": "Your name (or your organization/company/team)",
    "python_version": "3.12",
    "open_source_license": ["Not open source", "MIT license", "BSD license", "Apache-2.0"],
    "docs_mkdocs": ["y", "n"],
    "use_vscode_devcontainer": ["y", "n"]
}
```

## Using This Template

To create a new project using this template:

```bash
cookiecutter gh:tiefenthaler/uv-datascience-project-template
```

You'll be prompted to provide values for each variable defined in `cookiecutter.json`.

## Template Features

The template includes hooks that:

1. **Pre-generation** (`pre_gen_project.py`):
   - Validates repository and module names
   - Checks for valid Python identifiers

2. **Post-generation** (`post_gen_project.py`):
   - Removes unused files based on your choices
   - Sets up the project structure
   - Configures selected tools

## Customization Options

The template allows you to customize:

- Project structure (`directory_structure`)
- Testing setup (`testing_framework`)
- Code quality tools (`linting_and_formatting`, `static_type_checking`)
- Documentation (`docs_mkdocs`)
- Development environment (`use_vscode_devcontainer`)
- Production setup (`use_docker_production`)

## File Generation

Based on your choices, the template will:

1. Generate appropriate configuration files
2. Set up documentation structure if `docs_mkdocs="y"`
3. Configure GitHub Actions if `github_actions_ci="y"`
4. Set up dev containers if `use_vscode_devcontainer="y"`

## Best Practices

When using this template:

1. Choose meaningful project and module names
2. Provide a clear project description
3. Review generated files before committing
4. Follow the post-generation setup instructions in the README

## Additional Resources

- [Official Cookiecutter Documentation](https://cookiecutter.readthedocs.io/)
- [Template Repository](https://github.com/tiefenthaler/uv-datascience-project-template)
