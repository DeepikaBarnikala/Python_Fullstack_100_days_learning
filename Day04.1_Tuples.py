''' Tuple: tuple is a collection of diff datatypes and is immutable and represented by ()
ordered, immutable, allows duplicates ,mixed data types
methods--> index(),count()'''
how=(1,2,3,4,"Python",[4,5],(90,78))
print(type(how))
print(how) #mixed data types
print(how[4])
print(how[-3])#can perform indexing
print(how) #immutable
print(len(how))
# built-in functions
num=[1,2,3,4,4,5,6,10,10,10,1]
print(tuple(num[3:7])) #here slicing will return a list so i used tuple() func to chnage the list into tuple
print(max(num))
print(min(num))
print(sum(num))
print(sorted(num)) # this sorted fun will sorts the tuple in ascending order and returns a "list"
print(tuple(sorted(num)))# this tuple() func will convert a list into tuple
#methods
print(num.count(10))#count() method counts how many times an element appears
print(num.index(10))# returns the first index of the specified element


t=(1,2,3)
print(t*3)#tuple repetetion
s=(4,5,6)
print(s+t) #tuple concatination
#lets try to modify the tuple
t[1]=5
print(t)
