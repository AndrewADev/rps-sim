from rps.game import play_game, play_games
from rps.player import Player
from rps.play import Play

def get_mock_player(mocker, play_val):
  player = Player()
  player_mock = mocker.patch.object(player, 'play', return_value=play_val)
  return player_mock

def test_play_game_invokes_play_for_both_players(mocker):
  mockPlayer1 = get_mock_player(mocker, Play.PAPER)
  mockPlayer2 = get_mock_player(mocker, Play.ROCK)
  play_game(mockPlayer1, mockPlayer2)
  assert mockPlayer1.play.call_count == 1
  assert mockPlayer2.play.call_count == 1


def test_play_games_invokes_play_x_times(mocker):
  mockPlayer1 = get_mock_player(mocker, Play.PAPER)
  mockPlayer2 = get_mock_player(mocker, Play.ROCK)
  play_games(mockPlayer1, mockPlayer2, 5)
  assert mockPlayer1.play.call_count == 5
  assert mockPlayer2.play.call_count == 5