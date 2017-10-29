import os
import shutil
import tempfile
import unittest
from importlib import reload
from mock import call, mock_open, patch

from tradebot import config, constants as const


def setup_and_teardown(f):
    def wrapper(*args, **kwargs):
        try:
            self = args[0]
            os.environ.pop('XDG_CONFIG_HOME', None)
            os.environ.pop('HOME', None)
            self.config = config.AppConfig()
            self.tmpdir = tempfile.mkdtemp()
            return f(*args, **kwargs)
        finally:
            shutil.rmtree(self.tmpdir)
    return wrapper


def setup_config_file(path, content):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, const.CFG_FILE), 'w') as f:
        f.write(content)


class TestConfig(unittest.TestCase):

    @setup_and_teardown
    def test_get_config_file_failed(self):
        os.environ['XDG_CONFIG_HOME'] = 'notreal'
        os.environ['HOME'] = 'notreal'
        reload(const)

        with self.assertRaises(OSError):
            config.get_cfg_file()

    @setup_and_teardown
    def test_get_xdg_config_file(self):
        os.environ['XDG_CONFIG_HOME'] = self.tmpdir
        setup_config_file(os.path.join(self.tmpdir, 'tradebot'), '')
        reload(const)

        res = config.get_cfg_file()

        self.assertEqual(res, os.path.join(os.environ['XDG_CONFIG_HOME'],
                                            'tradebot', const.CFG_FILE))
