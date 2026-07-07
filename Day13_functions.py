'''
-->passing by value
def some(a):
    print(a+9)
some(8)

def some_(a):
    for j in a:
        print(j)
some_([1,2,3])
some_((4,5,6,7))

--> return keyword: In a function if a return is executed then
it will exit from the function with certain returned values
def myfunc_(b):
    return 5+b
a=myfunc_(10)
print(a)
c=myfunc_(100)
print(c) 

def myfunc_(b=10):
    return 5+b
print(myfunc_())

import builtins
builtin_functions=[
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"total built-in functions are {len(builtin_functions)}")

-->Recursive function: calling a function by itself repeatedly until
a specified condition is met.
syntax:
def functionName(parameters):
    if condition: --> base case
        return statement
    else:
        return statement
print(functionName(arguments))'''


def number(n):
    if n==1:
        return 1
    else:
        return n*number(n-1)
n=int(input("enter a num:"))
print(number(n))



































