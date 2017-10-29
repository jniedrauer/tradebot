"""Main module"""


from .config import AppConfig


def main():
    """Module entrypoint"""
    config = AppConfig()
    config.load()
    print(config.get('log'))
    print(config.get('plugin'))
