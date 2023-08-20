import abc

from .play import Play
from .strategy import PlaySelectionStrategy


class Player(object):
    name: str

    @abc.abstractmethod
    def play(self) -> Play:
        """Required method"""


class BotPlayer(Player):
    def __init__(self, play_strategy: PlaySelectionStrategy, name: str = "Bot Player"):
        self.__strategy = play_strategy
        self.name = name

    def play(self) -> Play:
        return self.__strategy.play()
