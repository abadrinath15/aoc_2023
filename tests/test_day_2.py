from pytest import mark
from aoc_2023 import day_2


@mark.parametrize(
    ["draw", "exp"],
    [
        ("3 blue, 4 red", day_2.ElfDraw(4, 3, 0)),
        ("3 green, 4 blue, 1 red", day_2.ElfDraw(1, 4, 3)),
        ("1 red", day_2.ElfDraw(1, 0, 0)),
    ],
)
def test_elf_draw_from_str(draw: str, exp: day_2.ElfDraw) -> None:
    res = day_2.elf_draw_from_str(draw)
    assert exp == res


@mark.parametrize(
    ["line", "exp"],
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            day_2.Game(
                1,
                [
                    day_2.ElfDraw(4, 3, 0),
                    day_2.ElfDraw(1, 6, 2),
                    day_2.ElfDraw(0, 0, 2),
                ],
            ),
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            day_2.Game(
                3,
                [
                    day_2.ElfDraw(20, 6, 8),
                    day_2.ElfDraw(4, 5, 13),
                    day_2.ElfDraw(1, 0, 5),
                ],
            ),
        ),
    ],
)
def test_line_to_gamerecord(line: str, exp: day_2.Game) -> None:
    res = day_2.line_to_game(line)
    assert exp == res


@mark.parametrize(
    ["game", "exp"],
    [
        (
            day_2.Game(
                1,
                [
                    day_2.ElfDraw(4, 3, 0),
                    day_2.ElfDraw(1, 6, 2),
                    day_2.ElfDraw(0, 0, 2),
                ],
            ),
            True,
        ),
        (
            day_2.Game(
                3,
                [
                    day_2.ElfDraw(20, 6, 8),
                    day_2.ElfDraw(4, 5, 13),
                    day_2.ElfDraw(1, 0, 5),
                ],
            ),
            False,
        ),
    ],
)
def test_is_game_possible(game: day_2.Game, exp: bool) -> None:
    res = day_2.is_game_possible(game, 12, 13, 14)
    assert res == exp


def test_sum_possible_games() -> None:
    res = day_2.sum_possible_games("aoc_2023/examples/day_2a.txt", 12, 13, 14)
    assert res == 8


@mark.parametrize(
    ["game", "exp"],
    [
        (
            day_2.Game(
                1,
                [
                    day_2.ElfDraw(4, 3, 0),
                    day_2.ElfDraw(1, 6, 2),
                    day_2.ElfDraw(0, 0, 2),
                ],
            ),
            48,
        ),
        (
            day_2.Game(
                3,
                [
                    day_2.ElfDraw(20, 6, 8),
                    day_2.ElfDraw(4, 5, 13),
                    day_2.ElfDraw(1, 0, 5),
                ],
            ),
            1560,
        ),
    ],
)
def test_min_power_for_game(game: day_2.Game, exp: int) -> None:
    res = day_2.min_power_for_game(game)
    assert exp == res


def test_sum_powers_for_games() -> None:
    res = day_2.sum_powers_for_games("aoc_2023/examples/day_2a.txt")
    assert res == 2286
