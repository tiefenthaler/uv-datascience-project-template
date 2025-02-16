# Continuous Integration (CI)

Continuous Integration is a development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run. This helps to detect integration errors early and ensures that the codebase remains in a working state.

- [Continuous Integration (CI)](#continuous-integration-ci)
  - [Integration of Workflows and Actions](#integration-of-workflows-and-actions)
  - [CI Workflows in this Project](#ci-workflows-in-this-project)
  - [Custom GitHub Actions](#custom-github-actions)
    - [`setup-python-with-uv`](#setup-python-with-uv)
    - [`setup-git-config`](#setup-git-config)
  - [Getting Started: Set Up GitHub Actions and Workflows](#getting-started-set-up-github-actions-and-workflows)

## Integration of Workflows and Actions

The CI process is orchestrated through GitHub Actions workflows (defined in the `.github/workflows` directory). Each workflow defines a series of jobs, which in turn consist of steps. These steps can either be individual commands or calls to reusable actions.

For example, the `test.yml` workflow uses the `setup-python-with-uv` action to set up the Python environment before running tests. Similarly, the `ruff.yml` workflow uses `setup-python-with-uv` before running the Ruff linter and formatter.

This modular approach allows for a clear and maintainable CI configuration, where common setup tasks are encapsulated in reusable actions, and workflows define the overall CI process.

## CI Workflows in this Project

This project uses GitHub Actions for CI Workflows. Upon each push or pull request to the `main` branch, the following steps, defined in `.github/workflows` directory, are executed:

1. **Linting:**

      - **Ruff:** The code is checked for stylistic errors, potential bugs, and adherence to coding standards using [Ruff](https://github.com/astral-sh/ruff). This includes both linting and formatting checks.
      - **Hadolint:** The `Dockerfile` and `.devcontainer/Dockerfile.debug` are checked for errors and best practices using [Hadolint](https://github.com/hadolint/hadolint).

2. **Type Checking:**

      - **Pyright:** Static type checking is performed using [Pyright](https://github.com/microsoft/pyright) to catch type-related errors.

3. **Testing:**

      - **Pytest:** Unit tests are executed using [Pytest](https://docs.pytest.org/en/stable/) to verify the correctness of individual components.
      - **Pytest-Coverage:** Coverage reports are generated and posted as comments on pull requests using [Pytest-cov](https://pytest-cov.readthedocs.io/en/latest/).

4. **Building:**

      - **Docker:** The project's Docker image is built to ensure that all dependencies are correctly resolved and that the application can be containerized successfully. This includes building both the main `Dockerfile` and the development container `Dockerfile.debug`.

5. **Documentation Deployment:** The project documentation is automatically built and deployed to GitHub Pages using [mkdocs](https://www.mkdocs.org/).

6. **CI Workflow Status:** Provides a summary of the CI workflow status, passed and failed jobs.

You can check the status of the latest CI run on the GitHub repository under the "Actions" tab.

## Custom GitHub Actions

This project utilizes custom GitHub Actions to encapsulate reusable steps within the CI Workflows. These actions are defined in the `.github/actions` directory.

### `setup-python-with-uv`

This action sets up a Python environment using the `uv` package manager. It handles:

- Installing `uv`.
- Pinning the specified Python version.
- Caching `uv` files to speed up subsequent runs.
- Installing project dependencies using `uv sync`.

### `setup-git-config`

This action configures Git user name and email. It is used to:

- Set the Git user name to `github-actions[bot]`.
- Set the Git user email to `41898282+github-actions[bot]@users.noreply.github.com`.

## Getting Started: Set Up GitHub Actions and Workflows

To set up GitHub Actions and Workflows in your project, follow these steps:

- Create a `.github/workflows` directory in the root of your repository.
- Define your workflows in YAML files within this directory.  
      Example: `.github/workflows/pyright.yml`

      ```yaml
      name: Pyright

      on:
      push:
      branches: [main]
      pull_request:
      branches: [main]

      jobs:
      type-check:
      runs-on: ubuntu-latest

      strategy:
            matrix:
            python-version: ["3.9", "3.10", "3.11", "3.12", "3.13"]

      steps:
            - uses: jakebailey/pyright-action@v2
                  with:
                  python-version: ${{ matrix.python-version }}
      ```

- Define jobs and steps within each workflow file.
- Use reusable actions to encapsulate common steps.
      You can use existing actions from the GitHub Marketplace or create custom actions.  
      Example: `.github/actions/setup-python-with-uv/action.yml`

      ```yaml
      name: Install Python with uv
      description: |
      This GitHub Action installs Python using uv.
      It pins the specified Python version, caches uv files, and installs dependencies.

      inputs:
      python-version:
      description: Python version
      required: true

      runs:
      using: composite
      steps:
      - name: Install uv
            uses: astral-sh/setup-uv@v4
            with:
            enable-cache: true
            python-version: ${{ inputs.python-version }}

      - name: Install Dependencies
            run: uv sync --all-groups
            shell: bash
      ```

- Commit and push your changes to trigger the workflows.
      ```bash
      git add .
      git commit -m "Set up GitHub Actions for Pyright"
      git push origin main
      ```
- Monitor the Actions tab in your GitHub repository to check the status of your workflows.
      Go to the "Actions" tab in your GitHub repository to check the status of your CI workflows. You should see the workflows running based on the configuration in your workflow files.

By following these steps, you can set up GitHub Actions for Continuous Integration in your project, ensuring that your codebase is automatically tested and built upon each push or pull request.
