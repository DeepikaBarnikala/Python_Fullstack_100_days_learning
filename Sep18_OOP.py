'''
OOP - Object Oriented Programming - Objects

getter and setter-->access modifiers

POP - Procedure Oriented Programming - Functions

#Chair (Object) - Wood(Materials), Design(Dimensions), Person

A class is a blueprint of an object
A Object is a real world entity which contains
    - Attributes (Variables)
    - Methods (Functions)

class keyword

Flipkart - Prodducts - Laptop, Mmobile, Gadgets..


Features -Encapsulation, Inheritance, Polymorphism

class ClassName:
    """docString"""
    #attributes (define the data)
    .......
    ........
    def fname(self): #behaviour
    defd __init__(self):
        statements(s)....
        .........
obj = ClassName()


#Student--> name,age
class Student:
    """Student details"""
    name="Deepika Barnikala"
    age=22
    place="vizag"

    def details(self):
        #print(f'{name} is in {vizag} and age of {age} years')-->without reference
        print(f'{self.name} is in {self.place} and age of {self.age} years')

#creation of objects
st1=Student()
print(st1)
print(dir(st1))
print(st1.name,st1.age,st1.place)
#print(st1.details())#TypeError:Student.details() takes 0 positional arguments but 1 was given-->without 'self' in details class
#print(st1.details())
#NameError: name 'name' is not defined. Did you mean: 'self.name'
#-->after passing self in details()--> ie we have thrown self but no referenc
#now lets pass the referenc
st1.details()
st2=Student()
st2.details()


#In above case how many objects u create the result will be same
class Students:
    """Student details for multiple students"""
    def details(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    #access those details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1=Students()
st1.details("Deepika",22,"Vizag")
print(st1.name,st1.age,st1.place)
st1.display()
print(st1.__class__)
print(st1.__doc__)
print(st1.__dict__)

st2=Students()
st2.details("Laya",23,"Vijayanagaram")
print(st2.name,st2.age,st2.place)
st1.display()
print(st2.__class__)
print(st2.__doc__)
print(st2.__dict__)

#in this case we want object to be initialized --> "__init__()"
class Students:
    """Student details for multiple Students"""
    def __init__(self,name,age,place):
        self.name=name  #instance variables
        self.age=age
        self.place=place
    #now to access those details
    def display(self): #instance method
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1=Students("Arun",25,"Hybd")
st1.display()
print(st1.__dict__)
st2=Students("Sumanth",25,"banglore")
st2.display()

#create a cars class with attributes as brand,name,price
#create multiple objects

class Cars:
    """Car details for multiple brands"""
    def __init__(self,bname,price,milage,features):
        self.bname=bname
        self.price=price
        self.milage=milage
        self.features=features
    def display(self):
        print(self.bname,self.price,self.milage,self.features)
        print(f'The car {self.bname} costs {self.price} and its milage is {self.milage}km per hr with key features{self.features}')
        

c1=Cars("Audi",4000000,40,"Safety,Luxury")
c1.display()
print(c1.__dict__)
c2=Cars("Tata",500000,60,"Safety")
c2.display()
c3=Cars("Benz",7500000,50,"Comfort,Safety,Luxury")
c3.display()


#Encapsulation - How the methods and attributes are binded into single class
#In simmilar way how we can access the data - public, private, protecte

#Public Attributes--> can be created and modified even outside the class
class Users:
    """ Usage of public attributes"""
    def __init__(self,username):
        self.user=username #public attribute
    def display(self):
        print(f'Username is {self.user}')

u1=Users("John")
print(u1.user)
u1.user="Sam" #we can modify the public attribute
print(u1.user)
u1.display()

#Protected Attribute - These can also be modified outside the class
#Its mainly useful as a hint/coding convention for other user/developers

#To create a protected attribute we use underscore - _otp

class Users:
    """usage of Public attributes"""
    def __init__(self,username,_otp):
        self.user=username #public attribute
        self._otp=_otp #protected attribute
    def display(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')
u1=Users("Saketh",2345)
u1.display()
u1._otp=4567
u1.display()


#Private Attributes--> restrict the usage and cannot be directly accessed
#we have the usage or notation as double leading underscore--> __password

class Users:
    """usage of Public attributes"""
    def __init__(self,username,_otp,__password):
        self.user=username #public attribute
        self._otp=_otp #protected attribute
        self.__password=__password#private attribute
    def display(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')
        print(f'password is {self.__password}')
u1=Users("Saketh",2345,"admin123")
print(u1.user,u1._otp)
#print(u1.__password)-->AttributeError: 'Users' object has no attribute '__password'
#in the above case password can not be accessed directly-->we go for--> NameMangling-->ie with the className
print(u1._Users__password)
'''

#Usage of getter(),setter() methods--> to get and update the protected data

class Users:
    """USage of Public attributes"""
    def __init__(self, username, _otp, __password):
        self.username = username   #Public attribute
        self._otp = _otp  #Protected attribute
        self.__password = __password   #Private attribute
    #Usage of getter() or get() method for password
    def get_password(self):
        """Getter method for password"""
        #return "**"
        return self.__password
    #Usage of setter() to modify the data
    def set_password(self, new_password):
        if len(new_password) < 6:
            return "Password length is not matching"
        else:
            self.__password = new_password
            return "Password Updated"
user1 = Users("Sumanth", 4873, "Pandu")
print(user1.get_password())
#print(user1.set_password("Pandu"))
print(user1.set_password("Pandu2000"))
print(user1.get_password())

















    
