"""
Create Game:
 - Create a sudoku board
    Print the board
 - Create a solver
    Solve, and Print the solve
"""


class GameBoard(object):

    def __init__(self, level):
        self.level = level
        self.board = []

    def create_board(self):
        for x in range(9):
            self.board.append(["[ ]"] * 9)
        return self.board

    def starter_board(self):
        pass

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print("______________________________")

    def validate_guess(self, row_guess, col_guess, guess):
        valid_row = True
        valid_column = True
        valid_box = True

        for check_row in range(9):
            if "[" + str(guess) + "]" != self.board[row_guess][check_row]:
                valid_row = True
            else:
                valid_row = False
                break

        for check_column in range(9):
            if "[" + str(guess) + "]" != self.board[check_column][col_guess]:
                valid_column = True
            else:
                valid_column = False
                break

        box_row = (row_guess - (row_guess % 3))
        box_column = (col_guess - (col_guess % 3))
        while box_row < row_guess and valid_box:
            while box_column < col_guess and valid_box:
                if "[" + str(guess) + "]" != self.board[box_row][box_column]:
                    valid_box = True
                else:
                    valid_box = False
                    break
                box_column += 1
            box_row += 1

        valid_guess = valid_column and valid_row and valid_box
        return valid_guess

    def fill_guess(self, row_guess, col_guess, guess):
        self.board[row_guess][col_guess] = "[" + str(guess) + "]"
        return self.board


new_board = GameBoard(2)
new_board.create_board()
new_board.print_board()
fill_amount = 0
while fill_amount < 81:
    print("What column would you like to enter your guess?")
    col_guess = int(input())
    print("What row would you like to enter your guess?")
    row_guess = int(input())
    print("What is your guess?")
    guess = int(input())
    if new_board.validate_guess(row_guess, col_guess, guess):
        new_board.fill_guess(row_guess, col_guess, guess)
        new_board.print_board()
        fill_amount += 1
    else:
        print("That is not a valid guess. Try again")
