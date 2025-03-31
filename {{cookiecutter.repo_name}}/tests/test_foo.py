from {{cookiecutter.module_name}}.foo import foo # type: ignore # noqa: D103


def test_foo() -> None:
    assert foo("foo") == "foo" # type: ignore
