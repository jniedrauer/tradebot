"""Object models"""


class Order(object):
    """An open order"""

    def __init__(self, order_id, market, price, volume,
                 min_price=None, max_price=None):
        self.id = order_id
        self.market = market
        self.price = price
        self.volume = volume
        self.min = min_price
        self.max = max_price
        self.api_orders = []
        self.remaining = volume

    def cancel(self):
        """Cancel any open orders and self destruct"""
        order = None
        for order in self.api_orders:
            self.market.api.cancel(order)
        return bool(order)
