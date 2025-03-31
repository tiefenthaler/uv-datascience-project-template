import re
import sys

if __name__ == "__main__":
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

    print("Pre-Generation Hooks Complete")
