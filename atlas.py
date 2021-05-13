import click
from src.Atlas import Atlas


@click.command()
@click.option('-e', '--exchange', type=click.Choice(['binance', 'coinbase'], case_sensitive=False))
@click.option('--test/--real-shit', default=True, help='Test or Live environment')
def main(exchange: str, test: bool):
    print("""
          _        _________   _____             _          ______   
         / \      |  _   _  | |_   _|           / \       .' ____ \  
        / _ \     |_/ | | \_|   | |            / _ \      | (___ \_| 
       / ___ \        | |       | |   _       / ___ \      _.____`.  
     _/ /   \ \_  _  _| |_  _  _| |__/ | _  _/ /   \ \_  _| \____) | 
    |____| |____|(_)|_____|(_)|________|(_)|____| |____|(_)\______.' 
    """)
    atlas = Atlas(platform=exchange, is_test=test)
    print(atlas)


if __name__ == "__main__":
    main()
