from decred.mining import Consumption, Production, Profitability
from decred.currency import MarketPrice

DECRED_TO_DOLLAR = -1  # get from web
DOLLAR_TO_EURO = -1  # get from web
CONSUMPTION_IDLE = 0.063
CONSUMPTION_MINING = 0.315
PRICE_KWH = 0.35  # euros
DECRED_PER_HOUR = 0.1388888888888889


def make_profitability():
    market_price = MarketPrice(DECRED_TO_DOLLAR, DOLLAR_TO_EURO)
    consumption = Consumption(CONSUMPTION_IDLE, CONSUMPTION_MINING, PRICE_KWH)
    production = Production(market_price, DECRED_PER_HOUR)
    market_price.get_from_web()

    return Profitability(market_price, consumption, production)


if __name__ == '__main__':
    profitability = make_profitability()
    hours = 1
    while hours > 0:
        hours = int(input('Enter number of hours : '))
        print(profitability.mine(hours).to_euro())
