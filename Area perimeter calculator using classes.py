import math



class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (f"\n\tarea of circle is : {math.pi*self.radius*self.radius}")

class Rectangle:
    def __int__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def perimeter(self):
        return (f"\n\tPerimeter of ractangle is : {2*self.length + 2*self.breadth}")





S = Circle(int(input("Radius of circle: ")))

P = Rectangle()
P.length=int(input("Length of ractangle: "))
P.breadth=int(input("breadth of ractangle: "))
print( P.perimeter())
print(  S.area())