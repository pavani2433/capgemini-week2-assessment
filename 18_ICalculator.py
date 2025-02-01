from abc import ABC, abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def subtract(self):
        pass
    @abstractmethod
    def multiply(self):
        pass
    @abstractmethod
    def divide(self):
        pass
class BasicCalculator(ICalculator):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return a+b
    def subtract(self):
        return a-b
    def multiply(self):
        return a*b
    def divide(self):
        if b>0:
            print(f'Division of {self.a} and {self.b} is {a/b}')
        else:
            print("0 can't be divided" )
a=int(input("Enter first number"))
b=int(input("Enter second number"))
basiccalci=BasicCalculator(a,b)
addition=basiccalci.add()
print(f'Addition of {a} and {b} is {addition}')
subtraction=basiccalci.subtract()
print(f'Subtraction of {a} and {b} is {subtraction}')
multiplication=basiccalci.multiply()
print(f'Multiplication of {a} and {b} is {multiplication}')
basiccalci.divide()

