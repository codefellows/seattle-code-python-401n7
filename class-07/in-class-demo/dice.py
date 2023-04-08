from random import randint


def default_roller():
    """
    Roll 2 six-sided dice
    :return: a tuple of 2 dice
    """
    return tuple([randint(1, 6), randint(1, 6)])


print(default_roller())



