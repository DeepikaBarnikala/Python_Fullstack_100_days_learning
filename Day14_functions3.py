''' lambda function: This is also called as annonymous function. A lambda function can take n
number of arguments but having only one expression 
Syntax: lambda arguments: expression '''

some=lambda an :an+5
print(some(10))

ex=lambda a,b,c:a+b*c
print(ex(4,5,7))

'''filter():It is a built-in function used to filter elements from an iterables such as
list,tuples and set based condition

Syntax: filter(function,iterable)

--> this filter() function returns filter object so we can convert that into other types like list,set and tuple'''

nums=[1,2,3,4,5]
rev=filter(lambda a:a%2==0,nums)
#print(list(rev))
print(set(rev))
#print(tuple(rev))

num=[1,2,3,4,5]
rev=filter(lambda a:a%2!=0,num)
print(list(rev))
#print(set(rev))
#print(tuple(rev))
#print(str(rev))--> gives filter object

'''List Comprehension:
This offers a shorter syntax when we want to create a new list from the old

Syntax: Varname=[expression loop  condition]'''

old_=[1,2,3,4,5,6,7,8,9]
new_=[i for i in old_]
print(new_)

old=[1,2,3,4,5,6,7,8,9]
new=[i for i in old_  if i%2==0]
print(new)

'''Dictionary comprehension:
This offers a shorter syntax when we want to create a new dict from the old dict

Syntax:Varname={expression loop} '''

old_dict={1:2,3:4,5:6}
new_dict={i:j for (i,j) in old_dict.items()}
print(new_dict)

olddict={1:7,3:4,5:9}
newdict={k:n for (k,n) in olddict.items()if n%2!=0 }
print(newdict)



































