''' Type Conversion: The process of converting one data type to another type
Built-in functions:
str()
int()
float()
list()
tuple()
dict()

note:comment each section while running the other section'''
#Integer--> String, Float
num=89
print(type(num))
num=float(num)
print(num)
print(type(num))
so=8725
print(type(so))
so=str(so)
print(so)
print(type(so))
#Float--> String & float-->int
n=8.9
n=str(n)
print(n)
print(type(n))
for i in n:
    print(i)
num_2=int(n)
print(num_2)
print(type(num_2)) 
#str-->int,float
hai="78"
num=int(hai)
print(num+10)
hello="67.89"
num_2=float(hello)
print(num_2)
print(num+num_2)
#str-->list,tuple
any_="Python"
con_=list(any_)
print(con_)
con_2=tuple(any_)
print(con_2) 
#list --> str,tuple,dict
var_=['p','y','t','h','o','n']
text=str(var_)
for i in text:
    print(i)
con_="".join(var_)
print(con_)
some=tuple(var_)
print(some)

pyth_=[('a',1),('b',8)]
convert=dict(pyth_)
print(convert)

#tuple-->list,str,dict
tuple_=(1,2,3,4,5,6,7,8,9)
print(list(tuple_))
tuple_2=('h','e','l','l','o')
print(tuple_2)
text_2="".join(tuple_2)
print(text_2)
pyth_=(('a',1),('b',8))
convert=dict(pyth_)
print(convert)















































