class Animal:
    def speak(self):
        print("Animals can make sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak()
class Cat(Animal):
    def speak(self):
        super().speak()
        print("Cat is an animal")

c=Cat()
c.speak()
d=Dog()
d.speak()