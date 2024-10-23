"""Summing the elements of a list using different loops"""

__author__ = 730765850


def w_sum(vals: list[float]) -> float:
    i = 0
    total = 0.0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total


def f_sum(vals: list[float]) -> float:
    total = 0.0
    for i in vals:
        total += i
    return total


def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total
