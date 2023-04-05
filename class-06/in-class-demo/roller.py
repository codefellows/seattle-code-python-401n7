import random

def dice_roller(n):
    """
    Rolls n dice.
    :param n: Number of dice
    :return: Tuple of n integers, each integer being between 1 - 6 inclusive
    """
    return tuple(random.randint(1, 6) for _ in range(n))

if __name__ == "__main__":
    print(dice_roller(6))

