from typing import Literal
import click
from rps.player import BotPlayer
from rps.play import human_readable
from rps.strategy import get_strategy, Strategy
from rps.game import play_games


@click.command
@click.option(
    "--games",
    default=3,
    type=click.IntRange(min=1, max=1000),
    help="Number of games to play",
)
@click.option("--p1-name", default="Player 1", help="Name of first player")
@click.option("--p2-name", default="Player 2", help="Name of second player")
@click.option(
    "--p1-strategy",
    default=Strategy.RANDOM,
    type=click.Choice([Strategy.RANDOM, Strategy.SEQUENCE]),
    help="Strategy for player 1",
)
@click.option(
    "--p2-strategy",
    default=Strategy.RANDOM,
    type=click.Choice([Strategy.RANDOM, Strategy.SEQUENCE]),
    help="Strategy for player 2",
)
def simple_sim(
    games: int, p1_name: str, p2_name: str, p1_strategy: Strategy, p2_strategy: Strategy
) -> None:
    player1 = BotPlayer(get_strategy(p1_strategy), p1_name)
    player2 = BotPlayer(get_strategy(p2_strategy), p2_name)
    results = play_games(player1, player2, games)

    for result in results:
        # Simple message with results
        print("Result:", player1.name, human_readable(result))

    print("Simulation finished.")


if __name__ == "__main__":
    simple_sim()
