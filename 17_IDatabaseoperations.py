#17 Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC, abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class SQLDatabase(IDatabaseOperations):
    def insert(self,e):
        sql.append(e)
    def update(self,old,new):
        if old in sql:
            index=sql.index(old)
            sql[index]=new
            print(f"Database after updating number {old} to {new} ")
            print(sql)
        else:
            print(f"There is no {old} in the list ")

    def delete(self,d):
        if d in sql:
                sql.remove(d)
                print("Database after deleting number ")
                print(sql)
        else:
            print(f"There is no {d} in the list ")

sqldb=SQLDatabase()
sql=[]
n=int(input("Enter nuber of elements you want to insert in SQLDatabase "))
for i in range(n):
    e=int(input("Enter number you want to insert in SQLDatabase "))
    sqldb.insert(e)
d=int(input("Enter number you want to delete in SQLDatabase "))
sqldb.delete(d)
old=int(input("Enter number in the database that you need to be replaced in SQLDatabase "))
new=int(input("Enter number you want to replace in SQLDatabase "))
sqldb.update(old,new)


class NoSQLDatabase(IDatabaseOperations):
    def insert(self,e):
        nosql.append(e)
    def update(self,old,new):
        if old in sql:
            index=nosql.index(old)
            nosql[index]=new
            print(f"Database after updating number {old} to {new}")
            print(nosql)
        else:
            print(f"There is no {old} in the list")

    def delete(self,d):
        if d in nosql:
                nosql.remove(d)
                print("Database after deleting number ")
                print(nosql)
        else:
            print(f"There is no {d} in the list")

nosqldb=NoSQLDatabase()
nosql=[]
n=int(input("Enter nuber of elements you want to insert in NoSQLDatabase "))
for i in range(n):
    e=int(input("Enter number you want to insert in NoSQLDatabase "))
    nosqldb.insert(e)
d=int(input("Enter number you want to delete in NoSQLDatabase "))
nosqldb.delete(d)
old=int(input("Enter number in the database that you need to be replaced in NoSQLDatabase "))
new=int(input("Enter number you want to replace in NoSQLDatabase "))
nosqldb.update(old,new)
        