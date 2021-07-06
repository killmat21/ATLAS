from src.command import Commands
from src.exchange import Exchange


class Atlas:
    def __init__(self, is_test: bool):
        self.test = is_test
        self.exchange = Exchange(is_test)
        self.command = Commands(self.exchange.exchange)

    def __str__(self):
        return f"EXCHANGE: {self.exchange}\nTEST MODE: {self.test}"
