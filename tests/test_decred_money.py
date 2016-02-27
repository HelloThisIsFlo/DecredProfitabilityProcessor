import pytest
from decred.currency import Decred, MarketPrice

DECRED_TO_DOLLAR_RATE = 2.6
DOLLAR_TO_EURO_RATE = 0.91

DECRED_TEST_VALUE = 172


@pytest.fixture
def decred(request):
    from decred.currency import MarketPrice, Decred
    market_price = MarketPrice(DECRED_TO_DOLLAR_RATE, DOLLAR_TO_EURO_RATE)
    return Decred(request.param, market_price)


@pytest.mark.parametrize('decred', [DECRED_TEST_VALUE], indirect=True)
def test_convert_decred_to_dollar(decred):
    expected = DECRED_TEST_VALUE * DECRED_TO_DOLLAR_RATE
    assert expected == decred.to_dollar()


@pytest.mark.parametrize('decred', [DECRED_TEST_VALUE], indirect=True)
def test_convert_decred_to_euro(decred):
    expected = DECRED_TEST_VALUE * DECRED_TO_DOLLAR_RATE * DOLLAR_TO_EURO_RATE
    assert expected == decred.to_euro()


@pytest.mark.parametrize('decred', [DECRED_TEST_VALUE], indirect=True)
def test_substraction(decred):
    five_decred = Decred(5, MarketPrice(DECRED_TO_DOLLAR_RATE, DOLLAR_TO_EURO_RATE))
    expected = decred.amount - five_decred.amount
    assert expected == decred.minus(five_decred).amount


def test_from_euro():
    import decred.currency
    from_euro = decred.currency.from_euro(5, MarketPrice(DECRED_TO_DOLLAR_RATE, DOLLAR_TO_EURO_RATE))
    assert 5 == from_euro.to_euro()