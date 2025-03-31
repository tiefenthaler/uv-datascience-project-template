import os
import shutil
import sys


def copy_files_from_base_repository() -> bool:
    """Copy files to avoid duplicate files in cookiecutter folder."""
    try:
        # testing_framework
        os.remove(
            "{{cookiecutter.repo_name}}/pytest.ini"
        )  # placeholder only to indicate presence in cookiecutter
        shutil.move("pytest.ini", "{{cookiecutter.repo_name}}/pytest.ini")
        os.remove(
            "{{cookiecutter.repo_name}}/.coveragerc"
        )  # placeholder only to indicate presence in cookiecutter
        shutil.move(".coveragerc", "{{cookiecutter.repo_name}}/.coveragerc")
        # ruff
        os.remove(
            "{{cookiecutter.repo_name}}/ruff.toml"
        )  # placeholder only to indicate presence in cookiecutter
        shutil.move("ruff.toml", "{{cookiecutter.repo_name}}/ruff.toml")
        # pyright
        os.remove(
            "{{cookiecutter.repo_name}}/pyrightconfig.json"
        )  # placeholder only to indicate presence in cookiecutter
        shutil.move("pyrightconfig.json", "{{cookiecutter.repo_name}}/pyrightconfig.json")
        # CI
        shutil.rmtree(
            "{{cookiecutter.repo_name}}/.github"
        )  # placeholder only to indicate presence in cookiecutter
        shutil.move(".github", "{{cookiecutter.repo_name}}/.github")
        # devcontainer
        shutil.rmtree(
            "{{cookiecutter.repo_name}}/.devcontainer"
        )  # placeholder only to indicate presence in cookiecutter
        shutil.move(".devcontainer", "{{cookiecutter.repo_name}}/.devcontainer")
        # docker production
        os.remove(
            "{{cookiecutter.repo_name}}/.dockerignore"
        )  # placeholder only to indicate presence in cookiecutter
        shutil.move(".dockerignore", "{{cookiecutter.repo_name}}/.dockerignore")
        os.remove(
            "{{cookiecutter.repo_name}}/Dockerfile"
        )  # placeholder only to indicate presence in cookiecutter
        shutil.move("Dockerfile", "{{cookiecutter.repo_name}}/Dockerfile")
        os.remove(
            "{{cookiecutter.repo_name}}/multistage.Dockerfile"
        )  # placeholder only to indicate presence in cookiecutter
        shutil.move("multistage.Dockerfile", "{{cookiecutter.repo_name}}/multistage.Dockerfile")
        os.remove(
            "{{cookiecutter.repo_name}}/docker-compose.yml"
        )  # placeholder only to indicate presence in cookiecutter
        shutil.move("docker-compose.yml", "{{cookiecutter.repo_name}}/docker-compose.yml")
        return True
    except (FileNotFoundError, OSError) as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    if not copy_files_from_base_repository():
        print("ERROR: Could not copy files from base repository.")
        sys.exit(1)
    print("Pre-Prompt Hooks Complete")
