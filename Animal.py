class Animal():

    def __init__(self):
        print("ANIMAL")
    
    def whatAnimal(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

mydog = Dog()
mydog.eat()
mydog.whatAnimal()
