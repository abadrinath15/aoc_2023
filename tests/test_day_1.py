from typing import Callable
from aoc_2023 import day_1
from pytest import mark


@mark.parametrize(
    ["fp", "cal_func", "exp"],
    [
        ("aoc_2023/examples/day_1a.txt", day_1.calibration_value, 142),
        ("aoc_2023/examples/day_1b.txt", day_1.mixed_calibration_value, 281),
    ],
)
def test_sum_calibration_values(
    fp: str, cal_func: Callable[[str], int], exp: int
) -> None:
    res = day_1.sum_calibration_values(fp, cal_func)
    assert res == exp
