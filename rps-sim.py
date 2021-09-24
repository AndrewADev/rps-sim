from warnings import resetwarnings
from rps.player import BotPlayer
from rps.play import human_readable
from rps.strategy import RandomPlayStrategy
from rps.game import play_games


player1 = BotPlayer(RandomPlayStrategy)
player2 = BotPlayer(RandomPlayStrategy)
results = play_games(player1, player2, 3)

# Hard-coded, simple demonstration of a play-through
for result in results:
    print("Result: Player 1...", human_readable(result))


print ("Simulation finished.")


