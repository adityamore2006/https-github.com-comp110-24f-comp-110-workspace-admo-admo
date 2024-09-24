"""Find how many of a letter"""

__author__ = "730765850"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    """the amount of the chosen letter stored in count"""
    track: int = 0
    """stores what index we are at in the word for searching"""
    while track < len(phrase):
        """used for iterating through the word"""
        if phrase[track] == search_char:
            count += 1
        track += 1

    return count


print(num_instances(phrase="hello", search_char="e"))
