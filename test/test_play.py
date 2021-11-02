from rps.play import Play, PlayResult
from enum import IntEnum
import pytest


class TestPlay:
    def test_Play_has_range(self):
        assert Play.min() < Play.max()

    @pytest.mark.parametrize(
        "first,second",
        [
            (Play.ROCK, Play.SCISSORS),
            (Play.SCISSORS, Play.PAPER),
            (Play.PAPER, Play.ROCK),
        ],
    )
    def test_Play_match_identifies_win(self, first, second):
        assert first.match(second) == PlayResult.WIN

    @pytest.mark.parametrize(
        "first,second",
        [
            (Play.ROCK, Play.PAPER),
            (Play.SCISSORS, Play.ROCK),
            (Play.PAPER, Play.SCISSORS),
        ],
    )
    def test_Play_match_identifies_loss(self, first, second):
        assert first.match(second) == PlayResult.LOSS

    @pytest.mark.parametrize(
        "first,second",
        [
            (Play.ROCK, Play.ROCK),
            (Play.SCISSORS, Play.SCISSORS),
            (Play.PAPER, Play.PAPER),
        ],
    )
    def test_Play_match_identifies_draw(self, first, second):
        assert first.match(second) == PlayResult.DRAW

    def test_Play_match_against_unknown_is_draw(self):
        class UnknownEnum(IntEnum):
            WHOOPS = (1,)
            UHOH = 2

        assert Play.ROCK.match(UnknownEnum.UHOH) == PlayResult.DRAW
