import logging

import pytest
import structlog
from structlog.dev import ConsoleRenderer
from structlog.processors import JSONRenderer

from project_name.config.log import (
    TypeRenderer,
    _configure_logging,
    _get_logging_level,
    _get_structlog_renderer,
    get_logger,
)
from project_name.config.settings import LogLevel, LogRenderer


def test_configure_logging_configures_logging() -> None:
    structlog.reset_defaults()
    assert structlog.is_configured() is False
    _configure_logging()
    assert structlog.is_configured() is True


@pytest.mark.parametrize(
    argnames=["log_level", "logging_level"],
    argvalues=[
        [LogLevel.CRITICAL, logging.CRITICAL],
        [LogLevel.ERROR, logging.ERROR],
        [LogLevel.WARNING, logging.WARNING],
        [LogLevel.INFO, logging.INFO],
        [LogLevel.DEBUG, logging.DEBUG],
    ],
)
def test__get_logging_level_returns_correct_logging_level(
    log_level: LogLevel, logging_level: int
) -> None:
    assert _get_logging_level(log_level=log_level) == logging_level


@pytest.mark.parametrize(
    argnames=["log_renderer", "structlog_renderer"],
    argvalues=[
        [LogRenderer.CONSOLE, ConsoleRenderer],
        [LogRenderer.JSON, JSONRenderer],
    ],
)
def test__get_structlog_renderer_returns_correct_structlog_renderer(
    log_renderer: LogRenderer, structlog_renderer: TypeRenderer
) -> None:
    assert (
        type(_get_structlog_renderer(log_renderer=log_renderer))
        is structlog_renderer  # type:ignore[comparison-overlap]
    )


def test_get_logger_returns_configured_logger() -> None:
    structlog.reset_defaults()
    assert structlog.is_configured() is False
    get_logger(name=__name__)
    assert structlog.is_configured() is True
