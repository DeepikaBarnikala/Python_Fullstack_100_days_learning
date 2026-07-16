'''
Constructor:
self keyword 

Access Modifiers:
They control who can access the data or methods.
-->Public (variable)
Can be accessed from anywhere.
Example:
self.name = "Deepika"

-->Protected (_variable)
Meant to be used within the class and its subclasses.
It's a convention; Python doesn't strictly enforce it.
Example:
self._salary = 50000

-->Private (__variable)
Intended to be accessed only inside the class.
Python uses name mangling to make direct access difficult.
Example:
self.__password = "abc123"

-->Name Mangling
Private variables can still be accessed using:
object._ClassName__variable
Example:
obj._Bank__balance

-->Encapsulation: it wraps the data and metods into a single unit(class) while
controlling access to the data.'''

#public
class Student:
    def __init__(self):
        self.name = "Deepika"

s = Student()
print(s.name)

#protected
class fam:
    def __init__(self):
        self._name="Deepika"

f=fam()
print(f._name)

#private
class bank:
    def __init__(self):
        self.__pin='6600'
AC=bank()
print(AC._bank__pin) 


class Bank:
    def __init__(self):
        self.__pin='7700'
    def display(self):
        print(self.__pin)
ac=Bank()
ac.display()

#Encapsulation
class atm:
    def __init__(self,balance):
        self._balance=balance
    def deposite(self,amount):
        self._balance+=amount
        print(self._balance)

tran=atm(balance=int(input("enter amount:")))
tran.deposite(amount=int(input("Enter money to deposite:"))) 






































