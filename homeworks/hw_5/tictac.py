from typing import List
from collections import Counter
from itertools import chain

CORRECT_COORDINATES_MESSAGE = "Введены корректные координаты\n"
WRONG_COORDINATES_MESSAGE = "Введены некорректные координаты - значение координат должно лежать в диапазоне [0, 2], пожалуйста введите корректные координаты\n"
WRONG_CELL_MESSAGE = "Введены некорректные координаты - ячейка уже занята, пожалуйста введите корректные координаты\n"
WRONG_NUMBER_COORDINATES_MESSAGE = (
    "Число введенных координат должно равняться 2, пожалуйста введите две координаты\n"
)
DRAW_MESSAGE = "Draw in the game!!!\n"
NEXT_STEP_MESSAGE = "next step...\n"


class Player:
    def __init__(self, mark: str = "x"):
        self.mark = mark
        self.ocuppied_states = []
        self.stat_ocuppied_states_hor = Counter()
        self.stat_ocuppied_states_ver = Counter()

    def check_is_win(self):
        for _, value in chain(
            self.stat_ocuppied_states_hor.items(), self.stat_ocuppied_states_ver.items()
        ):
            if value == 3:
                return True
        if all(
            item in self.ocuppied_states for item in [[0, 0], [1, 1], [2, 2]]
        ) or all(item in self.ocuppied_states for item in [[0, 2], [1, 1], [2, 0]]):
            return True
        return False

    def update_ocuppied_states(self, coordinates: tuple):
        self.stat_ocuppied_states_hor.update([coordinates[0]])
        self.stat_ocuppied_states_ver.update([coordinates[1]])
        self.ocuppied_states.append(coordinates)


class TicTacGame:
    def __init__(self, empty_element=" "):
        self.empty_element = empty_element
        self.board = self.init_board()
        self.winner = None

    def init_board(self):
        return [[self.empty_element] * 3 for i in range(3)]

    def show_board(self):
        for el in self.board:
            print(el, flush=True)

    def validate_input(self, coordinates):
        if len(coordinates) != 2:
            raise ValueError(WRONG_NUMBER_COORDINATES_MESSAGE)
        x, y = coordinates
        x, y = int(x), int(y)
        if (not 0 <= x < 3) or (not 0 <= y < 3):
            raise ValueError(WRONG_COORDINATES_MESSAGE)
        elif self.board[x][y] != self.empty_element:
            raise ValueError(WRONG_CELL_MESSAGE)

    def check_input(self, coordinates: List[int]) -> str:
        """
        Check the correctness of cell coordinates
        Args:
            coordinates (List[int]): the coordinates of cells

        Returns:
            str:  true_input if cell coordinates are correct, else the message of error
        """
        try:
            self.validate_input(coordinates)
        except Exception as e:
            return e.args[0]
        return CORRECT_COORDINATES_MESSAGE

    def fill_board_cell(self, coordinates, player):
        x, y = coordinates
        self.board[x][y] = player.mark

    def check_fill_all_cells(self):
        for row in self.board:
            if row.count(self.empty_element) > 0:
                return False
        return True

    def start_game(self):
        start_idx = 0
        first_player = Player("x")
        second_player = Player("o")
        inp = ""
        while self.winner is None:

            if start_idx % 2 == 0:
                temp_player = first_player
            else:
                temp_player = second_player

            inp = input()
            inp = list(map(int, inp.split()))

            while self.check_input(inp) != CORRECT_COORDINATES_MESSAGE:
                message = self.check_input(inp)
                print(message, flush=True)
                inp = list(
                    map(
                        lambda x: int(x.strip()),
                        input().strip().split(),
                    )
                )
            self.fill_board_cell(inp, temp_player)
            if self.check_fill_all_cells():
                print(DRAW_MESSAGE, flush=True)
                self.show_board()
                return
            temp_player.update_ocuppied_states(inp)
            if temp_player.check_is_win():
                print(f"{temp_player.mark} win!!!", flush=True)
                self.show_board()
                return
            self.show_board()
            start_idx += 1
            print(NEXT_STEP_MESSAGE, flush=True)


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
