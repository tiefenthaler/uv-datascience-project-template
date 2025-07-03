# Supercharge Your Data Science Projects with the UV Data Science Project Template

<div align="center">
  <img src="../readme/supercharge_python_datascience_project.png" alt="Banner" width="75%" height="75%">
  <p><em>Image by David T. [Source: Astral]</em></p>
</div>

Data science is a field that thrives on innovation, but even the most groundbreaking ideas can falter without a solid foundation. Setting up a robust, reproducible, and scalable project structure is often a daunting task. Enter the **UV Data Science Project Template** — a modern, feature-rich framework designed to streamline your workflow and provide a solid foundation for your projects.

In this article, we’ll explore why this template exists, dive into the powerful tools it integrates (like UV or Ruff), examine its structure, and see how it can transform your approach to data science projects.

<div align="center">
  <img src="../readme/cookiecutter_medium.png" alt="Banner" width="30%" height="30%">
</div>

**Key Feature:** Automatic Project Setup Generation using Cookiecutter.

Find the related [GitHub Repo](https://github.com/tiefenthaler/uv-datascience-project-template) and related [Docs](https://tiefenthaler.github.io/uv-datascience-project-template/) here.

<br /> <!--new line-->

**Table of Contents**

- [Supercharge Your Data Science Projects with the UV Data Science Project Template](#supercharge-your-data-science-projects-with-the-uv-data-science-project-template)
  - [Why Battle Setup? Use the UV Data Science Project Template](#why-battle-setup-use-the-uv-data-science-project-template)
  - [A Curated Toolkit for Modern Data Science](#a-curated-toolkit-for-modern-data-science)
    - [**UV: The Swift Foundation**](#uv-the-swift-foundation)
    - [**Ruff: Lightning-Fast Linting and Formatting**](#ruff-lightning-fast-linting-and-formatting)
    - [**Pyright: Robust Type Checking**](#pyright-robust-type-checking)
    - [**Pytest and Coverage.py: Ensuring Reliability**](#pytest-and-coveragepy-ensuring-reliability)
    - [**Pre-Commit Hooks: Quality Control at Commit Time**](#pre-commit-hooks-quality-control-at-commit-time)
    - [**CI with GitHub Actions: Automated Workflows**](#ci-with-github-actions-automated-workflows)
    - [**MkDocs: Professional Project Documentation**](#mkdocs-professional-project-documentation)
    - [**Docker Production: Consistent Environments Anywhere**](#docker-production-consistent-environments-anywhere)
    - [**VSCode DevContainer: Seamless Development Environments**](#vscode-devcontainer-seamless-development-environments)
      - [Usage](#usage)
      - [Benefits](#benefits)
  - [Project Structure: A Place for Everything](#project-structure-a-place-for-everything)
  - [Example Use Case: Autoencoder for Image Compression](#example-use-case-autoencoder-for-image-compression)
    - [Objective](#objective)
    - [Dataset](#dataset)
    - [Implementation](#implementation)
    - [FastAPI Integration](#fastapi-integration)
  - [Automate Project Kick-off with Cookiecutter](#automate-project-kick-off-with-cookiecutter)
    - [How to Use](#how-to-use)
  - [Conclusion: Build Better, Faster](#conclusion-build-better-faster)

## Why Battle Setup? Use the UV Data Science Project Template

The UV Data Science Project Template is engineered to tackle common challenges during setup and development of data science projects by providing a structured environment that ensures your projects are:

- **Reproducible by Design**: Forget "it works on my machine." By leveraging **Docker** for containerization and **UV** for precise dependency management, the template creates isolated, consistent environments every time, everywhere.
- **Collaboration-Ready**: Stop reinventing the wheel for team workflows. Pre-configured CI/CD pipelines using **GitHub Actions**, automated code quality checks with **pre-commit hooks**, and standardized documentation tools (**MkDocs**) make teamwork seamless and efficient.
- **Scalable from the Start**: Transitioning from development to production shouldn't be an afterthought. With production-ready configurations and tools like **Docker**, the template is built for deploying and scaling your data science applications.

By adopting this template, you free yourself to focus on what truly matters: extracting insights, building models, and solving complex data problems, rather than wrestling with the project setup.

## A Curated Toolkit for Modern Data Science

The UV Data Science Project Template integrates a suite of powerful, best-in-class tools, each chosen to optimize specific parts of the data science project development lifecycle.

| Tool                        | Description                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------|
| **UV**                      | A fast and efficient package manager for Python, written in Rust. It replaces tools like pip and virtualenv. |
| **Ruff**                    | An extremely fast Python linter, formatter, and code assistant, written in Rust.                  |
| **PyRight**                 | A static type checker for Python, helping to catch type-related errors early in the development process. |
| **PyTest**                  | A powerful and flexible testing framework for Python, simplifying writing and running tests.      |
| **Coverage**                | A tool for measuring code coverage of Python programs, helping to ensure that all parts of the code are tested. |
| **Pre-Commit**              | A framework for managing and maintaining multi-language pre-commit hooks to ensure code quality.  |
| **CI-GitHub**               | Continuous Integration setup using GitHub Actions to automate testing, linting, and deployment.   |
| **MkDocs**                  | A static site generator geared towards building project documentation, written in Markdown.       |
| **VSCode-DevContainer**     | A development environment setup using Docker and VS Code, providing a consistent and isolated workspace. |
| **Docker-Production**       | Docker setup for creating a lean, efficient, and secure production environment for applications.  |
| **Cookiecutter**       | A command-line utility that creates projects from project templates.  |

### **UV: The Swift Foundation**

[UV](https://github.com/astral-sh/uv) is an extremely fast Python package installer and resolver, written in Rust by Astral (the makers of Ruff). It aims to be a drop-in replacement for tools like `pip`, `pip-tools`, and `virtualenv`.

- **Blazing Fast Dependency Management**: Resolves and installs packages significantly faster than traditional tools.
- **Unified Environment Management**: Creates and manages virtual environments seamlessly.
- **Project Packaging**: Simplifies building and distributing your Python projects.
- **Usage**: Manage dependencies, run scripts, and handle virtual environments effortlessly. For example:

    ```bash
    # Add a new dependency
    uv add pytest

    # Install dependencies from pyproject.toml
    uv sync

    # Run pytest within the managed environment
    uv run pytest
    ```

For more details, refer to the [UV Guide](https://tiefenthaler.github.io/uv-datascience-project-template/guides/uv/).

### **Ruff: Lightning-Fast Linting and Formatting**

[Ruff](https://github.com/astral-sh/ruff) is an incredibly fast Python linter and formatter, also written in Rust. It can replace multiple tools like Flake8, isort, and Black, dramatically speeding up code quality checks.

- **Comprehensive Code Quality**: Enforces style consistency, identifies potential bugs, and sorts imports automatically.
- **Pre-Commit Integration**: Ensures code is linted and formatted *before* it even gets committed.
- **Usage**: Keep your codebase clean and consistent with simple commands:

    ```bash
    # Check for linting errors
    uv run ruff check .

    # Format the codebase
    uv run ruff format .
    ```

For configuration details, see the [Ruff Guide](https://tiefenthaler.github.io/uv-datascience-project-template/guides/ruff/).

### **Pyright: Robust Type Checking**

[Pyright](https://github.com/microsoft/pyright), developed by Microsoft, is a fast static type checker for Python. Catching type errors early saves debugging time down the line.

- **Static Analysis**: Verifies type annotations for functions, variables, and data structures, preventing runtime errors.
- **Usage**: Integrated into the CI pipeline and runnable locally:

    ```bash
    uv run pyright
    ```

Learn more in the [Pyright Guide](https://tiefenthaler.github.io/uv-datascience-project-template/guides/pyright/).

### **Pytest and Coverage.py: Ensuring Reliability**

Reliable code requires thorough testing. [Pytest](https://pytest.org) makes writing tests simple and powerful, while [Coverage.py](https://coverage.readthedocs.io/) measures your test coverage.

- **Effective Testing**: Write and run unit, integration, or functional tests with Pytest's intuitive framework.
- **Code Coverage Insights**: Identify which parts of your code aren't covered by tests, guiding further testing efforts.
- **Usage**: Execute tests and get a coverage report:

    ```bash
    uv run pytest --cov
    ```

For detailed instructions, refer to the [Pytest Guide](https://tiefenthaler.github.io/uv-datascience-project-template/guides/pytest/).

### **Pre-Commit Hooks: Quality Control at Commit Time**

[Pre-commit](https://pre-commit.com/) hooks run checks on your code *before* you commit it, catching issues early and enforcing standards across the team.

- **Automated Checks**: The template includes hooks for Ruff (linting/formatting) and Pyright (type checking).
- **Usage**: Install once, and it runs automatically on `git commit`.

    ```bash
    # Install the hooks
    uv run pre-commit install

    # Run hooks manually on all files
    uv run pre-commit run --all-files
    ```

For setup and customization, refer to the [Pre-Commit Guide](https://tiefenthaler.github.io/uv-datascience-project-template/guides/pre_commit/).

### **CI with GitHub Actions: Automated Workflows**

[GitHub Actions](https://github.com/features/actions) automate your CI/CD (Continuous Integration/Continuous Deployment) pipelines directly within your repository.

- **Automated Quality Gates**: Automatically run linting, type checking, and tests on every push or pull request.
- **Streamlined Deployment**: Automate tasks like building documentation and deploying it to GitHub Pages.
- **Usage**: Defined in `.github/workflows/`, these pipelines run automatically based on repository events.

For more information, see the [CI Guide](https://tiefenthaler.github.io/uv-datascience-project-template/guides/ci_github/).

### **MkDocs: Professional Project Documentation**

Clear documentation is crucial for maintainability and collaboration. [MkDocs](https://www.mkdocs.org/) generates a polished static website from your Markdown files.

- **Effortless Documentation**: Write docs in familiar Markdown; MkDocs handles the rest.
- **Helpful Plugins**: Includes `mkdocstrings` to generate API documentation directly from your code's docstrings and `mkdocs-material` for a modern, responsive theme.
- **Usage**: Keep documentation in the `docs/` folder and preview changes locally:

    ```bash
    uv run mkdocs serve
    ```

For setup and deployment, see the [MkDocs Guide](./guides/mkdocs.md).

### **Docker Production: Consistent Environments Anywhere**

[Docker](https://www.docker.com/) containerizes your application, ensuring it runs identically regardless of the underlying system.

- **Development Consistency**: Use the provided `docker-compose.yml` for an easy-to-set-up, isolated development environment.
- **Optimized Production Images**: Leverage the `multistage.Dockerfile` to build lean, secure images suitable for deployment.
- **Usage**: Build and run your application within a container:

    ```bash
    docker-compose up --build
    ```

For a detailed breakdown, refer to the [Docker Production Guide](https://tiefenthaler.github.io/uv-datascience-project-template/guides/docker_prod/).

### **VSCode DevContainer: Seamless Development Environments**

The **VSCode DevContainer** setup simplifies development by providing a pre-configured, containerized environment tailored for data science projects. It ensures consistency across different systems and eliminates the "it works on my machine" problem.

- **Pre-Configured Environment**: Includes Python, UV, Docker, and essential VSCode extensions like Python, Jupyter, and Ruff.
- **Volume Mapping**: Syncs your local files with the container, enabling real-time updates without rebuilding the image.
- **Multi-Stage Build**: Optimizes the container size while maintaining all necessary tools for development.

#### Usage

1. **Install Prerequisites**:
      - Install Docker Desktop.
      - Install VSCode and the Remote - Containers extension.

2. **Start the DevContainer**:
      - Open the project in VSCode.
      - Use the command palette (`F1`) and select "Open Folder in Container...".

3. **Run the Application**:
      - Run demo.py in the Python virtual environment: `uv run main.py`.
      - The FastAPI application is available at `http://localhost:8000`.
      - Test endpoints using `curl`:

        ```bash
        curl -X GET http://localhost:8000/
        curl -X POST http://localhost:8000/train
        curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"n_fake_images": 1}'
        ```

#### Benefits

- **Consistency**: Ensures all team members work in the same environment.
- **Customization**: Easily extend the setup with additional tools or configurations.
- **Integration**: Works seamlessly with Docker Compose and GitHub Actions.

For more details, refer to the [DevContainer Guide](https://tiefenthaler.github.io/uv-datascience-project-template/guides/docker_vscode_devcontainer/).

## Project Structure: A Place for Everything

The UV Data Science Project Template provides a logical and extensible directory structure:

- **`src/`**: Contains your core Python source code. The example includes:
  - A PyTorch Lightning-based autoencoder model (`src/lit_auto_encoder.py`).
  - Training logic (`src/train_autoencoder.py`).
  - A FastAPI application (`src/app_fastapi_autoencoder.py`) to serve the ML model.
- **`tests/`**: Houses unit and integration tests written using Pytest.
- **`docs/`**: Holds your project documentation in Markdown format, ready for MkDocs.
- **Configuration Files**: Root directory contains pre-configured files like `pyproject.toml` (for UV, Ruff, Pytest, Pyright), `.pre-commit-config.yaml`, etc.
- **Docker Support**: `Dockerfile`, `multistage.Dockerfile`, and `docker-compose.yml` provide containerization setups for development and production.
- **CI/CD Workflows**: `.github/workflows/` defines the automated GitHub Actions pipelines.
- **Cookiecutter Template**: The template structure is designed to be used with Cookiecutter, allowing you to create new projects based on this template easily. Including a Makefile to simplify common tasks like installing dependencies, running tests, and starting the FastAPI server.

## Example Use Case: Autoencoder for Image Compression

To demonstrate the template's practical application, it includes a machine learning use case: training an autoencoder on the MNIST dataset using PyTorch Lightning and serving it via FastAPI.

### Objective

The autoencoder learns a compressed representation (encoding) of handwritten digit images and reconstructs them, showcasing unsupervised feature learning.

### Dataset

The classic [MNIST dataset](http://yann.lecun.com/exdb/mnist/) of 28x28 grayscale handwritten digits.

### Implementation

- **`LitAutoEncoder`**: A `pytorch_lightning.LightningModule` defining the encoder, decoder, and training/validation logic, simplifying PyTorch boilerplate.
- **`train_litautoencoder`**: A function orchestrating the data loading and model training process.

### FastAPI Integration

A simple API built with [FastAPI](https://fastapi.tiangolo.com/) allows interaction with the model:

- Train the autoencoder via an API endpoint.
- Generate embeddings (compressed representations) for new image data.

This demonstrates how the template structure supports integrating model training and API deployment within a single, organized project.

## Automate Project Kick-off with Cookiecutter

Manually copying templates is error-prone. This template leverages **Cookiecutter** to automate the creation of new projects based on its structure.

- **Consistency**: Every new project starts with the same proven structure and tooling.
- **Speed**: Skip the repetitive setup and jump straight into development.
- **Customization**: Tailor essential project metadata during creation.

Cookiecutter turns starting a best-practice data science project into a simple command-line interaction.

### How to Use

1. **Install Cookiecutter** (if you haven't already):

    ```bash
    pip install cookiecutter
    ```

1. **Generate Your Project**:

    ```bash
    cookiecutter gh:tiefenthaler/uv-datascience-project-template
    ```

1. **Customize**: Cookiecutter will prompt you for details like project name, author, Python version, etc.
1. **Get Started**: `cd` into your newly created project directory and follow the setup instructions in its `README.md`.
1. Use the **`Makefile`** to manage the project:
   - Create virtual environment and install dependencies:

      ```bash
      make install
      ```

   - Run checks for code quality:

      ```bash
      make check
      ```

   - Run the FastAPI application:

      ```bash
      make run
      ```

   - Run help command to see available `Makefile` options:

      ```bash
      make help
      ```

   - Run additional commands like "test", "build", and others as needed.
   - Happy coding!

For more details, see the [Cookiecutter Guide](./guides/cookiecutter.md).

## Conclusion: Build Better, Faster

The **UV Data Science Project Template** offers a robust, modern foundation for your data science endeavors. By integrating fast, efficient tools like UV and Ruff, promoting best practices like reproducibility and automated testing, and simplifying setup with Cookiecutter, it empowers you to focus on innovation rather than infrastructure.

Stop reinventing the project setup wheel. Give your next data science project a significant head start with this template and experience a more streamlined, collaborative, and production-ready workflow.

**Ready to try it out? Find the template on [GitHub](https://github.com/tiefenthaler/uv-datascience-project-template).**
