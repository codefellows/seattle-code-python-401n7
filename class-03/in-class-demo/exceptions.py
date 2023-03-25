try:
    print(3 / 0)
except ZeroDivisionError:
    print("you can't do that")


try:
    "a" + 1
except TypeError:
    print("Incompatible types.")


