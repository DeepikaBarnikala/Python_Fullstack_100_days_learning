'''
Loops: used to reprat a block of code repeatedly
1.for loop--> it is used to iterate over a sequence,list,tuple
2.while loop--> loop runs as long as the given condition is true
#where k , i ,j are called instance variables only defines at runtime
so it wont throw any error

range()-->it is a built-in function that is used to generate a sequence upto a limit
It starts from 0 and goes upto endVAlue-1
Syntax--> range(start,stop,step)

Control statements:
1.break-->stops the loop and the program exists the loop and go for nxt statements
2.continue-->skips the current iteration and moves directly to the next interation of the loop
3.pass-->its a space holder and does nothing to the program '''
#for
any_="python is a language" #string
for k in any_: 
    print(k)

list_=[1,2,3,4,5,5,5,66,7,8,9] #list
tuple_=(12,4,6,7,8,9) #tuple
for i in list_:
    print(i)
for j in tuple_:
    print(j)

dict_={"name":"Deepika","Role":"Trainee","Batch":4} #dictionary
for a in dict_.items():
    print(a)

#loops with conditional statements--> after for loop executes then else block will executes 
so=[1,"deeps",'r',9.4,True]
for n in so:
    print(n)
else:
    print("Program Ended") 
#break --> if break statement present in the code then else block will not be printed.
any__=[1,2,3,4,5,6]
for j in any__:
    print(j)
    if j==3:
        break
else:
    print("The program ended")

#continue
so=[1,2,3,4,5]

for i in so:
    if i==3:
        continue
    print(i)
else:
    print("Ended") 

#pass
so_=[1,2,3,4,5]
for i in so_:
    if i==3:
        pass
    print(i)
else:
    print("Ended")

#range()
for w in range(5):
    print("HI")
for k in range(1,30):
    print(k)

for y in range(2,100,5):
    print(y)

for x in range(50,1,-2):
    print(x) 

#while()
i=1
while i<=10:
    print("*")
    print(i)
    i+=1

j=0
while j<=1:
    print(j) #infinite loop runs 

'''assert-->this keyword isused to check whether a condition is true.
if the condition is True, the program continue.
If false then python raises an AssertionError and we can make our own errors ststements'''
age=int(input())
assert age>=18, "age must be 18 or more to vote"
print("you can vote")


































    
    
    



















    


