import logging


def create_logger(name, config):
    logging.basicConfig(format=config.FORMAT, level=config.LEVEL)
    logger = logging.getLogger(name)
    return logger
