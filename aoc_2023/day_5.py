from re import match as re_match
from typing import Iterable
from dataclasses import dataclass


def parse_seeds(line: str) -> list[int]:
    if (seed_match := re_match(r"seeds: ([0-9 ]+)", line)) is None:
        raise ValueError("Parsing seeds failed. Whoops.")

    return [int(x) for x in seed_match[1].split()]


def parse_map_line(line: str) -> tuple[tuple[int, int], int]:
    dest_left, source_left, length = map(int, line.strip().split(" "))
    return (source_left, source_left + length - 1), dest_left


@dataclass
class SourceDestMap:
    source_endpoints: list[tuple[int, int]]
    dest_left: list[int]


def parse_map(file: Iterable[str]) -> SourceDestMap:
    file_iter = iter(file)
    next(file_iter)
    sd_map = SourceDestMap([], [])
    for line in file_iter:
        if (cleaned_line := line.strip()) == "":
            return sd_map

        source_endpoints, dest_left = parse_map_line(cleaned_line)
        sd_map.source_endpoints.append(source_endpoints)
        sd_map.dest_left.append(dest_left)

    return sd_map


def pass_through_map(sources: list[list[int]], sd_map: SourceDestMap) -> None:
    for source in sources:
        curr = source[-1]
        for index, source_endpoint in enumerate(sd_map.source_endpoints):
            if curr >= (left := source_endpoint[0]) and curr <= source_endpoint[1]:
                source.append(curr - left + sd_map.dest_left[index])
                break

        else:
            source.append(curr)


def lowest_location(fp: str) -> int:
    with open(fp) as file:
        file_iter = iter(file)
        seeds = parse_seeds(next(file_iter))
        sources = [[seed] for seed in seeds]
        maps: list[SourceDestMap] = []
        next(file_iter)
        while True:
            try:
                sd_map = parse_map(file_iter)

            except StopIteration:
                return min(source[-1] for source in sources)

            maps.append(sd_map)
            pass_through_map(sources, sd_map)


def main() -> None:
    print(lowest_location("aoc_2023/inputs/day_5.txt"))


if __name__ == "__main__":
    main()
