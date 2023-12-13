from collections import abc
import re
import itertools
import functools
import math
import typing


def map_from_str(lines: abc.Iterable[str]) -> dict[str, tuple[str, str]]:
    node_map: dict[str, tuple[str, str]] = {}
    for line in lines:
        if (
            node_data := re.match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", line.strip())
        ) is None:
            raise ValueError(f"yikes, parsing {line=} failed")

        node_map[node_data[1]] = (node_data[2], node_data[3])

    return node_map


def map_from_str_aas(
    lines: abc.Iterable[str],
) -> tuple[dict[str, tuple[str, str]], list[str]]:
    node_map: dict[str, tuple[str, str]] = {}
    aaas: list[str] = []
    for line in lines:
        if (
            node_data := re.match(
                r"([1-9 A-Z]+) = \(([1-9 A-Z]+), ([1-9 A-Z]+)\)", line.strip()
            )
        ) is None:
            raise ValueError(f"yikes, parsing {line=} failed")

        node_map[node_data[1]] = (node_data[2], node_data[3])
        if node_data[1].endswith("A"):
            aaas.append(node_data[1])

    return node_map, aaas


def num_steps(
    node_map: dict[str, tuple[str, str]],
    instructions: str,
    curr: str,
    end_condition: typing.Callable[[str], bool],
) -> int:
    steps = 0
    for instruction in itertools.cycle(instructions):
        steps += 1
        left, right = node_map[curr]
        curr = left if instruction == "L" else right
        if end_condition(curr):
            return steps

    raise ValueError("somehow the loop terminated?")


def num_steps_ghosty(
    node_map: dict[str, tuple[str, str]], instructions: str, a_enders: list[str]
) -> int:
    return functools.reduce(
        math.lcm,
        (num_steps(node_map, instructions, start, ghosty_end) for start in a_enders),
    )


def standard_end(curr: str) -> bool:
    return curr == "ZZZ"


def ghosty_end(curr: str) -> bool:
    return curr.endswith("Z")


def num_steps_from_file(fp: str) -> int:
    with open(fp) as file:
        file_iter = iter(file)
        instructions = next(file_iter).strip()
        next(file_iter)
        node_map = map_from_str(file_iter)
        return num_steps(node_map, instructions, "AAA", standard_end)


def num_steps_from_file_ghost(fp: str) -> int:
    with open(fp) as file:
        file_iter = iter(file)
        instructions = next(file_iter).strip()
        next(file_iter)
        node_map, aaas = map_from_str_aas(file_iter)
        return num_steps_ghosty(node_map, instructions, aaas)


def main() -> None:
    fp = "aoc_2023/inputs/day_8.txt"
    print(num_steps_from_file(fp))
    print(num_steps_from_file_ghost(fp))


if __name__ == "__main__":
    main()
