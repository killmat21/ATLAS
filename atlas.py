import click
from src.engine import Atlas


@click.command()
@click.option(
    "-e",
    "--exchange",
    type=click.Choice(["binance", "coinbasepro"], case_sensitive=False),
    required=True,
)
@click.option("--test/--real-shit", default=True, help="Test or Live environment")
@click.option(
    "--manual/--skynet",
    default=True,
    help="You pass manual orders or you let Atlas take control",
)
def main(exchange: str, test: bool, manual: bool):
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
    atlas = Atlas(exchange_name=exchange, is_test=test, is_manual=manual)
    print(atlas)


if __name__ == "__main__":
    main()
