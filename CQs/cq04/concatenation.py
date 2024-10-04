"""a program that deals with concatenating strings"""

__author__ = "730765850"


def concat(a: str, b: str) -> str:
    return str(a) + str(b)


word1 = "happy"
word2 = "tuesday"

if __name__ == "__main__":
    print(concat(a=word1, b=word2))
    # At first I put the variabes under the IF statment instead of calling of concat
