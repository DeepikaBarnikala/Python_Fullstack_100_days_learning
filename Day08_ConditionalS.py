'''
statements-->3 types
1.conditional--> if ,if-else,elif,nested if
2.control statements-->pass, break,continue
3.looping--> for, while
1.Conditinal Statements:Its makes a decision based on whether a condition is True or False '''
#if--> executes the block only if condition is True and if ans is false so no output willbe displayed.
num=9
if num%2==0:
    print("Even number") 

#if-else--> also called fallback statement,if condition is false then, else block will be executed.
age=int(input("enter age:"))
if age>=18:
    print("eligibel to vote")
else:
    print("not eligible")

#nested if -->if inside the if 
Deepika_BankDetails={'ATM PIN': '7337'}
pin_=input("Enter your valid pin:")
if len(pin_)==4:
    if pin_ in Deepika_BankDetails['ATM PIN'] 
        print("Welcome")
    else:
        print("Enter valid pin")
else:
    print("Enter 4 digit valid pin only.")

#elif--> used when multiple conditions are there
marks=float(input("Enter your marks:"))
if marks>=90:
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B+")
elif marks>=60:
    print("B")
elif marks>=50:
    print("C")
else:
    print("Fail")



