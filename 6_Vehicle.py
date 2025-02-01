class Vehicle:
    def __init__(self):
        print("Vehicle Constructor")
    def vehicle(self):
        print("Vehicle method")
class Car(Vehicle):
    def __init__(self):
        print("Car Contructor")
    def car(self):
        print("Car method")
class Bike(Vehicle):
    def __init__(self):
        print("Bike Constructor")
    def bike(self):
        print("Bike method")
class ElectricCar(Car):
    def __init__(self):
        print("Electric Car constructor")
        super().__init__()
    def electriccar(self):
        print("Electric car method")
v=Vehicle()
c=Car()
b=Bike()
ec=ElectricCar()
ec.vehicle()
ec.car()
b.bike()
ec.electriccar()
