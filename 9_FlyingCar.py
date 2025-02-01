class Car:
    def move(self):
        print("car is moving")
class Airplane:
    def move(self):
        print("Airplane is moving")
class FlyingCar(Car,Airplane):
    def __init__(self):
        print("Flying car constructor")
    def move(self):
        print("Flying car is moving")
        super().move()
f=FlyingCar()
f.move()
