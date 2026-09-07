email_id="saketh@codegnan.com"
print(email_id[7:15])

emailIds=["saketh@codegnan.com","deepikabarnikala@gmail.com","diyaSeela@gmail.com","ceo@codegnan.com"]
'''print(len(emailIds))
print(emailIds[1])
print(emailIds[-2:])
emailIds.extend(["sample@gmail.com","info@gmail.com","support@gmail.com"])
print(emailIds)
print(str(emailIds[1:9]))
for i in emailIds:
    print(f'mail id of the person is: {i}')
emailIds.extend(["sample@gmail.com","info@gmail.com","support@gmail.com"])
print(emailIds)

users={}
users=dict.fromkeys(emailIds)
print(users)'''
emailIds.extend(["sample@gmail.com","info@gmail.com","support@gmail.com"])
print(emailIds)
users={}
#using loops
for i in range(len(emailIds)):
    users[i+1]=emailIds[i]
    #print(i)
print(users)

#enumerate--> it provides by default a counter object(you can store in desired collection)
data=dict(enumerate(emailIds,1))
print(data)
          
print(dict(enumerate(users)))
print(dict(enumerate(emailIds)))
print(dict(enumerate(users,1)))
print(dict(enumerate(emailIds,1)))

#python-object
#functions--> first class objects
#Set is an unordered collection as no indexing




 

















  
