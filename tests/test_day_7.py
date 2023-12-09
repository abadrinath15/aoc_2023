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
    ["hand_1", "hand_2", "use_joker", "exp"],
    [
        ("33332", "2AAAA", False, False),
        ("77788", "77888", False, True),
        ("KK677", "KTJJT", False, False),
        ("JKKK2", "QQQQ2", True, True),
    ],
)
def test_hand_type_lesser(hand_1: str, hand_2: str, use_joker: bool, exp: bool) -> None:
    res = day_7.hand_type_lesser(hand_1, hand_2, use_joker)
    assert res == exp


@pytest.mark.parametrize(["use_joker", "exp"], [(False, 6440), (True, 5905)])
def test_total_winnings(use_joker: bool, exp: int) -> None:
    res = day_7.total_winnings("aoc_2023/examples/day_7a.txt", use_joker)
    assert res == exp
