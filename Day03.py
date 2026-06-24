#Strings: sequence of the characters that are enclosed in '',"",""" """. It's Immutable ie the values can not be changeable.

#concatination
First_name="Deepika"
Second_name="Barnikala"
print(First_name+" "+Second_name)
#indexing
a="Python is a interepreted language"
b="   Python  "
c="bnahvxhsxhzy"
d=["python","is","a","interpreted","language"]
print(b+c)# + operator performs concatination of strings
print(a[12]) #positive index
print(a[-2]) #negative index
#replace-->Used to chnage any sub-string in the main-string.
print(a.replace("Python","Java"))
print(a.replace("a","A",3)) # 3 tells replace 3 a's with 3 A's
print(a.upper())#all letters in strings will be upper
print(a.lower())#strings converts intlo lowercase
print(a.capitalize())#First letter of the string will be capital
print(a.title()) #first letter of each word will be capital
print(len(a)) #total length of the string-->inbuilt str function
print(a.swapcase())#upper to lower and vice versa
print(a.find("i"))#returns position of a particular char
print(a.count("a"))#counts a char occurance
print(a.split("is"))#converts str into list
print(a.split())
print(b.strip())#remobes spaces from both ends
print("-".join(d))#joins list elemnts intlo string
print("$".join(a))#used to combine multiple strings into a single string using a separator.
print(max(c))#gives max letter char in the alphabetical order
print(min(c))#gives smallest char in alphabetical order before that min func will consider "whitespace" as min value 
print(b)
print(a)
print(c)

'''
time_="16:56" #conversion of time 
parts_=time_.split(":")
print(type(parts_))
print(type(time_))
print(int(parts_[0])- 12,":",parts_[1]) '''



