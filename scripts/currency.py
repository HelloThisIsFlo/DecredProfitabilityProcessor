class Decred:
    def __init__(self, amount, market_price):
        self.amount = amount
        self.market_price = market_price

    def to_euro(self):
        de_do_rate = self.market_price.decred_to_dollar_rate
        do_e_rate = self.market_price.dollar_to_euro_rate
        return self.amount * de_do_rate * do_e_rate

    def to_dollar(self):
        rate = self.market_price.decred_to_dollar_rate
        return self.amount * rate


class MarketPrice:
    def set_dollar_to_euro_rate(self, dollar_to_euro_rate):
        self.dollar_to_euro_rate = dollar_to_euro_rate

    def set_decred_to_dollar_rate(self, decred_to_dollar_rate):
        self.decred_to_dollar_rate = decred_to_dollar_rate

    def to_dollar(self, decred_amount):
        try:
            return decred_amount * self.decred_to_dollar_rate
        except AttributeError:
            raise RateNotSetException()

    def to_euro(self, decred_amount):
        try:
            return decred_amount * self.decred_to_dollar_rate * self.dollar_to_euro_rate
        except AttributeError:
            raise RateNotSetException()


class RateNotSetException(Exception):
    pass
