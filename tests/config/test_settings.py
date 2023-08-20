import pytest
from pytest import MonkeyPatch

from project_name.config import SETTINGS
from project_name.config.settings import Environment, _Settings


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
    assert settings.ENVIRONMENT is Environment(environment)


def test_Settings_ENVIRONMENT_has_correct_default_when_missing(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.delattr(target=_Settings, name="model_config")
    settings = _Settings()
    assert settings.ENVIRONMENT is Environment.DEFAULT


def test_SETTINGS_singleton_has_ENVIRONMENT() -> None:
    assert SETTINGS.ENVIRONMENT in Environment
