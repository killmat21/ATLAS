from src.command import Commands
from src.exchange import Exchange


class Atlas:
    def __init__(self, exchange_name: str, is_test: bool, is_manual: bool):
        self.manual = is_manual
        self.test = is_test
        self.exchange = Exchange(exchange_name, is_test)
        self.command = Commands(self.exchange)

    def __str__(self):
        return f"EXCHANGE: {self.exchange}\nTEST MODE: {self.test}\nSKYNET MODE: {not self.manual}"
