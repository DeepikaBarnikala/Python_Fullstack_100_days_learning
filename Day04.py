''' List Datatype: It is a collection of different data types(diff items) that are enclosed in []. 
MUTABLE                             IMMUTABLE
1.datatypes can be modified         1. Cant be modified on a particular variable
eg.List                             eg. String '''
# can store mixed data types
all_types=[1,"python",[2,3]] 
print(type(all_types))
for i in all_types:
    print(i)
'''List is mutable ---> changes done to the list saves permanently
   List is ordered--> ie items have an index
methods in list
1.append()--> adds new a item in the list at the last index position and takes exactly one argument.
2.extend()--> Add multiples elemensts/items also adds multiple lists into single lists.
It will also add a item at the last index position and gives each value in the each index position
It will take only iterables.
3.pop()--> removes an item by index,if no index given then removes last item
4.insert()--> Adds an item at a specific index
5.remove()--> removes the first matching value ie removes direct value
6.clear()-->remove all items
7.index()--> returns index of an element
8.count()-->counts how many times an element appears
8.sort()--> sorts list of items in ascending order
9.reverse()--> reverse the list
10.copy()--> creates a copy of list '''
#append()
any_=[1,2,3,4,5]
print(any_)
any_.append(6)
print(any_)
any_.append(10,20) #error
print(any_) # hence List is mutable 
#extend()
a=[1,2,3]
b=["apple","banana"]
a.extend(b)
#b.extend(a)
print(a)
#print(b)
any_.extend('python')
print(any_)
print(len(any_)) 
any_ =[1,2,"python is a language",[45,78,"Java is a language",[1,23],90],'hello']
print(any_[3])
print(any_[3][2])
print(any_[3][2][10]) 
#pop()
any_=[1,2,3,4,5,6,7]
any_.pop(3)
any_.pop()
print(any_)
#remove()
fruits=["apple","banana","grapes","mango","kiwi"]
fruits.remove("mango")
fruits.remove(1) #throws error when we're trying the item by index position
print(fruits)
#insert()
num=[10,20,30]
num.insert(2,25)
print(num)

#clear()
fruits=["apple","banana","grapes","mango","kiwi"]
print(fruits.index("kiwi")) #index()
print(fruits.clear())
n=[1,2,3]
n.clear()
print(n)

#count()
list_of_=[1,1,2,3,4,3,4,6,7,8,9,0,5,4,3,2,1,1]
print(list_of_.count(1))
print(list_of_)
#sort
list_of_=[1,1,2,3,4,3,4,6,7,8,9,0,5,4,3,2,1,1]
list_of_.sort() 
print(list_of_)
#copy()
a=[1,4.5,"python",[1,3,6],True]
b=a.copy()
print(a)
print(b)

#reverse
a=[1,4.5,"python",[1,3,6],True]
a.reverse()
print(a) 

#printing list in decending order
num_=[1,2,1,5,3,2,7,5,9,8,7]
num_.sort(reverse=True)
print(num_)

# Note: i used same var names for some list methods so before perform any method kindly comment the remaining variables in diff methods
