import time
from loguru import logger

from classes.utils.utils import seconds_to_hms


def timeIt(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        logger.info(f"Calling {func}")
        func(*args, **kwargs)
        logger.info(f"{func} completed in {seconds_to_hms(time.time() - t1)} seconds")
    return wrapper
