import pytest
from decred import ParameterNotSetException


@pytest.fixture
def processor():
    from decred import Processor
    return Processor()


def test_ZeroHour_returnZero(processor):
    assert 0 == processor.earnings_in_euro(0)


def test_AllRatesAt1FreeElectricity_XHours_returnX(processor):
    decred_per_hour = 1
    dollar_to_euro = 1
    decred_to_dollar = 1
    price_kwh = 0
    consumption = 0

    processor.set_decred_per_hour(decred_per_hour)
    processor.set_dollar_to_euro(dollar_to_euro)
    processor.set_decred_to_dollar(decred_to_dollar)
    processor.set_price_kwh(price_kwh)
    processor.set_consumption(consumption)
    assert 17 == processor.earnings_in_euro(17)


def test_fixedRates_returnHoursTimesEarningRate(processor):
    decred_per_hour = 1
    dollar_to_euro = 1
    decred_to_dollar = 1
    price_kwh = 0
    consumption = 0

    earning_rate = (decred_per_hour * decred_to_dollar * dollar_to_euro) - (consumption * price_kwh)

    processor.set_decred_per_hour(decred_per_hour)
    processor.set_dollar_to_euro(dollar_to_euro)
    processor.set_decred_to_dollar(decred_to_dollar)
    processor.set_price_kwh(price_kwh)
    processor.set_consumption(consumption)
    assert 13 * earning_rate == processor.earnings_in_euro(13)


def test_missingParameter_throwException(processor):
    decred_per_hour = 1
    dollar_to_euro = 1
    price_kwh = 0
    consumption = 0

    processor.set_decred_per_hour(decred_per_hour)
    processor.set_dollar_to_euro(dollar_to_euro)
    processor.set_consumption(consumption)

    with pytest.raises(ParameterNotSetException):
        processor.earnings_in_euro(354)


