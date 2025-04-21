# Contributing to UV Data Science Project Template

This document outlines the guidelines for contributing to the UV Data Science Project Template. We welcome contributions from the community, including bug reports, feature requests, and code contributions.
Please follow the guidelines below to ensure a smooth contribution process.

## Reporting Issues

To report bugs and issues with Daft, please report in detail:

1. Operating system
2. UV Data Science Project Template version
3. Python version
4. Runner that your code is using

## Proposing Features

Please start a GitHub Discussion under [Issues](https://github.com/tiefenthaler/uv-datascience-project-template/issues). Once the feature is clarified, fleshed out and approved, the corresponding issue(s) will be created from the GitHub discussion.

When proposing features, please include:

1. Feature Summary (no more than 3 sentences)
2. Example usage (pseudo-code to show how it is used)
3. Corner-case behavior (how should this code behave in various corner-case scenarios)

## Contributing Code

### Development Environment

To set up your development environment:

1. Ensure that your system has a suitable Python version installed (>=3.9)
2. Clone the repo: `git clone https://github.com/tiefenthaler/uv-datascience-project-template`
   - If you are a contributor, please fork the repo and clone your fork
   - If you are a maintainer, clone the main repo
   - If you are a user, clone the main repo
3. Run `make install` from your new cloned repository to create a new virtual environment with all of its development dependencies installed
4. Run `make install-hooks` to install pre-commit hooks: these will run tooling on every commit to ensure that your code meets Daft development standards
5. Run `make check` to check that your code meets development standards

### Developing

1. `make build`: recompile your code after modifying code in `src/`
2. `make test`: run tests
3. `make docs`: build docs
4. `make docs-serve`: build docs in development server
