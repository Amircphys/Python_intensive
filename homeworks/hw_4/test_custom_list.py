from typing import List
import pytest
from custom_list import CustomList


@pytest.mark.parametrize(
    "inp_1,inp_2,expected_output",
    [
        ([], [], []),
        ([1], [], []),
        ([], [1, 2], []),
        ([1, 2], [3, 4], [4, 6]),
        ([1, 2, 3], [3, 4], [4, 6]),
        ([1, 2], [3, 4, 5], [4, 6]),
        ([-1, -2], [3, 4, 5], [2, 2]),
    ],
)
def test_sum(inp_1: List, inp_2: List, expected_output: List):
    """Тесты на сумму"""
    custom_inp_1 = CustomList(inp_1)
    custom_inp_2 = CustomList(inp_2)
    output = custom_inp_1 + custom_inp_2
    assert output == CustomList(
        expected_output
    ), f"Expected output is {expected_output}, your output: {output}"


@pytest.mark.parametrize(
    "inp_1,inp_2,expected_output",
    [
        ([], [], []),
        ([1], [], []),
        ([], [1, 2], []),
        ([1, 2], [3, 4], [-2, -2]),
        ([3, 4], [1, 2], [2, 2]),
        ([1, 2, 3], [3, 4], [-2, -2]),
        ([1, 2], [3, 4, 5], [-2, -2]),
        ([-1, -2], [3, 4, 5], [-4, -6]),
    ],
)
def test_sub(inp_1: List, inp_2: List, expected_output: List):
    """Тесты на разность"""
    custom_inp_1 = CustomList(inp_1)
    custom_inp_2 = CustomList(inp_2)
    output = custom_inp_1 - custom_inp_2
    assert output == CustomList(
        expected_output
    ), f"Expected output is {expected_output}, your output: {output}"


@pytest.mark.parametrize(
    "inp_1,inp_2,expected_output",
    [
        ([], [], True),
        ([1], [], False),
        ([], [1, 2], False),
        ([-1, 4], [1, 2], True),
        ([-1, 5], [1, 2], False),
    ],
)
def test_eq(inp_1: List, inp_2: List, expected_output: bool):
    """Тесты на =="""
    custom_inp_1 = CustomList(inp_1)
    custom_inp_2 = CustomList(inp_2)
    output = custom_inp_1 == custom_inp_2
    assert (
        output == expected_output
    ), f"Expected output is {expected_output}, your output: {output}"


@pytest.mark.parametrize(
    "inp_1,inp_2,expected_output",
    [
        ([], [], False),
        ([1], [], False),
        ([], [1, 2], True),
        ([-1, 4], [1, 2], False),
        ([-1, 5], [1, 2], False),
        ([1, -5], [1, 2], True),
    ],
)
def test_lt(inp_1: List, inp_2: List, expected_output: bool):
    """Тесты на <"""
    custom_inp_1 = CustomList(inp_1)
    custom_inp_2 = CustomList(inp_2)
    output = custom_inp_1 < custom_inp_2
    assert (
        output == expected_output
    ), f"Expected output is {expected_output}, your output: {output}"


@pytest.mark.parametrize(
    "inp_1,inp_2,expected_output",
    [
        ([], [], False),
        ([1], [], True),
        ([], [1, 2], False),
        ([-1, 4], [1, 2], False),
        ([-1, 5], [1, 2], True),
        ([1, -5], [1, 2], False),
    ],
)
def test_gt(inp_1: List, inp_2: List, expected_output: bool):
    """Тесты на >"""
    custom_inp_1 = CustomList(inp_1)
    custom_inp_2 = CustomList(inp_2)
    output = custom_inp_1 > custom_inp_2
    assert (
        output == expected_output
    ), f"Expected output is {expected_output}, your output: {output}"


@pytest.mark.parametrize(
    "inp_1,inp_2,expected_output",
    [
        ([], [], True),
        ([1], [], True),
        ([], [1, 2], False),
        ([-1, 4], [1, 2], True),
        ([-1, 5], [1, 2], True),
        ([1, -5], [1, 2], False),
    ],
)
def test_ge(inp_1: List, inp_2: List, expected_output: bool):
    """Тесты на >="""
    custom_inp_1 = CustomList(inp_1)
    custom_inp_2 = CustomList(inp_2)
    output = custom_inp_1 >= custom_inp_2
    assert (
        output == expected_output
    ), f"Expected output is {expected_output}, your output: {output}"


@pytest.mark.parametrize(
    "inp_1,inp_2,expected_output",
    [
        ([], [], True),
        ([1], [], False),
        ([], [1, 2], True),
        ([-1, 4], [1, 2], True),
        ([-1, 5], [1, 2], False),
        ([1, -5], [1, 2], True),
    ],
)
def test_le(inp_1: List, inp_2: List, expected_output: bool):
    """Тесты на <="""
    custom_inp_1 = CustomList(inp_1)
    custom_inp_2 = CustomList(inp_2)
    output = custom_inp_1 <= custom_inp_2
    assert (
        output == expected_output
    ), f"Expected output is {expected_output}, your output: {output}"
