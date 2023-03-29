# Classes start with a capital letter
# Singular
class Dog:
    # this gets invoked every time a new object is created
    # initialize the instance's attributes
    def __init__(self, name="unknown"):
        self.name = name
        self.age = 5
        self.color = "brown"
        self.cute = True


# sub class!
class 


if __name__ == "__main__":
    # create an instance of a Dog:
    brock = Dog("Brock")
    print(brock.name)
    kai = Dog()
    print(kai.cute)
    print(kai.name)
