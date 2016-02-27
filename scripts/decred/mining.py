from decred.currency import Decred
import decred.currency


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


class Profitability:
    def __init__(self, market_price, consumption, production):
        self.market_price = market_price
        self.consumption = consumption
        self.production = production
        pass

    def per_hour(self):
        produced_one_hour = self.production.mine(1)
        spent_one_hour = self.consumption.mining_cost(1)

        return decred.currency.from_euro(produced_one_hour.to_euro() - spent_one_hour, self.market_price)

    def mine(self, hours):
        earned = self.per_hour().amount * hours
        return Decred(earned, self.market_price)