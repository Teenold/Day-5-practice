class Circle():

    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    
    def circumference(self):
        return self.radius * Circle.pi*2
    def area(self):
        return self.radius**2 * Circle.pi
    
    

myCirc = Circle(10)
circumOfCirc =myCirc.circumference()
areaOfCirc = myCirc.area()

print(circumOfCirc)
print(areaOfCirc)

with open("Circle 2.py", "w") as wf:
    wf.write("#")