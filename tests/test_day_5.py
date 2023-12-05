from aoc_2023 import day_5
from pytest import fixture


@fixture
def sd_map() -> day_5.SourceDestMap:
    return day_5.SourceDestMap([(98, 99), (50, 97)], [50, 52])


@fixture
def seeds() -> list[int]:
    return [79, 14, 55, 13]


def test_parse_seeds(seeds: list[int]) -> None:
    res = day_5.parse_seeds("seeds: 79 14 55 13")
    assert res == seeds


def test_parse_map_line() -> None:
    res = day_5.parse_map_line("50 98 2\n")
    assert res == ((98, 99), 50)


def test_parse_map(sd_map: day_5.SourceDestMap) -> None:
    res = day_5.parse_map(["seed-to-soil map:\n", "50 98 2\n", "52 50 48\n"])
    assert res == sd_map


def test_pass_through_map(seeds: list[int], sd_map: day_5.SourceDestMap) -> None:
    seeds_as_source = [[x] for x in seeds]
    day_5.pass_through_map(seeds_as_source, sd_map)
    assert seeds_as_source == [[79, 81], [14, 14], [55, 57], [13, 13]]


def test_lowest_location() -> None:
    res = day_5.lowest_location("aoc_2023/examples/day_5a.txt")
    assert res == 35
