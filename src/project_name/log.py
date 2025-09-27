import logging
import logging.config

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
    "formatters": {
        "structlog": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": _get_structlog_renderer(SETTINGS.LOG_RENDERER),
            "foreign_pre_chain": [
                structlog.contextvars.merge_contextvars,
                structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
                structlog.processors.add_log_level,
                structlog.stdlib.add_logger_name,
                structlog.processors.CallsiteParameterAdder(
                    parameters={
                        structlog.processors.CallsiteParameter.FILENAME,
                        structlog.processors.CallsiteParameter.FUNC_NAME,
                        structlog.processors.CallsiteParameter.LINENO,
                    },
                ),
                structlog.processors.EventRenamer(to="message"),
                structlog.processors.StackInfoRenderer(),
            ],
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "structlog",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "project_name": {
            "level": _get_logging_level(SETTINGS.LOG_LEVEL),
            "handlers": ["stdout"],
            "propagate": False,
        },
        "root": {
            "level": _get_logging_level(SETTINGS.LOG_LEVEL_THIRD_PARTY),
            "handlers": ["stdout"],
        },
    },
}


def _configure_logging() -> None:
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
            structlog.processors.add_log_level,
            structlog.stdlib.add_logger_name,
            structlog.processors.CallsiteParameterAdder(
                parameters={
                    structlog.processors.CallsiteParameter.FILENAME,
                    structlog.processors.CallsiteParameter.FUNC_NAME,
                    structlog.processors.CallsiteParameter.LINENO,
                },
            ),
            structlog.processors.EventRenamer(to="message"),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    logging.config.dictConfig(config=STANDARD_LOGGING_CONFIG)


def get_logger(name: str = "project_name") -> BoundLogger:
    if not structlog.is_configured():
        _configure_logging()
    if name != "project_name" and not name.startswith("project_name."):
        name = f"project_name.{name}"
    return structlog.stdlib.get_logger(name)
