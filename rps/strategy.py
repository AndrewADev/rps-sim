import abc
from random import randrange
from .play import Play


class PlaySelectionStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def play(self) -> Play:
        """Required method"""


class RandomPlayStrategy(PlaySelectionStrategy):
    def play(self) -> Play:
        return Play(randrange(Play.min(), Play.max() + 1))
