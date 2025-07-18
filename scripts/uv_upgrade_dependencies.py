import re
import subprocess
import tomllib
from pathlib import Path


def uv_command_for_remove_or_add_package(subcommand: str, packages: list[str], group: str | None):
    """Run the `uv` command to remove or add packages."""
    extra_arguments = []
    if group:
        extra_arguments.extend(["--group", group])

    subprocess.check_call(["uv", subcommand, *packages, "--no-sync"] + extra_arguments)


def uv_upgrade_dependencies() -> None:
    """Upgrade python packages to latest version within the pyproject.toml.

    Warning:
    from the `pyproject.toml` file, this may delete:
        - comments
        - upper bounds etc
        - markers
        - ordering of dependencies
        - tool.uv.sources
    """
    pyproject = tomllib.loads(Path("pyproject.toml").read_text())
    package_name_pattern = re.compile(r"^([-a-zA-Z\d]+)(\[[-a-zA-Z\d,]+])?")
    for group, dependencies in {
        None: pyproject["project"]["dependencies"],
        **pyproject["dependency-groups"],
    }.items():
        to_remove = []
        to_add = []
        for dependency in dependencies:
            package_match = package_name_pattern.match(dependency)
            assert package_match, f"invalid package name '{dependency}'"
            package, extras = package_match.groups()
            to_remove.append(package)
            to_add.append(f"{package}{extras or ''}")
        uv_command_for_remove_or_add_package("remove", to_remove, group=group)
        uv_command_for_remove_or_add_package("add", to_add, group=group)
    subprocess.check_call(["uv", "sync"])


if __name__ == "__main__":
    uv_upgrade_dependencies()
