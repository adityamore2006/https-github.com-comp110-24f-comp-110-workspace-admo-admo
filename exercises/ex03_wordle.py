""" a program of our very own wordle!!!"""

__author__ = "730765850"


def input_guess(secret_word_len: int) -> str:
    """ensures the inputed string is the approriate length"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = str(input(f"That wasn't {secret_word_len} chars! Try again: "))
        # I LOVE FSTRINGS!!!
        # was stumped until realizing that the guess function would
        # need to be prompted to change inside the loop
    return guess


def contains_char(input_str: str, chr_searching_for: str) -> bool:
    """compares an input string of letters with a singular letter
    to see if theres any matching letters"""

    assert len(chr_searching_for) == 1
    count: int = 0
    # could be written more effiecently in hindsight... (while loop in the disguise of
    # a for loop)
    while input_str[count] != chr_searching_for:
        count += 1
        if count == len(input_str):
            return False
    return True


def emojified(str_guess: str, secret_wrd: str) -> str:
    """this function decides what color block should be labeled at each index
    to hint the user at where their guess lands them compared to the actual word"""
    assert len(str_guess) == len(secret_wrd)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_trail: str = ""
    index_iterate: int = 0
    while index_iterate < len(secret_wrd):
        # initially tried calling contains_char at a broader scope and using its value
        # like that. that didnt work so i called it in conditional instead
        if str_guess[index_iterate] == secret_wrd[index_iterate]:
            emoji_trail += GREEN_BOX
        elif contains_char(
            input_str=secret_wrd, chr_searching_for=str_guess[index_iterate]
        ):
            emoji_trail += YELLOW_BOX
        else:
            emoji_trail += WHITE_BOX
        index_iterate += 1
    return emoji_trail


def main(secret: str) -> None:
    """The entrypoint of the program and the main game loop."""
    index: int = 1

    while index <= 6:
        print(f"=== Turn {index}/6 ===")
        abstract: str = input_guess(secret_word_len=len(secret))
        print(emojified(str_guess=abstract, secret_wrd=secret))

        if abstract == secret:
            print(f"You won in {index}/6 turns!")
            index = 8
            # needs to be a number greater than 6 to terminate the program and say you
            # failed.

        index += 1

    if index == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
# main function wasnt working and I was so confused until i remembered i need these two
# lines haha
