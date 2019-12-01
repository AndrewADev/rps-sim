import abc

class PlaySelectionStrategy(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def play(self):
    """Required method"""

class RandomPlayStrategy(PlaySelectionStrategy):
  def play(self):
    return super().play()
