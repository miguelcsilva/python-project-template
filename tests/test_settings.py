import pytest

from project_name.settings import (
    Environment,
    _get_settings,
    _LocalSettings,
    _Settings,
    _TestSettings,
)


@pytest.mark.parametrize(
    argnames=("environment", "additional_attributes", "expected_settings"),
    argvalues=[
        ("local", {}, _LocalSettings(ENVIRONMENT=Environment.LOCAL)),
        ("test", {}, _TestSettings(ENVIRONMENT=Environment.TEST)),
        ("default", {}, _Settings()),
        (None, {}, _Settings()),
    ],
)
def test_get_settings_from_environment(
    monkeypatch: pytest.MonkeyPatch,
    environment: str | None,
    additional_attributes: dict[str, str],
    expected_settings: _Settings,
) -> None:
    if environment:
        monkeypatch.setenv("ENVIRONMENT", environment)
    for name, value in additional_attributes.items():
        monkeypatch.setenv(name, value)
    settings = _get_settings()
    assert settings == expected_settings
