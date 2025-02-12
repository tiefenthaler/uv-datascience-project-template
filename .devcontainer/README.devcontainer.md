# VSCode Dev-Container (Docker) Setup for Data Science Projects using UV

<!--docs-ref-readme-devcontainer-1-start-->

This is a [**containerized dev setup**](https://code.visualstudio.com/docs/devcontainers/containers) respectively related for using [**remote containers**](https://code.visualstudio.com/docs/remote/containers) to work on data science / machine learning projects using **[UV](https://docs.astral.sh/uv/), [Git](https://git-scm.com/)** with **[VSCode](https://code.visualstudio.com/)**.

The repository contains a setup of a local development container using docker compose and VS Code to develop data science projects with UV in a consistent and robust but yet in a simple and customizable way. The Repo provides the configurations and installations for your container, so you can straight get started with your data science work while enjoying the benefits of using docker containers.

Find the [**Documentation**](https://tiefenthaler.github.io/uv-datascience-project-template/guides/docker_vscode_devcontainer/) about this VSCode Dev-Container for Data Science.

<!--docs-ref-readme-devcontainer-1-end-->

- [VSCode Dev-Container (Docker) Setup for Data Science Projects using UV](#vscode-dev-container-docker-setup-for-data-science-projects-using-uv)
  - [Dev Container Main Configurations and Installations](#dev-container-main-configurations-and-installations)
    - [Setup organization within: Dockerfile.debug | docker-compose.yml | devcontainer.json](#setup-organization-within-dockerfiledebug--docker-composeyml--devcontainerjson)
  - [Getting Started](#getting-started)
  - [VS Code Extensions for Data Science Projects](#vs-code-extensions-for-data-science-projects)
    - [Additional python packages for development](#additional-python-packages-for-development)
    - [Additional python packages for project and code documentation](#additional-python-packages-for-project-and-code-documentation)
    - [Additional tools to support development](#additional-tools-to-support-development)

<!--docs-ref-readme-devcontainer-2-start-->

## Dev Container Main Configurations and Installations

Using a Python image with UV pre-installed, which includes Python, as well as a Debian base image including the VS Code devcontainer base image.  
Multi-Stage Build: Despite using two base images, only one container is built. The final container is based on the second image, while copying content from the UV stage into the final stage.

- **UV**, an extremely fast Python package, virtual environment and project manager.
    - 🚀 A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more.
    - ⚡️ 10-100x faster than pip.
    - 🐍 Installs and manages Python versions.
    - 🛠️ Runs and installs Python applications.
    - ❇️ Runs single-file scripts, with support for inline dependency metadata.
    - 🗂️ Provides comprehensive project management, with a universal lockfile.
    - 🔩 Includes a pip-compatible interface for a performance boost with a familiar CLI.
    - 🏢 Supports Cargo-style workspaces for scalable projects.
- **Volume Mapping**: A volume will be used to map a directory on your local file system to a directory inside the Docker container. This way, any changes you make to your code locally will be immediately reflected inside the container, where you can run and test the code.
- **Git:** A distributed version control system that tracks changes in any set of computer files, usually used for coordinating work among programmers who are collaboratively developing source code during software development.
- **VS Code**, including extensions like Python, Jupyter Notebooks, Docker, PyLance, Ruff and more. Find my list of VS Code **Extensions** for Data Science Projects in [this](#vs-code-extensions-for-data-science-projects) section below.

### Setup organization within: Dockerfile.debug | docker-compose.yml | devcontainer.json

Those files define the dev container setup for data science projects. The list below gives a short overview of the single files. Details can be found in the comments in the single files.

- **Dockerfile.debug:** This file defines the base image for your development container and the steps needed to configure it. Think of it as the blueprint for your container's operating system, dependencies, and tools. It's the foundation upon which everything else is built.

  <details>
  <summary>Click to toggle contents of the <code>Dockerfile</code></summary>
  <div markdown="1">

  ```Dockerfile
  # Dockerfile for development purposes.
  # ------------------------------------
  # Use a python image with uv pre-installed and a Debian base image including the VS Code devcontainer base image.
  # To use the image without VS CODE IDE, add lines as indicated (adjust docker-compose.yml as well as documented).
  # ---------------------------------

  # Define a build-time argument with a default value for base container images.
  ARG UV_VER=0.5.24
  ARG DEBIAN_VER=bookworm
  ARG WORKSPACE_NAME_=workspace
  ARG PROJECT_NAME_=${PROJECT_NAME}

  # Multi-Stage Build: Despite using two base images, only one container is built and run.
  # The final container is based on the second image, while copying content from the uv stage into the final stage.
  # FROM ghcr.io/astral-sh/uv:python3.12-bookworm
  FROM ghcr.io/astral-sh/uv:$UV_VER AS uv

  FROM mcr.microsoft.com/vscode/devcontainers/base:$DEBIAN_VER

  # Install/Update linux packages; install common dev tools like: git, process tools, ...
  # hadolint ignore=DL3008
  RUN apt-get update \
      && apt-get install -y --no-install-recommends\
      procps \
      build-essential \
      curl \
      swig \
      wget \
      # To reduce the image size, it is recommended refresh the package cache as follows.
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/*

  # Copies files or directories from the uv stage into the final stage,
  # and ensures that the ownership of the copied files is adjusted to the user and group in the final image,
  # and making its functionality or binaries available in the final container.
  COPY --from=uv --chown=vscode: /uv /uvx /bin/

  WORKDIR /vscode/${WORKSPACE_NAME_}

  # The code to run when container is started:
  # Common practice to keep the Docker container running without performing any significant action.
  ENTRYPOINT ["tail", "-f", "/dev/null"]
  ```
  
  </div>
  </details>

- **docker-compose.yml:** (Optional, but often used) This file is used when you have multiple containers that need to work together for your development environment. It defines how these containers interact, their dependencies, and their network configuration. Even if only a single service is used, it defines the additional configuration specific for your data science projects like volume mapping or ports which is optional and therefore not defined in the Dockerfile.debug. This enables the dev container setup to be used with other IDEs then VS Code.

  <details>
  <summary>Click to toggle contents of the <code>docker-compose.yml</code></summary>
  <div markdown="1">

  ```yaml
  # Dev Container Configuration File.
  # ---------------------------------
  # Standard Configuration for the service to be used to develop data science applications.
  # Using bind mounts instead of watch for development to sync changes made in the container back to the host.
  # This file depends on a .env file in the root directory of the dev container for dynamic variable interpolation.
  # - The .env file is automatically loaded per default by Docker Compose and is not passed to the container during build.
  # ---------------------------------

  # The x-args section defines a reusable set of arguments using YAML anchors.
  # - BUILD arguments ("UV_VER", "DEBIAN_VER" and "WORKSPACE_NAME") to pass to Dockerfile.
  x-args: &default-args
    UV_VER: "0.5.5"
    DEBIAN_VER: "bookworm"
    WORKSPACE_NAME_: ${WORKSPACE_NAME}
    PROJECT_NAME_: ${PROJECT_NAME}

  services: # Top level element to configure the arguments of multiple services.
    myproject: # "project" refers to the name of your project/application for which configurations are defined.
      build: # Tells Docker Compose to build the Docker image using the Dockerfile in the specified directory.
        context: .
        dockerfile: ./Dockerfile.debug
        # Build argument (passed to Dockerfile only)
        args:
          <<: *default-args # The <<: *default-args syntax merges the default-args into the args section of the build configuration.
      image: "${DEV_USER}.dev-container-uv.${PROJECT_NAME}" # Explicit way to define the image name

      # Host the FastAPI application on port 8000.
      ports:
        - "8000:8000"

      # Volumes are persistent data stores (outside container), mounted to be usable by the container.
      volumes:
        # Mount the current directory to ${WORKSPACE_NAME} so code changes don't require an image rebuild. .venv is excluded in the .dockerignore file.
        - type: bind
          source: ..
          target: /vscode/${WORKSPACE_NAME}
        # Mount the virtual environment separately, so the developer's environment doesn't end up in the container.
        - type: volume
          source: venv
          target: /vscode/${WORKSPACE_NAME}/.venv

      working_dir: /vscode/${WORKSPACE_NAME}

      # Runtime environment variable, passed to devcontainer.json. Not available for volumes, networks, or build arguments.
      # Since docker detects a .env file during build per default, the .env file will be loaded anyways.
      # Set explicitly for clarity to indicate that the environment variables are used.
      env_file:
        - path: .env
          required: true

      # Default command to start the dev container.
      command:
        - sh -c "chmod -R 777 /vscode/${WORKSPACE_NAME} && tail -f /dev/null" # Set permissions on the working directory for root user.
        - docker-compose down # Remove the container after exiting.

  # Define the volumes of the docker container.
  volumes:
    venv: # Volume for the virtual environment for persistent in the container.
  ```

</div>
</details>

- **devcontainer.json:** It configures VS Code (or other supporting IDEs) to use the Docker container as your development environment. It links the Dockerfile (or docker-compose.yml) to VS Code and defines various settings like VS Code extensions or the default environment used by VS Code that are only related to use the given IDE.

  <details>
  <summary>Click to toggle contents of the <code>devcontainer.json</code></summary>
  <div markdown="1">

  ```json
  // UV | VS Code - Setup.
  //---------------------
  // This config is set up to be only specific to VS Code.
  // Other configs that do not relate to VS Code are defined in the docker-compose.yml file.
  // This enables the dev container setup to be used with other IDEs, ignoring this file.
  //---------------------
  // Default and dynamic properties for the devcontainer setup:
  // - Default service: "myproject", relates to the service defined in the docker-compose.yml.
  // - Default "workspaceFolder" is set to "workspace" (within the "/vscode/" folder in the container).
  // For format details, see https://aka.ms/devcontainer.json.
  //---------------------

  {
    "name": "${localEnv:LOGNAME}.dev-container-uv.${localWorkspaceFolderBasename}",
    // Build image using docker compose based on build specs in docker-compose.yml
    "dockerComposeFile": ["./docker-compose.yml"],
    "service": "myproject",
    "runServices": ["myproject"],
    "workspaceFolder": "/vscode/workspace",
    "postCreateCommand": {
      "uv-sync--frozen": "uv sync --frozen --no-binary-package ${localWorkspaceFolderBasename}" // By default, uv installs projects and workspace members in editable mode, such that changes to the source code are immediately reflected in the environment.
    },
    "postStartCommand": {
      // Optional: If applicable, add the following lines for installations.
      "uv-run-pre-commit-install": "uv run pre-commit install"
    },
    "features": {
          "ghcr.io/dhoeric/features/hadolint:1": {}
      },
    "customizations": {
      // When connecting to a docker container your local VS Code starts an instance without extensions to ensure isolation and consistency.
      // Therefore extensions can be specified here for automatic installation when connecting.
      "vscode": {
        "settings": {
          // Define terminal shell for Dev Container.
          "terminal.integrated.profiles.linux": {
            "bash": {
              "path": "/bin/bash"
            }
          },
          "jupyter.notebookFileRoot": "${workspaceRoot}",
          "python.pythonPath": "/home/vscode/workspace/.venv/bin/python"
        },
        // Use the VS Code Extensions "Identifier" to define extensions.
        "extensions": [
          // Python
          "ms-python.python",
          "ms-toolsai.jupyter",
          // Docker
          "ms-azuretools.vscode-docker",
          "ms-vscode-remote.remote-containers",
          "ms-vscode-remote.remote-ssh-edit",
          "ms-vscode-remote.remote-ssh",
          "exiasr.hadolint",
          // Formatting and Linting
          "charliermarsh.ruff",
          "davidanson.vscode-markdownlint",
          "xshrim.txt-syntax",
          "tamasfe.even-better-toml",
          "streetsidesoftware.code-spell-checker",
          "ms-pyright.pyright",
          "ms-python.vscode-pylance",
          // Data
          "alexcvzz.vscode-sqlite",
          "grapecity.gc-excelviewer",
          "mechatroner.rainbow-csv",
          "zainchen.json",
          "yzane.markdown-pdf",
          "ms-toolsai.datawrangler",
          "yzhang.markdown-all-in-one",
          // Cloud
          //"ms-azuretools.vscode-docker",
          // Git
          "github.remotehub",
          // AI Coding Assistant
          "github.copilot",
          "github.copilot-chat",
          // Other
          "richie5um2.vscode-sort-json",
          "oliversen.chatgpt-docstrings"
        ]
      }
    },
    "remoteUser": "vscode"
  }
  ```

  </div>
  </details>

## Getting Started

- Install Docker Desktop.
- Install VSCode.
- Install VSCode Extensions.
    - Install VSCode remote container extension: [ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
- Start dev container:  F1 + "Open folder in container ...".
- To try the setup:
    - Clone the repository.
    - Run demo.py in the Python virtual environment (used as default, see `devcontainer.json`).
    - Your application will be available at <http://localhost:8000>.
        - Welcome root request of the FastAPI app, providing an app description.

            ```bash
            curl -X GET http://localhost:8000/
            ```

        - Test the machine learning endpoints with curl:

            ```bash
            curl -X POST http://localhost:8000/train \
            curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"n_fake_images": 1}'
            ```

    - For more information about the application, see the [README](https://tiefenthaler.github.io/uv-datascience-project-template/) in the root directory of the repository.

Optional Steps:

- Change the Docker Container in Dockerfile and/or docker-compose.yml.
- Add/remove VSCode settings and extensions in .devcontainer/devcontainer.json.
- Update .gitignore and other config files to match your setup.

## VS Code Extensions for Data Science Projects

The below extensions are installed for VS Code in the dev container, as defined in `devcontainer.json`.

```yaml
alexcvzz.vscode-sqlite # SQLite query execution and browsing
charliermarsh.ruff # Python linter and code formatter
davidanson.vscode-markdownlint # Markdown linter
exiasr.hadolint # A Dockerfile linter
github.copilot # AI-powered code completion
github.copilot-chat # Chat with your AI coding assistant
github.remotehub # Manage your GitHub repositories
grapecity.gc-excelviewer # Excel file viewer
hediet.vscode-drawio # Draw.io integration
jeff-hykin.polacode-2019 # Generate code blocks from images
mechatroner.rainbow-csv # Colorizes CSV files for better readability
ms-azuretools.vscode-docker # Docker extension for VS Code
ms-pyright.pyright # Static type checker
ms-python.python # Python language support
ms-python.vscode-pylance # Python language server for enhanced code analysis
ms-toolsai.datawrangler # Data transformation and cleaning tool
ms-toolsai.jupyter # Jupyter Notebooks
ms-pyright.pyright # Static type checker
oliversen.chatgpt-docstrings
richie5um2.vscode-sort-json # Sorts JSON objects
streetsidesoftware.code-spell-checker # Spell checker for multiple languages
tamasfe.even-better-toml # Enhanced TOML language support
tomoki1207.pdf # PDF viewer
xshrim.txt-syntax # Syntax highlighting for plain text files
zainchen.json # JSON language support (likely provides syntax highlighting, validation, etc.)
yzane.markdown-pdf # Generate PDF from Markdown files
yzhang.markdown-all-in-one # All-in-one Markdown extension
```

### Additional python packages for development

- uv
- ruff
- pytest
- pytest-cov
- pre-commit
- pyright
- ipykernel
- jupyterlab
- toml-sort

### Additional python packages for project and code documentation

- mkdocs
- mkdocs-include-markdown-plugin
- mkdocs-jupyter
- mkdocs-material
- mkdocstrings[python]

### Additional tools to support development

- GitHub
- GitHub Actions and Workflows for CI
- GitHub Pages (to host your documentation)

<!--docs-ref-readme-devcontainer-2-end-->
