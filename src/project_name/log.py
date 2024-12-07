import logging
import logging.config
from typing import Any

import structlog
from structlog.dev import ConsoleRenderer
from structlog.processors import JSONRenderer
from structlog.stdlib import BoundLogger

from project_name.settings import SETTINGS, LogLevel, LogRenderer


def _get_logging_level(log_level: LogLevel) -> int:
    mapper = {
        LogLevel.CRITICAL: logging.CRITICAL,
        LogLevel.ERROR: logging.ERROR,
        LogLevel.WARNING: logging.WARNING,
        LogLevel.INFO: logging.INFO,
        LogLevel.DEBUG: logging.DEBUG,
    }
    return mapper[log_level]


TypeRenderer = ConsoleRenderer | JSONRenderer


def _get_structlog_renderer(log_renderer: LogRenderer) -> TypeRenderer:
    mapper: dict[LogRenderer, TypeRenderer] = {
        LogRenderer.TEXT: ConsoleRenderer(),
        LogRenderer.JSON: JSONRenderer(),
    }
    return mapper[log_renderer]


STANDARD_LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(levelname)s: %(message)s"}},
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "root": {
            "level": _get_logging_level(SETTINGS.THIRD_PARTY_LOG_LEVEL),
            "handlers": ["stdout"],
        },
    },
}


def _configure_logging() -> None:
    log_level = _get_logging_level(SETTINGS.LOG_LEVEL)
    renderer = _get_structlog_renderer(SETTINGS.LOG_RENDERER)
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        processors=[
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
            structlog.processors.add_log_level,
            structlog.processors.CallsiteParameterAdder(
                parameters={
                    structlog.processors.CallsiteParameter.FILENAME,
                    structlog.processors.CallsiteParameter.FUNC_NAME,
                    structlog.processors.CallsiteParameter.LINENO,
                },
            ),
            structlog.processors.EventRenamer(to="message"),
            renderer,
        ],
    )
    logging.config.dictConfig(config=STANDARD_LOGGING_CONFIG)


def _get_logger(*args: Any, **initial_values: dict[str, Any]) -> BoundLogger:  # noqa: ANN401
    if not structlog.is_configured():
        _configure_logging()
    return structlog.stdlib.get_logger(*args, **initial_values)


LOGGER = _get_logger("project_name")
