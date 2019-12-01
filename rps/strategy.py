import abc
from random import randrange
from .play import Play

class PlaySelectionStrategy(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def play(self):
    """Required method"""

class RandomPlayStrategy(PlaySelectionStrategy):
  def play(self):
    return Play(randrange(Play.min(), Play.max() + 1))
