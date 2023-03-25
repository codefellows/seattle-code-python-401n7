try:
    print(3 / 0)
except ZeroDivisionError:
    print("you can't do that")


try:
    "a" + 1
except TypeError:
    print("Incompatible types.")


my_list = [1, 2, 3, 4, 5]
try:
    print(my_list[7])
except IndexError:
    print("that index doesn't exist!")


# Custom error handling
class InsufficientFundsError(Exception):
    pass


def withdraw(account_balance, amount):
    if amount > account_balance:
        raise InsufficientFundsError("Insufficient funds.")
    return account_balance - amount


try:
    new_balance = withdraw(1, 20)
except InsufficientFundsError as e:
    print(e)
    print("other logic can also go here")
