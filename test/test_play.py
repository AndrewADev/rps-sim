from rps.play import Play

class TestPlay:
  def test_Play_has_range(self):
    assert Play.min() < Play.max()