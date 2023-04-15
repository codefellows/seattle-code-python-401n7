from ten_thousand.game_logic import GameLogic


def play(roller=GameLogic.roll_dice):
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    welcome = input("> ")
    if welcome == "n":
        print("OK. Maybe another time")
        return

    total_score = 0

    # Do 20 rounds
    for round_number in range(1, 21):
        result = do_round(round_number, roller)
        if result == "q":
            break  # exits for loop
        total_score += result
        print(f"You banked {result} points in round {round_number}\nTotal score is {total_score} points")
    print(f"Thanks for playing. You earned {total_score} points")


def do_round(round_number, roller):
    print(f"Starting round {round_number}")
    dice_remaining = 6
    unbanked_points = 0
    while dice_remaining:
        roll = roller(dice_remaining)
        print(f"Rolling {dice_remaining} dice...")
        print_dice(roll)
        # do zilch!
        if GameLogic.calculate_score(roll) == 0:
            do_zilch()
            return 0
        keepers = do_keepers(roll)  # new argument/param
        if keepers == "q":
            return "q"
        unbanked_points += GameLogic.calculate_score(keepers)
        dice_remaining -= len(keepers)
        # do hot dice!
        if dice_remaining == 0:
            dice_remaining = 6
        rbq = do_rbq(unbanked_points, dice_remaining)
        if rbq == "b":
            return unbanked_points
        if rbq == "q":
            return "q"


def do_rbq(unbanked_points, dice_remaining):
    print(f"You have {unbanked_points} unbanked points and {dice_remaining} dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    rbq = input("> ")
    return rbq


def print_dice(dice):
    # print("***", *dice, "***")
    print(f"*** {' '.join([str(i) for i in dice])} ***")


def do_keepers(roll):
    """Asks user if they want to keep dice, or quit, validates input. Returns choice"""
    while True:
        print("Enter dice to keep, or (q)uit:")
        keepers = input("> ")
        if keepers == "q":
            return "q"

        # turn the keepers string into a tuple of ints
        keepers = tuple(int(num) for num in keepers if num.isnumeric())

        # verify the keepers! are the cheating?
        cheating = GameLogic.is_cheating(roll, keepers)
        if not cheating:
            # let them leave the while loop
            break

        print("Cheater!!! Or possibly made a typo...")
        print_dice(roll)
    return keepers


def do_zilch():
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")


if __name__ == "__main__":
    test_straight = GameLogic([(1, 2, 3, 4, 5, 4)])
    # play(test_straight.mock_roller)
    play()
