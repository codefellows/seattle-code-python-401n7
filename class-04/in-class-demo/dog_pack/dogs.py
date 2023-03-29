class Animal:
    pass


# Classes start with a capital letter
# Singular
class Dog(Animal):
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

    def __repr__(self):
        return f'Lab("{self.name}")'


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


class DogPack:
    """
    A class that represents a collection of Dog instances.
    Each instance of a DogPack is a list of Dog instances.
    """
    def __init__(self, dogs):
        self.dogs = dogs

    def __str__(self):
        dog_strings = [str(dog) for dog in self.dogs]
        return " ".join(dog_strings)


if __name__ == "__main__":
    # create an instance of a Dog:
    # brock = Dog("Brock")
    # print(brock.name)
    # kai = Dog()
    # print(kai.cute)
    # print(kai.name)
    # hachiko = Lab("Hachiko")
    # print(hachiko.name)
    # print(hachiko.cute)
    # hachiko.greet()
    yoshi = Collie("Yoshi")
    # yoshi.say_good_morning()
    print(yoshi)
    # print(str(yoshi))
    # print(repr(yoshi))

    midnight = Collie("Midnight")
    kenai = Collie("Kenai")
    kaya = Collie("Kaya")

    # My DogPack is a COLLECTION of dogs
    # vs. a baseclass/subclass relationship with Dog
    dog_pack_01 = DogPack([midnight, kenai, kaya])
    print(dog_pack_01)
