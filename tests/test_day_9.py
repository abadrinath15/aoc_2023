from aoc_2023 import day_9
import pytest
import pandas


@pytest.mark.parametrize(
    ["history", "exp"],
    [
        (pandas.Series([0, 3, 6, 9, 12, 15]), 18),
        (pandas.Series([1, 3, 6, 10, 15, 21]), 28),
    ],
)
def test_extrapolate_history(history: "pandas.Series[float]", exp: int) -> None:
    res = day_9.extrapolate_history(history)
    assert res == exp


def test_extrapolate_history_front() -> None:
    history = pandas.Series([10, 13, 16, 21, 30, 45])
    res = day_9.extrapolate_history_front(history)
    assert res == 5


def test_sum_extrapolated_histories() -> None:
    fp = "aoc_2023/examples/day_9.txt"
    res = day_9.sum_extrapolated_histories(fp, day_9.extrapolate_history_front)
    assert res == 2
