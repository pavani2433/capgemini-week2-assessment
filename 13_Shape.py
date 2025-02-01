#13 Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
class Shape:
    def area(self):
        print("Area of triangle and square are")
class Square(Shape):
    def area(self,s):
        print(f'Area of square is {s*s}')

class Triangle(Shape):
    def area(self,l,b):
        print(f'Area of triangle is {(1/2)*l*b}')

side=int(input("Enter side of the square"))
length=int(input("Enter length of triangle"))
breadth=int(input("Enter breadth of triangle"))
s=Square()
s.area(side)
t=Triangle()
t.area(length,breadth)
