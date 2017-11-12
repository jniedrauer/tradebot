"""Main module"""


import logging
import sys
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
    log.debug('Configuration loaded: %s', config._config)

    app = MainApp(config)

    app.run_commandline()


class MainApp(object):
    """Main application state"""

    def __init__(self, config):
        self.config = config
        self.log = logging.getLogger(__name__)
        self.cmd = Commandline()

    def run_commandline(self):
        """Begin the command line loop"""
        self.cmd.cmdloop()
        sys.stdout.write('\n')
        self.log.info('Exited')
