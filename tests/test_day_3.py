from aoc_2023 import day_3
from pytest import mark, fixture
from itertools import permutations, product


@fixture
def example_nn_sl() -> (
    tuple[list[tuple[int, set[tuple[int, int]]]], dict[tuple[int, int], str]]
):
    return day_3.number_neighbors_and_symbol_locations("aoc_2023/examples/day_3a.txt")


@mark.parametrize(
    ["coord", "line_length", "exp"],
    [
        ((0, 0), 2, set([(1, 0), (1, 1), (0, 1)])),
        ((1, 1), 3, set(permutations([0, 1, 2, 2, 0], r=2))),
    ],
)
def test_neighboring_coordinates(
    coord: tuple[int, int], line_length: int, exp: set[tuple[int, int]]
) -> None:
    res = day_3.neighboring_coordinates(coord, line_length)
    assert res == exp


@mark.parametrize(
    ["start", "end", "row", "line_length", "exp"],
    [
        (1, 2, 1, 3, set(permutations([0, 1, 2, 2, 0], r=2))),
        (1, 3, 1, 4, set(product(range(3), range(4))) - set([(1, 1), (1, 2)])),
    ],
)
def test_neighbors_for_number(
    start: int, end: int, row: int, line_length: int, exp: set[tuple[int, int]]
) -> None:
    res = day_3.neighbors_for_number(start, end, row, line_length)
    assert res == exp


@mark.parametrize(
    ["line", "exp"],
    [
        ("...*......", [("*", 3)]),
        ("467..114..", []),
        ("617*......", [("*", 3)]),
        ("...$.*....", [("$", 3), ("*", 5)]),
        ("...*.*....", [("*", 3), ("*", 5)]),
        ("..........", []),
    ],
)
def test_symbol_index(line: str, exp: list[tuple[str, int]]) -> None:
    res = day_3.symbol_index(line)
    assert list(res) == exp


def test_sum_part_numbers(
    example_nn_sl: tuple[
        list[tuple[int, set[tuple[int, int]]]], dict[tuple[int, int], str]
    ]
) -> None:
    res = day_3.sum_part_numbers(*example_nn_sl)
    assert res == 4361


def test_sum_gear_ratios(
    example_nn_sl: tuple[
        list[tuple[int, set[tuple[int, int]]]], dict[tuple[int, int], str]
    ]
):
    res = day_3.sum_gear_ratios(*example_nn_sl)
    assert res == 467835
