class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

mydog = Dog()
