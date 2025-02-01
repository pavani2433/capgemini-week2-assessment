class BankAccount:   
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,money):  
        self.balance+=money
        print(f'Money deposited: {money}, Total balance: {self.balance}')
    def withdraw(self,withdrawmoney):
        if withdrawmoney>self.balance:
            print("Insufficient money") 
        else:
            self.balance-=withdrawmoney
            print(f'Available balance after withdrawing {withdrawmoney} is {self.balance}')
ba=BankAccount(1000)
while True:
    choice=input("Enter your choice for deposit or withdraw. Enter 'exit' to not perform any operation ")
    if choice.lower()=="deposit":
        money=int(input("Enter money you want to deposit "))
        ba.deposit(money)
    elif choice.lower()=="withdraw":
        withdrawmoney=int(input("Enter money you need to withdraw "))
        ba.withdraw(withdrawmoney)
    elif choice.lower()=="exit":
        break
    else:
        print("Invalid choice, please select deposit or withdraw")