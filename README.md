# Tutorial Project for 1) Data Science in a Dev Container, and 2) for a Machine Learning Application in Production; using Docker, UV, and FastAPI

This guide provides instructions on how to use Docker Compose with `uv` to create a container for a machine learning Python project that uses FastAPI for a production setup.

## Table of Contents
- [Tutorial Project for 1) Data Science in a Dev Container, and 2) for a Machine Learning Application in Production; using Docker, UV, and FastAPI](#tutorial-project-for-1-data-science-in-a-dev-container-and-2-for-a-machine-learning-application-in-production-using-docker-uv-and-fastapi)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Docker and Docker Compose](#docker-and-docker-compose)
    - [Dockerfile](#dockerfile)
    - [Docker Compose](#docker-compose)
  - [Using uv to Manage the Project](#using-uv-to-manage-the-project)
    - [pyproject.toml](#pyprojecttoml)
  - [Custom Code in src Folder](#custom-code-in-src-folder)
    - [lit\_auto\_encoder.py](#lit_auto_encoderpy)
  - [FastAPI Application](#fastapi-application)
    - [demo.py](#demopy)
  - [Production Setup for the Machine Learning FastAPI App hosted in the Docker container](#production-setup-for-the-machine-learning-fastapi-app-hosted-in-the-docker-container)
  - [Development in Dev Container](#development-in-dev-container)
    - [Post-Create and Post-Start Commands](#post-create-and-post-start-commands)

## Overview

This project demonstrates how to set up a machine learning application using FastAPI, Docker, and Docker Compose. The project uses `uv` to manage dependencies and the virtual Python environment inside the container.

## Docker and Docker Compose

### Dockerfile

The `Dockerfile.debug` is used to build the Docker image for the project. It includes the following steps:

1. Define build-time arguments for the base container images and workspace name.
2. Use a Python image with `uv` pre-installed.
3. Set the working directory.
4. Enable bytecode compilation for faster startup.
5. Copy and install dependencies without installing the project.
6. Copy the application source code and install it.
7. Add executables and source to environment paths.
8. Set the default command to run the FastAPI application.

```dockerfile
# filepath: Dockerfile.debug
# ...existing code...
```

### Docker Compose

The `docker-compose.yml` file is used to define and run multi-container Docker applications. It includes the following configurations:

1. Build the image from the `Dockerfile.debug`.
2. Define the image name.
3. Host the FastAPI application on port 8000.
4. Mount the current directory to the app directory in the container.
5. Set environment variables.
6. Define the default command to start the FastAPI application.

```dockercompose
# filepath: docker-compose.yml
# ...existing code...
```

## Using uv to Manage the Project

`uv` is a tool that simplifies the management of Python projects and virtual environments. It handles dependency installation, virtual environment creation, and other project configurations. In this project, `uv` is used to manage dependencies and the virtual environment inside the Docker container, ensuring a consistent and reproducible setup.

### pyproject.toml

The `pyproject.toml` file includes the following sections:

1. Project metadata (name, version, description, etc.).
2. Dependencies required for the project.
3. Dependency groups for development and linting.
4. Configuration for `pylint` and `tomlsort`.

```toml
# filepath: pyproject.toml
# ...existing code...
```

## Custom Code in src Folder

The `src` folder contains the custom code for the machine learning project. The main components include:

### lit_auto_encoder.py

This file defines the `LitAutoEncoder` class, which is a LightningModule for training an autoencoder using PyTorch Lightning. The `LitAutoEncoder` class includes:

1. An `__init__` method to initialize the encoder and decoder.
2. A `training_step` method to define the training loop.
3. A `configure_optimizers` method to set up the optimizer.

```python
# filepath: src/litautoencoder/lit_auto_encoder.py
# ...existing code...
```

## FastAPI Application

The FastAPI application is defined in the `demo.py` file. It includes the following endpoints:

1. `GET /`: Root endpoint that provides a welcome message and instructions.
2. `POST /train`: Endpoint to train the autoencoder model.
3. `POST /embed`: Endpoint to embed fake images using the trained autoencoder.

### demo.py

This file defines the FastAPI application and the endpoints. It includes:

1. Importing necessary libraries and modules.
2. Defining global variables for the encoder, decoder, and model training status.
3. A `NumberFakeImages` class for input validation.
4. A `train_litautoencoder` function to initialize and train the autoencoder.
5. A `read_root` function to handle the root endpoint.
6. A `train_model` function to handle the model training endpoint.
7. An `embed` function to handle the embedding endpoint.
8. The application entry point to run the FastAPI application.

```python
# filepath: demo.py
# ...existing code...
```

## Production Setup for the Machine Learning FastAPI App hosted in the Docker container

- Build the docker image and start a container:

```bash
docker-compose up --build
```

- Test the endpoint with curl:

- Get docs of the request options of the FastAPI app:

```bash
curl -X GET http://0.0.0.0:8000/docs
```

- Welcome root endpoint

```bash
curl -X GET http://0.0.0.0:8000/
```

- Test the endpoint with curl by training the model first, followed by requesting predictions for n fake images

```bash
curl -X POST http://0.0.0.0:8000/train \
curl -X POST http://0.0.0.0:8000/embed -H "Content-Type: application/json" -d '{"n_fake_images": 4}'
```

## Development in Dev Container

- Run the server: `uv run /workspace/demo.py`
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

### Post-Create and Post-Start Commands

The `devcontainer.json` file includes post-create and post-start commands to configure the development environment.

```jsonc
# filepath: .devcontainer/devcontainer.json
# ...existing code...
```

This guide provides a comprehensive overview of setting up and running the machine learning FastAPI project using Docker Compose and `uv`. Follow the instructions to build and run the application in both development and production environments.
