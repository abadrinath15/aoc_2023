from re import match as re_match


def winners_yours_from_line(line: str) -> tuple[int, set[int], list[int]]:
    if (match_res := re_match(r"Card (\d+): ([0-9 ]+) \| ([0-9 ]+)", line)) is not None:
        card_number = int(match_res[1])
        winners = set(int(x) for x in match_res[2].split())
        yours = [int(x) for x in match_res[3].split()]

        return card_number, winners, yours

    raise ValueError(f"The regex didn't match. Whoops. {line=} ")


def score_card(winners: set[int], yours: list[int]) -> int:
    total = 0
    any_found = False
    for num in yours:
        if num in winners:
            if any_found:
                total *= 2
            else:
                any_found = True
                total = 1

    return total


def sum_card_scores(fp: str) -> int:
    total = 0
    with open(fp) as file:
        for line in file:
            line_cleaned = line.strip()
            _, winners, yours = winners_yours_from_line(line_cleaned)
            total += score_card(winners, yours)

    return total


def main() -> None:
    fp = "aoc_2023/inputs/day_4.txt"
    print(sum_card_scores(fp))


if __name__ == "__main__":
    main()
