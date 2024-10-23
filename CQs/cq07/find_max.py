"""Finds the max value in a list and removes all occurences"""

__author__ = "730765850"


def find_and_remove_max(given_list: list[int]) -> int:
    if len(given_list) == 0:
        return -1

    max: int = given_list[0]
    for i in given_list:
        if max < i:
            max = i

    i: int = 0
    while i < len(given_list):
        if max == given_list[i]:
            given_list.pop(i)
        else:
            i += 1
    # originally tried to do with for loop but after removing an index value
    # the iteration got messed up
    return max
