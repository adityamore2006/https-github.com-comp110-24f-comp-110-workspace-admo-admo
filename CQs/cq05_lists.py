"""Mutating Functions"""

__author__ = "730765850"


def manual_append(original: list[int], appending: int) -> None:
    original.append(appending)
    return None


def double(original: list[int]) -> None:
    i = 0
    while i < len(original):
        original[i] = original[i] * 2
        i += 1
    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(original=list_2)
print(list_1)
print(list_2)

# predicted that both will print the same values since mutating is universal
