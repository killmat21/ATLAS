import pytest
from src.engine import Atlas
from src.exchange import Exchange
from src.command import Commands


@pytest.mark.parametrize(
    "exchange, is_test, is_manual, exchange_exp",
    [
        ("coinbasepro", True, True, "Coinbase Pro"),
        ("coinbasepro", False, False, "Coinbase Pro"),
        ("binance", True, True, "Binance"),
        ("binance", False, True, "Binance"),
        ("binance", True, True, "Binance"),
    ],
)
def test__atlas(mocker, exchange, is_test, is_manual, exchange_exp):
    mocker.patch("src.engine.Exchange.set_exchange_config")
    atlas = Atlas(exchange_name=exchange, is_test=is_test, is_manual=is_manual)
    assert isinstance(atlas.test, bool)
    assert isinstance(atlas.exchange, Exchange)
    assert isinstance(atlas.command, Commands)
