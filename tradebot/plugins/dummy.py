"""A dummy plugin for basic API testing"""


class ApiPlugin(object):
    """A dummy plugin class"""

    def __init__(self, config):
        self.config = config

    def _do_an_api_call(self, endpoint, *args, **kwargs):
        """This would normally be an HTTP request"""
        return 0.0

    def buy(self, ticker, price, volume):
        """Open buy order"""
        self._do_an_api_call('/')
        success = True
        error = None

        return {
            'success': success,
            'error': error,
        }


    def sell(self, ticker, price, volume):
        """Open sell order"""
        self._do_an_api_call('/')
        success = True
        error = None

        return {
            'success': success,
            'error': error,
        }


    def cancel(self, order_id):
        """Cancel order"""
        self._do_an_api_call('/')
        success = True
        error = None

        return {
            'success': success,
            'error': error,
        }


    def get_price(self, ticker):
        """Get current price of ticker"""
        price = self._do_an_api_call('/')
        success = True
        error = None

        return {
            'success': success,
            'error': error,
            'price': price,
        }


    def get_holdings(self, ticker):
        """Get volume held of ticker"""
        holdings = self._do_an_api_call('/')
        success = True
        error = None

        return {
            'success': success,
            'error': error,
            'holdings': holdings,
        }
