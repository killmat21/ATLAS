import click
from src.engine import Atlas
from src.metrics import is_resistance, is_support


@click.command()
@click.option(
    "-e",
    "--exchange",
    type=click.Choice(["binance", "coinbasepro"], case_sensitive=False),
    required=True,
)
@click.option("--test/--real-shit", default=True, help="Test or Live environment")
def main(exchange: str, test: bool):
    print(
        """
          _        _________   _____             _          ______   
         / \      |  _   _  | |_   _|           / \       .' ____ \  
        / _ \     |_/ | | \_|   | |            / _ \      | (___ \_| 
       / ___ \        | |       | |   _       / ___ \      _.____`.  
     _/ /   \ \_  _  _| |_  _  _| |__/ | _  _/ /   \ \_  _| \____) | 
    |____| |____|(_)|_____|(_)|________|(_)|____| |____|(_)\______.' 
    """
    )
    atlas = Atlas(exchange_name=exchange, is_test=test)
    sticks = atlas.command.get_ohlcv("BTC/USDT", 60, "1m")
    resistance = -1
    it = 0
    while resistance == -1 and it < len(sticks):
        start = it
        end = start + 5
        resistance = is_resistance(sticks[start:end])
        it += 1
    print(resistance)


if __name__ == "__main__":
    main()
