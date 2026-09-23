'''
#Methoding overriding --> calling superclass method
#super().method()

class Square:
    """ Area of Square-->base class """
    def __init__(self,x):
        self.x=x
    def area(self):
        print( f'Area of Square is {self.x * self.x}')
class Rectangle(Square):
    """Derived class """
    def __init__(self,x,y):
        self.y=y
        super().__init__(x) #calling super class constructor with arguments
    def area(self):
         #calling super class with method
        print(f'Area of Rectangle is {self.x *self.y}')
        super().area()
obj1=Rectangle(7,8)
obj1.area()
x,y=map(int,input("Enter the values:").split(','))
obj2=Rectangle(x,y)
obj2.area()
#obj2=Square(5) #as we are creating different objects its possible
#print(obj2.area())
'''
'''
#Multiple Inheritance --> WHATSAPP SCENARIO --> Users,business
class base1:
   statement(S)....
   ...
class base2:
  statement2....
  .....
class derived(base1,base2):
    statement(s)....
    .....]

class Users:
    """users class with basic features"""
    def voice_call(self):
        print("User can make voice calls")
class Notifications:
    """ Notifications reaching out """
    def send_notifications(self):
        print("User can get pop-up notifications")
class PremiumUsers(Users,Notifications):
    """ extra features added"""
    def verification_badge(self):
        print("User is verified and bluetick added")
u1=PremiumUsers()
u1.verification_badge()
u1.voice_call()
print(dir(u1))

'''
#Multilevel Inheritance --> level by level
'''
class base1:
    statements...
    .......
class base2(base1):
    statement(S)...
    .......
class base3(base2):
    statement(S)...
    .......

class Users:
    """ users class with base functions"""
    def send_messages(self):
        print("User can send messages")
    def voice_call(self):
        print("making voice calls")
class BusinessUsers(Users):
    """First derived class """
    def create_catalog(self):
        print("Details added succesfully")
class PremiumUsers(BusinessUsers):
    """ second Derived Class """
    def verification_badge(self):
        print("Account is verified")
u1=PremiumUsers()
u1.verification_badge()
u1.create_catalog()
u1.send_messages()
u1.voice_call()
'''

'''#Hierarchical inheritance--> Hybrid Inheritance(one or more types of inheritance)

class A:
    statements...
    .......
class B(A):
    statements...
    .......
class C(A):
    statements...
    .......
class D(A):
    statements...
    .......
    
class GrandParents:
    def habbits(self):
        print("They are rich in habbits")
    def property(self):
        print("My grandparents Own a jewellary shop")
        
class Parents(GrandParents):
    def property(self):
        super().property()
        print("My Parents Own thier own house")
class Children(Parents,GrandParents):
    def property(self):
        super().property()
        print("they own their own car")
        
c1=Children()
c1.habbits()
c1.property()
        
'''

#Polymorphism--> Method Overloading,method overriding,operator overloading
#poly-->many
#morph-->forms

#Hotstar-->Free Users, Premium Users, VIP users

class HotStar:
    """Understanding Ploymorphism"""
    def watch(self):
        print("User logged in and surfing basic content")
    def watch(self,movie):
        self.movie=movie
        print(f'user watcjing {self.movie}')
u1=HotStar()
u1.watch("Leo")
#in the above scenario only the recent watch method is accessible








































































    
