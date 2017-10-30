"""Main module"""


from .config import AppConfig
from .input import read_commandline_args


def main():
    """Module entrypoint"""
    args = read_commandline_args()
    config = AppConfig(**args)
    config.load()
    print(config._config)
