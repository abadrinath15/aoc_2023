from typing import Callable


def calibration_value(line: str) -> int:
    for first in line:
        if first.isdigit():
            break

    else:
        raise ValueError

    for second in line[::-1]:
        if second.isdigit():
            break

    else:
        raise ValueError

    return 10 * int(first) + int(second)


def sum_calibration_values(fp: str, func: Callable[[str], int]) -> int:
    with open(fp) as file:
        return sum(map(func, file))


def mixed_calibration_value(line: str) -> int:
    word_numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    string_numbers = dict(
        zip(
            word_numbers + [str(x) for x in range(1, 10)],
            list(range(1, 10)) * 2,
        )
    )
    left_str = right_str = ""
    left = right = -1
    for num in string_numbers:
        new_left, new_right = line.find(num), line.rfind(num)
        if left == -1 or (new_left != -1 and new_left < left):
            left, left_str = new_left, num

        if right == -1 or (new_right != -1 and new_right > right):
            right, right_str = new_right, num

    return 10 * string_numbers[left_str] + string_numbers[right_str]


def main() -> None:
    fp1 = "aoc_2023/inputs/day_1.txt"
    print(sum_calibration_values(fp1, calibration_value))
    print(sum_calibration_values(fp1, mixed_calibration_value))


if __name__ == "__main__":
    main()
