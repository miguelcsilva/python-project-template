from my_project.__main__ import hello_world


def test_hello_world() -> None:
    assert hello_world() == "Hello world!"
