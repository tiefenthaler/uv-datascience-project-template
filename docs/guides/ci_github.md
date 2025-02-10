# Continuous Integration (CI)

Continuous Integration is a development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run. This helps to detect integration errors early and ensures that the codebase remains in a working state.

- [Continuous Integration (CI)](#continuous-integration-ci)
  - [Integration of Workflows and Actions](#integration-of-workflows-and-actions)
  - [CI Workflows in this Project](#ci-workflows-in-this-project)
  - [Custom GitHub Actions](#custom-github-actions)
    - [`setup-python-with-uv`](#setup-python-with-uv)
    - [`setup-git-config`](#setup-git-config)

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
