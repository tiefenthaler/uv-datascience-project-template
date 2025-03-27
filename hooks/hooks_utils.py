"""This module contains utility functions for the cookiecutter hooks."""

import os
import shutil

REPO_DIRECTORY = os.path.realpath(os.path.curdir)


def test_print() -> None:
    """This function is used to test the hooks."""
    print("test")


def remove_file(filepath: str) -> None:
    """Remove a file from the repository directory.

    Args:
        filepath (str): The path of the file to be removed.
    """
    os.remove(os.path.join(REPO_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    """Remove a directory from the repository directory.

    Args:
        filepath (str): The path of the directory to be removed.
    """
    shutil.rmtree(os.path.join(REPO_DIRECTORY, filepath))


def move_file(filepath: str, target: str) -> None:
    """Move a file from one location to another within the repository directory.

    Args:
        filepath (str): The path of the file to be moved.
        target (str): The target path where the file should be moved.
    """
    os.rename(os.path.join(REPO_DIRECTORY, filepath), os.path.join(REPO_DIRECTORY, target))


def move_dir(src: str, target: str) -> None:
    """Move a directory from one location to another within the repository directory.

    Args:
        src (str): The source directory path.
        target (str): The target directory path.
    """
    shutil.move(os.path.join(REPO_DIRECTORY, src), os.path.join(REPO_DIRECTORY, target))


def move_parent_dir(src: str, target: str) -> None:
    """Move a directory from one location to another.

    Even if the target is outside the current directory.
    Supports absolute paths and relative paths that go up the directory tree.
    Relative paths is relative to the current directory (REPO_DIRECTORY).

    Args:
        src (str): The source directory path.
        target (str): The target directory path.
    """
    source_path = os.path.abspath(src) if os.path.isabs(src) else os.path.join(REPO_DIRECTORY, src)
    target_path = (
        os.path.abspath(target) if os.path.isabs(target) else os.path.join(REPO_DIRECTORY, target)
    )
    shutil.move(source_path, target_path)
