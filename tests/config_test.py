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
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, 'w') as f:
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
        reload(const)
        setup_config_file(os.path.join(self.tmpdir, 'tradebot',
                                       const.CFG_FILE), '')

        res = config.get_cfg_file()

        self.assertEqual(res, os.path.join(os.environ['XDG_CONFIG_HOME'],
                                            'tradebot', const.CFG_FILE))

    @setup_and_teardown
    def test_get_config_value(self):
        os.environ['XDG_CONFIG_HOME'] = self.tmpdir
        reload(const)
        content = (
            'test_key: test_value\n'
        )
        setup_config_file(os.path.join(self.tmpdir, 'tradebot',
                                       const.CFG_FILE), content)

        self.config.load()

        self.assertEqual('test_value', self.config.get('test_key'))

    @setup_and_teardown
    def test_get_default_config_value(self):
        os.environ['XDG_CONFIG_HOME'] = self.tmpdir
        reload(const)
        setup_config_file(os.path.join(self.tmpdir, 'tradebot',
                          const.CFG_FILE), '')

        self.config.load()

        self.assertNotEqual(None, self.config.get('log'))

    @setup_and_teardown
    def test_get_config_value_override_default(self):
        os.environ['XDG_CONFIG_HOME'] = self.tmpdir
        reload(const)
        content = (
            'log: test_value\n'
        )
        setup_config_file(os.path.join(self.tmpdir, 'tradebot',
                                       const.CFG_FILE), content)

        self.config.load()

        self.assertEqual('test_value', self.config.get('log'))

    @setup_and_teardown
    def test_set_config_value(self):
        os.environ['XDG_CONFIG_HOME'] = self.tmpdir
        reload(const)
        content = (
            'test_key: test_value\n'
        )
        setup_config_file(os.path.join(self.tmpdir, 'tradebot',
                                      const.CFG_FILE), content)
        self.config.load()
        self.config.set(test_key='override')

        self.assertEqual('override', self.config.get('test_key'))

    @setup_and_teardown
    def test_environment_config_file(self):
        os.environ['TRADEBOT_CONFIG_FILE'] = os.path.join(self.tmpdir, 'test.yml')
        os.environ['XDG_CONFIG_HOME'] = self.tmpdir
        reload(const)

        wrong_content = (
            'test_key: wrong_value\n'
        )
        right_content = (
            'test_key: right_value\n'
        )
        setup_config_file(os.path.join(self.tmpdir, 'tradebot',
                                      const.CFG_FILE), wrong_content)
        setup_config_file(os.environ['TRADEBOT_CONFIG_FILE'], right_content)

        self.config.load()

        self.assertEqual('right_value', self.config.get('test_key'))

    @setup_and_teardown
    def test_commandline_args(self):
        os.environ['TRADEBOT_CONFIG_FILE'] = os.path.join(self.tmpdir, 'test.yml')
        reload(const)
        setup_config_file(os.environ['TRADEBOT_CONFIG_FILE'], '---')

        expected = {'test_key': 'test_value'}
        self.config = config.AppConfig(**expected)
        self.config.load()

        self.assertEqual('test_value', self.config.get('test_key'))
