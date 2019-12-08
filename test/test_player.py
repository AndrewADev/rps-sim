from rps.player import BotPlayer
from rps.strategy import RandomPlayStrategy

# Mocker seems to want bare functions, 
# or I just haven't figured out class syntax
# Ether way, this works for now.


def test_BotPlayer_calls_strategy(mocker):
  play_spy = mocker.spy(RandomPlayStrategy, 'play')
  sut = BotPlayer(RandomPlayStrategy())
  sut.play()
  assert play_spy.call_count == 1