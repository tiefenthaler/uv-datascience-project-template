"""This module contains the post generation hooks for the cookiecutter template."""

import os
import shutil


def main() -> None:
    """This function is called after the project is generated."""

    ### LICENSE ###
    if "{{cookiecutter.open_source_license}}" == "Not open source":
        os.remove("LICENSE_MIT")
        os.remove("LICENSE_BSD")
        os.remove("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "MIT license":
        shutil.move("LICENSE_MIT", "LICENSE")
        os.remove("LICENSE_BSD")
        os.remove("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "BSD license":
        shutil.move("LICENSE_BSD", "LICENSE")
        os.remove("LICENSE_MIT")
        os.remove("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "Apache-2.0":
        shutil.move("LICENSE_APACHE", "LICENSE")
        os.remove("LICENSE_MIT")
        os.remove("LICENSE_BSD")

    ### Directory Structure ###
    if "{{cookiecutter.directory_structure}}" == "src":
        shutil.move(
            "{{cookiecutter.module_name}}", os.path.join("src", "{{cookiecutter.module_name}}")
        )

    ### Testing Framework ###
    if "{{cookiecutter.testing_framework}}" == "pytest-only":
        os.remove(".coveragerc")
        os.remove("tests/conftest.py")
        os.remove("tests/test_coverage.py")

    if "{{cookiecutter.testing_framework}}" == "pytest-and-code-coverage":
        pass

    if "{{cookiecutter.testing_framework}}" == "none":
        os.remove(".coveragerc")
        os.remove("pytest.ini")
        os.remove("tests/conftest.py")
        os.remove("tests/test_coverage.py")
        shutil.rmtree("tests")

    ### Linting and Formatting ###
    if "{{cookiecutter.linting_and_formatting}}" == "none":
        shutil.rmtree("ruff.toml")

    ### Static Type Checking ###
    if "{{cookiecutter.static_type_checking}}" == "none":
        os.remove("pyrightconfig.json")

    ### Docs ###
    if "{{cookiecutter.docs_mkdocs}}" == "n":
        os.remove("mkdocs.yml")
        shutil.rmtree("docs")

    ### Pre-commit Hooks ###
    if "{{cookiecutter.pre_commit_hooks}}" == "n":
        os.remove(".pre-commit-config.yaml")

    ### Github Actions CI ###
    if "{{cookiecutter.github_actions_ci}}" == "n":
        shutil.rmtree(".github")

    ### VSCode Dev Container ###
    if "{{ cookiecutter.use_vscode_devcontainer }}" == "n":
        shutil.rmtree(".devcontainer")

    ### Docker Production ###
    if "{{ cookiecutter.use_docker_production }}" == "none":
        os.remove("Dockerfile")
        os.remove("multistage.Dockerfile")
        os.remove("docker-compose.yml")
        os.remove(".dockerignore")

    if "{{ cookiecutter.use_docker_production }}" == "Dockerfile":
        os.remove("multistage.Dockerfile")

    if "{{ cookiecutter.use_docker_production }}" == "multistage.Dockerfile":
        os.remove("Dockerfile")


if __name__ == "__main__":
    main()
    print("Post-Generation Hooks Complete")
