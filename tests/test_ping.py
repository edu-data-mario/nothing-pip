from nothing_pip.ping import Ping


def test_pong():
    assert Ping.pong() == "pong"


