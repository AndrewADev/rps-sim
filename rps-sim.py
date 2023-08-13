import click
from rps.player import BotPlayer
from rps.play import human_readable
from rps.strategy import RandomPlayStrategy
from rps.game import play_games



@click.command
@click.option("--games", default=3, type=click.IntRange(min=1, max=1000), help="Number of games to play")
def simple_sim(games: int) -> None:
    player1 = BotPlayer(RandomPlayStrategy())
    player2 = BotPlayer(RandomPlayStrategy())
    results = play_games(player1, player2, games)

    for result in results:
        # Simple message with results
        print("Result: Player 1", human_readable(result))

    print("Simulation finished.")


if __name__ == '__main__':
    simple_sim()