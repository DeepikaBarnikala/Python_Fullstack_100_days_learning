Python Introduction.

Python is a high-level, interpreted, Object oriented programming language that is easy to read and write. It was created by Guido van Rossum and first released in 1991.

What is Python?

Python allows programmers to write instructions that computers can understand and execute. It is used for:

* Web development
* Data analysis
* Artificial Intelligence (AI) and Machine Learning
* Automation and scripting
* Game development
* Scientific computing
* Cybersecurity

eg:print("Hello, World!")

output:Hello, World!

----------------------------------------------------------------------------------------------------------------

Why Python?

Python is popular because:

**Easy to Learn**

Simple and readable syntax.

Great for beginners.

**Versatile**

Can be used in many fields, from websites to AI.

**Large Community**

Millions of developers use Python and share resources.

**Rich Libraries**

Thousands of ready-made packages help you build applications faster.

**Cross-Platform**

Runs on Windows, macOS, and Linux.

**High Demand**

Widely used by companies and organizations worldwide, including Google, Netflix, and Spotify

**Dynamically Typed**

You don't need to tell Python the data type of a variable. Python automatically figures it out while the program runs.

**Interpreted Language**

Python code is executed line by line by an interpreter, instead of being fully converted into machine code before execution. If error raises at any line of the code the execution will stops and it won't executes the further lines in the code.

----------------------------------------------------------------------------------------------------------------

**Procedural Programming lang VS OOP lang:**

Procedural Programming---> What steps to do.

Program is written as a step-by-step set of instructions (functions).Programming focuses on procedures/functions.
Languages: C, Pascal

Object-Oriented Programming (OOP)---> How to do

Program is organized around objects (things that have data and actions).Programming focuses on objects and classes.

Languages: Python, Java, C++

----------------------------------------------------------------------------------------------------------------

**Tokens**

Definition: Tokens are the smallest meaningful units in a Python program. Python breaks your code into tokens before executing it.

Types of Tokens

a) Keywords
Reserved words that have a special meaning in Python.

eg: if, else, for, while, True, False etc

age = 20
if age >= 18:
   print("Eligible")

b) Identifiers
Names given to variables, functions, classes, etc.

name = "Deepika"
age = 22

Here:
name → Identifier
age → Identifier

c) Literals
Fixed values written directly in code.

age = 22
name = "Deepika"

Here:
22 → Integer Literal
"Deepika" → String Literal

d) Operators
Symbols that perform operations.

a = 10
b = 5
print(a + b)

Output:
15
Here + is an operator.

e) Separators
Used to separate code elements.

print("Hello")

Here:
( and ) are separators.

----------------------------------------------------------------------------------------------------------------

2). Comments

Comments are notes written for programmers. Python ignores comments during execution.

* Single-Line Comment--> #

#This stores employee salary
salary = 25000

-->Use when explanation fits in one line.

* Multi-Line Comment ---> ''' ''', """ """.

""" Employee Management System

Created by Deepika

Version 1.0 """

--->Used for: Documentation, Program description, Long explanations 

----------------------------------------------------------------------------------------------------------------
**Variables in Python**

What is a Variable?

A variable is a named memory location used to store data values.
Think of a variable as a labeled container that stores information.

Example:
name = "Deepika"
age = 22

Here:
name stores "Deepika"
age stores 22

* Creating Variables
  
Variables are created automatically when a value is assigned.

Example
city = "Hyderabad"
salary = 25000

* Displaying Variable Values

name = "Deepika"
age = 22
print(name)
print(age)

Output:
Deepika
22

* Variable Naming Rules

Python follows specific rules while naming variables.

**Rule 1**: Must Start with a Letter or Underscore

Valid
name = "Deepika"
_age = 22

Invalid
1name = "Deepika"
Error: SyntaxError

**Rule 2**: Cannot Start with a Number  

Invalid
100marks = 95

Valid
marks100 = 95

**Rule 3**: Can Contain Letters, Numbers, and Underscores

Valid
student_name = "Deepika"
student1 = "Ravi"

Invalid
student-name = "Deepika"

Hyphen (-) is not allowed.

**Rule 4**: Variable Names are Case Sensitive

name = "Python"
Name = "Java"
print(name)
print(Name)

Output:
Python
Java

**Rule 5**: Keywords Cannot Be Used as Variable Names

Invalid
class = "Python"
Valid
course_class = "Python"

----------------------------------------------------------------------------------------------------------------
**Naming Conventions**

* Snake Case (Recommended)
  
student_name = "Deepika"
total_marks = 450

* Camel Case
  
studentName = "Deepika"

* Pascal Case
  
StudentName = "Deepika"

**Multiple Assignment**

Multiple assignment allows assigning values to multiple variables in a single statement.

* Assign Different Values

name, age, city = "Deepika", 22, "Hyderabad"
print(name)
print(age)
print(city)

Output:
Deepika
22
Hyderabad

* Assign Same Value to Multiple Variables
  
x = y = z = 100
print(x)
print(y)
print(z)

Output:
100
100
100

* Reassignment
  
Reassignment means changing the value stored in a variable.

Example:

age = 22
print(age)
age = 23
print(age)

Output:
22
23

* Reassigning Different Data Types
  
Python is dynamically typed.

value = 10
print(value)
value = "Python"
print(value)
value = True
print(value)

Output:
10
Python
True

**Variable Swapping**

Swapping means exchanging values between variables.

* Traditional Method
a = 10
b = 20

temp = a
a = b
b = temp

print(a)
print(b)

Output:
20
10

* Pythonic Way (Recommended)
a = 10
b = 20
a, b = b, a
print(a)
print(b)

Output:
20
10

**Deleting Variables**

Python provides the  "del" keyword to remove variables from memory.

* Syntax:
del variable_name
Example
name = "Deepika"
del name

#Attempting to access it again:

print(name)
Output
NameError: name 'name' is not defined

**Deleting Multiple Variables**

x = 10
y = 20
del x, y

**Variable Type Checking**

Use the type() function.

Example:

name = "Deepika"
age = 22
print(type(name))
print(type(age))
Output:
<class 'str'>
<class 'int'>

----------------------------------------------------------------------------------------------------------------
**Boolean Data Type**

Boolean is a built-in data type that represents logical values.
A Boolean variable can have only one of two values:
True
False

* Why Boolean is Important?

Booleans are used in:
Decision making
Conditions
Loops
Comparisons
Authentication systems
Real-world logical operations

* Creating Boolean Values
#Direct Assignment
is_student = True
is_employee = False

print(is_student)
print(is_employee)

Output:
True
False

* Boolean Type Verification
  
value = True
print(type(value))
Output
<class 'bool'>

1.Stores True or False

2.Used in conditions and comparisons

3.Created directly or through comparisons

4.Checked using type()

5.Converted using bool()

6.Includes Truthy and Falsy concepts

















