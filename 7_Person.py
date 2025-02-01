class Person:
    def __init__(self,name):
        self.name=name
    def details(self):
        print(f"Name of the person is {self.name}")
class Employee(Person):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
    def details(self):
        super().details()
        print(f"{self.name} is an {self.age} years old")
class Manager(Employee):
    def __init__(self, name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def details(self):
        super().details()
        print(f"{self.name} is {self.age} years old with {self.salary} salary")
    def approve_leave(self,a):
        if a<10:
            print("Leave is approved")
        else:
            print("Not approved")
m=Manager("Pavani",21,45000)
m.details()
m.approve_leave(7)
