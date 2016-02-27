import json, urllib.request


class Decred:
    def __init__(self, amount, market_price):
        self.amount = amount
        self.market_price = market_price

    def to_euro(self):
        return self.amount * self.market_price.dec_eur

    def to_dollar(self):
        rate = self.market_price.dec_usd
        return self.amount * rate

    def minus(self, decred):
        return Decred(self.amount - decred.amount, self.market_price)


def from_euro(euro, market_price):
    decred = euro / market_price.dec_eur
    return Decred(decred, market_price)


class MarketPrice:
    def __init__(self, decred_to_dollar, dollar_to_euro):
        self.dec_usd = decred_to_dollar
        self.dec_eur = decred_to_dollar * dollar_to_euro

    def get_from_web(self):
        data = urllib.request.urlopen("http://coinmarketcap-nexuist.rhcloud.com/api/dcr/price").read()
        output = json.loads(data.decode())
        self.dec_eur = float(output['eur'])
        self.dec_usd = float(output['usd'])
