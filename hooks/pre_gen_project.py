import re
import sys

from .hooks_utils import move_file, move_parent_dir, remove_dir, remove_file

REPO_NAME_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"
repo_name = "{{cookiecutter.repo_name}}"
if not re.match(REPO_NAME_REGEX, repo_name):
    print(
        "ERROR: The repository name "
        f"{repo_name} is not a valid Python repository name."
        "Please do not use a _ and use - instead"
    )
    # Exit to cancel project
    sys.exit(1)


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{cookiecutter.module_name}}"
if not re.match(MODULE_REGEX, module_name):
    print(f"ERROR: {module_name} is not a valid Python module name!")
    # Exit to cancel project
    sys.exit(1)

### Copy Files; to avoid duplicate files in cookiecutter folder ###
# testing_framework
remove_file("pytest.ini")  # placeholder only to indicate presence in cookiecutter
move_file("../pytest.ini", "pytest.ini")
remove_file(".coveragerc")  # placeholder only to indicate presence in cookiecutter
move_file("../.coveragerc", ".coveragerc")
# ruff
remove_file("ruff.toml")  # placeholder only to indicate presence in cookiecutter
move_file("../ruff.toml", "ruff.toml")
# pyright
remove_file("pyrightconfig.json")  # placeholder only to indicate presence in cookiecutter
move_file("../pyrightconfig.json", "pyrightconfig.json")
# devcontainer
remove_dir(".devcontainer")  # placeholder only to indicate presence in cookiecutter
move_parent_dir("../.devcontainer", ".devcontainer")
# docker production
remove_file(".dockerignore")  # placeholder only to indicate presence in cookiecutter
move_file("../.dockerignore", ".dockerignore")
remove_file("Dockerfile")  # placeholder only to indicate presence in cookiecutter
move_file("../Dockerfile", "Dockerfile")
remove_file("multistage.Dockerfile")  # placeholder only to indicate presence in cookiecutter
move_file("../multistage.Dockerfile", "multistage.Dockerfile")
remove_file("docker-compose.yml")  # placeholder only to indicate presence in cookiecutter
move_file("../docker-compose.yml", "docker-compose.yml")
