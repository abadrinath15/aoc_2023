from __future__ import annotations
import pandas


def extrapolate_history(history: "pandas.Series[float]") -> int:
    reduced_histories: "list[pandas.Series[float]]" = [history]
    while (history.dropna() != 0).any():
        history = history.diff()
        reduced_histories.append(history)

    return int(sum(x.iat[-1] for x in reduced_histories))


def sum_extrapolated_histories(fp: str) -> int:
    total = 0
    with open(fp) as file:
        for line in file:
            history_str = line.split()
            history = pandas.Series(history_str).astype("float")
            total += extrapolate_history(history)

    return total


def main() -> None:
    print(sum_extrapolated_histories("aoc_2023/inputs/day_9.txt"))


if __name__ == "__main__":
    main()
