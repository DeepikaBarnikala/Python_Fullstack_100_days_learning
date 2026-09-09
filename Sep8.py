'''
#Control Block (if,elif,else,for,while,break,continue)

#BMI UseCase--->BMI (Body Mass Index)

#BMI=(weigth)/((height)**2))
#weight-->kgs
#height-->meters

#feet -->12 inches -->inch -->2.54

#BMI Chain Rule

< 18.5 -->Under Weight
18.5 - 24.9 -->Normal weight
25-29.9 -->Over Weight
 >=30 -->Obesity

number_of_times_user_input=int(input("Enter the Values:"))
for i in range(number_of_times_user_input):
    #weight=75
    weight=float(input("Enter the weight in Kgs:"))
    #height=1.45
    height=float(input("Enter the height in meters:"))

    name=input("Enter Your name:")

    if weight>0 and height>0:
        bmi=(weight)/((height)**2)
        
        if bmi<18.5:
            print(f'{name} is into Under Weight category and BMI is {bmi}')
        elif  18.5<=bmi<=24.9:
                print(f'{name} is into Normal Weight category and BMI is {bmi}')
        elif 25<=bmi<=29.9:
            print(f'{name} is into Over Weight category and BMI is {bmi}')
        elif bmi>=30:
            print(f'{name} is into Obesity category and BMI is {bmi}')
     
    else:
        print("Enter Only Positive values")



#task-->Store the results of name,weight,height --> BMI into a collection


#Repetition -->While
# same above task we need to handle the erros(Expection handling) and also
#Make user strictly to enter only numeric values
'''
results = []
number_of_users = int(input("Enter the number of users: "))
for i in range(number_of_users):
    while True:
        try:
            name = input("Enter your name: ")
            weight = float(input("Enter the weight in Kgs: "))
            height = float(input("Enter the height in meters: "))

            if weight > 0 and height > 0:
                break
            else:
                print("Enter only positive values")

        except ValueError:
            print("Enter only numeric values for weight and height")

    bmi = weight / (height ** 2)

    if bmi<18.5:
        print(f'{name} is into Under Weight category and BMI is {bmi}')
    elif  18.5<=bmi<=24.9:
        print(f'{name} is into Normal Weight category and BMI is {bmi}')
    elif 25<=bmi<=29.9:
        print(f'{name} is into Over Weight category and BMI is {bmi}')
    elif bmi>=30:
        print(f'{name} is into Obesity category and BMI is {bmi}')

    result = {
        "name": name,
        "weight": weight,
        "height": height,
        "BMI": bmi,
    }

    results.append(result)

print("\nBMI Results:")

for result in results:
    print(result)






