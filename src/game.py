class Game:
    def __init__(self: object):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.player_selection = ""

        self.WINNING_COMBINATIONS = [
            (0, 1, 2),
            (0, 3, 6),
            (0, 4, 8),
            (1, 4, 7),
            (2, 4, 6),
            (2, 5, 8),
            (3, 4, 5),
            (6, 7, 8)
        ]


    def display_board(self: object):
        print(f" {' | '.join(self.board[0:3])} ")
        print("-----------")
        print(f" {' | '.join(self.board[3:6])} ")
        print("-----------")
        print(f" {' | '.join(self.board[6:10])} ")

    def current_player(self: object) -> str:
        if self.board.count('X') >= 1 and self.board.count('X') % 2 == 0:
            return 'O'
        else:
            return 'X'

    def get_desired_position(self: object):
        self.player_selection = input("Please select a position to place your mark.\n")

        if self.player_selection not in [str(i) for i in range(1, 10)]:
            self.reset_player_selection()
            print("Invalid selection. Enter a number from 1 to 9.")

    def update_board(self: object):
        new_board = self.board.copy()
        new_board[int(self.player_selection) - 1] = self.current_player()
        self.board = new_board

    def is_winner(self: object) -> bool:
        for combination in self.WINNING_COMBINATIONS:
            if (
                all(self.board[index] == 'X' for index in combination) or
                all(self.board[index] == 'O' for index in combination)
                ):
                return True
        return False

    def is_tie(self: object) -> bool:
        if not self.is_winner() and all(item in ['X', 'O'] for item in self.board):
            return True
        return False

    def determine_winner(self: object) -> str:
        for combination in self.WINNING_COMBINATIONS:
            if all(self.board[index] == 'X' for index in combination):
                return 'X'
            elif all(self.board[index] == 'O' for index in combination):
                return 'O'

    def reset_board(self: object):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def reset_player_selection(self: object):
        self.player_selection = ""

    def initiate_turn(self: object):
        pass
        # check if the game is over (someone won or it is a tie)
        # check which user's turn it is
        # ask the user for input
        # update the board with the user's input
        # display the board

    def is_over(self) -> bool:
        return True if self.is_winner() or self.is_tie() else False