from .config.log import get_logger


def main() -> None:
    logger = get_logger(name=__name__)

    logger.info("This is a logging message.")


main()
