""" A small step toward Wordle."""

__author__ = "730765850"


def input_word() -> str:
    chosen_wrd: str = input("Enter a 5-character word: ")
    if len(chosen_wrd) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    print("'" + str(chosen_wrd) + "'")
    return chosen_wrd


def input_letter() -> str:
    chosen_ltr: str = input("Enter a single character: ")
    if len(chosen_ltr) != 1:
        print("Error: Character must be a single character.")
        exit()
    print("'" + str(chosen_ltr) + "'")
    return chosen_ltr


def contains_char(word: str, letter: str) -> None:
    print("Enter a 5-character word: " + str(word))
    print("Enter a single character: " + str(letter))
    if len(letter) != 1:
        print("Error: Character must be a single character")
    print("Searching for " + str(letter) + " in " + str(word))
    count: int = 0
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
    print(str(count) + " instances of " + str(letter) + " found in " + str(word))


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


main()

if __name__ == "__main__":
    main()
