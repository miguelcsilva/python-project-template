from structlog import get_logger

from .config import configure_logging


def main() -> None:
    configure_logging()

    logger = get_logger(name=__name__)

    logger.info("This is a logging message.", magic_number=42)


main()
