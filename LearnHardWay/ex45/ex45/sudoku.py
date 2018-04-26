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
import copy


class GeneralError(Exception):
    pass


class NotValidString(Exception):
    pass


class Board(object):

    def __init__(self):
        self.board = []

    def convert_board_to_string(self) -> str:
        row_count = 1
        board_string = "________________________________________"
        for row in self.board:
            board_string += "\n"
            column_count = 1
            for box in row:
                board_string += ''.join(str(box))
                if column_count % 3 == 0:
                    board_string += "  |  "
                column_count += 1
            if row_count % 3 == 0:
                board_string += "\n________________________________________"
            row_count += 1
        return board_string

    def validate_guess(self, row_guess, column_guess, guess) -> bool:
        valid_row = self._check_row(row_guess, guess)
        valid_column = self._check_column(column_guess, guess)
        valid_box = self._check_box(row_guess, column_guess, guess)

        valid_guess = valid_column and valid_row and valid_box
        return valid_guess

    def _check_box(self, row_guess, column_guess, guess) -> bool:
        valid_box = True
        box_row_start = (row_guess - (row_guess % 3))
        box_column_start = (column_guess - (column_guess % 3))
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

    def _check_column(self, col_guess, guess) -> bool:
        for row_in_column in range(9):
            if "[" + str(guess) + "]" != self.board[row_in_column][col_guess]:
                valid_column = True
            else:
                valid_column = False
                break
        return valid_column

    def _check_row(self, row_guess, guess) -> bool:
        for check_row in range(9):
            if "[" + str(guess) + "]" != self.board[row_guess][check_row]:
                valid_row = True
            else:
                valid_row = False
                break
        return valid_row

    def validate_empty(self, row_guess, col_guess) -> bool:
        if self.board[row_guess][col_guess] == "[ ]":
            return True
        else:
            return False

    def fill_guess(self, row_guess, col_guess, guess):
        self.board[row_guess][col_guess] = "[" + str(guess) + "]"
        return self.board

    def set_options_to_blank(self, row_guess, col_guess):
        self.board[row_guess][col_guess] = []
        return self.board

    def set_location_to_empty(self, row_guess, col_guess):
        self.board[row_guess][col_guess] = "[ ]"
        return self.board

    def remove_mirror_location(self, row_guess, col_guess):
        mirror_row = 8 - row_guess
        mirror_column = 8 - col_guess
        self.board[mirror_row][mirror_column] = "[ ]"
        return self.board

    def remove_options(self, row_guess, column_guess, guess):
        self._remove_from_row(row_guess, guess)
        self._remove_from_column(column_guess, guess)
        self._remove_from_box(row_guess, column_guess, guess)
        return self.board

    def _remove_from_column(self, column_guess, guess):
        for row_in_column in range(9):
            if guess in self.board[row_in_column][column_guess]:
                self.board[row_in_column][column_guess].remove(guess)
        return self.board

    def _remove_from_row(self, row_guess, guess):
        for column_in_row in range(9):
            if guess in self.board[row_guess][column_in_row]:
                self.board[row_guess][column_in_row].remove(guess)
        return self.board

    def _remove_from_box(self, row_guess, column_guess, guess):
        box_row_start = (row_guess - (row_guess % 3))
        box_column_start = (column_guess - (column_guess % 3))
        box_row_count = 0

        while box_row_count < 3:
            box_column_count = 0

            while box_column_count < 3:
                box_row_check = box_row_start + box_row_count
                box_column_check = box_column_start + box_column_count

                if guess in self.board[box_row_check][box_column_check]:
                    self.board[box_row_check][box_column_check].remove(guess)

                box_column_count += 1
            box_row_count += 1
        return self.board

    def find_minimum_options(self):
        minimum_row = 0
        minimum_column = 0
        minimum_number_available = 9
        minimum_available = 0
        for row in range(9):
            for column in range(9):
                is_empty = self.validate_empty(row, column)
                if not is_empty and 0 < len(self.board[row][column]) <= minimum_number_available:
                    minimum_row = row
                    minimum_column = column
                    minimum_available = self.board[row][column]
                    minimum_number_available = len(self.board[row][column])
        return minimum_row, minimum_column, minimum_available

    def fill_solution(self, options_board):
        count_placement = 1
        while count_placement <= 81:
            minimum_row, minimum_column, minimum_available = options_board.find_minimum_options()
            random_guess = random.choice(minimum_available)
            validate = self.validate_guess(minimum_row, minimum_column, random_guess)
            is_empty = self.validate_empty(minimum_row, minimum_column)
            if validate and is_empty:
                self.fill_guess(minimum_row, minimum_column, random_guess)
                options_board.remove_options(minimum_row, minimum_column, random_guess)
                options_board.set_options_to_blank(minimum_row, minimum_column)
                count_placement += 1
        return self.board


class BlankBoard(Board):

    def __init__(self):
        self.board = [['[ ]' for y in range(9)] for x in range(9)]


class OptionsBoard(Board):

    def __init__(self):
        self.board = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for y in range(9)] for x in range(9)]


class PlayGame(object):

    def __init__(self):
        self.game_board = BlankBoard()
        self.options = OptionsBoard()
        self.solution = BlankBoard()
        self.starting_board = BlankBoard()

    def create_solution(self):
        solution_options = OptionsBoard()
        self.solution.fill_solution(solution_options)
        return self.solution

    def create_starting_board(self, level):
        self.starting_board = copy.deepcopy(self.solution)
        while level <= 81:
            random_row = random.randint(0, 8)
            random_column = random.randint(0, 8)
            is_empty = self.starting_board.validate_empty(random_row, random_column)
            if not is_empty:
                self.starting_board.set_location_to_empty(random_row, random_column)
                self.starting_board.remove_mirror_location(random_row, random_column)
                level += 2
        self.game_board = copy.deepcopy(self.starting_board)
        return self.starting_board, self.game_board

    def play_game(self, level):

        while level <= 81:

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

            if self.game_board.validate_guess(row_guess, col_guess, guess)\
                    and self.starting_board.validate_empty(row_guess, col_guess):
                self.game_board.fill_guess(row_guess, col_guess, guess)
                print(self.game_board.convert_board_to_string())
                level += 1
            else:
                print(self.game_board.convert_board_to_string())
                print("That is not a valid guess. Try again")

        return self.game_board


def signal_handler(signal, frame):
    print('\nYou pressed Ctrl+C!\nEnding program execution gracefully')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


LEVELS = {"expert": 17, "hard": 26, "medium": 32, "easy": 40}
print("How hard would you like the game to be?\n"
      "expert, hard, medium, easy")
chosen_level = input()

new_game = PlayGame()

new_game.create_solution()
new_game.create_starting_board(LEVELS[chosen_level])

print(new_game.game_board.convert_board_to_string())

new_game.play_game(LEVELS[chosen_level])

signal.pause()
