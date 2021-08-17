from io import StringIO
from src.game import Game

def test_initiate_turn():
    game = Game()
    assert game.current_player() == 'X'
    # check if the game is over (someone won or it is a tie)
    # check which user's turn it is
    # ask the user for input
    # update the board with the user's input
    # display the board
    pass