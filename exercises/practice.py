ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

ice_cream["mint"] = 3
ice_cream["vanilla"] = 10

ice_cream.pop("mint")

for i in ice_cream:
    """print(f"{key} has {ice_cream[key]} orders.")"""
    print(str(i) + " has " + str(ice_cream[i]) + " orders.")
