from aoc_2023 import day_7
import pytest


@pytest.mark.parametrize(
    ["hand", "exp"],
    [
        ("AAAAA", 7),
        ("AA8AA", 6),
        ("23332", 5),
        ("TTT98", 4),
        ("23432", 3),
        ("A23A4", 2),
        ("23456", 1),
    ],
)
def test_hand_to_type(hand: str, exp: int) -> None:
    res = day_7.hand_to_type(hand)
    assert res == exp


@pytest.mark.parametrize(
    ["hand_1", "hand_2", "exp"],
    [("33332", "2AAAA", False), ("77788", "77888", True), ("KK677", "KTJJT", False)],
)
def test_hand_type_lesser(hand_1: str, hand_2: str, exp: bool) -> None:
    res = day_7.hand_type_lesser(hand_1, hand_2)
    assert res == exp


def test_total_winnings() -> None:
    res = day_7.total_winnings("aoc_2023/examples/day_7a.txt")
    assert res == 6440
