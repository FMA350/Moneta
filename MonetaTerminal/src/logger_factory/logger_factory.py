import logging


class logger_factory:

    def get_logger(name: str, *others) -> logging.Logger:
        logger = logging.getLogger(name)
        
        return logger