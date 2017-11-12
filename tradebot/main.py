"""Main module"""


import importlib
import logging
import pkg_resources
from .api import ApiInterface
from .config import AppConfig
from .input import read_commandline_args
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
    plugin = importlib.import_module(plugins.get(config.get('plugin')))

    api = ApiInterface(plugin, config)

    print(api.get_holdings('test'))
