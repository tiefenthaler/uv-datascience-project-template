import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def create_test_reports_dir() -> None:
    """Pytest fixture to create a directory for test reports.

    This fixture is executed automatically before any tests are run, and it ensures that
    the directory for storing test coverage reports exists.

    Scope:
        session: The fixture is executed once per test session.

    Autouse:
        True: The fixture is automatically used by all tests without explicitly requested.

    Raises:
        AssertionError: If the directory is not created successfully.

    Side Effects:
        Creates the directory specified by `test_reports_dir`.
    """
    test_reports_dir = ".test_reports/coverage/"
    os.makedirs(test_reports_dir, exist_ok=True)
    assert os.path.exists(test_reports_dir), f"Directory not created: {test_reports_dir}"
