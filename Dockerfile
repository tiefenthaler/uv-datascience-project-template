# Dockerfile for a production setup python application incl. custom source package using uv.
# ------------------------------------------------------------------------------------------
# The image is defined in a way, where both base images are integrated.
# Custom python code should be a packaged application.
# For more information, see: https://docs.astral.sh/uv/concepts/projects/init/
#   and see: https://docs.astral.sh/uv/concepts/projects/workspaces/
# ------------------------------------------------------------------

# Define a build-time argument with a default value for base container images.
ARG UV_VER=python3.12-bookworm
# Define a build-time argument with a default value for the workspace name.
ARG WORKSPACE_NAME=app

# Use a python image with uv pre-installed and a Debian base image.
FROM ghcr.io/astral-sh/uv:$UV_VER AS uv

# Set the working directory.
WORKDIR /${WORKSPACE_NAME}

# Enable bytecode compilation for faster startup.
ENV UV_COMPILE_BYTECODE=1

# Production setup: Copy and install dependencies without installing the project.
# COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Production setup: Copy application and related package source code and install it.
#     For an even more robust setup, consider installing packages using a wheel file.
# Installing separately from its dependencies allows optimal layer caching.
COPY . /${WORKSPACE_NAME}
# Use the uv interface to install the packages.
RUN --mount=type=cache,target=/root/.cache/uv \
    # If a build system is defined in the pyproject.toml, it will be used to build the package.
    uv sync --frozen --no-dev
    # If a build system is defined in the pyproject.toml and you do not want to build the packages.
    # Use "--no-editable" to install the package from source code, but without a dependency on the originating source code.
    # uv sync --frozen --no-dev --no-editable

# Add executables to environment paths, to ensure that these executables are used instead of any system-wide versions.
ENV PATH="/${WORKSPACE_NAME}/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`, ensure container won't run any command by default.
ENTRYPOINT []

# Run the FastAPI application by default with `uvicorn`.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
