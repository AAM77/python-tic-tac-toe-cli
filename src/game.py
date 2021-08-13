class Game:
    def __init__(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.winning_combinations = [
            (0, 1, 2),
            (0, 3, 6),
            (0, 4, 8),
            (1, 4, 7),
            (2, 4, 6),
            (2, 5, 8),
            (3, 4, 5),
            (6, 7, 8)
        ]

    def display_board(self):
        print(f" {' | '.join(self.board[0:3])} ")
        print("-----------")
        print(f" {' | '.join(self.board[3:6])} ")
        print("-----------")
        print(f" {' | '.join(self.board[6:10])} ")

    def current_player(self):
        if self.board.count('X') % 2 == 0:
            return 'O'
        else:
            return 'X'

    def determine_winner(self):
        for combination in self.winning_combinations:
            if all(self.board[index] == 'X' for index in combination):
                return 'X'
            elif all(self.board[index] == 'O' for index in combination):
                return 'O'