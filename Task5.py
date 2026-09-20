import segno

# Developer Profile Details
profile =( """
================================
        DEVELOPER PROFILE
================================

Name: Deepika Barnikala

Role: Python Full Stack Developer

Skills:
Python
SQL
HTML
CSS
JavaScript
Bootstrap
React

Email:
deepikabarnikala0410@gmail.com

LinkedIn:
https://www.linkedin.com/in/deepika-barnikala-ab5a4b301/?trk=opento_sprofile_topcard

GitHub:
https://github.com/DeepikaBarnikala

YouTube:
https://www.youtube.com/

Instagram:
https://www.instagram.com/deepika_barnikala/

================================
        THANK YOU!
================================
""")

# Create QR Code
qr = segno.make(profile)

# Save QR Code
qr.save("developer_profile.png", scale=10)

print("Developer Profile QR Code Created Successfully!")
