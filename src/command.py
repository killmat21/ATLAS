class Commands:
    def __init__(self, exchange):
        self.exchange = exchange

    def get_balance(self):
        print("Fetching your account balance...")
        print(self.exchange.fetchBalance())

    def stop(self):
        print("Atlas is closing all open orders")
        self.exchange.cancel_all_orders()

    def buy_order(self, coin: str, amount: float):
        print(f"Atlas is buying {amount} {coin}")
        self.exchange.create_order(coin, "buy", "market", amount)

    def sell_order(self, coin: str, amount: float):
        print(f"Atlas is selling {amount} {coin}")
        self.exchange.create_order(coin, "sell", "market", amount)
