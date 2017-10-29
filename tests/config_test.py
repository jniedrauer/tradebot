import os
import shutil
import tempfile
import unittest
from mock import call, mock_open, patch

from tradebot import config


def setup_and_teardown(f):
    def wrapper(*args, **kwargs):
        try:
            self = args[0]
            self.config = config.AppConfig()
            self.tmpdir = tempfile.mkdtemp()
            return f(*args, **kwargs)
        finally:
            del self.config
            shutil.rmtree(self.tmpdir)
    return wrapper


class TestConfig(unittest.TestCase):

    @setup_and_teardown
    def test_get_config_file_failed(self):
        os.environ['XDG_CONFIG'] = 'notreal'
        os.environ['HOME'] = 'notreal'
        with self.assertRaises(OSError):
            config.get_cfg_path()

    @setup_and_teardown
    def test_get_xdg_config_file(self):
        os.environ['XDG_CONFIG'] = self.tmpdir
