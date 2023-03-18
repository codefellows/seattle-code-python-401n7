"""
This is an example docstring
:return: no return
"""


def main():
    hello = "hi"
    name = input("What is your name?")
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


if __name__ == "__main__":
    main()
