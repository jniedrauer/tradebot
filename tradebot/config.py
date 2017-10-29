"""Configuration loading"""


import os
from . import constants as const


def get_cfg_file():
    """Identify the config file in order of preference"""
    for path in const.CFG_FILES:
        if os.path.isfile(path):
            return path
    else:
        raise OSError('Configuration not found')


class AppConfig(object):
        """Global statefull configuration"""

        def __init__(self, **kwargs):
            self.kwargs = kwargs
            self._config = {}

        def load(self):
            """Load configuration from file and return dict"""
            pass

        def get(self, arg):
            """Get a configuration parameter"""
            return self._config.get(arg)

        def set(self, **kwargs):
            """Merge two sets of parameters, with kwargs overriding existing
            values"""
            self._config = {**self._config, **kwargs}
