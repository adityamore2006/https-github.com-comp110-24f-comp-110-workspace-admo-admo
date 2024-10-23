"""defining utility functions"""

__author__ = 730765850


def only_evens(inpt_list: list[int]) -> list[int]:
    even_list: list[int] = []
    for i in inpt_list:
        if i % 2 == 0:
            even_list.append(i)  # Append the element to even_list if it is even
    return even_list  # Return the list containing only even numbers


def sub(inpt_list: list[int], start: int, end: int) -> list[int]:
    sub_list: list[int] = []
    if start < 0:
        start = 0  # Ensure start index is not negative
    if end > len(inpt_list):
        end = len(inpt_list)
    if len(inpt_list) == 0 or start >= len(inpt_list) or end <= 0:
        return (
            []
        )  # Return empty list if input list is empty or indices are out of bounds
    for i in range(start, end):
        sub_list.append(
            inpt_list[i]
        )  # Append elements from start to end index to sub_list
    return sub_list


def add_at_index(inpt_list: list[int], int_elmt: int, idx: int) -> None:
    if idx > len(inpt_list) or idx < 0:
        raise IndexError("Index is out of bounds for the input list")
    inpt_list.append(int_elmt)
    count = len(inpt_list) - 1
    while count > idx:
        inpt_list[count] = inpt_list[count - 1]
        count -= 1
    inpt_list[idx] = int_elmt
    # this was very tricky, i tried a for loop and than a while loop that moved elements
    # to the end from the index value. it didnt work so i started moving elements to the
    # right starting at the end.
