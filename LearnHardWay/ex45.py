"""
Create Game:
 - Create a sudoku board
    Print the board
 - Create a solver
    Solve, and Print the solve
"""

import signal
import sys
import random


class GeneralError(Exception):
    pass


class NotValidString(Exception):
    pass


class GameBoard(object):

    def __init__(self):
        self.board = []
        self.level_options = {"expert": 17, "hard": 26, "medium": 32, "easy": 40}

    def create_board(self):
        for x in range(9):
            self.board.append(["[ ]"] * 9)
        return self.board

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print("______________________________")

    def validate_guess(self, row_guess, col_guess, guess) -> bool:
        valid_row = self._check_row(guess, row_guess)  # bool
        valid_column = self._check_column(col_guess, guess)
        valid_box = self._check_box(col_guess, guess, row_guess)

        valid_guess = valid_column and valid_row and valid_box

        return valid_guess

    def _check_box(self, row_guess, col_guess, guess):
        valid_box = True
        box_row_start = (row_guess - (row_guess % 3))
        box_column_start = (col_guess - (col_guess % 3))
        box_row_count = 0
        while box_row_count < 3 and valid_box:
            box_column_count = 0

            while box_column_count < 3 and valid_box:
                box_row_check = box_row_start + box_row_count
                box_column_check = box_column_start + box_column_count

                if "[" + str(guess) + "]" != self.board[box_row_check][box_column_check]:
                    valid_box = True
                else:
                    valid_box = False
                    break

                box_column_count += 1
            box_row_count += 1
        return valid_box

    def _check_column(self, col_guess, guess):
        for check_column in range(9):
            if "[" + str(guess) + "]" != self.board[check_column][col_guess]:
                valid_column = True
            else:
                valid_column = False
                break
        return valid_column

    def _check_row(self, row_guess, guess):
        for check_row in range(9):
            if "[" + str(guess) + "]" != self.board[row_guess][check_row]:
                valid_row = True
            else:
                valid_row = False
                break
        return valid_row

    def validate_empty(self, row_guess, col_guess):
        if self.board[row_guess][col_guess] == "[ ]":
            return True
        else:
            return False

    def fill_guess(self, row_guess, col_guess, guess):
        self.board[row_guess][col_guess] = "[" + str(guess) + "]"
        return self.board

    # This attempts at filling a starting board with the bare minimum of numbers based on level selected,
    # but it fails at creating a board that can be solved.
    def start_board(self, level):
        level_chosen = self.level_options[level]
        count_placement = 1
        while count_placement <= level_chosen:
            random_guess = random.randint(1, 9)
            random_row = random.randint(0, 8)
            random_column = random.randint(0, 8)
            validate = self.validate_guess(random_row, random_column, random_guess)
            is_empty = self.validate_empty(random_row, random_column)
            while validate and is_empty and count_placement <= level_chosen:
                self.fill_guess(random_row, random_column, random_guess)
                random_guess = random.randint(1, 9)
                random_row = random.randint(0, 8)
                random_column = random.randint(0, 8)
                validate = self.validate_guess(random_row, random_column, random_guess)
                is_empty = self.validate_empty(random_row, random_column)
                count_placement += 1

    # This will attempt at filling the whole solution randomly,
    # but it fails when it runs into a position that has already been filled.
    def fill_solution(self):
        populate_number = 1
        while populate_number <= 9:
            count_placement = 1
            while count_placement <= 9:
                random_row = random.randint(0, 8)
                random_column = random.randint(0, 8)
                validate = self.validate_guess(random_row, random_column, populate_number)
                is_empty = self.validate_empty(random_row, random_column)
                while validate and is_empty and count_placement <= 9:
                    self.fill_guess(random_row, random_column, populate_number)
                    self.print_board()
                    random_row = random.randint(0, 8)
                    random_column = random.randint(0, 8)
                    validate = self.validate_guess(random_row, random_column, populate_number)
                    is_empty = self.validate_empty(random_row, random_column)
                    count_placement += 1
                    print("count_placement" + str(count_placement) + "for" + str(populate_number))
            populate_number += 1

    # def fill_squares(self):
    #     rows = {"top": 3, "middle": 6, "bottom": 9}
    #     columns = {"top": 3, "middle": 6, "bottom": 9}
    #     for row in rows:
    #
    #     while populate_number <= 9:
    #         random_row = random.randint()


def signal_handler(signal, frame):
    print('\nYou pressed Ctrl+C!\nEnding program execution gracefully')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

new_board = GameBoard()
new_board.create_board()
print("How hard would you like the game to be?\n"
      "expert, hard, medium, easy")
chosen_level = input()
new_board.start_board(chosen_level)
new_board.print_board()

MAX_GUESSES = 81

fill_amount = 0
while fill_amount < MAX_GUESSES:

    print("What column would you like to enter your guess?")
    col_guess = int(input()) - 1
    while 0 > col_guess or col_guess > 8:
        print("That is not a valid column, please try again.")
        col_guess = int(input()) - 1

    print("What row would you like to enter your guess?")
    row_guess = int(input()) - 1
    while 0 > row_guess or row_guess > 8:
        print("That is not a valid row, please try again.")
        row_guess = int(input()) - 1

    print("What is your guess?")
    guess = int(input())
    while 1 > guess or guess > 9:
        print("That is not a valid guess, please try again.")
        guess = int(input())

    if new_board.validate_guess(row_guess, col_guess, guess):
        new_board.fill_guess(row_guess, col_guess, guess)
        new_board.print_board()
        fill_amount += 1
    else:
        new_board.print_board()
        print("That is not a valid guess. Try again")

signal.pause()
