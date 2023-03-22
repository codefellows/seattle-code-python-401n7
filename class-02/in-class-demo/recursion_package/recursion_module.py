def factorial(n):
    """
    Return n! representing the factorial
    :param n: the number to get the factorial of
    :return: n! aka n factorial
    """
    # base case
    if n == 1:
        return 1

    # recursive case
    return n * factorial(n - 1)

