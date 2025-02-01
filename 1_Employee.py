class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def emp(self):
        print(f'Name of the employee: {self.name}\nID: {self.id}\nDepartment: {self.department}')
name=input("Enter name of the employee")
id=int(input("Enter id of the Employee"))
department=input("Enter department of Employee")
e=Employee(name,id,department)
e.emp()
