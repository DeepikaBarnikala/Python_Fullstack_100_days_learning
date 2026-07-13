'''
SMTP module
email.message
bgqw rwgl gnli hyja '''
import smtplib
import ssl
from email.message import EmailMessage
sender_email="deepikabarnikala0410@gmail.com"
password="bgqw rwgl gnli hyja"

receiver_email="deepikabarnikala@gmail.com, barnikaladeepika.22.eee@anits.edu.in"
message=EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="Welcome Mail: Your Offer Letter from XXXXX PVT LTD"
message.set_content(f"""Dear Deepika Barnikala,Greetings from xxxxxx Pvt. Ltd.
Hope this email finds you well.
Congratulations once again on your successful selection for the position at NXT SYNC Pvt. Ltd.!
We are excited to have you join our team.Please note that your official internship offer letter has been sent to your email.
Kindly check your inbox for the document that outlines your role, onboarding date, stipend, and other relevant details regarding your internship.
Please revert back to the same email with I AGREE within the next 2 Business Days so that we can proceed ahead with your Background Verification and Onboarding process.
If you have any questions or need further clarification regarding the offer letter, feel free to reach out to the HR team.
We look forward to working with you and wish you a successful start to your journey with us!

Best regards,
9xxxxxxxx1/ 90xxxxxxxx
Kavuri Hills, Madhapur, Hyderabad, TG – 500033
""")
context=ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com" , port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email, password)
    smtp.send_message(message) 
