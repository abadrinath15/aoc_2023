from aoc_2023 import day_6
import pytest


def test_get_times() -> None:
    res = day_6.times_from_line("Time:      7  15   30")
    assert res == [7, 15, 30]


def test_get_distances() -> None:
    res = day_6.distances_from_line("Distance:  9  40  200")
    assert res == [9, 40, 200]


@pytest.mark.parametrize(
    ["time", "distance", "exp"], [(7, 9, 4), (15, 40, 8), (30, 200, 9)]
)
def test_winning_performances(time: int, distance: int, exp: int) -> None:
    res = day_6.winning_performances(time, distance)
    assert res == exp


def test_product_winning_performances() -> None:
    res = day_6.product_winning_performances("aoc_2023/examples/day_6a.txt")
    assert res == 288
