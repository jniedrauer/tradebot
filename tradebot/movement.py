"""High level logic for entry and exit from plays"""


class Movement(object):
    """A stateful movement"""

    def __init__(self, config, api):
        self.config = config
        self.api = api

    def enter(self, price=0.0, volume=0.0, spread=0.0, timeout=0.0):
        """Enter a position"""
        pass

    def exit(self, price=0.0, volume=0.0, spread=0.0, timeout=0.0):
        """Exit a position"""
        pass
