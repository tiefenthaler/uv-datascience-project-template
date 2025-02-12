# Pytest and Coverage Guide

This guide explains how to use `pytest` for testing and `coverage.py` for measuring test coverage in this project.

- [Pytest and Coverage Guide](#pytest-and-coverage-guide)
  - [Introduction to Pytest](#introduction-to-pytest)
    - [Key Features](#key-features)
  - [Running Tests](#running-tests)
    - [Specific Tests](#specific-tests)
  - [Introduction to Coverage.py](#introduction-to-coveragepy)
    - [Coverage Key Features](#coverage-key-features)
  - [Running Tests with Coverage](#running-tests-with-coverage)
  - [Configuration](#configuration)
    - [.coveragerc](#coveragerc)
    - [pytest.ini or pyproject.toml](#pytestini-or-pyprojecttoml)
  - [Usage in This Project](#usage-in-this-project)
  - [Example Workflow](#example-workflow)

## Introduction to Pytest

[pytest](https://docs.pytest.org/en/stable/) is a powerful and flexible testing framework for Python. It simplifies writing and running tests, and provides a rich set of features for test discovery, parametrization, fixtures, and more.

### Key Features

- **Simple Syntax:** Pytest uses a simple and intuitive syntax for writing tests.
- **Test Discovery:** It automatically discovers test files and test functions.
- **Fixtures:** Fixtures provide a way to set up and tear down test environments.
- **Plugins:** A rich ecosystem of plugins extends pytest's functionality.

## Running Tests

To run tests, use the following command in the project's root directory:

```bash
uv run pytest
```

This command will discover and run all files matching `test_*.py` or `*_test.py` in the project's directory and subdirectories.

### Specific Tests

To run a specific test file or test function, you can specify its path:

```bash
uv run pytest tests/test_module.py
uv run pytest tests/test_module.py::test_function
```

## Introduction to Coverage.py

[coverage.py](https://coverage.readthedocs.io/en/stable/) is a tool for measuring code coverage in Python. It monitors your program, notes which parts of the code have been executed, and then analyzes the source to identify code that could have been executed but was not.

### Coverage Key Features

- **Line Coverage:** Measures which lines of code were executed during testing.
- **Branch Coverage:** Measures which branches in the code were taken during testing.
- **Integration with Pytest:** Seamless integration with pytest for running tests and collecting coverage data.
- **Reporting:** Generates reports in various formats, including HTML, XML, and text.

## Running Tests with Coverage

To run tests with coverage, use the following command:

```bash
uv run pytest --cov
```

This command will run all tests and collect coverage data for the `src` directory. The `--cov` flag specifies the source directory to measure coverage for.

## Configuration

### .coveragerc

The `.coveragerc` file configures how `coverage.py` collects and reports coverage data.  
Key settings include:

- `data_file`: Specifies the location where coverage data is stored. In this project, it's set to `.test_reports/coverage/.coverage`.
- `source`: Specifies the source directories to measure coverage for. In this project, it's set to `src`.
- `branch`: Enables branch coverage.
- `omit`: Specifies files to exclude from coverage reporting.
- `report`: This will create an HTML report in the `.test_reports/coverage/html` directory. You can then open the `index.html` file in your browser to view the report.
  - XML Report: In the CI Workflow a XML report will be created in the `.test_reports/coverage/coverage.xml` file, which can be used for integration with CI/CD systems.

### pytest.ini or pyproject.toml

Pytest can be configured using a `pytest.ini` file or a `pyproject.toml` file. This project uses a `pytest.ini` file.

- `testpaths`: Specifies the directories to search for tests.
- `addopts`: Specifies command-line options to always use when running pytest.
- `filterwarnings`: To handle warnings during testing.

## Usage in This Project

This project is set up to automatically collect coverage data when running tests. The `.coveragerc` file is configured to:

- Store coverage data in the `.test_reports/coverage/` directory.
- Measure coverage for the `src` directory.
- Generate Terminal reports in the `.test_reports/coverage/` directory.
- Generate HTML reports in the `.test_reports/coverage/html` directory.

## Example Workflow

1. Write your code in the `src` directory.
2. Write tests for your code in the `tests` directory.
3. Run tests with coverage: `uv run pytest --cov`
4. Check the terminal report to see which parts of your code are not covered by tests.
5. Write more tests to increase coverage.
6. Repeat steps 3-5 until you have sufficient coverage.

By following this guide, you can effectively use `pytest` and `coverage.py` to write and test your code, ensuring high code quality and reliability.
