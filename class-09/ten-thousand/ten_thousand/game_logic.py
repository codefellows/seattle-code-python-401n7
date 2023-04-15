from collections import Counter
import random


class GameLogic:
    def __init__(self, mock_rolls=None):
        """
        Initialize an instance of the GameLogic class for testing. Accepts optional argument of a list of mock rolls.
        :param mock_rolls: List of tuples, each tuple is a list of integers representing a mocked roll.
        """
        self.mock_rolls = mock_rolls

    def mock_roller(self, _):
        return self.mock_rolls.pop(0)

    @staticmethod
    def roll_dice(n):
        """
        Rolls n 6-sided dice.
        :param n: Number of dice.
        :return: Tuple of dice rolls.
        """
        rolls = tuple(random.randint(1, 6) for _ in range(n))
        return rolls

    @staticmethod
    def is_cheating(roll, keepers): # (1, 2, 1, 3, 3, 4)  (1, 1, 1)
        """
        Returns True if user is cheating!
        :param roll: Tuple of integers, representing the dice roll
        :param keepers: Tuple of integers, representing dice the user is keeping
        :return: Boolean! True if the user is trying to cheat. False if not cheating.
        """
        return bool(Counter(keepers) - Counter(roll))
        pass

    @staticmethod
    def calculate_score(roll):
        """
        Scores a give roll according to the rules of Ten Thousand.
        :param roll: A tuple of integers representing dice values.
        :return: An integer representing the score.
        """
        roll = Counter(roll)
        score = 0

        # Check for straight
        if len(roll) == 6:
            return 1500

        # Check for 3 pair
        if len(roll) == 3 and roll.most_common()[0][1] == 2:
            return 1500

        # 3 or more of any number
        for i in range(1, 7):
            quantity = roll[i]
            if quantity >= 3:
                if i == 1:
                    score += (quantity - 2) * 1000
                else:
                    score += (quantity - 2) * i * 100

        # 1s and 5s
        score += 100 if roll[1] == 1 else 0
        score += 200 if roll[1] == 2 else 0
        score += 50 if roll[5] == 1 else 0
        score += 100 if roll[5] == 2 else 0

        return score

    @staticmethod
    def get_scorers(dice):
        # version_3

        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        # for i in range(len(dice)):

        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1:]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(val)

        return tuple(scorers)
