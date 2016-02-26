from decred.currency import Decred, MarketPrice


def test__change_rate_in_marketprice__rate_changed_in_decred():
    market_price = MarketPrice(10, 0)
    five_decred = Decred(5, market_price)

    assert 5 * 10 == five_decred.to_dollar()

    market_price.dec_usd = 39

    assert 5 * 39 == five_decred.to_dollar()
