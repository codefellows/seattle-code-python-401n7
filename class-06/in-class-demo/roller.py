import random


def dice_roller(n):
    """
    Rolls n dice.
    :param n: Number of dice
    :return: Tuple of n integers, each integer being between 1 - 6 inclusive
    """
    # One-liner with tuple comprehension
    # return tuple(random.randint(1, 6) for _ in range(n))

    dice = []
    for i in range(n):
        dice.append(random.randint(1, 6))
    return tuple(dice)


if __name__ == "__main__":
    print(dice_roller(6))
