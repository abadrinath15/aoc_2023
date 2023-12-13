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
