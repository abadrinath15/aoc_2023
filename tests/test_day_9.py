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


@pytest.mark.parametrize(
    ["history", "exp"],
    [
        (pandas.Series([10, 13, 16, 21, 30, 45]), 5),
        (
            pandas.Series(
                [
                    12,
                    16,
                    19,
                    16,
                    -4,
                    -57,
                    -159,
                    -311,
                    -455,
                    -360,
                    650,
                    4330,
                    14992,
                    42932,
                    112235,
                    278107,
                    664353,
                    1542439,
                    3494604,
                    7743519,
                    16805383,
                ]
            ),
            10,
        ),
    ],
)
def test_extrapolate_history_front(history: "pandas.Series[float]", exp: int) -> None:
    res = day_9.extrapolate_history_front(history)
    assert res == exp


def test_sum_extrapolated_histories() -> None:
    fp = "aoc_2023/examples/day_9.txt"
    res = day_9.sum_extrapolated_histories(fp, day_9.extrapolate_history_front)
    assert res == 2
