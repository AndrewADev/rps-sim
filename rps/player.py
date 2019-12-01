import abc

class Player(object):

  @abc.abstractmethod
  def play(self):
    """Required method"""

class BotPlayer(Player):
  def __init__(self, play_strategy):
    self.__strategy = play_strategy
  
  def play(self):
    return self.__strategy.play()