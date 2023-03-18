"""
game.py is a demo of python's inputs and outputs
"""


def main():
    """
    This is an example docstring
    :return: no return
    """
    name = input("What is your name? ")
    # let's use an f string
    print(f"Hello {name}")
    menu = """**************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears"""
    print(menu)
    if name == "Adam":
        print("you are the instructor of 401n7.")
    elif name == "adam":
        print("you are the instructor of 401n7.")
    else:
        print("You are not the instructor!!")

    while name != "Adam":
        name = input("What is your name again? ")
    

if __name__ == "__main__":
    main()
