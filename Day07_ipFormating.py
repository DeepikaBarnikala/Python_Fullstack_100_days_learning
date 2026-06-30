'''Input formatting:nput formatting means taking user input and converting it
into the required data type or structure.
map()-->Takes many values. Applies the same function to each value.'''
#input()-->basic ip that takes input as a string by default.
a=input()
print(a)
print(type(a))
print(a+ "morning")

#int()-->used to convert string into an integer
age_=int(input('enter age:'))
print(age_)
print(type(age_))

#float()--> used for decimal values
salary=float(input('enter your salary:'))
print(salary)
print(type(salary))

#reading a list using list()
group_=list(map(int,input() .split()))
print(group_)
print(type(group_))

#reading a tuple using tuple()
some=tuple(map(int,input().split()))
print(some)
grp=tuple(input().split())
print(grp) 

#eval()-->Think of eval() as a function that reads a string and treats it like Python code.
#It automatically converts the input into the correct Python data type.
x=eval(input("enter:"))
print(x)
print(type(x)) 

#formatting types
name=input("enter your name:")
age=int(input("enter your age:"))
print(name, "you are age is",age)# standard print formatting
print(f"{name} you are age is {age}") #f string
print("my name is %s and i'm %d yrs old" %(name,age)) #modulo formatting




    
