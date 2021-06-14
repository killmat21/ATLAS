import pytest
from src.engine import Atlas
from src.exchange import Exchange
from src.command import Commands


@pytest.mark.parametrize(
    "exchange, is_test, exchange_exp",
    [
        ("coinbasepro", True, "Coinbase Pro"),
        ("coinbasepro", False, "Coinbase Pro"),
        ("binance", True, "Binance"),
        ("binance", False, "Binance"),
    ],
)
def test__atlas(mocker, exchange, is_test, exchange_exp):
    mocker.patch("src.engine.Exchange.set_exchange_config")
    atlas = Atlas(exchange_name=exchange, is_test=is_test)
    assert isinstance(atlas.test, bool)
    assert isinstance(atlas.exchange, Exchange)
    assert isinstance(atlas.command, Commands)
