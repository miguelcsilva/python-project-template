from project_name.__main__ import hello_world


def test_hello_world() -> None:
    assert hello_world() == "Hello world!"
