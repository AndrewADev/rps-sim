import abc

from .play import Play
from .strategy import PlaySelectionStrategy


class Player(object):
    @abc.abstractmethod
    def play(self) -> Play:
        """Required method"""


class BotPlayer(Player):
    def __init__(self, play_strategy: PlaySelectionStrategy):
        self.__strategy = play_strategy

    def play(self)  -> Play:
        return self.__strategy.play()
