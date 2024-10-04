"""a program that deals with matching coordinates of strings"""

__author__ = "730765850"


def get_coords(xs: str, ys: str) -> None:
    index_1: int = 0
    index_2: int = 0
    # the while loop in a while loop took some thinking to wrap my head around. neat trick for this situation I will remeber
    while index_1 < len(xs):
        index_2: int = 0
        while index_2 < len(ys):
            print(f"{xs[index_1],ys[index_2]}")
            index_2 += 1
        index_1 += 1  # forgot to increment by 1 so the loop never ended
