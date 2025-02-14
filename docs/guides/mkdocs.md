# MkDocs Documentation

MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

- [MkDocs Documentation](#mkdocs-documentation)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Using mkdocstrings](#using-mkdocstrings)
  - [Using mkdocs-jupyter](#using-mkdocs-jupyter)
  - [Create Documentation](#create-documentation)
    - [Init Documentation](#init-documentation)
    - [Create MkDocs Configuration File](#create-mkdocs-configuration-file)
    - [Generate General Documentation](#generate-general-documentation)
    - [Generate API Documentation](#generate-api-documentation)
  - [Building the Documentation](#building-the-documentation)
  - [Serving the Documentation](#serving-the-documentation)
  - [Deploying the Documentation](#deploying-the-documentation)

## Installation

Install MkDocs and the related extensions (using uv):

- [mkdocs](https://www.mkdocs.org/)
- [mkdocs-include-markdown-plugin](https://github.com/mondeja/mkdocs-include-markdown-plugin#documentation)
- [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
- [mkdocstrings](https://mkdocstrings.github.io/)
- [mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter)

## Configuration

The `mkdocs.yml` file is the configuration file for MkDocs. It contains settings such as the site name, navigation, theme, and plugins.

Key Configuration Options Used in this Project:

- `site_name`: The name of the site.
- `nav`: The navigation structure of the site. This defines the table of contents.
- `theme`: The theme used for the site. We use the material theme.
- `plugins`: A list of plugins used by MkDocs.
    - `search`: The built-in search plugin adds a search box to the site.
    - `include-markdown`: This plugin allows you to include Markdown files within other Markdown files. This is useful for reusing content across multiple pages.
    - `mkdocstrings`: This plugin generates documentation from Python docstrings. It is used to generate the "Source Code API Reference" section in the navigation.
    - `mkdocs-jupyter`: This plugin allows you to include Jupyter notebooks in your MkDocs documentation.
- `extra_css`:
    - `stylesheets/extra.css`: Custom CSS file to style the documentation.

## Using mkdocstrings

The mkdocstrings plugin is configured to use the google docstring style. This means that the plugin will parse docstrings that follow the Google docstring format. For example:

```Python
def my_function(arg1, arg2):
    """
    This is a function that does something.

    Args:
        arg1: The first argument.
        arg2: The second argument.

    Returns:
        The result of the function.
    """
    return arg1 + arg2
```

The mkdocstrings plugin will automatically generate documentation for this function, including the arguments, return value, and description. The "Source Code API Reference" section in the navigation is generated using this plugin.

## Using mkdocs-jupyter

The mkdocs-jupyter plugin allows you to include Jupyter notebooks in your MkDocs documentation. To include a notebook, simply add it to the nav section of your mkdocs.yml file. The plugin will automatically convert the notebook to HTML and include it in your documentation. This is very useful for tutorials. For example:

```yaml
nav:
  - Notebook: notebook.ipynb
```

## Create Documentation

### Init Documentation

Init documentation using `mkdocs` for an existing project:

```shell
uv run mkdocs new .
```

This will create a mkdocs.yml file and a docs/ folder with an index.md file.

```Text
project/
│
├── src/calculator/
│   ├── __init__.py
│   └── calculations.py
│
├── docs/
│   └── index.md
│
├── mkdocs.yml
├── README.md
├── pyproject.toml
└── ...
```

### Create MkDocs Configuration File

Create mkdocs Configuration File: Edit the mkdocs.yml file in the root of your project. This file will contain the configuration for your mkdocs site.

```yaml
site_name: UV Data Science Project Template
nav:
  - Home: index.md
  - Guides:
    - Ruff: guides/ruff.md
    - UV: guides/uv.md
    - PyTest: guides/pytest.md
    - PyRight: guides/pyright.md
    - Pre-Commit: guides/pre-commit.md
    - MkDocs: guides/mkdocs.md
    - Docker-Production: guides/docker_prod.md
    - Docker-VSCode-DevContainer: guides/docker_vscode_devcontainer.md
    - CI-GitHub: guides/ci_github.md
  - Source Code API Reference:
      - Autoencoder: api/autoencoder.md
      - Training: api/training.md
      - FastAPI: api/fastapi_app.md
theme:
  name: material
plugins:
  - search
  - include-markdown
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: google
```

### Generate General Documentation

Generate General Documentation: For example use the `index.md` to reference your `README.md` file.
**`docs/index.md`:**

```md
# Dev Container UV Data Science

Welcome to the documentation for the Dev Container UV Data Science project.

<!-- Include the content of README.devcontainer.md -->
<!-- Using PyMdown Snippets for inclusion relative to the base_path defined in the mkdocs.yml-->
<!-- Uncomment the following lines to include the README.devcontainer.md file -->
<!-- --8<-- ".devcontainer/README.devcontainer.md" -->
```

### Generate API Documentation

Use `mkdocstrings` to generate API documentation from your Python docstrings. In your `autoencoder.md` and `training.md` files, you can include references to your Python modules:

- Create Documentation Files: Create a docs directory in the root of your project. Inside this directory, create the necessary Markdown files for your documentation.

    ```bash
    mkdir docs/api
    touch docs/api/autoencoder.md
    touch docs/api/training.md
    ```

**`docs/docs/autoencoder.md`:**

```Markdown
# Autoencoder

::: dev_container_uv_datascience.lit_auto_encoder
```

**`docs/training.md`:**

```Markdown
# Training

::: dev_container_uv_datascience.train_autoencoder
```

## Building the Documentation

To build the documentation, run the command below. This will generate a static site in the site directory.

```bash
uv run mkdocs build
```

## Serving the Documentation

To serve the documentation locally, run the command below. This will start a local web server that you can use to view the documentation.

```bash
uv run mkdocs serve
```

## Deploying the Documentation

The documentation can be deployed to a variety of platforms, such as GitHub Pages, Netlify, or AWS S3. This project is set up to deploy to GitHub Pages using GitHub Actions. See the CI-GitHub guide for more information.

To deploy your documentation, you can use the `mkdocs gh-deploy` command to deploy it to GitHub Pages:

```bash
uv run mkdocs gh-deploy
```

Ensure you enable GitHub pages via the repo settings, see:

- [GitHub - Deploy MkDocs](https://github.com/marketplace/actions/deploy-mkdocs)
- [MkDocs - Deploying your docs](https://www.mkdocs.org/user-guide/deploying-your-docs/#read-the-docs)
- [Publishing your site](https://squidfunk.github.io/mkdocs-material/publishing-your-site/?h=deploy#with-github-actions)
- [GitHub Pages](https://pages.github.com/)
