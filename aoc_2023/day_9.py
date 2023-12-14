from __future__ import annotations
import pandas
import typing
import functools


def extrapolate_history(history: "pandas.Series[float]") -> int:
    reduced_histories: "list[pandas.Series[float]]" = [history]
    while (history.dropna() != 0).any():
        history = history.diff()
        reduced_histories.append(history)

    return int(sum(x.iat[-1] for x in reduced_histories))


def extrapolate_history_front(history: "pandas.Series[float]") -> int:
    reduced_histories: "list[pandas.Series[float]]" = [history]
    while (history != 0).any():
        history = history.diff().dropna()
        reduced_histories.append(history)

    return int(
        functools.reduce(lambda x, y: y - x, (x.iat[0] for x in reduced_histories))
    )


def sum_extrapolated_histories(
    fp: str, extrapolation_function: typing.Callable[["pandas.Series[float]"], int]
) -> int:
    total = 0
    with open(fp) as file:
        for line in file:
            history_str = line.split()
            history = pandas.Series(history_str).astype("float")
            total += extrapolation_function(history)

    return total


def main() -> None:
    fp = "aoc_2023/inputs/day_9.txt"
    print(sum_extrapolated_histories(fp, extrapolate_history))
    print(sum_extrapolated_histories(fp, extrapolate_history_front))


if __name__ == "__main__":
    main()
