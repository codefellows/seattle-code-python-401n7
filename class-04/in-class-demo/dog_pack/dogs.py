# Classes start with a capital letter
# Singular
class Dog:
    # this gets invoked every time a new object is created
    # initialize the instance's attributes
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    # create an instance of a Dog:
    brock = Dog("Brock")
    print(brock.name)
    kai = Dog()
