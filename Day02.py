#Operators in Python--- Special sysbol used t o perform operations on variables and v alues
''' Arthimatic Operators(used for math calculations)---+,-,*,/,%.**,//
a=10
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #gives remainder
print(a//b) # floor division-- removes decimal part
print(a**b) # exponential-- gives a power b val  '''

'''Comparision or Relational operators(used for compare values)--- ==, !=,>,<,>=,<=
num1=20
num2=15
a=[1,2]
b=[1,2]
print(a==b)#compares the values in the given location
print(a is b)
print(num1==num2) 
print(num1!=num2)
print(num1>=num2)
print(num1<=num2)
print(num1>num2)
print(num1<num2) '''

'''Logical opearators(used to combine conditions)--- and, or , not 
a=65
b=38
c=56
print(a>b and a<c) #both the conditions must true
print(a>b or a<c)  #one condition must be true
print(not a>c)  #reverse the result '''

''' Assignment Operators(used to assign values)--- =,+=,-=,*=,/=,%=.//=,**= 
x=15
y=[1,2,3]
print(id(type(x))) #'id' will give the location of the variable where 'type' specifies the datatype of the variable
print(type(y))
x+=5 #x=x+5
x-=5
x*=5
x/=5
x//=5
x**=5
x%=5
print(x) '''

'''Bitwise Operators(work on binary bits)--- &,|,^,~,<<,>>  
print(5&3) #AND
print(5|3)#OR
print(5^3)#XOR
print(5<<3)#LEFT SHIFT
print(5>>3)#RIGHT SHIFT
print(~5)#NOT '''

''' Membership Operators(checks whether an element exists in a sequence or not)--- in(present), not in (Not presenr)
fruits=["apple","banana","grapes","mango"]
print("apple" in fruits)
print("orange" not in fruits) '''

'''Identity Operators(check whether two variables refer to the same object or not)--- is(same obj), is not (different obj) '''
a=[1,2,3,4]
b=[1,2,3,4]
c=[45,5]
d=c
print(id(c))
print(id(d))
print(c is d)
print(c is not d)
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
print(a==b)




