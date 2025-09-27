from project_name.log import get_logger

LOGGER = get_logger()


def main() -> None:
    LOGGER.info("Program started.")
    try:
        result = 1 / 0
        LOGGER.info("Division successful.", result=result)
    except ZeroDivisionError:
        LOGGER.exception("Cannot divide by 0.")
    LOGGER.info("Program finished.")


if __name__ == "__main__":
    main()
