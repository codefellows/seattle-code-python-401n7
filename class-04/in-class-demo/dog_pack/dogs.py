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
class Lab(Dog):
    # An instance method!
    def greet(self):
        print(f"Hello I'm {self.name}")


class Collie(Dog):
    def say_good_morning(self):
        print(f"Good morning, my name is {self.name}")

    # user friendly string representation of an object
    # invoked with print() and str()
    def __str__(self):
        return f"I am a collie named {self.name}!"

    # developer friendly string representation of an object
    def __repr__(self):
        # return a string with how to reproduce the object
        return f'Collie("{self.name}")'


if __name__ == "__main__":
    # create an instance of a Dog:
    # brock = Dog("Brock")
    # print(brock.name)
    # kai = Dog()
    # print(kai.cute)
    # print(kai.name)
    hachiko = Lab("Hachiko")
    print(hachiko.name)
    print(hachiko.cute)
    hachiko.greet()
    yoshi = Collie("Yoshi")
    yoshi.say_good_morning()
    print(yoshi)
    print(str(yoshi))
    print(repr(yoshi))
