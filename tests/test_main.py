from my_project.__main__ import hello_world


def test_hello_world(capfd):
    hello_world()
    console_output, _ = capfd.readouterr()
    assert console_output.strip() == "Hello world!"
