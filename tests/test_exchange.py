import pytest
from src.exchange import Exchange


@pytest.mark.parametrize("name, file_exists, sections, exchange_name_exp", [
    ("binance", ["test.ini"], ["binance"], "Binance"),
    ("binance", [], ["binance"], "Binance"),
    ("binance", ["test.ini"], ["coinbasepro"], "Binance"),
    ("coinbasepro", ["test.ini"], ["binance"], "Coinbase Pro"),
    ("coinbasepro", ["test.ini"], ["coinbasepro"], "Coinbase Pro"),
])
def test__set_exchange_config(mocker, name, file_exists, sections, exchange_name_exp):
    mock_open = mocker.patch('src.exchange.open')
    mock_config = mocker.patch('src.exchange.configparser.ConfigParser')
    mock_input = mocker.patch('src.exchange.input')
    mocker.patch('src.exchange.Exchange.check_exchange_credentials')
    mock_config.read.return_value = file_exists
    mock_config.sections.return_value = sections
    exchange = Exchange(name, True)
    mock_open.assert_called()
    assert mock_input.call_count == 2
    assert str(exchange) == exchange_name_exp


@pytest.mark.parametrize("name, isTestMode", [("binance", True), ("coinbase", False)])
def test__init_exchange(mocker, name, isTestMode):
    mocker.patch('src.exchange.Exchange.set_exchange_config')
    config = {
        name: {
            "api_key": "",
            "secret_key": ""
        }
    }
    assert str(Exchange(name, isTestMode).init_exchange(config, name)).lower() == name


@pytest.mark.parametrize("name, is_exc", [
    ("binance", False),
    ("binance", True),
    ("coinbase", True),
    ("coinbase", False),
])
def test__check_exchange_credentials(mocker, name, is_exc):
    mocker.patch('src.exchange.Exchange.set_exchange_config')
    mock_open = mocker.patch('src.exchange.open')
    mock_exit = mocker.patch('src.exchange.exit')
    mock_exchange = mocker.Mock()
    mock_config = mocker.Mock()
    if is_exc:
        mock_exchange.fetchBalance.side_effect = Exception("Test")
    Exchange(name, True).check_exchange_credentials(mock_exchange, mock_config, name)
    mock_exchange.fetchBalance.assert_called_once()
    if is_exc:
        mock_config.remove_section.assert_called_with(name)
        mock_open.assert_called_once()
        mock_exit.assert_called_once()


