# UV, an extremely fast Python package and project manager, written in Rust

[UV](https://docs.astral.sh/uv/) is used as a fast and efficient package manager for this project, replacing tools like pip, virtualenv, and pip-tools. It significantly speeds up the installation of dependencies and management of the virtual environment, making the development process smoother and faster. UV ensures consistent dependency resolution and environment setup across different development environments.

- [UV, an extremely fast Python package and project manager, written in Rust](#uv-an-extremely-fast-python-package-and-project-manager-written-in-rust)
  - [Getting Started with UV](#getting-started-with-uv)
    - [Install uv](#install-uv)
      - [macOS and Linux](#macos-and-linux)
      - [Windows](#windows)
    - [Install Python](#install-python)
    - [Install Python packages and dependencies](#install-python-packages-and-dependencies)
    - [Run Python code](#run-python-code)
    - [Launching JupyterLab](#launching-jupyterlab)
    - [Optional: Manage virtual environments manually](#optional-manage-virtual-environments-manually)
    - [UV self update](#uv-self-update)
    - [UV update packages (dependencies)](#uv-update-packages-dependencies)

**UV**, an extremely fast Python package, virtual environment and project manager.

- 🚀 A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more.
- ⚡️ 10-100x faster than pip.
- 🐍 Installs and manages Python versions.
- 🛠️ Runs and installs Python applications.
- ❇️ Runs single-file scripts, with support for inline dependency metadata.
- 🗂️ Provides comprehensive project management, with a universal lockfile.
- 🔩 Includes a pip-compatible interface for a performance boost with a familiar CLI.
- 🏢 Supports Cargo-style workspaces for scalable projects.

**Specifically, UV is utilized for:**

- **Dependency Management:** UV manages both project dependencies and development dependencies, ensuring that all necessary packages are installed quickly and efficiently. This includes `pydantic-settings` for robust configuration management.
- **Virtual Environment Creation:** UV creates and manages the project's virtual environment, isolating project dependencies from the global Python environment.
- **Speed and Efficiency:** UV's speed advantage over traditional tools like `pip` significantly reduces the time spent on environment setup and dependency installation, especially in projects with many dependencies.
- **Consistency:** By using UV, the project ensures that the development environment is consistent across different machines and platforms, reducing the risk of "it works on my machine" issues.
- **Integration with pyproject.toml:** UV leverages the `pyproject.toml` file for project configuration, making it easy to define and manage dependencies, scripts, and other project settings.
- **Running Tools:** UV is used to run development tools like `ruff`, `pytest`, and `toml-sort` directly from the command line, ensuring that the correct versions of these tools are used and that they are isolated from other projects. Example: `uv run ruff .`
- **Packaging:** UV can be used to package the project for distribution, creating a `wheel` file that can be uploaded to PyPI or installed directly.
- **Lockfile Management:** UV uses a `uv.lock` file to ensure that all dependencies are installed at the exact versions specified, preventing compatibility issues and ensuring reproducibility.

**Key features of UV include:**

- **Written in Rust:** UV is written in Rust, which provides excellent performance and memory safety.
- **Compatibility:** UV is compatible with `pip` and `virtualenv`, so it can be used with existing Python projects without requiring major changes.
- **pyproject.toml Support:** UV fully supports the `pyproject.toml` file, which is the recommended way to configure Python projects.
- **Speed:** UV is significantly faster than `pip` for most operations, especially when installing dependencies from scratch.
- **Global Cache:** UV uses a global cache to store downloaded packages, so they don't need to be downloaded again for each project.

## Getting Started with UV

Refer to the official [UV - Getting Started - Documentation](https://docs.astral.sh/uv/getting-started/) for detailed instructions on installing and using UV.

This section guides you through the Python setup and package installation procedure using `uv` native commands over the `uv pip` interface and is based on the content of **Sebastian Raschka**'s [GitHub repository](https://github.com/rasbt/LLMs-from-scratch/tree/main).

> [!NOTE]
> There are alternative ways to install Python and use `uv`. For example, you can install Python directly via `uv` and use `uv add` instead of `uv pip install` for even faster package management.
>
> If you prefer the `uv pip` commands, I recommend checking the official [`uv` documentation](https://docs.astral.sh/uv/).
>
> While `uv add` offers additional speed advantages, `uv pip` might be slightly more user-friendly for with your existing habits. However, if you're new to Python package management, the native `uv` interface is also a great opportunity to learn it from the start. It's also how I use `uv`, but I realized the barrier to entry is a bit higher if you are coming from `pip` and `conda/mamba`.

### Install uv

Uv can be installed as follows, depending on your operating system.

#### macOS and Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

or

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

#### Windows

```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | more"
```

### Install Python

You can install Python using uv:

```bash
uv python install 3.10
```

### Install Python packages and dependencies

To install all required packages from a `pyproject.toml` file (such as the one located at the top level of this GitHub repository), run the following command, assuming the file is in the same directory as your terminal session:

```bash
uv add . --group dev
```

> [!NOTE]
> If you have problems with the following commands above due to certain dependencies (for example, if you are using Windows), you can always fall back to regular pip:
> `uv add pip`
> `uv run python -m pip install -U -r requirements.txt`

Note that the `uv add` command above will create a separate virtual environment via the `.venv` subfolder. (In case you want to delete your virtual environment to start from scratch, you can simply delete the `.venv` folder.)

You can install new packages, that are not specified in the `pyproject.toml` via `uv add`, for example:

```bash
uv add packaging
```

And you can remove packages via `uv remove`, for example:

```bash
uv remove packaging
```

### Run Python code

Your environment should now be ready to run the code in the repository. You can test it by running the following command to run a python script:

```bash
uv run python main.py
```

Or, if you don't want to type `uv run python` every time you execute code, manually activate the virtual environment first.

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows (PowerShell):

```bash
.venv\Scripts\activate
```

Then, run:

```bash
python main.py
```

### Launching JupyterLab

You can launch a JupyterLab instance via:

```bash
uv run jupyter lab
```

### Optional: Manage virtual environments manually

Alternatively, you can still install the dependencies directly from the repository using `uv pip install`. But note that this doesn't record dependencies in a `uv.lock` file as `uv add` does. Also, it requires creating and activating the virtual environment manually:

1. Create a new virtual environment

Run the following command to manually create a new virtual environment, which will be saved via a new `.venv` subfolder:

```bash
uv venv --python=python3.12
```

1. Activate virtual environment

Next, we need to activate this new virtual environment.

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows (PowerShell):

```bash
.venv\Scripts\activate
```

1. Install dependencies

To install the required dependencies from your local `requirements.txt` file, use the following command:

```bash
uv pip install -r requirements.txt
```

### UV self update

```bash
uv self update
```

### UV update packages (dependencies)

You can update all Python packages to the latest versions of the `uv.lock` file and sync the environment using the command below.
This will update all packages to their latest versions, which may not always be desirable.
If you want to update only specific packages, you can use `uv lock --upgrade <package_name>` instead.
This also does **not update** the specified dependencies **within the `pyproject.toml` file**. As of uv version 0.7.22 there is no way to update the dependencies in the `pyproject.toml` file automatically. Draft pull request: [#13934](https://github.com/astral-sh/uv/pull/13934).
You can update individual packages manually to the latest compatible version within the `pyproject.toml` file by using `uv add --upgrade <package_name>`.

```bash
uv lock --upgrade
uv sync --all-groups
```

> [!NOTE]
> Upgrade dependencies within the `pyproject.toml` file with the script `scripts/uv_upgrade_dependencies.py` respectively the Makefile target `update-packages`, [source](https://gist.github.com/yhoiseth/c80c1e44a7036307e424fce616eed25e):
>
> ```bash
> make update-packages
> ```
