""" A small step toward Wordle."""

__author__ = "730765850"


def input_word() -> str:
    """defined a function to hold the 'word' part of the program."""
    chosen_wrd: str = input("Enter a 5-character word: ")
    if len(chosen_wrd) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
        """exits the program and ends it all if the word isnt 5 letters"""
    print("'" + str(chosen_wrd) + "'")
    return chosen_wrd


def input_letter() -> str:
    """defined a function to hold the 'letter' part of the program"""
    chosen_ltr: str = input("Enter a single character: ")
    if len(chosen_ltr) != 1:
        print("Error: Character must be a single character.")
        exit()
        """exits the program and ends it all if the character isn't 1 character"""
    print("'" + str(chosen_ltr) + "'")
    return chosen_ltr


def contains_char(word: str, letter: str) -> None:
    """defined a function that uses conditionals to determine wether a certian index of word matches the chosen letter"""
    print("Enter a 5-character word: " + str(word))
    print("Enter a single character: " + str(letter))
    print("Searching for " + str(letter) + " in " + str(word))
    count: int = 0
    """using a variaible that increments for every matching index to keep count of how many instances of the letter are found"""
    if letter == word[0]:
        print(letter + " found at index [0]")
        count += 1
    if letter == word[1]:
        print(letter + " found at index [1]")
        count += 1
    if letter == word[2]:
        print(letter + " found at index [2]")
        count += 1
    if letter == word[3]:
        print(letter + " found at index [3]")
        count += 1
    if letter == word[4]:
        print(letter + " found at index [4]")
        count += 1
    """using the conditionals above to compare every index to letter"""
    print(str(count) + " instances of " + str(letter) + " found in " + str(word))


def main() -> None:
    """defined a function that lumps all the code parts into a usable program"""
    contains_char(word=input_word(), letter=input_letter())


main()

if __name__ == "__main__":
    main()
