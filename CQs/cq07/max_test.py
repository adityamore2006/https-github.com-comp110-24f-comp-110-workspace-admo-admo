"""Testing file for the find_max function"""

__author__ = "730765850"
from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    assert find_and_remove_max([1, 2, 3, 4, 5]) == 5


def test_mutate_find_and_remove_max() -> None:
    b: list[int] = [1, 2, 3, 4, 5, 4]
    find_and_remove_max(b)
    assert b == [1, 2, 3, 4]


def test_edge_find_and_remove_max() -> None:
    assert find_and_remove_max([]) == -1
