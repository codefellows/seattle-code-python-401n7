from builtins import print


# save a reference to 'old print'
old_print = print

# old_print("hello world")


# This function will overwrite print
def new_print(name):
    old_print("Hello " + name)
    return "Hello " + name


print = new_print

print("Adam")
print("Hello world")


assert print("Adam") == "Hello Adam"


print = old_print
print("test")
