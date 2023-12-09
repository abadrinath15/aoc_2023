import collections
import typing
import functools


def hand_to_type(hand: str) -> typing.Literal[1, 2, 3, 4, 5, 6, 7]:
    counts = collections.Counter(hand)
    ordered_counts = counts.most_common()
    top = ordered_counts[0][1]
    match top:
        case 5:
            return 7

        case 4:
            return 6

        case 1:
            return 1

        case _:
            pass

    match ordered_counts[1][1]:
        case 2:
            return 5 if top == 3 else 3

        case 1:
            return 4 if top == 3 else 2

        case _:
            pass

    raise ValueError(f"Yikes, we couldn't score {hand=}")


def hand_type_lesser(hand_1: str, hand_2: str) -> bool:
    for card_1, card_2 in zip(hand_1, hand_2):
        if card_1 == card_2:
            continue

        if card_1.isdigit():
            if not card_2.isdigit():
                return True

            return int(card_1) < int(card_2)

        if card_2.isdigit():
            return False

        non_numbers = ["T", "J", "Q", "K", "A"]
        return non_numbers.index(card_1) < non_numbers.index(card_2)

    else:
        raise ValueError(
            f"Could not make a determination between {hand_1=} and {hand_2=}"
        )


def total_winnings(fp: str) -> int:
    type_dicts: dict[int, list[tuple[str, int]]] = {x: list() for x in range(1, 8)}
    with open(fp) as file:
        for line in file:
            hand, bid_str = line.split()
            hand_type = hand_to_type(hand)
            type_dicts[hand_type].append((hand, int(bid_str)))

    for lt in type_dicts.values():
        lt.sort(
            key=functools.cmp_to_key(
                lambda x, y: -1 if hand_type_lesser(x[0], y[0]) else 1
            )
        )

    total = 0
    counter = 1
    for v in type_dicts.values():
        for v_1 in v:
            total += counter * v_1[1]
            counter += 1

    return total


def main(fp: str) -> None:
    print(total_winnings(fp))


if __name__ == "__main__":
    main("aoc_2023/inputs/day_7.txt")
