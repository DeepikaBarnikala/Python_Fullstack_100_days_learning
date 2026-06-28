''' Set: set is a collection of unordered elements that are separated by ,
-->set is mutable
-->can remove duplicate value by itself
-->represented by {}
methods in set:
1. union()--> symbol- | --> used to combine the elements
2.intersection--> & --> gives common element from the both sets
3. symmetric_difference()--> removes common elements from the sets and return the combined set--> ^

4. add() --> used to add new element into set at the last position
5.update()-->adds multiple elements from a list,tuple or another set.
6. remove()--> to delete the element from the set based on element ie removes a specific element
if no element found then raises a key error
7. pop()--> removes last element from the set or an arbitary element
8.discard()-->removes an element if present but doesnt  raise an error if the element is absent
9.clear()-->revomes all elements and output is set()'''
sample_={1,2,3,4,5,6}
print(sample_)
print(type(sample_))
#set operations
sample_2={3,4,5,6,7,8,9}
print(sample_ | sample_2)
print(sample_.union(sample_2))
print(sample_2.union(sample_))
print(sample_.intersection(sample_2))
print(sample_2.intersection(sample_))
print(sample_ ^ sample_2)
print(sample_ - sample_2) #difference A-B
print(sample_2 - sample_) #B-A
print(sample_.symmetric_difference(sample_2))

go={1,2,3,4,4,4,5,2,1,2,3,3}
print(go) #prints unique values only no duplicates
colors_={"red","green","pink","black"}
print(colors_) #unordered ie output order may differ each time.
#built in functions in sets
so={1,2,5,3,6,4,9,8,7}
print(len(so))
print(max(so))
print(min(so))
print(sum(so))
print(type(so))
print(sorted(so))

fruits={"apples","banana","mango"}
print(fruits)
fruits.add("orange")
print(fruits)
fruits.update(["grapes","kiwi"]) #list
fruits.update({"cherry","watermelon"})#set
print(fruits)
fruits.remove("grapes")
print(fruits)
fruits.discard("orange")
fruits.discard("papaya")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)


