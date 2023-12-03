from typing import Iterator
from re import finditer, Match
from itertools import permutations


def neighboring_coordinates(
    coord: tuple[int, int], line_length: int
) -> set[tuple[int, int]]:
    neighbors: set[tuple[int, int]] = set()
    for adjustment in set(permutations([-1, 1, 0, -1, 1], r=2)):
        adjusted = coord[0] + adjustment[0], coord[1] + adjustment[1]
        if -1 in adjusted or line_length in adjusted:
            continue

        neighbors.add(adjusted)

    return neighbors


def neighbors_for_number(
    start: int, end: int, row: int, line_length: int
) -> set[tuple[int, int]]:
    neighbors: set[tuple[int, int]] = set()
    for col in range(start, end):
        neighbors = neighbors | neighboring_coordinates((row, col), line_length)

    return neighbors - set([(row, col) for col in range(start, end)])


def symbol_index(line: str) -> Iterator[tuple[str, int]]:
    for symbol_match in finditer(r"[^0-9\.]", line):
        yield symbol_match[0], symbol_match.start(0)


def number_match(line: str) -> Iterator[Match[str]]:
    yield from finditer(r"[0-9]+", line)


def number_neighbors_and_symbol_locations(
    fp: str,
) -> tuple[list[tuple[int, set[tuple[int, int]]]], dict[tuple[int, int], str]]:
    with open(fp) as file:
        line_length = len(next(iter(file)))

    number_neighbors: list[tuple[int, set[tuple[int, int]]]] = []
    symbol_locations: dict[tuple[int, int], str] = {}

    with open(fp) as file:
        for row, line in enumerate(file):
            line_cleaned = line.strip()
            for num_match in number_match(line_cleaned):
                number_neighbors.append(
                    (
                        int(num_match[0]),
                        neighbors_for_number(
                            num_match.start(0), num_match.end(0), row, line_length
                        ),
                    )
                )

            for sym_location in symbol_index(line_cleaned):
                symbol_locations[(row, sym_location[1])] = sym_location[0]

    return number_neighbors, symbol_locations


def sum_part_numbers(
    number_neighbors: list[tuple[int, set[tuple[int, int]]]],
    symbol_locations: dict[tuple[int, int], str],
) -> int:
    total = 0
    for num, neighbors in number_neighbors:
        for neigh in neighbors:
            if neigh in symbol_locations:
                total += num

    return total


def sum_gear_ratios(
    number_neighbors: list[tuple[int, set[tuple[int, int]]]],
    symbol_locations: dict[tuple[int, int], str],
) -> int:
    banned: set[tuple[int, int]] = set()
    ones: dict[tuple[int, int], int] = {}
    twos: dict[tuple[int, int], int] = {}
    for num, neighbors in number_neighbors:
        for neigh in neighbors:
            if (
                neigh in symbol_locations
                and symbol_locations[neigh] == "*"
                and neigh not in banned
            ):
                if neigh in twos:
                    twos.pop(neigh)
                    banned.add(neigh)
                elif neigh in ones:
                    curr = ones.pop(neigh)
                    twos[neigh] = curr * num
                else:
                    ones[neigh] = num

    return sum(twos.values())


def main() -> None:
    fp = "aoc_2023/inputs/day_3.txt"
    number_neighbors, symbol_locations = number_neighbors_and_symbol_locations(fp)
    print(sum_part_numbers(number_neighbors, symbol_locations))
    print(sum_gear_ratios(number_neighbors, symbol_locations))


if __name__ == "__main__":
    main()
