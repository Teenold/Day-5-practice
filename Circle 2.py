class MyCirc():
    pi = 3.142

    def __init__(self,radius):
        self.radius = radius
    def circum(self):
        return (self.radius*2*MyCirc.pi)
    def area(self):
        return ((self.radius**2) *MyCirc.pi)
    
print("WELCOME")
choice =" "
while choice not in ["1","2"]:
    choice = input("Enter 1 to calculate area or 2 to calculate Circumference: ")

if choice==1:
    rad = int(input("Enter the radius: "))
    circ = MyCirc(rad)
    areaOfCirc = circ.area()
    print(f"The area of the circle is: {areaOfCirc}")

else:
    rad = int(input("Enter the radius: "))
    circ = MyCirc(rad)
    circumOfCirc = circ.circum()
    print(f"The area of the circle is: {circumOfCirc}")
    



