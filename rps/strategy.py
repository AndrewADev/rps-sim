import abc
from random import randrange
from typing import Any, Sequence
from .play import Play
from enum import auto, StrEnum


class PlaySelectionStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def play(self) -> Play:
        """Required method"""


class Strategy(StrEnum):
    RANDOM = auto()
    SEQUENCE = auto()


class RandomPlayStrategy(PlaySelectionStrategy):
    def play(self) -> Play:
        return Play(randrange(Play.min(), Play.max() + 1))


default_sequence = [Play.ROCK, Play.PAPER, Play.SCISSORS]


class SequencePlayStrategy(PlaySelectionStrategy):
    def __init__(self, sequence: Sequence[Play] = default_sequence):
        self._sequence = sequence if sequence is not None else default_sequence
        self._idx = 0

    def play(self) -> Play:
        item = self._sequence[self._idx]
        self._idx = (self._idx + 1) % len(self._sequence)
        return item


def get_strategy(strategy: Strategy, args: Any = None) -> PlaySelectionStrategy:
    if strategy is Strategy.RANDOM:
        return RandomPlayStrategy()
    elif strategy is Strategy.SEQUENCE:
        return SequencePlayStrategy(sequence=args)
