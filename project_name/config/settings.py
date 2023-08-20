from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    DEFAULT = "default"
    LOCAL = "local"


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
    )

    ENVIRONMENT: Environment = Environment.DEFAULT


SETTINGS = _Settings()
