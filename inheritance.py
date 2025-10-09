from abc import ABC,abstractmethod #abstract base class

class MobileTransaction(ABC):
    def __init__(self):
        print("this is parent class")
    def parent_method(self):
        print("this is parent method")
    @abstractmethod
    def send_money(self):
        pass

class bkash(MobileTransaction):
    def __init__(self): #overide #polymorphism
        print("this is bkash constructor")
    def parent_method(self):
        print("this bkash method")
    
    def send_money(self,phone,amount,fee,pin,finger_press):
        print(phone,amount,fee,pin,finger_press)

class nexuspay(MobileTransaction):
    def __init__(self): #overide #polymorphism
        print("this is nexus constructor")
    def parent_method(self):
        print("this nexu method")
    
    def send_money(self,phone,amount,fee,pin,otp):
        print(phone,amount,fee,pin,otp)        

b = bkash()
# b.send_money(0,100,5,12345,1)
# nex = nexuspay()
# nex.send_money(0,100,2,123456,4678)
