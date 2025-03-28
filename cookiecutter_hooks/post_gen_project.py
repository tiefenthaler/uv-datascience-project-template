import os

from .hooks_utils import (  # type: ignore
    move_dir,
    move_file,
    remove_dir,
    remove_file,
    test_print,
)


def main() -> None:
    """This function is called after the project is generated."""
    test_print()

    ### LICENSE ###
    if "{{cookiecutter.open_source_license}}" == "Not open source":
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "MIT license":
        move_file("LICENSE_MIT", "LICENSE")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "BSD license":
        move_file("LICENSE_BSD", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "Apache-2.0":
        move_file("LICENSE_APACHE", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")

    ### Directory Structure ###
    if "{{cookiecutter.directory_structure}}" == "src":
        if os.path.isdir("src"):
            remove_dir("src")
        move_dir(
            "{{cookiecutter.module_name}}", os.path.join("src", "{{cookiecutter.module_name}}")
        )

    ### Testing Framework ###
    if "{{cookiecutter.testing_framework}}" == "pytest-only":
        remove_file(".coveragerc")
        remove_file("tests/conftest.py")
        remove_file("tests/test_coverage.py")

    if "{{cookiecutter.testing_framework}}" == "pytest-and-code-coverage":
        remove_file("pytest.ini")

    if "{{cookiecutter.testing_framework}}" == "none":
        remove_file(".coveragerc")
        remove_file("pytest.ini")
        remove_file("tests/conftest.py")
        remove_file("tests/test_coverage.py")
        remove_dir("tests")

    ### Linting and Formatting ###
    if "{{cookiecutter.linting_and_formatting}}" == "none":
        remove_file("ruff.toml")

    ### Static Type Checking ###
    if "{{cookiecutter.static_type_checking}}" == "none":
        remove_file("pyrightconfig.json")

    ### Docs ###
    if "{{cookiecutter.docs_mkdocs}}" == "n":
        remove_file("mkdocs.yml")
        remove_dir("docs")

    ### Pre-commit Hooks ###
    if "{{cookiecutter.pre_commit_hooks}}" == "n":
        remove_file(".pre-commit-config.yaml")

    ### Github Actions CI ###
    if "{{cookiecutter.github_actions_ci}}" == "n":
        remove_dir(".github")

    ### VSCode Dev Container ###
    if "{{ cookiecutter.use_vscode_devcontainer }}" == "n":
        remove_dir(".devcontainer")

    ### Docker Production ###
    if "{{ cookiecutter.use_docker_production }}" == "none":
        remove_file("Dockerfile")
        remove_file("multistage.Dockerfile")
        remove_file("docker-compose.yml")

    if "{{ cookiecutter.use_docker_production }}" == "Dockerfile":
        remove_file("multistage.Dockerfile")

    if "{{ cookiecutter.use_docker_production }}" == "multistage.Dockerfile":
        remove_file("Dockerfile")


if __name__ == "__main__":
    main()
