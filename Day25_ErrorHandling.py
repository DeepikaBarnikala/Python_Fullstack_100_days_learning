''' Error Handling:

Syntax error:
----------------
for j in range(1,10:
    print(j)
output: SyntaxError

Indentation Error:
-------------------
a=20
if a>=10:
print("Greater num") #raises error
else:
    print()
Output:IndentationError

ValueError:(Raised when a function receives the right type of argument but an inappropriate value.)
------------
a=int(input("enter a num:"))
Output:ValueError 

try
-------
The try block will test the code for error
syntax: try:

except:
----------
This except let us handle the errors in the code
syntax: except:

else:
----------------
If the try block doesnot have any error then the else block will execute.
sSyntax: else:

finally:
----------------
This block will executes whether the code has errors or not.
Syntax: finally:

try:
    n=int(input("enter a num:"))
except :
    print("Will get name error")
--------------------------------
try:
    n=int(input("enter a num:"))
except NameError:
    print("Will get name error")
-------------------------------------
try:
    n=int(input("Enter a num:"))
    n2=int(input("enter another num:"))
    print(n/n2)
except:
    print("Will get zero division error")

n=int(input("Enter a num:"))
n2=int(input("enter another num:"))
print(n/n2)'''


try:
    n=int(input("Enter a num:"))
    n2=int(input("enter another num:"))
    print(n/n2)
except ZeroDivisionError:
    print("Will get zero division error")
except ValueError:
    print("will get value error")
else:
    print("No Error")
finally:
    print("End.")






































                   
