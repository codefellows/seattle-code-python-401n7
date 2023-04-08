from random import randint


# The actual random rolling function
def default_roller():
    """
    Roll 2 randomly generated six-sided dice
    :return: a tuple of 2 dice
    """
    return tuple([randint(1, 6), randint(1, 6)])


def play_dice(roller):
    """
    Simulates a dice rolling game
    :param roller: is a rolling function, that return a tuple of dice rolls
    :return: None
    """
    while True:
        print("Enter (r) to roll or (q) to quit")
        choice = input("> ")

        if choice == "q":
            break

        else:
            roll = roller()
            print(roll)


# step? create a mock roller function!


if __name__ == "__main__":
    rolls = [(5, 6), (6, 1)]

    def mock_roller():
        """
        Returns 2 pre-determined 6 sided dice
        :return: a tuple of 2 dice
        """
        if rolls:
            return rolls.pop(0)
        else:
            return default_roller()

    play_dice(mock_roller)
