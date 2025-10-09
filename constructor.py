from dataclasses import dataclass


@dataclass(order=True)
class FaceBookRegistration:
    # x:int
    # y:int
    #initializer - constructor
    # def __init__(self,x,y):
    #     self.x = x
    #     self.y = y

        #print("this is a constructor")
    # def __str__(self):
    #     return self.name
    # def __add__(self,self2):
    #     return self.x + self2.x + self.y + self2.y

        # print(x,y,p,q)
    def sample_method(self):
        print("this is sample method")

name = "salman"
dob = "20-10-1978"
email = 'salmanmdsultan92@gmail.com'
pw = '123456'
# fb_obj = FaceBookRegistration(name,dob)
# print(fb_obj)
# print(fb_obj.__dict__)

fb_obj2 = FaceBookRegistration(10,20)
print(fb_obj2.x)
fb_obj4 = FaceBookRegistration(30,40)
print(fb_obj2==fb_obj4)
print(fb_obj2)
#__repr__()
#__eq__()
#__le__()
#__ge__()
#__gt__()
#__lt__()
# print(fb_obj2.__dir__())




