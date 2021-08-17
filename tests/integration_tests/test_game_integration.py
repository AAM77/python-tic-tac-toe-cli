from io import StringIO
from src.game import Game

def test_take_turn(capfd, monkeypatch):
    user_input = StringIO('2\n')
    monkeypatch.setattr('sys.stdin', user_input)

    game = Game()
    game.take_turn()
    out, _ = capfd.readouterr()
    assert game.player_selection == "2"
    assert game.board == ["1", "X", "3", "4", "5", "6", "7", "8", "9"]
    assert " 1 | X | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n" in out