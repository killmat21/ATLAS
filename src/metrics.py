def get_resistance():
    pass


def is_resistance(sticks):
    key = "high"
    if sticks.iloc[0][key] < sticks.iloc[1][key] < sticks.iloc[2][key] > sticks.iloc[3][key] > sticks.iloc[4][key]:
        return sticks.iloc[2][key]
    return -1


def get_support():
    pass


def is_support(sticks):
    key = "low"
    if sticks.iloc[0][key] > sticks.iloc[1][key] > sticks.iloc[2][key] < sticks.iloc[3][key] < sticks.iloc[4][key]:
        return sticks.iloc[2][key]
    return -1
