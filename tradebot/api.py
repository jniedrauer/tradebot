"""High level API for interacting with an exchange"""


import logging


class Market(object):
    """A single market ticker on an exchange"""

    def __init__(self, api, ticker, pair):
        self.api = api
        self.ticker = ticker
        self.pair = pair

    @property
    def price(self):
        """Current market price"""
        return self.api.get_price(self.ticker)

    @property
    def holdings(self):
        """Current volume owned"""
        return self.api.get_holdings(self.ticker)


class ApiInterface(object):
    """Interface for API plugins"""

    def __init__(self, plugin):
        self.plugin = plugin
        self.log = logging.getLogger(__name__)
        self.log.debug('Initialized interface with plugin %s', plugin)

    def buy(self, ticker, price, volume):
        """Create a remote buy order"""
        return self.plugin.buy(ticker, price, volume)

    def sell(self, ticker, price, volume):
        """Create a remote sell order"""
        return self.plugin.sell(ticker, price, volume)

    def cancel(self, order_id):
        """Cancel a remote order"""
        return self.plugin.cancel(order_id)

    def get_price(self, ticker):
        """Get remote price for a ticker"""
        return self.plugin.get_price(ticker)

    def get_holdings(self, ticker):
        """Get volume held of ticker"""
        return self.plugin.get_holdings(ticker)
