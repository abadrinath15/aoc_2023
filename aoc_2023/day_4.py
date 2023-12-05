from re import search


def winners_yours_from_line(line: str) -> tuple[int, set[int], list[int]]:
    if (match_res := search(r"(\d+): ([0-9 ]+) \| ([0-9 ]+)", line)) is not None:
        card_number = int(match_res[1])
        winners = set(int(x) for x in match_res[2].split())
        yours = [int(x) for x in match_res[3].split()]

        return card_number, winners, yours

    raise ValueError(f"The regex didn't match. Whoops. {line=} ")


def score_card(winners: set[int], yours: list[int], are_elves_stupid: bool) -> int:
    total = 0
    any_found = False
    for num in yours:
        if num in winners:
            if any_found:
                total = total * 2 if not are_elves_stupid else total + 1
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
            total += score_card(winners, yours, False)

    return total


def score_scratch_correct_rules(fp: str) -> int:
    score_map: dict[int, int] = {}
    with open(fp) as file:
        for line in file:
            line_cleaned = line.strip()
            game_num, winners, yours = winners_yours_from_line(line_cleaned)
            score_map[game_num] = score_card(winners, yours, True)

    scores = [1] * len(score_map)
    num_games = len(score_map)
    for i in range(num_games, 0, -1):
        local_score = 1
        for j in range(i, i + score_map[i]):
            local_score += scores[j]

        scores[i - 1] = local_score

    return sum(scores)


def main() -> None:
    fp = "aoc_2023/inputs/day_4.txt"
    print(sum_card_scores(fp))
    print(score_scratch_correct_rules(fp))


if __name__ == "__main__":
    main()
