import logging

LOG_FORMAT = '[%(asctime)s - %(levelname)s] %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


# config logger
def init():
    # Use console handler
    handler = logging.StreamHandler()

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # create formatter
    formatter = logging.Formatter(datefmt=LOG_DATE_FORMAT, fmt=LOG_FORMAT)
    # add formatter to handler
    handler.setFormatter(formatter)
    logger.addHandler(handler)
