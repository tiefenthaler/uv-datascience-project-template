from {{cookiecutter.module_name}}.foo import foo # type: ignore


def test_foo() -> None:
    assert foo("foo") == "foo" # type: ignore
