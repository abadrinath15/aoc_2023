import re
import functools
import operator


def times_from_line(line: str) -> list[int]:
    if (times_str := re.match(r"Time:[ ]+ ([0-9 ]+)", line)) is None:
        raise ValueError("Whoops, the parsing didn't work")

    return [int(x) for x in times_str[1].split()]


def distances_from_line(line: str) -> list[int]:
    if (times_str := re.match(r"Distance:[ ]+ ([0-9 ]+)", line)) is None:
        raise ValueError("Whoops, the parsing didn't work")

    return [int(x) for x in times_str[1].split()]


def winning_performances(time: int, distance: int) -> int:
    count = 0
    for held_time in range(0, time):
        performance = held_time * (time - held_time)
        if performance > distance:
            count += 1

    return count


def product_winning_performances(fp: str) -> int:
    with open(fp) as file:
        times = times_from_line(next(file))
        distances = distances_from_line(next(file))

    return functools.reduce(operator.mul, map(winning_performances, times, distances))


def main() -> None:
    print(product_winning_performances("aoc_2023/inputs/day_6.txt"))


if __name__ == "__main__":
    main()
