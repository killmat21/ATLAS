import click
from src.engine import Atlas
from src.robot_killer import RobotKiller


@click.command()
@click.option("--test/--real-shit", default=True, help="Test or Live environment")
def main(test: bool):
    print("""
          _        _________   _____             _          ______   
         / \      |  _   _  | |_   _|           / \       .' ____ \  
        / _ \     |_/ | | \_|   | |            / _ \      | (___ \_| 
       / ___ \        | |       | |   _       / ___ \      _.____`.  
     _/ /   \ \_  _  _| |_  _  _| |__/ | _  _/ /   \ \_  _| \____) | 
    |____| |____|(_)|_____|(_)|________|(_)|____| |____|(_)\______.' 
    """)
    robot_killer = RobotKiller()
    atlas = Atlas(is_test=test)
    print(atlas)
    while not robot_killer.shutdown:
        # Where startegy will go
        pass


if __name__ == "__main__":
    main()
