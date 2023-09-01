import pytest
from pytest import MonkeyPatch

from project_name.config.settings import (
    SETTINGS,
    Environment,
    LogLevel,
    LogRenderer,
    _Settings,
)


@pytest.mark.parametrize(
    argnames=["environment"],
    argvalues=[
        ["local"],
        ["default"],
    ],
)
def test_settings_environemnt_is_correctly_instantiated_when_passed(
    monkeypatch: MonkeyPatch, environment: str
) -> None:
    monkeypatch.setenv(name="ENVIRONMENT", value=environment)
    settings = _Settings()
    assert settings.ENVIRONMENT is Environment(value=environment)


def test_settings_environment_has_correct_default_when_missing(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.delattr(target=_Settings, name="model_config")
    settings = _Settings()
    assert settings.ENVIRONMENT is Environment.DEFAULT


@pytest.mark.parametrize(
    argnames=["log_level"],
    argvalues=[
        ["critical"],
        ["error"],
        ["warning"],
        ["info"],
        ["debug"],
    ],
)
def test_settings_log_level_is_correctly_instantiated_when_passed(
    monkeypatch: MonkeyPatch, log_level: str
) -> None:
    monkeypatch.setenv(name="LOG_LEVEL", value=log_level)
    settings = _Settings()
    assert settings.LOG_LEVEL is LogLevel(value=log_level)


def test_settings_log_level_has_correct_default_when_missing(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.delattr(target=_Settings, name="model_config")
    settings = _Settings()
    assert settings.LOG_LEVEL is LogLevel.INFO


@pytest.mark.parametrize(
    argnames=["log_renderer"],
    argvalues=[
        ["console"],
        ["json"],
    ],
)
def test_settings_log_renderer_is_correctly_instantiated_when_passed(
    monkeypatch: MonkeyPatch, log_renderer: str
) -> None:
    monkeypatch.setenv(name="LOG_RENDERER", value=log_renderer)
    settings = _Settings()
    assert settings.LOG_RENDERER is LogRenderer(value=log_renderer)


def test_settings_log_renderer_has_correct_default_when_missing(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.delattr(target=_Settings, name="model_config")
    settings = _Settings()
    assert settings.LOG_RENDERER is LogRenderer.JSON


def test_settings_singleton_has_environment() -> None:
    assert SETTINGS.ENVIRONMENT in Environment


def test_settings_singleton_has_log_level() -> None:
    assert SETTINGS.LOG_LEVEL in LogLevel


def test_settings_singleton_has_log_renderer() -> None:
    assert SETTINGS.LOG_RENDERER in LogRenderer
