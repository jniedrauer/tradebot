"""Main module"""


import logging
import sys
import pkg_resources
from .config import AppConfig
from .input import Commandline, read_commandline_args
from .logging import setup_logging


def main():
    """Module entrypoint"""
    args = read_commandline_args()
    config = AppConfig(**args)
    config.load()
    setup_logging(
        log=config.get('log'),
        loglevel=config.get('loglevel')
    )
    log = logging.getLogger(__name__)
    # pylint: disable=protected-access
    log.debug('Configuration loaded: %s', config._config)

    plugins = {
        entry_point.name: entry_point.load()
        for entry_point
        in pkg_resources.iter_entry_points('tradebot.plugins')
    }
    plugins['dummy'] = 'tradebot.plugins.dummy'

    log.debug('Loaded plugins: %s', plugins)

    cmd = Commandline()
    cmd.cmdloop()
    sys.stdout.write('\n')
    log.info('Exited')
