try:
    print(3 / 0)
except ZeroDivisionError:
    print("you can't do that")


try:
    "a" + 1
except TypeError:
    print("Incompatible types.")


my_list = [1, 2, 3, 4, 5]
print(my_list[7])
