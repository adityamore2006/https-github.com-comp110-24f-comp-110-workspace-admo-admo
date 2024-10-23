"""Creating Utility Funcitons!!!"""

__author__ = 730765850


def all(int_list: list[int], int_input: int) -> bool:
    """returns bool indicating if all the values in the list are the same as the given
    int"""
    if len(int_list) == 0:
        return False
    # short circuits the function and ends it, returning false if list is empty
    total: int = 0
    for i in int_list:
        if i == int_input:
            total += 1
            # Incremented to come to final conclusion
    if total == len(int_list):
        return True
    else:
        return False


def max(int_list: list[int]) -> int:
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    # if list is empty value error is raised
    else:
        num: int = int_list[0]
        # orignially set num to equal 0 but then edge cases get annoying
        # better if list is compared to first value in list
        for i in int_list:
            if i > num:
                num = i
        return num


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    value = 0
    if len(int_list1) != len(int_list2):
        return False
    for i in range(len(int_list1)):
        if int_list1[i] == int_list2[i]:
            value += 1
            # comapares first index of each list and increments if same.
    if value == len(int_list1) and value == len(int_list2):
        # if value is incremented the same amount of len lists
        # then the lists must be the same.
        # this also returns false if list lenghts arent same.
        return True
    else:
        return False


def extend(int_list1: list[int], int_list2: list[int]) -> None:
    for i in range(len(int_list2)):
        # forgot about the append function for a hot sec.
        int_list1.append(int_list2[i])
