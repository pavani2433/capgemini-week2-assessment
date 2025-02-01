from abc import ABC, abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self,Gusername,Gpassword):
        if Gpassword=='abcd@123':
            print(f"Google account is logged in by {Gusername}")
        else:
            print("Please enter correct password")
    def logout(self,glogout):
        if glogout=='logout':
            print("Google account is logged out")
        else:
            print("Couldn't logout, try again later")
class FacebookAuth(UserAuthentication):
    def login(self,fusername,fpassword):
        if fpassword=='f@123':
            print(f"Facebook account is logged in by {fusername}")
        else:
            print("Please enter correct password")
    def logout(self,flogout):
            if flogout=='logout':
                print("Facebook account is logged out")
            else:
                print("Couldn't logout, try again later")

g=GoogleAuth()
Gusername=input("Enter user name for google account")
Gpassword=input("Enter your password for google account ")
g.login(Gusername,Gpassword)
glogout=input("Enter logout to logout from google account")
g.logout(glogout)
f=FacebookAuth()
fusername=input("Enter user name for facebook account")
fpassword=input("Enter facebook password to login")
f.login(fusername,fpassword)
flogout=input("Enter logout to logout from facebook account")
f.logout(flogout)