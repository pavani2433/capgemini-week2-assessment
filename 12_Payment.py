#12. Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.

class Payment:
    def process_payment(self):
        print("Payment")
class CreditCard(Payment):
    def process_payment(self):
        print("CreditCard payment is successfull")
        
class PayPalPayment(Payment):
    def process_payment(self):
        print("PayPal payment is successfull")

class BitcoinPayment(Payment):
    def process_payment(self):
        print("Bitcoin payment is successfull")


paymenttype=input("Enter payment type ")
bitcoinpayment=BitcoinPayment()
paypalpayment=PayPalPayment()
creditcardpayment=CreditCard()
payment=Payment()
if paymenttype=="Bitcoin":
    bitcoinpayment.process_payment()
elif paymenttype=="Paypal":
    paypalpayment.process_payment()
elif paymenttype=="Creditcard":
    creditcardpayment.process_payment()
else:
    print("No such payment available")


