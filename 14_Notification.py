class Notification:
    def send(self,notification):
        self.notification=notification
        print(f"Recieved a notification: {notification}")

class EmailNotification(Notification):
    def send(self,email):
        print(f"Recieved an email: {email}")

class SMSNotification(Notification):
    def send(self,message):
        print(f"Recieved a message: {message}")
        
sms=SMSNotification()
sms.send("Hello")
email=EmailNotification()
email.send("Congratulations! You have been selected")
notification=Notification()
notification.send("Hi")