from .player import Player
from .play import PlayResult

def play_game(firstPlayer: Player, secondPlayer: Player) -> PlayResult:
    firstPlay = firstPlayer.play()
    secondPlay = secondPlayer.play()
    return firstPlay.match(secondPlay)


def play_games(firstPlayer: Player, secondPlayer: Player, times: int) -> list[PlayResult]:
    results = []
    for _ in range(times):
        results.append(play_game(firstPlayer, secondPlayer))
    return results
