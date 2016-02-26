import pytest
from currency import Decred, MarketPrice, RateNotSetException


def test_to_euro__missing_rate__raise_exception():
    with pytest.raises(RateNotSetException):
        market_price = MarketPrice()
        market_price.to_euro(3)


def test_to_dollar__missing_rate__raise_exception():
    with pytest.raises(RateNotSetException):
        market_price = MarketPrice()
        market_price.to_dollar(3)


def test__change_rate_in_marketprice__rate_changed_in_decred():
    market_price = MarketPrice()
    market_price.set_decred_to_dollar_rate(10)
    five_decred = Decred(5, market_price)

    assert 5 * 10 == five_decred.to_dollar()

    market_price.set_decred_to_dollar_rate(39)

    assert 5 * 39 == five_decred.to_dollar()
