#File Mode --> 'r', 'w', 'a'
#r mode --> Will make a file to be read if already created
#w mode --> Creates a new file, it also overwrited the existing file

'''
with open('sample.txt','w') as f:
    f.write("Hi there hows ur day")

with open('sample.txt','a') as f:
    f.write("\nHi there hows ur day")
'''

'''
write a python program for a placement attendence analyzer. Read attendence percentage for 5 students, validate each value is between 0 and 100, calculate the average,print the lowest and
highest attendence, and list students eligible when attendence >= 75. Use at least one function.

write clean,executable python. Mention any assumptions.

'''
#First we will define the function to take eligible
def eligible(attendance):
    """Eligibility Check"""
    return attendance >= 75

#To take marks of students we will create a list
student = []
for i in range(5):
    name = input(f"Enter the student name:{i + 1}) ")
    while True:

        #Exception handling to check all cases of +ve, -ve
        try:
            attendance = float(input(f"Enter the attendance for {name} in 0 - 100: "))

            #if attendace >= 0 and attendance <= 100
            if 0 <= attendance <= 100:
                break
            print("Enter value only between 0 - 100")

        except ValueError:
            print("Enter only +ve values and make sure its in given range")
    student.append((name, attendance))
print(student)

result = [att for (name, att) in student]
print(result)

avg = sum(result) / len(result)

print(f"Average: {avg}")
print(f"Highest Attendance is {max(result)}")
print(f"lowest Attendance is {min(result)}")

#To list eligible students
print("Eligible Students list: ")

for name, attendance in student:
    #Now we will use our function here
    if eligible(attendance):
        print(f"Student name is {name} - attendance is {attendance}")
























