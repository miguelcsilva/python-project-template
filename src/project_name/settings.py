import os
from enum import StrEnum, auto

from pydantic_settings import BaseSettings, SettingsConfigDict


class LogLevel(StrEnum):
    CRITICAL = auto()
    ERROR = auto()
    WARNING = auto()
    INFO = auto()
    DEBUG = auto()


class LogRenderer(StrEnum):
    TEXT = auto()
    JSON = auto()


class Environment(StrEnum):
    LOCAL = auto()
    TEST = auto()
    DEFAULT = auto()


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(
        frozen=True,
    )
    ENVIRONMENT: Environment = Environment.DEFAULT
    LOG_LEVEL: LogLevel = LogLevel.INFO
    LOG_RENDERER: LogRenderer = LogRenderer.TEXT
    THIRD_PARTY_LOG_LEVEL: LogLevel = LogLevel.WARNING


class _LocalSettings(_Settings):
    model_config = SettingsConfigDict(
        env_file=".env",
        frozen=True,
    )
    ENVIRONMENT: Environment = Environment.LOCAL


class _TestSettings(_Settings):
    model_config = SettingsConfigDict(
        frozen=True,
    )
    ENVIRONMENT: Environment = Environment.TEST


def _get_settings() -> _Settings:
    environment_str = os.environ.get("ENVIRONMENT", "default")
    environment = (
        Environment(environment_str)
        if environment_str in Environment
        else Environment.DEFAULT
    )
    mapping = {
        Environment.DEFAULT: _Settings,
        Environment.LOCAL: _LocalSettings,
        Environment.TEST: _TestSettings,
    }
    return mapping[environment](ENVIRONMENT=environment)


SETTINGS = _get_settings()
