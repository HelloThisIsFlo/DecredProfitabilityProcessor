from decred.mining import Production
from decred.currency import MarketPrice
import pytest

DECRED_MINED_PER_HOUR = 0.1
DECRED_TO_DOLLAR_RATE = 2.6
DOLLAR_TO_EURO_RATE = 0.91


@pytest.fixture
def production():
    market_price = MarketPrice(DECRED_TO_DOLLAR_RATE, DOLLAR_TO_EURO_RATE)
    return Production(market_price, DECRED_MINED_PER_HOUR)


def test_production_per_hour(production):
    hours = 4
    expected = hours * DECRED_MINED_PER_HOUR
    assert expected == production.mine(hours).amount


def test__production_in_euro(production):
    hours = 4
    expected = hours * DECRED_MINED_PER_HOUR * DECRED_TO_DOLLAR_RATE * DOLLAR_TO_EURO_RATE
    assert expected == production.mine(hours).to_euro()
