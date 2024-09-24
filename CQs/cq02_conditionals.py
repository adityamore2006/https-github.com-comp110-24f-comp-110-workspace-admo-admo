"""Guess a number game!"""

__author__ = "730765850"


def guess_a_number() -> None:
    secret: int = 7
    gNumber: int = int(input("Guess a number: "))
    print("Your guess was " + str(gNumber))

    if gNumber == secret:
        print("You got it!")

    elif gNumber > secret:
        print("Your guess was too high! The secret number is " + str(secret))

    else:
        print("Your guess was too low! The secret number is " + str(secret))

    return None


if __name__ == "__main__":
    guess_a_number()
