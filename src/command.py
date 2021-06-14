import datetime
import pandas as pd


class Commands:
    def __init__(self, exchange):
        self.exchange = exchange

    def get_balance(self):
        print("Fetching your account balance...")
        print(self.exchange.fetchBalance())

    def get_ohlcv(self, coin, since, timeframe):
        print("Atlas is getting candles information")
        df = []
        cur_time = datetime.datetime.now()
        time_ago_in_milliseconds = int((cur_time - datetime.timedelta(minutes=since)).timestamp() * 1000)
        if self.exchange.has['fetchOHLCV']:
            res = self.exchange.fetch_ohlcv(symbol=coin, timeframe=timeframe, since=time_ago_in_milliseconds)
            df = pd.DataFrame(res, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
            df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].astype(float).div(100)
            print(df)
        return df

    def stop(self):
        print("Atlas is closing all open orders")
        self.exchange.cancel_all_orders()

    def buy_order(self, coin: str, amount: float):
        print(f"Atlas is buying {amount} {coin}")
        self.exchange.create_order(coin, "buy", "market", amount)

    def sell_order(self, coin: str, amount: float):
        print(f"Atlas is selling {amount} {coin}")
        self.exchange.create_order(coin, "sell", "market", amount)
