import pytest
import ccxt
from src.engine import Atlas


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
def test__atlas_str(mocker, exchange, is_test, is_manual, exchange_exp):
    mock_exchange = mocker.patch("src.engine.Exchange")
    mock_exchange.return_value = str(getattr(ccxt, exchange)())
    atlas = Atlas(exchange_name=exchange, is_test=is_test, is_manual=is_manual)
    str_exp = (
        f"EXCHANGE: {exchange_exp}\nTEST MODE: {is_test}\nSKYNET MODE: {not is_manual}"
    )
    assert str(atlas) == str_exp
