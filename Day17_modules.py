'''
Modules: a module is a python file(.py) that contains resusable code
1.variables
2.functions
3.classes
4.objects
5.statements

Why Modlues??
-->Insted of writing the same code repeatedly, we cabn stire it in a module
and use it whenever needed...

Types of Modules:
1.User-define modules:

2.Built-in modules:
math--> contains mathematical functions
os-->used to iteract with operating systems
sys-->access system specific parameters and will provide the info about python interpreter
random-->generates random numbers
datetime-->work with dates and times
'''


import D17_firstModule
print(D17_firstModule.add(4,6))
print(D17_firstModule.sub(564,432))
print(D17_firstModule.mul(78,3))
print(D17_firstModule.div(200,25))

#import a specific function: if i want to call a specific function from another file
from D17_firstModule import add,sub
print(add(10,5))
print(sub(49,4))

#Alias Name
import D17_firstModule as m
print(m.floor_(4,6))
print(m.modulo(564,432))
print(m.power_(78,3))
print(m.cap(4,3)) 

#build-in modules:math module
import math
print(math.sqrt(36))
print(math.pi)
print(math.factorial(5))
print(math.pow(2,5)) #gives power
print(math.floor(10.44)) #round down
print(math.ceil(10.44)) #round up

#os module
import os
print(os.getcwd()) #to get the current directory
os.mkdir("Deeps") #creates a folder with name Deeps in the same directory
os.rmdir("Deeps")#removes Deeps folder from current directiory

#sys module
import sys
print(sys.version)

#random module
import random
print(random.randint(1000,9999))

clrs=['red','blue','yellow','black','pink']
print(random.choice(clrs))





























