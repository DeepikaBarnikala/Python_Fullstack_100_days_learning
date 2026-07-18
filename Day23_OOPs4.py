'''Polymorphism:
-->it means many forms
--> it allows same method, function or operator to perform different
tasks depending on the same object...

Types:
1.Method overloading:
-->It means having multiple methods with the same name but different parameters.'''

class cal:
    def add(self,num,num2=0):
        print(num+num2)
    def add(self,n,n2=0,n3=0):
        print(n+n2+n3)
obj=cal()
obj.add(4)
obj.add(4,7)
obj.add(6,4,5)

'''2.Method Overriding.
--> The method overriding occurs when a child class provides its own implementation of a method already
defined in its parent class...'''

class animal:
    def sound(self):
        print("Animals make sounds")

class dog(animal):
    def sound(self):
        print("Dogs barks")
d=dog()
d.sound()

'''3.Operator overloading.
--> this allows operators(+,-,*) to work differently for user-defined objects.
__add__(+)
__sub__(-)
__mul__(*)
__truediv__(/)
__eq__(==)
__It__(<)
'''
class student:
    def __init__(self,marks):
        self.marks=marks
    def __sub__(self,other):
        return self.marks-other.marks
s1=student(56)
s2=student(67)
print(s1-s2)

''' Data Abstraction:
--> It is the process of hiding implementation details and showing only the
essentaial data to the user.
--> Eg: ATM, APPS, CARS etc

from abc import ABC, abstractmethod
class parent:
    @abstractmethod
    def display(self):
        pass '''
from abc import ABC, abstractmethod
class bank:
    @abstractmethod
    def interest(self):
        raise NotImplementedError('subclass must implement interest()')
class SBI(bank):
    def interest(self):
        print('SBI interest rate: 6.5%')
class ICIC(bank):
    def interest(self):
        print('ICIC interest Rate: 5.5%')
class HDFC(bank):
    def interest(self):
        print('HDFC interest Rate: 5.2%')
banks = [SBI(),ICIC(),HDFC()]

for j in banks:
    j.interest()


















