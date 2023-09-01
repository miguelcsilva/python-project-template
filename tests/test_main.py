import logging

from pytest import LogCaptureFixture

from project_name.__main__ import main


def test_main_produces_log(caplog: LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO):
        main()
    assert "This is a logging message." in caplog.text
