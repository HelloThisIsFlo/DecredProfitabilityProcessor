class Decred:
    def __init__(self, amount, market_price):
        self.amount = amount
        self.market_price = market_price

    def to_euro(self):
        de_do_rate = self.market_price.dec_usd
        do_e_rate = self.market_price.usd_eur
        return self.amount * de_do_rate * do_e_rate

    def to_dollar(self):
        rate = self.market_price.dec_usd
        return self.amount * rate


class MarketPrice:
    def __init__(self, decred_to_dollar, dollar_to_euro):
        self.dec_usd = decred_to_dollar
        self.usd_eur = dollar_to_euro
