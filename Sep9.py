'''
python Project --> POP/OOP -->DSA (logic Based-->Pattern Bases --> platform
POP(Procedure Orientend Programming)--> dividing the entire code into blocks--> those blocks are cslled procedures--> functions(def)
Functions --> A reusable block of code(A block of statements which performs a specific tasks)

Syntax:
def <functionname>(parameters):  #function definition
    """Doc String """
    statements...
    ............     #body of the function
    return value(s)...
functionName(args) #functioncall 

'''
#simple scenario to understand a function
'''def add(a,b):
    """ Addition function """
    return a+b
print(add(7,65))
c,d='python','java'
print(add(c,d)) #concatination
e,f=map(str(input("enter the val:").split())
print(add(e,f))
print(add([1,2,3],[4,6,7])) #merging
print(add(1,3,4,5)) #positional argumrnts fail error--> value error

#variable length arguments--> *args we can pass any number of Positional arguments
#arguments--> data will be stored in tuple..()
#return --> print()
def sample(*a):
    """ demo of variable length arguments"""
    print(a)
    print(type(a))
sample()
sample('codegnan',234,3+8j,566.765)
sample(1,2,3,4,6,8,9)

marks=[54,67,87,98,43]
sample(marks)
sample(*marks)

a,*b,c=12,'code','poll',23,4,5
print(a)
print(b)
print(c)

op:12
['code', 'poll', 23, 4]
5


*a,b,c=12,'code','poll',23,4,5
print(a)
print(b)
print(c)
op:
[12, 'code', 'poll', 23]
4
5


def add(*a):
"""Perform addition for numeric values
eg:
(2, 3, 4)
9
(2, 'deepika', 3, 4)
9
"""
    print(a)
    result=0
    for i in a:
        if type(i) in [int,float]:
        #if type(i)==int or type(i)==float:
            result=result+i
    return result
print(add(2,3,4))
print(add(2,'deepika',3,4))

#Keyword Arguments--> we can pass the name for the arguments
def batch(name,age,place='vizag'):
#def batch(name='deepika',age,place='vizag'):--> error:non-default always follows default arguments 
    """Keyword arguments usage """
    print(f'{name} is in {place} and age is {age} years')
batch('deepika',22,'vizag')
batch('deepika','vizag',22)
batch(place='vizag',name='Deepika',age=23) #keyword arguments only needs name matching not order
batch(name='deepika') #default arguments can accept a value as default

print(4,5)
print(4,5,sep=':') #here keyword argument is sep and we are changing the default value for sep '''


#keyword variable length arguments (**kwargs) --> any num of keyword arguments, data is stored in dictionary
def batch(**a):
    """keyword variable length aruguments usage """
    print(a)
    print(type(a))
batch()
batch(name="akash",age=21,place="vizag",branch="CSE")
data={'name':['deepika','divya'],'place':['vizag','hyderabad']}
data.update({'batch':'PFS004'})
batch(**data)

#task:create a function with the usage of *args and **kwargs
'''
def fn(*a,**b):
    ....
    ....

'''




























































