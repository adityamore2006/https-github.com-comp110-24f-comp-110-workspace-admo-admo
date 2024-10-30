"""programs that use dictionaries"""

__author__ = 730765850


def invert(inpt: dict[str, str]) -> dict[str, str]:
    new_vals: list[str] = []
    new_keys: list[str] = []
    new_dict: dict[str, str] = {}
    for key in inpt:
        new_vals.append(key)
        new_keys.append(inpt[key])
        # had a seperate for loop for the append new_key
        # changed it
    for i in range(len(new_vals)):
        new_dict[new_keys[i]] = new_vals[i]
    for i in range(len(new_keys)):
        for j in range(i + 1, len(new_keys)):
            if new_keys[i] == new_keys[j]:
                raise KeyError("cannot have keys with same value")
            # initially had an else statement that returned new_dict. but that doesnt
            # allow
            # us to assign a return type. I had to put it out the for loop for it to
            #  work
    return new_dict


def favorite_color(inpt: dict[str, str]) -> str:
    max: int = 0
    color: str = ""
    for i in inpt:
        count: int = 0
        for j in inpt:
            if inpt[i] == inpt[j]:
                # initially tried to increment j by 1 comapred to i but
                # it needs to start at the same index to count that indexes color also
                count += 1
        if max < count:
            max = count
            color = inpt[i]
    return color


# i struggled a lot with this one comapred to the last one. the comparison of max and
# count is def something ill keep in mind for the future.


def count(inpt: list[str]) -> dict[str, int]:

    final: dict[str, int] = {}
    for i in inpt:
        if i in final:
            final[i] += 1
        else:
            final[i] = 1
    return final


def alphabetizer(inpt: list[str]) -> dict[str, list[str]]:
    for i in range(len(inpt)):
        inpt[i] = inpt[i].lower()

    final: dict[str, list[str]] = {}
    for i in inpt:
        # w hole string ex. cat
        letter: str = i[0]
        # down to first letter ex. c
        alike_words: list[str] = []
        for j in inpt:
            # whole string ex. cat
            if letter == j[0]:
                # if whole word (cat) == letter (c)
                alike_words.append(j)
                # initially had j be x but that resulted in a list of characters, not
                # words
        final[letter] = alike_words

    return final


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    if day in attendance_log:
        if student not in attendance_log[day]:
            # had to include this if statment to ensure a student wasn't logged
            # mulitple times
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]


attendance_log = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
