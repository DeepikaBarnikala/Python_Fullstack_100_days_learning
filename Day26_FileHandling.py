'''
File Handling:
File Handler is an object that gives more options like creating, updating.

there are two ways to open a file..
1.open():
syntax:
do=open('file name', 'mode')
#statements
close()
-------------------------
2.with (keyword):
syntax:
with open('file name', 'mode') as do:

do=open('any.txt','r')
print(do.read())
close()

Modes:
-------------
r-->used to read the file, incase if the file is not present it will raise error.
eg:
with open('any.txt','r') as do:
    print(do.read())
    
w-->used to write the text inside the file and it will override the text inside the file and
in result console it will give the count of the char or length of the txt.
if the file is not exixted then it will create new file with the given text.
eg:
with open('any.txt','w') as do:
    print(do.write("This is pyhton file"))

with open('an.txt','w') as do:
    print(do.write("This is pyhton file"))
    
a-->this is usde to add the text  at the last position inside the file.
eg:
with open('any.txt','a') as do:
    print(do.write("  Python is a high level interpreted language."))
    
x-->used to create a new file by adding inside the file.
eg:
with open('demo.txt','a') as do:
    print(do.write(" we are using file handling..."))

functionalities
-----------------
1.write()
-->this function is used to add the text inside a file or update a file with new text...
eg:
with open('an.txt','w') as do:
    print(do.write("This is pyhton file"))

2.read()
--> used to read  a file and this read() will read file chunk by chunk... we can also specify the size

eg:

with open('any.txt','r') as do:
    print(do.read(10))
    
3.readline()--> this readline() function will read the only one line at a time.
eg:
with open('any.txt','r') as do:
    print(do.readline())
    
4.readlines()-->
'''

with open('demo.txt','r') as do:
    print(do.readlines())





