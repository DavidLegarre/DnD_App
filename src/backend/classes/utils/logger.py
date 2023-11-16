import logging

import colorlog


def setup_logger(logger_name, log_file, level=logging.DEBUG):
    """
    Set up a logger with a specified name, log file, and logging level.

    Args:
    - logger_name (str): The name of the logger.
    - log_file (str): The path to the log file.
    - level (int): The logging level (default is INFO).
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )

    # Log to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Log to file
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


# Example usage:
if __name__ == "__main__":
    logger = setup_logger("example_logger", "example.log")

    # Log some messages
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
