import ccxt
from src.Commands import Commands

PLATFORMS = {
    "binance": ccxt.binance(),
    "coinbase": ccxt.coinbasepro()
}


class Atlas:
    def __init__(self, is_test: bool, platform: str):
        self.name = "Atlas"
        self.platform = PLATFORMS[platform]
        self.test = is_test
        self.platform.set_sandbox_mode(self.test)
        self.command = Commands(self.platform)

    def __str__(self):
        return f"PLATFORM: {self.platform}\nTEST MODE: {self.test}"
