import subprocess
import pytest
import time
from tictac import (
    TicTacGame,
    Player,
    CORRECT_COORDINATES_MESSAGE,
    WRONG_COORDINATES_MESSAGE,
    WRONG_CELL_MESSAGE,
    WRONG_NUMBER_COORDINATES_MESSAGE,
    DRAW_MESSAGE,
    NEXT_STEP_MESSAGE,
)


# Фикстуры для модульного тестирования
@pytest.fixture
def game():
    return TicTacGame()


@pytest.fixture
def player():
    return Player()


# Модульные тесты
@pytest.mark.parametrize(
    "coordinates,expected_output",
    [
        # correct coordinates
        ([0, 0], CORRECT_COORDINATES_MESSAGE),
        ([2, 2], CORRECT_COORDINATES_MESSAGE),
        ([1, 2], CORRECT_COORDINATES_MESSAGE),
        # wrong coordinates - going beyond the boundaries
        ([1, -1], WRONG_COORDINATES_MESSAGE),
        ([0, 3], WRONG_COORDINATES_MESSAGE),
        ([1, 6], WRONG_COORDINATES_MESSAGE),
        ([-1, -1], WRONG_COORDINATES_MESSAGE),
        ([0, -1], WRONG_COORDINATES_MESSAGE),
        ([2, 3], WRONG_COORDINATES_MESSAGE),
        ([3, 0], WRONG_COORDINATES_MESSAGE),
        # wrong coordinates  - the number of coordintes isn't equal 2
        ([1, 2, 0], WRONG_NUMBER_COORDINATES_MESSAGE),
        ([1], WRONG_NUMBER_COORDINATES_MESSAGE),
        ([1, 0, 0, 1], WRONG_NUMBER_COORDINATES_MESSAGE),
    ],
)
def test_validate_input_valid(coordinates, expected_output, game):
    assert game.check_input(coordinates) == expected_output


def test_validate_input_occupied_cell(game):
    game.fill_board_cell([0, 0], Player("x"))
    assert game.check_input([0, 0]) == WRONG_CELL_MESSAGE
    assert game.check_input([0, 1]) == CORRECT_COORDINATES_MESSAGE


@pytest.mark.parametrize(
    "fill_cells",
    [
        # win by row
        ([0, 0], [0, 1], [0, 2]),
        ([1, 0], [1, 1], [1, 2]),
        ([2, 0], [2, 1], [2, 2]),
        # win by column
        ([0, 0], [1, 0], [2, 0]),
        ([0, 1], [1, 1], [2, 1]),
        ([0, 2], [1, 2], [2, 2]),
        # win by diagonal
        ([0, 0], [1, 1], [2, 2]),
        ([0, 2], [1, 1], [2, 0]),
    ],
)
def test_player_win_condition(fill_cells, player):
    for cell in fill_cells:
        player.update_ocuppied_states(cell)
    assert player.check_is_win() is True


# Интеграционные тесты
def run_game(inputs):
    process = subprocess.Popen(
        ["python", "-u", "tictac.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        bufsize=0,
    )
    output = ""
    # Отправляем все входные данные
    output, _ = process.communicate("\n".join(inputs))
    process.stdin.close()
    return output


@pytest.mark.parametrize(
    "inputs,expected_output",
    [
        # win by row
        (
            [
                "0 0",  # X
                "1 1",  # O
                "0 1",  # X
                "2 2",  # O
                "0 2",  # X wins
            ],
            "x win!!!",
        ),
        (
            [
                "2 0",  # X
                "1 1",  # O
                "2 1",  # X
                "1 2",  # O
                "2 2",  # X wins
            ],
            "x win!!!",
        ),
        (
            [
                "2 0",  # X
                "1 1",  # O
                "2 1",  # X
                "1 0",  # O
                "0 2",  # X
                "1 2",  # o wins
            ],
            "o win!!!",
        ),
        # win by column
        (
            [
                "0 0",  # X
                "1 1",  # O
                "1 0",  # X
                "2 2",  # O
                "2 0",  # X wins
            ],
            "x win!!!",
        ),
        (
            [
                "2 2",  # X
                "1 1",  # O
                "1 2",  # X
                "1 0",  # O
                "0 2",  # X wins
            ],
            "x win!!!",
        ),
        (
            [
                "2 0",  # X
                "1 1",  # O
                "0 2",  # X
                "0 1",  # O
                "1 2",  # X
                "2 1",  # o wins
            ],
            "o win!!!",
        ),
        # win by diagonal
        (
            [
                "0 0",  # X
                "1 2",  # O
                "1 1",  # X
                "0 2",  # O
                "2 2",  # X wins
            ],
            "x win!!!",
        ),
        (
            [
                "0 0",  # X
                "0 2",  # O
                "1 2",  # X
                "1 1",  # O
                "0 1",  # X
                "2 0",  # o win
            ],
            "o win!!!",
        ),
        # draw in game
        (
            [
                "0 0",  # X
                "0 1",  # O
                "0 2",  # X
                "1 0",  # O
                "1 1",  # X
                "1 2",  # O
                "2 1",  # O
                "2 0",  # X
                "2 2",  # X
            ],
            DRAW_MESSAGE,
        ),
    ],
)
def test_full_game_win_x(inputs, expected_output):
    output = run_game(inputs)
    assert expected_output in output
