# UV Data Science Project Template

> **Tutorial Project for 1) Develop Data Science Projects in a Dev Container, and 2) Machine Learning Applications in Production**

<!--docs-ref-index-start-->

This guide provides instructions on how to develop and productionize machine learning applications in a robust and efficient way.  
It is demonstrated how to achieve this using a modern setup of tools, like UV, Docker, Ruff, FastAPI and more (see [Overview Tools](#overview-tools) Section). The focus of this project is to give an introduction to using those tools and not on how to properly set up a machine learning application (for production). Therefore only a simple machine learning pipeline based on PyTorch/Lightning and FastAPI is used.

> **See the related [Project Documentation](https://tiefenthaler.github.io/uv-datascience-project-template/) for additional information.**

## Table of Contents

- [UV Data Science Project Template](#uv-data-science-project-template)
  - [Table of Contents](#table-of-contents)
  - [Overview Tools](#overview-tools)
  - [Using uv to Manage the Project](#using-uv-to-manage-the-project)
    - [pyproject.toml](#pyprojecttoml)
  - [Custom Code in src Folder](#custom-code-in-src-folder)
    - [lit\_auto\_encoder.py](#lit_auto_encoderpy)
    - [train\_autoencoder.py](#train_autoencoderpy)
    - [FastAPI Application](#fastapi-application)
      - [app\_fastapi\_autoencoder.py](#app_fastapi_autoencoderpy)
    - [main.py](#mainpy)
  - [Production Setup for the Machine Learning FastAPI App hosted in the Docker container](#production-setup-for-the-machine-learning-fastapi-app-hosted-in-the-docker-container)
    - [Dockerfile](#dockerfile)
      - [Multi-Stage Dockerfile](#multi-stage-dockerfile)
    - [Docker Compose](#docker-compose)
    - [Build the docker image and run a container](#build-the-docker-image-and-run-a-container)
    - [Test the endpoint with curl](#test-the-endpoint-with-curl)
  - [Development in Dev Container](#development-in-dev-container)
  - [Conclusion](#conclusion)

## Overview Tools

The project includes the following components, for more details see [Documentation - Guides](https://tiefenthaler.github.io/uv-datascience-project-template/guides/):

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

## Using uv to Manage the Project

`UV` is a tool that simplifies the management of Python projects and virtual environments. It handles dependency installation, virtual environment creation, and other project configurations. In this project, `UV` is used to manage dependencies and the virtual environment inside the Docker container, ensuring a consistent and reproducible setup.

See [Guides - UV](https://tiefenthaler.github.io/uv-datascience-project-template/guides/uv/) for a comprehensive guide.

### pyproject.toml

The `pyproject.toml` file includes the following sections:

1. Project metadata (name, version, description, etc.).
2. Dependencies required for the project.
3. Dependency groups for development and documentation.
4. Configuration for tools and packaging.

```toml
# filepath: pyproject.toml
[project]
name = "uv-datascience-project-template"
version = "0.1.0"
description = "Tutorial Project for 1) Data Science in a Dev Container, and 2) for a Machine Learning Application in Production; using Docker, UV, and FastAPI"
readme = "README.md"
license = {text = "MIT"}
authors = [
    {name = "David Tiefenthaler"}
]
urls = {repository = "https://github.com/tiefenthaler/uv-datascience-project-template"}
keywords = [
    "data science project",
    "docker",
    "python",
    "template",
    "uv"
]
requires-python = ">=3.12.0, <3.13.0"
dependencies = [
    "fastapi[standard]>=0.115.6",
    "lightning>=2.4.0",
    "pydantic>=2.10.4",
    "torch>=2.4.1",
    "torchvision>=0.20.1",
    "uvicorn>=0.34.0"
]

# DEV SETTING
[dependency-groups]
dev = [
    "ipykernel>=6.29.5",
    "jupyterlab>=4.3.1",
    "pyright>=1.1.393",
    "pytest-cov>=6.0.0",
    "pytest>=8.1.1",
    "ruff>=0.9.4",
    "toml-sort>=0.24.2",
    "uv>=0.5.26",
    "pre-commit>=4.1.0",
]
docs = [
    "mkdocs>=1.6.1",
    "mkdocs-include-markdown-plugin>=7.1.3",
    "mkdocs-jupyter>=0.25.1",
    "mkdocs-material>=9.6.3",
    "mkdocstrings[python]>=0.15.0",
]

# DEV SETTING
[tool.uv]
default-groups = ["dev"]

# DEV SETTING
# ruff.toml file is used.
[tool.ruff]

# DEV SETTING
# pytest.ini file is used.
[tool.pytest]

# DEV SETTING
# .coveragerc file is used. A pytest fixture in .conftest.py is used to create coverage file/report directory.
[tool.coverage]

# DEV SETTING
# pyrightconfig.json file is used. NOTE: Ensure to set the python version correctly.
[tool.pyright]

# DEV SETTING
# NOTE: to sort, run: "uv run toml-sort pyproject.toml"
[tool.tomlsort]
in_place = true
no_sort_tables = true
sort_inline_arrays = true
spaces_before_inline_comment = 4
spaces_indent_inline_array = 4

[tool.hatch.build.targets.wheel]
packages = ["src/uv_datascience_project_template"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## Custom Code in src Folder

See [Source Code API Reference](https://tiefenthaler.github.io/uv-datascience-project-template/api/fastapi_app/) for a comprehensive documentation.

The `src` folder contains the custom code for the machine learning project. The main components include:

### lit_auto_encoder.py

This file defines the `LitAutoEncoder` class, which is a LightningModule an autoencoder using PyTorch Lightning. The `LitAutoEncoder` class includes:

1. An `__init__` method to initialize the encoder and decoder.
2. A `training_step` method to define the training loop.
3. A `configure_optimizers` method to set up the optimizer.

### train_autoencoder.py

This file defines the training function `train_litautoencoder` to initialize and train the model on the MNIST dataset using PyTorch Lightning.

### FastAPI Application

The FastAPI application is defined in the `app_fastapi_autoencoder.py` file. It includes the following endpoints:

1. `GET /`: Root endpoint that provides a welcome message and instructions.
2. `POST /train`: Endpoint to train the autoencoder model.
3. `POST /embed`: Endpoint to embed fake images using the trained autoencoder.

#### app_fastapi_autoencoder.py

See [Source Code API Reference](https://tiefenthaler.github.io/uv-datascience-project-template/api/fastapi_app/) for a comprehensive documentation.

This file defines the FastAPI application and the endpoints. It includes:

1. Importing necessary libraries and modules.
2. Defining global variables for the encoder, decoder, and model training status.
3. A `NumberFakeImages` class for input validation.
4. A `train_litautoencoder` function to initialize and train the autoencoder.
5. A `read_root` function to handle the root endpoint.
6. A `train_model` function to handle the model training endpoint.
7. An `embed` function to handle the embedding endpoint.
8. The application entry point to run the FastAPI application.

### main.py

This file defines the uvicorn server to run the FastAPI AutoEncoder application and the endpoints. It includes:

1. Importing necessary libraries and modules, including the source code of the project.
2. The application entry point to run the FastAPI application.

```python
# filepath: main.py

# Application entry point
if __name__ == "__main__":
    # Run the FastAPI application
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
```

## Production Setup for the Machine Learning FastAPI App hosted in the Docker container

See [Docker Production Setup](https://tiefenthaler.github.io/uv-datascience-project-template/guides/docker_prod/) for a comprehensive guide.

### Dockerfile

The `Dockerfile` is used to build the Docker image for the project. It includes the following steps:

1. Define build-time arguments for the base container images and workspace name.
2. Use a Python image with `uv` pre-installed.
3. Set the working directory.
4. Enable bytecode compilation for faster startup.
5. Copy and install dependencies without installing the project.
6. Copy the application source code and install it.
7. Add executables and source to environment paths.
8. Set the default command to run the FastAPI application.

#### Multi-Stage Dockerfile

To build the multistage image for a container optimized final image without uv use the `multistage.Dockerfile`.

### Docker Compose

The `docker-compose.yml` file is used to define and run multi-container Docker applications. It includes the following configurations:

1. Build the image from the `Dockerfile`.
2. Define the image name.
3. Host the FastAPI application on port 8000.
4. Mount the current directory to the app directory in the container.
5. Set environment variables.
6. Define the default command to start the FastAPI application.

<!--docs-ref-docker-prod-build-start-->
### Build the docker image and run a container

Build and run a specific or all services when multiple services ("app" and "app-optimized-docker") are defined in `docker-compose.yml`. Note that in the give example both services us the same port and only one service at a time should be used.

  ```bash
  docker-compose up --build
  ```

  or to build a single service only "app" respectively "app-optimized-docker".

  ```bash
  docker-compose up --build app
  ```

  ```bash
  docker-compose up --build app-optimized-docker
  ```

### Test the endpoint with curl

- Welcome root endpoint

    ```bash
    curl -X GET http://0.0.0.0:8000/
    ```

- Get docs of the request options of the FastAPI app:

    ```bash
    curl -X GET http://0.0.0.0:8000/docs
    ```

- Test the endpoint with curl by training the model first, followed by requesting predictions for n fake images

    ```bash
    curl -X POST http://0.0.0.0:8000/train \
    curl -X POST http://0.0.0.0:8000/embed -H "Content-Type: application/json" -d '{"n_fake_images": 4}'
    ```
<!--docs-ref-docker-prod-build-end-->

## Development in Dev Container

See [VSCode Dev-Container (Docker) Setup for Data Science Projects using UV](https://tiefenthaler.github.io/uv-datascience-project-template/guides/docker_vscode_devcontainer/) for a comprehensive guide.

- Run the server: `uv run /workspace/main.py`
- Test the standard endpoints with curl:
    - Get docs of the request options of the FastAPI app

        ```bash
        curl -X GET http://localhost:8000/docs
        ```

    - Welcome root request of the FastAPI app, providing an app description

        ```bash
        curl -X GET http://localhost:8000/
        ```

    - Test the machine learning endpoints with curl:

        ```bash
        curl -X POST http://localhost:8000/train \
        curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"n_fake_images": 1}'
        ```

## Conclusion

This guide provides a comprehensive overview of setting up and running the machine learning FastAPI project using Docker Compose and `uv`. Follow the instructions to build and run the application in both development and production environments.

<!--docs-ref-index-end-->

<!--docs-placeholder-start-->
<!--docs-placeholder-end-->
