import logging
import colorlog


def get_logger(mod_name):
    logger = logging.getLogger(mod_name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stream=None)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    formatter = colorlog.ColoredFormatter(
        fmt='%(log_color)s[%(levelname)s] [%(asctime)s] {%(name)s} %(message)s:',
        datefmt='%H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white'})
    handler.setFormatter(formatter)
    return logger
