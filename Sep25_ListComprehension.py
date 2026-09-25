
'''#List comprehension:
#Syntax --> [exprsn for var in collection/function]

lst =[4,5,6,2]
for i in lst:
    lst.append(i**2)    
    print(lst)
#In above it gets into infinite and also limits be exceeded
lst=[]
for i in range(10):
    lst.append(i)
    #print(lst) #in this case it prints for every iteration
print(lst)

#same above case can be taken in below simplest form
lst = [i for i in range(10)]
print(lst)
#squares of numbers
d = [i**2 for i in range(5)]
print(d)

#to access desired elements and make changes
data = ['codegnan','saketh','python']
new_data = []
#change every name to uppercase
for i in data:
    new_data.append(i.upper())
print(new_data)
#same above usage in simples way
new_data = [i.upper() for i in data]
print(new_data)

#to update each value in a list
marks = [45,25,35,65]
d= [i+5 for i in marks]
print(d)

d = [i%2==0 for i in range(1,21)]
print(d)
print(len(d))

#Every List Comprehension can be converted to loops,but every loop cannot be
#converted to List Comprehension..
'''

#list comprehension with if clause
#Syantax: [expression for var in collection/function if <condition>]


'''g=[i for i in range(1,21) if i%2==0]
print(g)

h=[i**2 for i in range(1,21) if i%2==0]
print(h)




a=int(input("enter a num:"))
for i in range(1,a):
    if i%2==0:
        print(i)


s=int(input("enter a num:"))
for i in range(0,s):
    if i%2==0:
        i**=2
        print(i)
    


a=int(input("Enter a num:"))
def add(a):
    """filtering even numbs """
    result=[]
    for i in range(1,a):
        if a>0:
            if i%2==0:
                result.append(i)
    return result
print(add(a))


b=int(input("Enter a num:"))
def sqr(b):
    """filtering even numbs along with sqre root """
    result=[]
    for i in range(1,b):
        if b>0:
            if i%2==0:
                i**=2
                result.append(i)
    return result
print(sqr(b))

#Same above case using filter
h=list(filter(lambda i:i%2==0,range(1,21)))
print(h)

k=list(filter(lambda x:len(x)>=6,["Deepika","Divya","Priyanka","Nishith","Srijayanth","Leo"]))
print(k)


names=["Deepika","Divya","Priyanka","Nishith","Srijayanth","Leo"]
g=list(map(lambda x: len(x),names))
print(g)

#group of values --> map
j=list(map(int,input().split(',')))#comma seperated values
print(j)

a,b=map(int,input().split())#space seperated values
print(f'value of a is {a}, value of b is {b}')

#multiple string values
name,place=input().split()
print(name,place)

#group of names
names=list(map(str,input().split()))
print(names)

prices=[2500,3500,5000,7000]
#create filtered prices by applying dicount of 10% for each
new_prices=list(map(lambda x:(x-(0.1*x)),prices))
print(new_prices)
    
#List comprehension with if-else usage
#Syntax --> [true_value if condition else false_value for expression in collection/func]

result=["even" if i%2==0 else "odd" for i in range(1,20)]
print(result)

#in below case even number will be squared and oddd will return as it is
res=[i**2 if i%2==0 else i for i in range(1,21)]
print(res)

#nested loop with comprehension
#Syntax: [expression for item1 in iterable1 for item2 in iterable2]
#combinations
colors=["pink","blue","yellow","white"]
sizes=['S','M','L','XL']
matching=[(i,j) for i in colors for j in sizes]
print(matching)


marks=[20,25,30,35,40]
weekly=[35,30,45,40,45]
#it gives the combination of marks we only need marks of each student
final=[mark+wmark for mark in marks for wmark in weekly]
print(final)
final=list(map(lambda mark,wmark:(mark+wmark),marks,weekly))
print(final)
'''

#nested comprehension with if-else combination
#Syntax:[true_value if <comdition> else false_value for item1 in iterable1 for item2 in iterable2...]
f=[1+4 if i>=j else i-3 for i in range(1,5) for j in range(1,5)]
print(f)
print(*f)
for i in f:
    print(i,end=' \n')































