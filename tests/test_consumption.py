import pytest
from decred.mining import Consumption

CONSUMPTION_IDLE = 62
CONSUMPTION_MINING = 380


@pytest.fixture
def consumption():
    return Consumption(CONSUMPTION_IDLE, CONSUMPTION_MINING)


def test_get_extra_consumption_when_mining(consumption):
    expected = CONSUMPTION_MINING - CONSUMPTION_IDLE
    assert expected == consumption.extra_power_when_mining()


def test_number_hours__return_price_spent(consumption):
    price = 0.35
    hours = 5

    consumption.price_kwh = price

    extra_consumption = CONSUMPTION_MINING - CONSUMPTION_IDLE
    expected_price = extra_consumption * price * hours

    assert expected_price == consumption.mining_cost(hours)
