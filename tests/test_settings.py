import pytest

from project_name.settings import (
    Environment,
    LogLevel,
    LogRenderer,
    _Settings,
)


@pytest.mark.parametrize(
    argnames=["name", "value", "expected"],
    argvalues=[
        ["ENVIRONMENT", "local", Environment.LOCAL],
        ["ENVIRONMENT", "default", Environment.DEFAULT],
        ["LOG_LEVEL", "debug", LogLevel.DEBUG],
        ["LOG_LEVEL", "info", LogLevel.INFO],
        ["LOG_LEVEL", "warning", LogLevel.WARNING],
        ["LOG_LEVEL", "error", LogLevel.ERROR],
        ["LOG_LEVEL", "critical", LogLevel.CRITICAL],
        ["LOG_RENDERER", "text", LogRenderer.TEXT],
        ["LOG_RENDERER", "json", LogRenderer.JSON],
        ["THIRD_PARTY_LOG_LEVEL", "debug", LogLevel.DEBUG],
        ["THIRD_PARTY_LOG_LEVEL", "info", LogLevel.INFO],
        ["THIRD_PARTY_LOG_LEVEL", "warning", LogLevel.WARNING],
        ["THIRD_PARTY_LOG_LEVEL", "error", LogLevel.ERROR],
        ["THIRD_PARTY_LOG_LEVEL", "critical", LogLevel.CRITICAL],
    ],
)
def test_settings_attribute_is_correctly_instantiated_when_provided(
    monkeypatch: pytest.MonkeyPatch,
    name: str,
    value: str,
    expected: str,
) -> None:
    monkeypatch.setenv(name=name, value=value)
    settings = _Settings()
    attribute = getattr(settings, name)
    assert attribute is expected


@pytest.mark.parametrize(
    argnames=["name", "expected"],
    argvalues=[
        ["ENVIRONMENT", Environment.DEFAULT],
        ["LOG_LEVEL", LogLevel.INFO],
        ["LOG_RENDERER", LogRenderer.TEXT],
        ["THIRD_PARTY_LOG_LEVEL", LogLevel.WARNING],
    ],
)
def test_settings_attribute_has_correct_default_when_missing(
    monkeypatch: pytest.MonkeyPatch,
    name: str,
    expected: str,
) -> None:
    monkeypatch.delattr(target=_Settings, name="model_config")
    settings = _Settings()
    attribute = getattr(settings, name)
    assert attribute is expected
