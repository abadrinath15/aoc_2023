from dataclasses import dataclass
from typing import cast
import re


@dataclass
class ElfDraw:
    reds: int
    blues: int
    greens: int


def elf_draw_from_str(draw: str) -> ElfDraw:
    num_cubes = [
        int(num_str[1])
        if (num_str := re.search(rf"([0-9]+) {color}", draw)) is not None
        else 0
        for color in ["red", "blue", "green"]
    ]
    return ElfDraw(*num_cubes)


@dataclass
class Game:
    game_id: int
    draws: list[ElfDraw]


def line_to_game(line: str) -> Game:
    if (gi_match := re.match(r"Game (\d+): (.+)", line)) is None:
        raise ValueError("Parsing didn't work. Ouch")

    game_id = int(gi_match[1])
    selections = cast(str, gi_match[2])
    return Game(game_id, [elf_draw_from_str(draw) for draw in selections.split("; ")])


def is_game_possible(game: Game, reds: int, greens: int, blues: int) -> bool:
    for draw in game.draws:
        if reds < draw.reds or blues < draw.blues or greens < draw.greens:
            return False

    return True


def sum_possible_games(fp: str, reds: int, greens: int, blue: int) -> int:
    game_id_sum = 0
    with open(fp) as file:
        for line in file:
            game = line_to_game(line)
            if is_game_possible(game, reds, greens, blue):
                game_id_sum += game.game_id

    return game_id_sum


def main() -> None:
    fp = "aoc_2023/inputs/day_2.txt"
    print(sum_possible_games(fp, 12, 13, 14))


if __name__ == "__main__":
    main()
