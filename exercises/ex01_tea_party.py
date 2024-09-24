"""calculates the amount of teabags, treats, and  cost for a tea party based on input"""

__author__: str = "730765850"


def main_planner(guests: int) -> None:
    """the entry point of the program; glues it all together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """returns the amount of teabags needed"""
    return people * 2


def treats(people: int) -> int:
    """returns the amount of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """returns the combined total cost of the tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
