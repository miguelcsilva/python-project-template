import logging
import sys

import structlog
from structlog.dev import ConsoleRenderer
from structlog.processors import JSONRenderer

from .settings import SETTINGS, LogLevel, LogRenderer


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
        LogRenderer.CONSOLE: ConsoleRenderer(),
        LogRenderer.JSON: JSONRenderer(),
    }
    return mapper[log_renderer]


def configure_logging() -> None:
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.CallsiteParameterAdder(
                {
                    structlog.processors.CallsiteParameter.FILENAME,
                    structlog.processors.CallsiteParameter.FUNC_NAME,
                    structlog.processors.CallsiteParameter.LINENO,
                }
            ),
            _get_structlog_renderer(log_renderer=SETTINGS.LOG_RENDERER),
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=_get_logging_level(log_level=SETTINGS.LOG_LEVEL),
    )
