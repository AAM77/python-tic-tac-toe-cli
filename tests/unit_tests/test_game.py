from io import StringIO
import pytest
from src.game import Game

def test_game_exists():
    assert Game()

def test_board():
    game = Game()
    assert game.board == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def test_display_board(capfd):
    game = Game()
    game.display_board()
    out, err = capfd.readouterr()
    assert out == " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n"

def test_winning_combinations():
    game = Game()
    assert game.WINNING_COMBINATIONS == [
        (0, 1, 2),
        (0, 3, 6),
        (0, 4, 8),
        (1, 4, 7),
        (2, 4, 6),
        (2, 5, 8),
        (3, 4, 5),
        (6, 7, 8)
    ]

def test_current_player_is_x():
    game = Game()
    game.board = ['X', 'O', 'X', 'O', 'X', 'O', '7', '8', '9']
    assert game.current_player() == 'X'

def test_current_player_is_o():
    game = Game()
    game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', '8', '9']
    assert game.current_player() == 'O'

def test_determine_winner_is_x():
    game = Game()
    game.board = ['X', 'X', 'X', 'O', 'X', 'O', 'O', 'O', '9']
    assert game.determine_winner() == 'X'

def test_determine_winner_is_o():
    game = Game()
    game.board = ['O', 'O', 'O', 'X', 'O', 'X', 'X', 'X', '9']
    assert game.determine_winner() == 'O'

def test_get_desired_position(capfd, monkeypatch):
    user_input = StringIO('1\n')
    monkeypatch.setattr('sys.stdin', user_input)

    game = Game()
    game.get_desired_position()
    out, err = capfd.readouterr()
    assert out == "Please select a position to place your mark.\n"

def test_get_desired_position_is_a_valid_number(monkeypatch):
    user_input = StringIO('1\n')
    monkeypatch.setattr('sys.stdin', user_input)

    game = Game()
    game.get_desired_position()
    assert game.player_selection.isdigit() == True
    assert game.player_selection == '1'

def test_get_desired_position_alerts_user_on_invalid_input_negative(capfd, monkeypatch):
    user_input = StringIO('-2\n')
    monkeypatch.setattr('sys.stdin', user_input)

    game = Game()
    game.get_desired_position()

    out, _ = capfd.readouterr()
    assert "\nInvalid selection. Enter a number from 1 to 9.\n" in out
    assert game.player_selection == ''

def test_get_desired_position_alerts_user_on_invalid_input_char(capfd, monkeypatch):
    user_input = StringIO('a\n')
    monkeypatch.setattr('sys.stdin', user_input)

    game = Game()
    game.get_desired_position()

    out, _ = capfd.readouterr()
    assert "\nInvalid selection. Enter a number from 1 to 9.\n" in out
    assert game.player_selection == ''

def test_get_desired_position_alerts_user_on_invalid_input_zero(capfd, monkeypatch):
    user_input = StringIO('0\n')
    monkeypatch.setattr('sys.stdin', user_input)

    game = Game()
    game.get_desired_position()

    out, _ = capfd.readouterr()
    assert "\nInvalid selection. Enter a number from 1 to 9.\n" in out
    assert game.player_selection == ''

def test_get_desired_position_alerts_user_on_invalid_input_ten(capfd, monkeypatch):
    user_input = StringIO('10\n')
    monkeypatch.setattr('sys.stdin', user_input)

    game = Game()
    game.get_desired_position()

    out, _ = capfd.readouterr()
    assert "\nInvalid selection. Enter a number from 1 to 9.\n" in out
    assert game.player_selection == ''

def test_update_board():
    game = Game()
    game.player_selection = 8
    game.update_board()
    assert game.board == ["1", "2", "3", "4", "5", "6", "7", "X", "9"]

def test_is_winner_true_if_x():
    game = Game()
    game.board = ['X', 'X', 'X', 'O', 'X', 'O', 'O', 'O', '9']
    assert game.is_winner() == True

def test_is_winner_true_if_o():
    game = Game()
    game.board = ['O', 'O', 'O', 'X', 'O', 'X', 'X', 'X', '9']
    assert game.is_winner() == True

def test_is_winner_false_if_empty():
    game = Game()
    assert game.is_winner() == False

def test_is_winner_false_if_tie():
    game = Game()
    game.board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
    assert game.is_winner() == False

def test_is_tie_true():
    game = Game()
    game.board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
    assert game.is_tie() == True

def test_is_tie_false():
    game = Game()
    game.board = ['X', 'X', 'X', 'O', 'X', 'O', 'O', 'O', '9']
    assert game.is_tie() == False

def test_reset_player_selection():
    game = Game()
    game.player_selection = 8
    game.reset_player_selection()
    assert game.player_selection == ""

def test_reset_board():
    game = Game()
    game.board = ["X", "O", "X", "X", "O", "O", "X", "X", "O"]
    game.reset_board()
    assert game.board == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]