import sys

from .hooks_utils import move_file, move_parent_dir, remove_dir, remove_file


def copy_files_from_base_repository() -> bool:
    """Copy files to avoid duplicate files in cookiecutter folder."""
    try:
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
        # CI
        remove_dir(".github")  # placeholder only to indicate presence in cookiecutter
        move_parent_dir("../.github", ".github")
        # devcontainer
        remove_dir(".devcontainer")  # placeholder only to indicate presence in cookiecutter
        move_parent_dir("../.devcontainer", ".devcontainer")
        # docker production
        remove_file(".dockerignore")  # placeholder only to indicate presence in cookiecutter
        move_file("../.dockerignore", ".dockerignore")
        remove_file("Dockerfile")  # placeholder only to indicate presence in cookiecutter
        move_file("../Dockerfile", "Dockerfile")
        remove_file(
            "multistage.Dockerfile"
        )  # placeholder only to indicate presence in cookiecutter
        move_file("../multistage.Dockerfile", "multistage.Dockerfile")
        remove_file("docker-compose.yml")  # placeholder only to indicate presence in cookiecutter
        move_file("../docker-compose.yml", "docker-compose.yml")
        return True
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    if not copy_files_from_base_repository():
        print("ERROR: Could not copy files from base repository.")
        sys.exit(1)
    print("Pre-Prompt Hooks Complete")
