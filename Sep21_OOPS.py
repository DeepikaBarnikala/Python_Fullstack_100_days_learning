'''
Inheritance --> It is one of the key properties of OOP 

we can acquire properties (features) from one class to another class

Single Inheritance --> Finger Print --> one child class inheriting properties
Multiple Inheritance --> Parents --> kids --> ome child classs can take proper 
Multilevel Inheritance --> level by level --> Family Tree
Hierarchial Inheritance --> multiple child classes inheriting from single parent
Hybrid Inheritance --> It's a combination of diff types of inheritance


Single Inheritance

class Baseclasss: #Parent class
     statement(s)......
     .....
class Derivedclass(Baseclass):
     statement(s)...
     .....

#updating user names in a profile page

class Users:
    """users class with basic details"""
    def __init__(self,fname,lname): #contructor and is automatically initialise objects
        self.fname=fname
        self.lname=lname  #instance or public attribute
    def fullname(self):
        return f'{self.fname+" "+self.lname}'

#u1=Users('Deepika','Barnikala')
#print(u1.fullname())

#Now we want to extend by updating user name
class Update_Users(Users):
    #pass
    def update(self):
        return f'{self.fname.title().strip()+" "+self.lname.title().strip()}'
u1=Update_Users('  divya ','seela ')
print(u1.fullname())
print(u1.update())
print(dir(u1))

#Usage of class attribute and class Method in inheritance

#class attributes - They can be accesed directly with class name
#class method -- @classmethod

#Banking scenario - RBI Bank (Base class) - SBI, HDFC

class RBI:
    """Base class with amount"""
    cash = 1000000  #class attribbutes
    @classmethod  #decorator
    def rbiCash(cls):
        return f"Available cash with RBI is {RBI.cash}"
rb = RBI()
print(rb.cash)
print(rb.rbiCash())
print(RBI.cash) #we can also access directly using classname
print(RBI.rbiCash())

class SBI(RBI):
    pass
b1=SBI()
print(b1.rbiCash())

class HDFC(RBI):
    cash=500000 #class attribute
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total Accessible cash is {cls.cash+cls.cash}')
b1=HDFC()
print(b1.cash) #in this case as cls attribute is same so its overridden
print(b1.rbiCash())
b1.hdfc_cash()


#the same case we will access with classnames
class HDFC(RBI):
    cash=500000 #class attribute
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total Accessible cash is {cls.cash+RBI.cash}')
b1=HDFC()
print(b1.cash)
print(b1.rbiCash())
b1.hdfc_cash()

#takeaway--> if same classes is having same names as class attributes
#t access them we will directly use class names as RBI.cash,HDFC.cash

#what if we have diff class attributes
class RBI:
    """Base class with amount"""
    cash = 1000000  #class attribbutes
    @classmethod  #decorator
    def rbiCash(cls):
        return f"Available cash with RBI is {RBI.cash}"

class HDFC(RBI):
    amount=500000 #class attribute
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total Accessible cash is {cls.cash+RBI.cash}')
b1=HDFC()
print(b1.cash)
print(b1.amount)
b1.hdfc_cash()
print(b1.rbiCash())


#single inheritance usage--> Base class and derived class with constructors
#kid,father --> Property scenario

class Father:
    """ Father class with base property amount"""
    def __init__(self):
        self.fproperty=2500000
    def father_property(self):
        print (f'Father property is {self.fproperty}')
u1=Father()
u1.father_property()

class Kid(Father):
    pass
print(u1.property)
u1.father_property()


#In the above case its as it is not change in method and attribute usage
class Kid(Father):
    """ Kid Started earning"""
    def __init__(self):
        self.property=500000
    def kid_property(self):
        print(f'Kid property is {self.property}')
        print(f'kid and father combined property is {self.property+self.property}')
u1=Kid()
u1.father_property()
u1.kid_property()
#in this case constructor overriding as parent and child classes is having
#constructor child class constructor will override parent class constructor

 we have the usage of super() method
-->we can call super class constructor(ie parent class constructor)-->super().__init__()
-->Superclass constructor with args --> super().__init__(args)    
-->Superclass method(method overriding) --> super().method()

class Kid(Father):
    """ Kid Started earning"""
    def __init__(self):
        super().__init__() #calling superclass constructor
        self.kproperty=500000
    def kid_property(self):
        print(f'Kid property is {self.kproperty}')
        print(f'kid and father combined property is {self.fproperty+self.kproperty}')
u1=Kid()
u1.father_property()
u1.kid_property()

#in above case we have modified the attributes kproperty for kids and
#fproperty for father with default values

#Usage of super()
#super with arguments--> supe().__init__(args)

class Father:
    """ Father class with base property amount"""
    def __init__(self,fproperty):
        self.fproperty=fproperty
    def father_property(self):
        print (f'Father property is {self.fproperty}')
class Kid(Father):
    """ kid class with kproperty argument"""
    def __init__(self,kproperty,fproperty):
        super().__init__(fproperty)
        self.kproperty=kproperty
    def kid_property(self):
        print (f'kid property is {self.kproperty}')
        print(f'Total combined Property is {self.fproperty + self.kproperty}')
u1=Kid(34556789,34567)
u1.kid_property() #AttributeError
u1.father_property()
print(u1.__dict__)

'''























































        
