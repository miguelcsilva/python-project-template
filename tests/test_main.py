from unittest.mock import patch

from project_name.__main__ import main


def test_main_configures_logging() -> None:
    with patch(
        target="project_name.__main__.configure_logging"
    ) as mock_configure_logging:
        main()

    mock_configure_logging.assert_called_once_with()
