# 1. VSCode Dev-Container (Docker) Setup for Data Science Projects

This is a [**containerized dev setup**](https://code.visualstudio.com/docs/devcontainers/containers) respectively related for using [**remote containers**](https://code.visualstudio.com/docs/remote/containers) to work on data science / machine learning projects using **[UV](https://docs.astral.sh/uv/), [Git](https://git-scm.com/) with [VSCode](https://code.visualstudio.com/)**.

The repository contains a setup of a local development container using docker compose and VS Code to develop data science projects in a consistent and robust but yet in a simple and customizable way. The Repo provides the configurations and installations for your container, so you can straight get started with your data science work while enjoying the benefits of using docker containers.

Find a detailed [**Guide**]() about this VSCode Dev-Container for Data Science on Medium.

## 1.1. Table of Contents

**Section 1 provides a brief overview of the purpose of the Dev Container.**  
**Section 2 describes the Dev Container main configurations and installations.**  
**Section 3 provides a short description to get started using the Dev Container.**  
**Section 4 gives an overview of VS Code Extensions I use to develop Data Science Projects.**

- [1. VSCode Dev-Container (Docker) Setup for Data Science Projects](#1-vscode-dev-container-docker-setup-for-data-science-projects)
  - [1.1. Table of Contents](#11-table-of-contents)
- [2. Dev Container Main Configurations and Installations](#2-dev-container-main-configurations-and-installations)
  - [Setup organization within: Dockerfile.debug | docker-compose.yml | devcontainer.json](#setup-organization-within-dockerfiledebug--docker-composeyml--devcontainerjson)
- [3. Getting Started](#3-getting-started)
- [4. VS Code Extensions for Data Science Projects](#4-vs-code-extensions-for-data-science-projects)

# 2. Dev Container Main Configurations and Installations

Using a python image with uv pre-installed which includes python, as well as a Debian base image including the VS Code devcontainer base image.  
Multi-Stage Build: Despite using two base images, only one container is built. The final container is based on the second image, while copying content from the uv stage into the final stage.

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
- **VS Code**, including extensions like Python, Jupyter Notebooks, Docker, PyLance, Ruff and more. Find my list of VS Code **Extensions** for Data Science Projects in [this](#4-vs-code-extensions-for-data-science-projects) section below.

## Setup organization within: Dockerfile.debug | docker-compose.yml | devcontainer.json

Those files define the dev container setup for data science projects. The list below gives a short overview of the single files. Details can be found in the comments in the single files.

- **Dockerfile.debug:** This file defines the base image for your development container and the steps needed to configure it. Think of it as the blueprint for your container's operating system, dependencies, and tools. It's the foundation upon which everything else is built.
- **docker-compose.yml:** (Optional, but often used) This file is used when you have multiple containers that need to work together for your development environment.  It defines how these containers interact, their dependencies, and their network configuration. Even if only a single service is used, it defines the additional configuration specific for your data science projects like volume mapping or ports which is optional and therefore not defined in the Dockerfile.debug.
- **devcontainer.json:** It configures VS Code (or other supporting IDEs) to use the Docker container as your development environment. It links the Dockerfile (or docker-compose.yml) to VS Code and defines various settings like VS Code extensions or the default environment used by VS Code.

# 3. Getting Started

- Install Docker Desktop.
- Install VSCode.
- Install VSCode Extension.
  - Install VSCode remote container extension: [ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
- Start dev container:  F1 + "Open folder in container ...".
- To try the setup:
  - Run demo.py in the python virtual environment (used as default, see `devcontainer.json`).
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

  - For more information about the application, see the [README](../README.md) in the root directory of the repository.

Optional Steps:

- Change Docker Container in Dockerfile and/or docker-compose.yml.
- Add/remove VSCode settings and extensions in .devcontainer/devcontainer.json.
- Update .gitignore and other config files to match your setup.

# 4. VS Code Extensions for Data Science Projects

The below extensions are installed for VS Code in the dev container, as defined in `devcontainer.json`.

```yml
alexcvzz.vscode-sqlite # SQLite query execution and browsing
charliermarsh.ruff # Python linter and code formatter
davidanson.vscode-markdownlint # Markdown linter
exiasr.hadolint # A Dockerfile linter
grapecity.gc-excelviewer # Excel file viewer
hediet.vscode-drawio # Draw.io integration
jeff-hykin.polacode-2019 # Generate code blocks from images
mechatroner.rainbow-csv # Colorizes CSV files for better readability
ms-azuretools.vscode-docker # Docker extension for VS Code
ms-python.python # Python language support
ms-python.vscode-pylance # Python language server for enhanced code analysis
ms-toolsai.datawrangler # Data transformation and cleaning tool
ms-toolsai.jupyter # Jupyter Notebooks
ms-pyright.pyright # Static type checker
richie5um2.vscode-sort-json # Sorts JSON objects
streetsidesoftware.code-spell-checker # Spell checker for multiple languages
tamasfe.even-better-toml # Enhanced TOML language support
tomoki1207.pdf # PDF viewer
xshrim.txt-syntax # Syntax highlighting for plain text files
yzane.markdown-pdf # Generate PDF from Markdown files
yzhang.markdown-all-in-one # All-in-one Markdown extension
```

Additional python packages for development:

- toml-sort
- ruff
- pytest
- jupyterlab
