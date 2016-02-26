import pytest
from decred import Decred

DECRED_TO_DOLLAR_RATE = 2.6
DOLLAR_TO_EURO_RATE = 0.91

@pytest.fixture
def decred(request):
    return Decred(request.param)


@pytest.mark.parametrize('decred', [0], indirect=['decred'])
def test_zero_decred__is_zero_euro(decred):
    assert 0 == decred.to_euro()
