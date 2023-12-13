from collections import abc
import re
import itertools


def map_from_str(lines: abc.Iterable[str]) -> dict[str, tuple[str, str]]:
    node_map: dict[str, tuple[str, str]] = {}
    for line in lines:
        if (
            node_data := re.match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", line.strip())
        ) is None:
            raise ValueError(f"yikes, parsing {line=} failed")

        node_map[node_data[1]] = (node_data[2], node_data[3])

    return node_map


def num_steps(node_map: dict[str, tuple[str, str]], instructions: str) -> int:
    steps = 0
    curr = "AAA"
    for instruction in itertools.cycle(instructions):
        steps += 1
        left, right = node_map[curr]
        curr = left if instruction == "L" else right
        if curr == "ZZZ":
            return steps

    raise ValueError("somehow the loop terminated?")


def num_steps_from_file(fp: str) -> int:
    with open(fp) as file:
        file_iter = iter(file)
        instructions = next(file_iter).strip()
        next(file_iter)
        node_map = map_from_str(file_iter)
        return num_steps(node_map, instructions)


def main() -> None:
    fp = "aoc_2023/inputs/day_8.txt"
    print(num_steps_from_file(fp))


if __name__ == "__main__":
    main()
