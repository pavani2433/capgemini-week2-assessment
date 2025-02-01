class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def studentdetails(self):
        return self.name,self.roll_number
name=input("Enter user's name")
rollnumber=int(input("Enter user's rollnumber"))
student=Student(name,rollnumber)
details=student.studentdetails()
print(details)
        