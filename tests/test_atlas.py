import pytest
from src.engine import Atlas
from src.exchange import Exchange
from src.command import Commands


@pytest.mark.parametrize(
    "is_test, exchange_exp",
    [
        (True, "Binance"),
        (False, "Binance"),
        (True, "Binance"),
    ],
)
def test__atlas(mocker, is_test, exchange_exp):
    mocker.patch("src.engine.Exchange.set_exchange_config")
    atlas = Atlas(is_test=is_test)
    assert isinstance(atlas.test, bool)
    assert isinstance(atlas.exchange, Exchange)
    assert isinstance(atlas.command, Commands)
