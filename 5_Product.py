class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        if quantity>self.stock:
            return "Requested quantity is not availabile"
        else:
            return "Requested quantity is available"
product=Product("Biscuits",200,4)
quantity=int(input("Enter the quantity of the product to check availability"))
avilability=product.check_availability(quantity)
print(avilability)
