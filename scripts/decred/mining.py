from decred.currency import Decred


class Consumption:
    def __init__(self, idle, mining, price_kwh=0):
        self.idle = idle
        self.mining = mining
        self.price_kwh = price_kwh

    def extra_power_when_mining(self):
        return self.mining - self.idle

    def mining_cost(self, hours):
        return hours * self.price_kwh * self.extra_power_when_mining()


class Production:
    def __init__(self, market_price, decred_per_hour):
        self.market_price = market_price
        self.per_hour = decred_per_hour

    def mine(self, hours):
        return Decred(hours * self.per_hour, self.market_price)
