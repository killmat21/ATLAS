from src.command import Commands
from src.exchange import Exchange


class Atlas:
    def __init__(self, exchange_name: str, is_test: bool):
        self.test = is_test
        self.exchange = Exchange(exchange_name, is_test)
        self.command = Commands(self.exchange.exchange)
        self.buy = True

    def __str__(self):
        return f"EXCHANGE: {self.exchange}\nTEST MODE: {self.test}"
