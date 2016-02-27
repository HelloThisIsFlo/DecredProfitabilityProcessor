from decred.mining import Consumption, Production, Profitability
from decred.currency import MarketPrice

DECRED_TO_DOLLAR = 2
DOLLAR_TO_EURO = 0.91
CONSUMPTION_IDLE = 61
CONSUMPTION_MINING = 380
PRICE_KWH = 0.35
DECRED_PER_HOUR = 0.1


def test_profitability_returns_correct_value():
    market_price = MarketPrice(DECRED_TO_DOLLAR, DOLLAR_TO_EURO)
    consumption = Consumption(CONSUMPTION_IDLE, CONSUMPTION_MINING, PRICE_KWH)
    production = Production(market_price, DECRED_PER_HOUR)

    profitability = Profitability(consumption, production)

    expected = 0.5  # euros
    assert expected == profitability.per_hour()
