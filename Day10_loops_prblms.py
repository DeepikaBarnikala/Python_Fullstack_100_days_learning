'''
#prime or not
num=int(input("Enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(f"{num} is a prime")
    print(count)
else:
    print(f"{num} is not a prime")
    #print("%s is not a prime"%(num))
    print(count)

#printinh the prime numbers in the given range
limit_=int(input("Enter a num:"))
for j in range(1,limit_+1):
    count=0
    for i in range(1,j+1):
        if j%i ==0:
            count+=1
            #print(count)
    if count==2:
        print(f"{j} is prime")

#printing right angle triangle
num=5
for j in range(1,num+1):
    for i in range(1,j+1):
        print("*", end=' ')
    print()

num=5
for k in range(1,num+1):
    for n in range(1,k+1):
        print(k, end=' ')
    print()

num=5
for y in range(1,num+1):
    for m in range(1,y+1):
        print(m, end=' ')
    print()
    
num=4
count=0
for j in range(1,num+1):
    for i in range(1,j+1):
        count+=1
        print(count,end=' ')
    print()

num=5
count=0
for j in range(num,0,-1):
    for i in range(1,j+1):
        count+=1
        print(count,end=' ')
    print()

num=5
count=0
for j in range(num,0,-1):
    for i in range(1,j+1):
        count+=1
        print(j,end=' ')
    print()


num=5
count=0
for j in range(num,0,-1):
    for i in range(1,j+1):
        count+=1
        print(i,end=' ')
    print() 

num=5
count=0
for j in range(num,0,-1):
    for i in range(1,j+1):
        count+=1
        print('*',end=' ')
    print()

#armstrong numbers
num=int(input("Enter a num:"))
length=len(str(num))
all_sum=0
for j in str(num):
    all_sum+=int(j) ** length
if all_sum==num:
    print(f"{num} is armstrong num")
else:
    print(f"{num} not a armstrong num")

#pyramid
num=int(input())
for j in range(num):
    print(" " *(num-j-1),end="")
    print("*" *(2*j+1)) '''





































