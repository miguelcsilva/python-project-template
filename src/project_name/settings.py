from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class LogLevel(StrEnum):
    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"


class LogRenderer(StrEnum):
    TEXT = "text"
    JSON = "json"


class Environment(StrEnum):
    LOCAL = "local"
    DEFAULT = "default"


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
    )

    ENVIRONMENT: Environment = Environment.DEFAULT
    LOG_LEVEL: LogLevel = LogLevel.INFO
    LOG_RENDERER: LogRenderer = LogRenderer.TEXT
    THIRD_PARTY_LOG_LEVEL: LogLevel = LogLevel.WARNING


SETTINGS = _Settings()
