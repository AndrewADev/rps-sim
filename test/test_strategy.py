from rps.strategy import RandomPlayStrategy
from rps.play import Play

class TestStrategy:
  def test_RandomPlayStrategy_returns_play(self):
    sut = RandomPlayStrategy()
    assert type(sut.play()) is Play