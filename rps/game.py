from .play import PlayResult

def play_game(firstPlayer, secondPlayer):
  firstPlay = firstPlayer.play()
  secondPlay = secondPlayer.play()
  return firstPlay.match(secondPlay)

def play_games(firstPlayer, secondPlayer, times):
  results = []
  for game in range(times):
    results.append(play_game(firstPlayer, secondPlayer))
  return results
