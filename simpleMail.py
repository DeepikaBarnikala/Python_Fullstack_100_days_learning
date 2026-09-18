'''
Now we are adding an attachment along with subject to send email...
'''

import smtplib
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase #loading the attachment as header file
from email import encoders #encoder the file into binary format
#now we can directly insert earlier subject mail code and add the attachment

#now we will provide the details
From = "deepikabarnikala0410@gmail.com"
To = "barnikaladeepika.22.eee@anits.edu.in"
subject = "Python full stack Training"
attach="mail_automation.py"  #make sure the file is in same location
body = "We have understood how to send automated emails using Python"
#Now we will check all the details and throw it to Multipart

msg = MIMEMultipart()
#print(msg)
#print(type(msg))
msg['From'] = From
msg['To'] = To
msg['Subject'] = subject
msg.attach(MIMEText(body))
#now we need to add attachment to our mail
part=MIMEBase('application','octet-stream')
print(part)
part.set_payload(open(attach).read())
encoders.encode_base64(part)
#lets add the header to our filename
part.add_header(f'Content-Disposition',f'attachment;filename={os.path.basename(attach)}')
#part.add_header('Content-Disposition','mail_automation.py)
msg.attach(part)
#finally convert this to string
text=msg.as_string()
#include your smtplib code
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("deepikabarnikala0410@gmail.com","tmmq uqlx wmxv pohw")
server.sendmail(From,To,text)
server.quit()
print("Mail Sent")
