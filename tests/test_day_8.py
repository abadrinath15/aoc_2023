from aoc_2023 import day_8
import pytest


@pytest.fixture
def exp_map(request: pytest.FixtureRequest) -> dict[str, tuple[str, str]]:
    if request.param == "b":
        return {"AAA": ("BBB", "BBB"), "BBB": ("AAA", "ZZZ"), "ZZZ": ("ZZZ", "ZZZ")}

    return {
        "AAA": ("BBB", "CCC"),
        "BBB": ("DDD", "EEE"),
        "CCC": ("ZZZ", "GGG"),
        "DDD": ("DDD", "DDD"),
        "EEE": ("EEE", "EEE"),
        "GGG": ("GGG", "GGG"),
        "ZZZ": ("ZZZ", "ZZZ"),
    }


@pytest.mark.parametrize(
    ["map_str", "exp_map"],
    [
        (
            "AAA = (BBB, CCC)\nBBB = (DDD, EEE)\nCCC = (ZZZ, GGG)\nDDD = (DDD, DDD)\nEEE = (EEE, EEE)\nGGG = (GGG, GGG)\nZZZ = (ZZZ, ZZZ)".split(
                "\n"
            ),
            "a",
        ),
        ("AAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)".split("\n"), "b"),
    ],
    indirect=["exp_map"],
)
def test_map_from_str(map_str: str, exp_map: dict[str, tuple[str, str]]) -> None:
    res = day_8.map_from_str(map_str)
    assert exp_map == res


@pytest.mark.parametrize(
    ["exp_map", "instructions", "exp"],
    [("a", "RL", 2), ("b", "LLR", 6)],
    indirect=["exp_map"],
)
def test_num_steps(
    exp_map: dict[str, tuple[str, str]], instructions: str, exp: int
) -> None:
    res = day_8.num_steps(exp_map, instructions, "AAA", day_8.standard_end)
    assert res == exp


@pytest.mark.parametrize(
    ["fp", "exp"],
    [("aoc_2023/examples/day_8a.txt", 2), ("aoc_2023/examples/day_8b.txt", 6)],
)
def test_num_steps_from_file(fp: str, exp: int) -> None:
    res = day_8.num_steps_from_file(fp)
    assert res == exp


def test_num_steps_from_file_ghost() -> None:
    res = day_8.num_steps_from_file_ghost("aoc_2023/examples/day_8c.txt")
    assert res == 6
