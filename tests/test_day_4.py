from pytest import mark
from aoc_2023 import day_4


@mark.parametrize(
    ["line", "exp"],
    [
        (
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            (1, set([41, 48, 83, 86, 17]), [83, 86, 6, 31, 17, 9, 48, 53]),
        ),
    ],
)
def test_winners_yours_from_line(
    line: str, exp: tuple[int, set[int], list[int]]
) -> None:
    res = day_4.winners_yours_from_line(line)
    assert exp == res


@mark.parametrize(
    ["winners", "yours", "exp"],
    [
        (set([41, 48, 83, 86, 17]), [83, 86, 6, 31, 17, 9, 48, 53], 8),
        (set([87, 83, 26, 28, 32]), [88, 30, 70, 12, 93, 22, 82, 36], 0),
    ],
)
def test_score_card(winners: set[int], yours: list[int], exp: int) -> None:
    res = day_4.score_card(winners, yours)
    assert res == exp


def test_sum_card_scores() -> None:
    res = day_4.sum_card_scores("aoc_2023/examples/day_4a.txt")
    assert res == 13


def test_score_scratch_correct_rules() -> None:
    res = day_4.score_scratch_correct_rules("aoc_2023/examples/day_4a.txt")
    assert res == 30
