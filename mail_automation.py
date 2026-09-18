'''
Simple Mail Automation
Mail Otp
Mail with subject & Attachments
Bulk Mail

#Simple Mail Automation
#SMTP-->Simple mail transfer protocal

import smtplib
#first lets make server connection
#port address and host
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("deepikabarnikala0410@gmail.com","tmmq uqlx wmxv pohw")
msg="Hello sir, You are the best Python mentor that I have ever seen"
server.sendmail("deepikabarnikala0410@gmail.com","saketh@codegnan.com",msg)

#close the connection
server.quit()
print("Mail.sent")



#now let's send OTP to mail and validate the script

import math
import random
import smtplib
import string
#first lets make server connection
#port address and host
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("deepikabarnikala0410@gmail.com","tmmq uqlx wmxv pohw")
OTP=random.randint(1000,9999)
msg=f"your OTP is {OTP}"
server.sendmail("deepikabarnikala0410@gmail.com","barnikaladeepika.22.eee@anits.edu.in",msg)

#close the connection
server.quit()
print("Mail.sent") #-->

#in this case I will use math and random modules together
#first lets make server connection
#port address and host
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("deepikabarnikala0410@gmail.com","tmmq uqlx wmxv pohw")
digits='123456789'
otp=""
for i in range(4):
    otp+=digits[math.floor(random.random()*10)]  #otp=otp+
    #print(otp)
msg=f'Your OTP is {otp}'
server.sendmail("deepikabarnikala0410@gmail.com","barnikaladeepika.22.eee@anits.edu.in",msg)
a=input("Enter the OTP received")
if a==otp:
    print("Access Granted")
else:
    print("Timed Out")
#close the connection
server.quit()
print("Mail.sent")
'''
import email
import smtplib

#MIME - Multipurpose Internet Mail Extention

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#now we will provide the details
From = "deepikabarnikala0410@gmail.com"
To = "barnikaladeepika.22.eee@anits.edu.in"
subject = "Python full stack Training"
#Now we will check all the details and throw it to Multipart

msg = MIMEMultipart()
#print(msg)
#print(type(msg))
msg['From'] = From
msg['To'] = To
msg['Subject'] = subject
text = "Hey guys, what's the learning plan for this week"
#msg.attach(text)

msg.attach(MIMEText(text, "plain"))

# SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login
server.login("deepikabarnikala0410@gmail.com", "tmmq uqlx wmxv pohw")

# Send mail
server.sendmail(From, To, msg.as_string())

# Close server
server.quit()

print("Mail sent successfully")



















                





