class Electronics:
    def __init__(self,name):
        self.name=name
    def device(self):
        print(f'Electronic device {self.name}')
class MobileDevice(Electronics):
    def __init__(self,name,type):
        super().__init__(name)
        self.type=type
    def device(self):
        print(f'Mobile Name: {self.name}, Mobile Type: {self.type}')
        
class SmartPhone(MobileDevice):
    def __init__(self,name,type,price):
        super().__init__(name,type)
        self.price=price
    def device(self):
        print(f"Name of the device is {self.name} Type of the device is {self.type} Price is {self.price}")
smartphone=SmartPhone("Oppo","A53",15000)
smartphone.device()
        

