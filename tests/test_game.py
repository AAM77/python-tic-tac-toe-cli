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

def test_combinations():
    game = Game()
    assert game.winning_combinations == [
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

def test_get_player_move(capfd):
    game = Game()
    game.get_player_move()
    out, err = capfd.readouterr()
    assert out == "Please select a position to place your mark.\n"