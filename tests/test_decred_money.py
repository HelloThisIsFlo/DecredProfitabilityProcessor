import pytest

DECRED_TO_DOLLAR_RATE = 2.6
DOLLAR_TO_EURO_RATE = 0.91

DECRED_TEST_VALUE = 172


@pytest.fixture
def decred(request):
    from currency import MarketPrice, Decred
    market_price = MarketPrice()
    market_price.set_decred_to_dollar_rate(DECRED_TO_DOLLAR_RATE)
    market_price.set_dollar_to_euro_rate(DOLLAR_TO_EURO_RATE)
    return Decred(request.param, market_price)


@pytest.mark.parametrize('decred', [DECRED_TEST_VALUE], indirect=True)
def test_convert_decred_to_dollar(decred):
    expected = DECRED_TEST_VALUE * DECRED_TO_DOLLAR_RATE
    assert expected == decred.to_dollar()


@pytest.mark.parametrize('decred', [DECRED_TEST_VALUE], indirect=True)
def test_convert_decred_to_euro(decred):
    expected = DECRED_TEST_VALUE * DECRED_TO_DOLLAR_RATE * DOLLAR_TO_EURO_RATE
    assert expected == decred.to_euro()
