from re import match as re_match
from typing import Iterable
from dataclasses import dataclass
from collections import deque
from itertools import batched


def parse_seeds(line: str) -> list[int]:
    if (seed_match := re_match(r"seeds: ([0-9 ]+)", line)) is None:
        raise ValueError("Parsing seeds failed. Whoops.")

    return [int(x) for x in seed_match[1].split()]


def parse_seeds_to_intervals(line: str) -> deque[tuple[int, int]]:
    if (seed_match := re_match(r"seeds: ([0-9 ]+)", line)) is None:
        raise ValueError("Parsing seeds failed. Whoops.")

    intervals: deque[tuple[int, int]] = deque()
    for left_end, len in batched((int(x) for x in seed_match[1].split()), n=2):
        intervals.append((left_end, left_end + len))

    return intervals


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


def pass_intervals_through(
    intervals: deque[tuple[int, int]], sd_map: SourceDestMap
) -> deque[tuple[int, int]]:
    new_intervals: deque[tuple[int, int]] = deque()
    while len(intervals) > 0:
        interval = intervals.popleft()
        for eps, dl in zip(sd_map.source_endpoints, sd_map.dest_left):
            # left and overlapping
            if interval[0] < eps[0] <= interval[1] and interval[1] <= eps[1]:
                left_only = interval[0], eps[0] - 1
                intervals.append(left_only)
                new_intervals.append((dl, dl + interval[1] - eps[0]))
                break

            # contained
            if interval[0] >= eps[0] and interval[1] <= eps[1]:
                dl_adjusted = dl + interval[0] - eps[0]
                new_intervals.append(
                    (dl_adjusted, dl_adjusted + interval[1] - interval[0])
                )
                break

            # overlapping and right
            if interval[0] <= eps[1] <= interval[1]:
                right_only = eps[1] + 1, interval[1]
                intervals.append(right_only)
                dl_adjusted = dl + interval[0] - eps[0]
                new_intervals.append((dl_adjusted, dl_adjusted + eps[1] - interval[0]))
                break

        else:
            # Non-overlapping
            new_intervals.append(interval)

    return new_intervals


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


def lowest_location_ranges(fp: str) -> int:
    with open(fp) as file:
        file_iter = iter(file)
        intervals = parse_seeds_to_intervals(next(file_iter))
        maps: list[SourceDestMap] = []
        next(file_iter)
        while True:
            try:
                sd_map = parse_map(file_iter)

            except StopIteration:
                return min(min(x) for x in intervals)

            maps.append(sd_map)
            intervals = pass_intervals_through(intervals, sd_map)


def main() -> None:
    print(lowest_location("aoc_2023/inputs/day_5.txt"))
    print(lowest_location_ranges("aoc_2023/inputs/day_5.txt"))


if __name__ == "__main__":
    main()
