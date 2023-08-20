import pytest
from pytest import MonkeyPatch

from project_name.config import SETTINGS, Environment, LogLevel, LogRenderer
from project_name.config.settings import _Settings


@pytest.mark.parametrize(
    argnames=["environment"],
    argvalues=[
        ["local"],
        ["default"],
    ],
)
def test_Settings_ENVIRONMENT_is_correctly_instantiated_when_passed(
    monkeypatch: MonkeyPatch, environment: str
) -> None:
    monkeypatch.setenv(name="ENVIRONMENT", value=environment)
    settings = _Settings()
    assert settings.ENVIRONMENT is Environment(value=environment)


def test_Settings_ENVIRONMENT_has_correct_default_when_missing(
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
def test_Settings_LOG_LEVEL_is_correctly_instantiated_when_passed(
    monkeypatch: MonkeyPatch, log_level: str
) -> None:
    monkeypatch.setenv(name="LOG_LEVEL", value=log_level)
    settings = _Settings()
    assert settings.LOG_LEVEL is LogLevel(value=log_level)


def test_Settings_LOG_LEVEL_has_correct_default_when_missing(
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
def test_Settings_LOG_RENDERER_is_correctly_instantiated_when_passed(
    monkeypatch: MonkeyPatch, log_renderer: str
) -> None:
    monkeypatch.setenv(name="LOG_RENDERER", value=log_renderer)
    settings = _Settings()
    assert settings.LOG_RENDERER is LogRenderer(value=log_renderer)


def test_Settings_LOG_RENDERER_has_correct_default_when_missing(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.delattr(target=_Settings, name="model_config")
    settings = _Settings()
    assert settings.LOG_RENDERER is LogRenderer.JSON


def test_SETTINGS_singleton_has_ENVIRONMENT() -> None:
    assert SETTINGS.ENVIRONMENT in Environment


def test_SETTINGS_singleton_has_LOG_LEVEL() -> None:
    assert SETTINGS.LOG_LEVEL in LogLevel


def test_SETTINGS_singleton_has_LOG_RENDERER() -> None:
    assert SETTINGS.LOG_RENDERER in LogRenderer
