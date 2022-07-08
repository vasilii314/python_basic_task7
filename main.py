class Animal:
    numInstances = 0

    def __init__(self):
        Animal.numInstances = Animal.numInstances + 1

    @staticmethod
    def print_num_instances():
        print(Animal.numInstances)

    def voice(self):
        pass


class Cat(Animal):

    def __init__(self):
        super().__init__()

    def voice(self):
        print("Meow-meow")


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def voice(self):
        print("Woof-woof")


class Bird(Animal):
    def __init__(self):
        super().__init__()

    def voice(self):
        print("Tweet-tweet")


[animal.voice() for animal in [Cat(), Dog(), Bird()]]

Animal.print_num_instances()
