'''
Functions: it is a block of code that can be reused.It will help to remove repeated lines of code.
Functions are of 2 types:
1.Built-in functions--> print(),max(),type(),min(),type()...
2.User define functions
--> this functions define by the user itself of his wish with the valid syntax
-->It starts with keyword called 'def' 
eg.
def func_name(parameters): --> definition line
    --------
    --------
    --------
func_name(parameters)--> calling line

types of arguments:
1.required arguments-->have to pass same number of arguments with the definition of the function
2.default
3.keyword--> we can pass as a pair like (variable=datatype)
4.variable length--> can pass n number of arguments by using 'args' in the parameters,
will receive tuple of arguments and we can access those arguments by using indexing.
--> * args--> tuple of elements
--> ** kwargs-->dict of items

SCOPE OF THE VARIABLES:
a. local variables: defines inside afunction and accessible only inside that function
b. global variable: defines outside of the func and uses everywhere in the program
c.global keyword -->use global when yp=ou want to modify a global variable inside a function'''

#required arguments
def add(a,b):
    print(a)
    print(b)
    print(a+b)
add(4,5)
add(3,8)
add(a=7,b=3)
add(a='h',b='i')

#default
a=int(input())
b=int(input())
c=int(input())
def add(n1,n2,n3):
    print(n1)
    print(n2)
    print(n3)
    print(n1+n2+n3)
add(a,b,c)
add(n1=4,n2=7,n3=5)

#variable length
n1=23
n2=3
n3=89
n4="pyhton"
def add(*a):
    print(a)
    print(a[2])
add(n1,n2,n3,n4)

def all_(**Any):
    print(Any)
    print(Any['Name'])
    print(Any['Age'])
all_(Name="Sumanth", Age=25)

#scope of the variable
num=9
def func_():
    global num
    num=89
    print(num)
func_()
print(num)
#a()--> raises NameError since a() carries local variable
#local
def a():
    num=10
    print(num+34)
a()
func_()



























