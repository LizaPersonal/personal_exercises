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


class Board(object):

    def __init__(self):
        self.board = []

    def convert_board_to_string(self) -> str:
        board_string = "___________________________"
        for row in self.board:
            board_string += "\n"
            for box in row:
                board_string += ''.join(str(box))
        board_string += "\n___________________________"
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

    def remove_guess(self, row_guess, col_guess):
        self.board[row_guess][col_guess] = "[ ]"
        return self.board

    def remove_mirror_guess(self, row_guess, col_guess):
        pass

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
                count_placement += 1
        return self.board


class BlankBoard(Board):

    def __init__(self):
        self.board = [['[ ]' for y in range(9)] for x in range(9)]

    def create_blank_board(self):
        self.board = [['[ ]' for y in range(9)] for x in range(9)]
        return self.board


class OptionsBoard(Board):

    def __init__(self):
        self.board = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for y in range(9)] for x in range(9)]

    def create_all_board_options(self):
        self.board = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for y in range(9)] for x in range(9)]
        return self.board


class PlayGame(object):

    def __init__(self):
        self.game_board = BlankBoard()
        self.options = OptionsBoard()
        self.solution = BlankBoard()

    def create_solution(self):
        # self.options.create_all_board_options()
        self.solution.fill_solution(self.options)

    def create_starting_board(self, level):
        self.game_board = copy.deepcopy(self.solution)

        while level <= 81:
            random_row = random.randint(0, 8)
            random_column = random.randint(0, 8)
            self.game_board.remove_guess(random_row, random_column)
            self.game_board.remove_mirror_guess(random_row, random_column)
            level += 1

    def find_solution(self):
        pass






    # This attempts at filling a starting board with the bare minimum of numbers based on level selected,
    # but it fails at creating a board that can be solved.
    # def start_board(self, level):
    #     count_placement = 1
    #     while count_placement <= level:
    #         random_guess = random.randint(1, 9)
    #         random_row = random.randint(0, 8)
    #         random_column = random.randint(0, 8)
    #         validate = self.validate_guess(random_row, random_column, random_guess)
    #         is_empty = self.validate_empty(random_row, random_column)
    #         if validate and is_empty and count_placement <= level:
    #             self.fill_guess(random_row, random_column, random_guess)
    #             count_placement += 1

    # This will attempt at filling the whole solution randomly,
    # but it fails when it runs into a position that has already been filled.
    # def fill_solution(self):
    #     populate_number = 1
    #     while populate_number <= 9:
    #         count_placement = 1
    #         while count_placement <= 9:
    #             random_row = random.randint(0, 8)
    #             random_column = random.randint(0, 8)
    #             validate = self.validate_guess(random_row, random_column, populate_number)
    #             is_empty = self.validate_empty(random_row, random_column)
    #             while validate and is_empty and count_placement <= 9:
    #                 self.fill_guess(random_row, random_column, populate_number)
    #                 print(self.convert_board_to_string())
    #                 random_row = random.randint(0, 8)
    #                 random_column = random.randint(0, 8)
    #                 validate = self.validate_guess(random_row, random_column, populate_number)
    #                 is_empty = self.validate_empty(random_row, random_column)
    #                 count_placement += 1
    #                 print("count_placement" + str(count_placement) + "for" + str(populate_number))
    #         populate_number += 1


def signal_handler(signal, frame):
    print('\nYou pressed Ctrl+C!\nEnding program execution gracefully')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


MAX_GUESSES = 81
LEVELS = {"expert": 17, "hard": 26, "medium": 32, "easy": 40}


new_game = PlayGame()

new_game.create_solution()
# print(new_game.options.create_all_board_options())

# new_board.fill_solution()
# new_board.remove_options_from_solution_for_starting_board()
#
# print(new_board.convert_board_to_string(new_board.board))


# print(new_board.convert_board_to_string(new_board.remove_options(1, 1, 1)))

# print("How hard would you like the game to be?\n"
#       "expert, hard, medium, easy")
# chosen_level = input()
# new_board.start_board(LEVELS[chosen_level])
# print(new_board.convert_board_to_string())
#
#
# fill_amount = 0
# while fill_amount < MAX_GUESSES:
#
#     print("What column would you like to enter your guess?")
#     col_guess = int(input()) - 1
#     while 0 > col_guess or col_guess > 8:
#         print("That is not a valid column, please try again.")
#         col_guess = int(input()) - 1
#
#     print("What row would you like to enter your guess?")
#     row_guess = int(input()) - 1
#     while 0 > row_guess or row_guess > 8:
#         print("That is not a valid row, please try again.")
#         row_guess = int(input()) - 1
#
#     print("What is your guess?")
#     guess = int(input())
#     while 1 > guess or guess > 9:
#         print("That is not a valid guess, please try again.")
#         guess = int(input())
#
#     if new_board.validate_guess(row_guess, col_guess, guess):
#         new_board.fill_guess(row_guess, col_guess, guess)
#         print(new_board.convert_board_to_string())
#         fill_amount += 1
#     else:
#         print(new_board.convert_board_to_string())
#         print("That is not a valid guess. Try again")
#
# signal.pause()
