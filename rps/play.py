from __future__ import annotations
from enum import IntEnum


class PlayResult(IntEnum):
    LOSS = -1
    DRAW = 0
    WIN = 1


def human_readable(result: PlayResult) -> str:
    if result == PlayResult.WIN:
        return "wins"
    elif result == PlayResult.LOSS:
        return "loses"
    elif result == PlayResult.DRAW:
        return "draws"


class Play(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def match(self, other: Play) -> PlayResult:
        if self.value == other.value or type(other) is not Play:
            return PlayResult.DRAW
        if self.value == self.ROCK:
            return PlayResult.WIN if other.value == self.SCISSORS else PlayResult.LOSS
        elif self.value == self.SCISSORS:
            return PlayResult.WIN if other.value == self.PAPER else PlayResult.LOSS
        elif self.value == self.PAPER:
            return PlayResult.WIN if other.value == self.ROCK else PlayResult.LOSS
        return PlayResult.DRAW

    @staticmethod
    def min() -> int:
        return min([Play.ROCK, Play.PAPER, Play.SCISSORS])

    @staticmethod
    def max() -> int:
        return max([Play.ROCK, Play.PAPER, Play.SCISSORS])
