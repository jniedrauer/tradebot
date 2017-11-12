"""Set up logging for other modules"""


import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
import os


def setup_logging(**kwargs):
    """Configure a root logger"""
    try:
        path = os.path.expanduser(kwargs['log'])
    except IndexError:
        raise RuntimeError('No log path provided')

    logging.getLogger().setLevel(logging.DEBUG) # Set root logger minimum level
    log_format = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    log_file = RotatingFileHandler(path, maxBytes=1000000, backupCount=3)
    log_file.setFormatter(log_format)
    log_file.setLevel(log_level_to_constant(kwargs.get('loglevel')))
    logging.getLogger().addHandler(log_file)

    log_console = StreamHandler()
    log_console.setFormatter(logging.Formatter('%(message)s'))
    log_console.setLevel(log_level_to_constant(kwargs.get('loglevel')))
    logging.getLogger().addHandler(log_console)


def log_level_to_constant(loglevel):
    """Convert human readable log level to logging constant"""
    return getattr(logging, loglevel)
