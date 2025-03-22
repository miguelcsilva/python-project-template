import logging

import pytest
from structlog.dev import ConsoleRenderer
from structlog.processors import JSONRenderer

from project_name.log import (
    TypeRenderer,
    _get_logging_level,
    _get_structlog_renderer,
)
from project_name.settings import LogLevel, LogRenderer


@pytest.mark.parametrize(
    argnames=("log_level", "logging_level"),
    argvalues=[
        (LogLevel.CRITICAL, logging.CRITICAL),
        (LogLevel.ERROR, logging.ERROR),
        (LogLevel.WARNING, logging.WARNING),
        (LogLevel.INFO, logging.INFO),
        (LogLevel.DEBUG, logging.DEBUG),
    ],
)
def test_get_logging_level_returns_correct_logging_level(
    log_level: LogLevel,
    logging_level: int,
) -> None:
    assert _get_logging_level(log_level=log_level) == logging_level


@pytest.mark.parametrize(
    argnames=("log_renderer", "structlog_renderer"),
    argvalues=[
        (LogRenderer.TEXT, ConsoleRenderer),
        (LogRenderer.JSON, JSONRenderer),
    ],
)
def test_get_structlog_renderer_returns_correct_structlog_renderer(
    log_renderer: LogRenderer,
    structlog_renderer: TypeRenderer,
) -> None:
    assert (
        type(_get_structlog_renderer(log_renderer=log_renderer)) is structlog_renderer  # type:ignore[comparison-overlap]
    )
