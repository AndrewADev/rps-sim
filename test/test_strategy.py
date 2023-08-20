from rps.strategy import (
    RandomPlayStrategy,
    SequencePlayStrategy,
    Strategy,
    get_strategy,
)
from rps.play import Play


class TestStrategy:
    def test_RandomPlayStrategy_returns_play(self) -> None:
        sut = RandomPlayStrategy()
        assert type(sut.play()) is Play

    def test_SequencePlayStrategy_returns_sequence(self) -> None:
        sequence = [Play.PAPER, Play.ROCK, Play.SCISSORS]
        sut = SequencePlayStrategy(sequence)
        first_play = sut.play()

        assert first_play == sequence[0]
        assert sut.play() == sequence[1]
        assert sut.play() == sequence[2]

    def test_SequencePlayStrategy_repeats_sequence_on_exhaustion(self) -> None:
        sequence = [Play.PAPER, Play.ROCK]
        sut = SequencePlayStrategy(sequence)
        first_play = sut.play()

        assert first_play == sequence[0]
        assert sut.play() == sequence[1]
        assert sut.play() == sequence[0]
        assert sut.play() == sequence[1]
        assert sut.play() == sequence[0]
        assert sut.play() == sequence[1]

    def test_SequencePlayStrategy_has_default_sequence(self):
        sut = SequencePlayStrategy()
        first_play = sut.play()
        assert first_play is not None
        second_play = sut.play()
        assert second_play is not None
        assert second_play != first_play
        third_play = sut.play()
        assert third_play is not None
        assert third_play != second_play
        assert third_play != first_play

    def test_get_strategy_returns_strategy(self):
        returned = get_strategy(Strategy.RANDOM)
        assert type(returned) is RandomPlayStrategy

    def test_get_strategy_returns_strategy_with_args(self):
        returned = get_strategy(Strategy.SEQUENCE, args=[Play.ROCK, Play.SCISSORS])
        assert type(returned) is SequencePlayStrategy
        first_play = returned.play()
        assert first_play == Play.ROCK

    def test_get_strategy_returns_strategy_with_args_when_defer_defaults(self):
        returned = get_strategy(Strategy.SEQUENCE)
        assert type(returned) is SequencePlayStrategy
        first_play = returned.play()
        assert first_play == Play.ROCK
