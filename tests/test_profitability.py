import pytest
from decred.mining import Consumption, Production, Profitability
from decred.currency import MarketPrice, Decred

DECRED_TO_DOLLAR = 2
DOLLAR_TO_EURO = 0.91
CONSUMPTION_IDLE = 0.061
CONSUMPTION_MINING = 0.380
PRICE_KWH = 0.35  # euros
DECRED_PER_HOUR = 0.1


@pytest.fixture
def profitability():
    market_price = MarketPrice(DECRED_TO_DOLLAR, DOLLAR_TO_EURO)
    consumption = Consumption(CONSUMPTION_IDLE, CONSUMPTION_MINING, PRICE_KWH)
    production = Production(market_price, DECRED_PER_HOUR)

    return Profitability(market_price, consumption, production)


def test_get_profitability_per_hour(profitability):
    assert abs(make_expected_result_for_one_hour() - profitability.per_hour().to_euro()) < 0.01


def test_get_profitability_multiple_hours(profitability):
    hours = 5
    assert abs(make_expected_result_for_one_hour() * hours - profitability.mine(hours).to_euro()) < 0.01


def make_expected_result_for_one_hour():
    extra_consumption = CONSUMPTION_MINING - CONSUMPTION_IDLE
    spent_one_hour = extra_consumption * PRICE_KWH  # euros

    produced_one_hour = DECRED_PER_HOUR * DECRED_TO_DOLLAR * DOLLAR_TO_EURO

    return produced_one_hour - spent_one_hour
