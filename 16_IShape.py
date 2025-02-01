from abc import ABC, abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area():
        pass
class Rectangle(IShape):
    def calculate_area(self,l,b):
        print(f'Area of rectangle is {l*b}')
class Circle(IShape):
    def calculate_area(self,s):
        print(f'Area of circle is {3.14*s*s}')
l=int(input("Enter length of the rectangle "))
b=int(input("Enter the breadth of rectangle "))
rectangle=Rectangle()
rectangle.calculate_area(l,b)
s=int(input("Enter radius of the circle "))
circle=Circle()
circle.calculate_area(s)

        
