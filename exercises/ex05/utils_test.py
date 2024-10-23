"""Testing utility functions"""

__author__ = 730765850

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens1() -> None:
    """Use case of a string of numbers mixed with even and odd"""
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_only_evens2() -> None:
    """Use case of numbers that are purely odd"""
    assert (
        only_evens(
            [
                1,
                3,
                5,
            ]
        )
        == []
    )


def test_only_evens3() -> None:
    """Edge case of negative numbers"""
    assert only_evens([-2, -4, -6]) == [-2, -4, -6]


def test_sub1() -> None:
    """Use case of a strong of numbers with 'normal' index start/stop"""
    assert sub([1, 2, 3, 4], 0, 3) == [1, 2, 3]


def test_sub2() -> None:
    """Edge case of start index starting at negative value"""
    assert sub([1, 2, 3, 4], -1, 3) == [1, 2, 3]


def test_sub3() -> None:
    """Edge case of empty string input"""
    assert sub([], 0, 3) == []


def test_add_at_index1() -> None:
    """initially tried asserting that it would return the mutated list but forgot
    the return type for add_at_index is None. had to get creative to check it
    this is use case"""
    inpt_list = [1, 2, 4, 5]
    add_at_index(inpt_list, 3, 2)
    assert inpt_list == [1, 2, 3, 4, 5]


def test_add_at_index2() -> None:
    """A use case test that seeks to insert a number into an empty list"""
    inpt_list = []
    add_at_index(inpt_list, 1, 0)
    assert inpt_list == [1]


def test_add_at_index3() -> None:
    """Tests that the function raises an IndexError for an index out of bounds"""
    import pytest

    inpt_list = [1, 2, 3, 4]
    with pytest.raises(IndexError):
        add_at_index(inpt_list, 0, 5)
