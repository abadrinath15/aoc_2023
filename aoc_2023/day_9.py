from __future__ import annotations
import pandas


def extrapolate_history(history: pandas.Series["float"]) -> int:
    reduced_histories: "list[pandas.Series[float]]" = [history]
    while (history.dropna() != 0.0).any():
        history = history.diff()
        reduced_histories.append(history)

    return sum(x.iat[-1] for x in reduced_histories)
