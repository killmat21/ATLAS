import ccxt
from src.command import Commands

PLATFORMS = {"binance": ccxt.binance(), "coinbase": ccxt.coinbasepro()}


class Atlas:
    def __init__(self, platform: str, is_test: bool, is_manual: bool):
        self.name = "Atlas"
        self.platform = PLATFORMS[platform]
        self.test = is_test
        self.manual = is_manual
        self.platform.set_sandbox_mode(self.test)
        self.command = Commands(self.platform)

    def __str__(self):
        return f"PLATFORM: {self.platform}\nTEST MODE: {self.test}\nSKYNET MODE: {self.manual}"
