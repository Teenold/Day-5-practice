class Gadget():
    def __init__ (self):
        print("GADGET")

    def gadget(self):
        print("This is a gadget")

class Phone(Gadget):
    def __init__(self):
        Gadget.__init__(self)
       # print("Phone Created")

    def color(self):
        print("Color is red")

    def version(self):
        print("Version 4.15")

myPhone = Phone()
myPhone
myPhone.color()
myPhone.version()