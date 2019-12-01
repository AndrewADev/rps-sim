from enum import IntEnum

class Play(IntEnum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

  @staticmethod
  def min():
    return min([Play.ROCK, Play.PAPER, Play.SCISSORS])

  @staticmethod
  def max():
    return max([Play.ROCK, Play.PAPER, Play.SCISSORS])
