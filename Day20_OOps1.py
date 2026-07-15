'''
OOP's: Object Oriented Programming system, this will organizes the code using classes and objects...
Use:
Code Reusable
easy maintenance
clear understanding
better security`'''

#simple calculator using OOPs
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print("Addition= ",self.a+self.b)

    def subtract(self):
        print("Subtraction= ",self.a-self.b)

    def multiply(self):
        print("Multiplication= ", self.a*self.b)

    def divide(self):
        if self.b!=0:
            print("Division= " ,self.a/self.b)
        else:
            print("CAnnot be divide by zero")

c1=Calculator(20,5)
c1.add()
c1.subtract()
c1.multiply()
c1.divide() 

#student details
class Student:
    def __init__(self,name,age,branch,id_):
        self.name=name
        self.age=age
        self.branch=branch
        self.id_=id_

    def details(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Branch :", self.branch)
        print("ID:", self.id_)
s1=Student("Deepika", 22, "EEE",66)
s1.details()

#BankAccount and details
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)

account = BankAccount("Deepika", 5000)
account.deposit(1000)
account.withdraw(2000)
account.check_balance()







































        
    
