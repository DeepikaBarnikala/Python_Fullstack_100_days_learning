#every pyhton file--> Module --> import keyword--> __name__-->

'''
import Sep10
print(dir(Sep10)) #dir-->directory will return all available methods, attributes
print(type(Sep10.employees))
print(type(Sep10.details))
Sep10.employees("Saketh",designation="Co-founder",
                location="Vizag")
print(Sep10.details.keys())
print(Sep10.details['Organization'])
Sep10.details.update({'batches':['PFS','JFS','DA','DS','AAA'],
                      'employees':200})
print(Sep10.details)


#from keyword
import Sep10
from Sep10 import employees,details
details.update({'batches':['PFS','JFS','DA','DS','AAA'],
                      'employees':200})
print(details)
print(Sep10.__doc__) '''

#built-in modules in python --> math,random,os,datetime
#we download modlues-->pypi(pyhton package index)

#Build a QRcode Scannerusing Python --> Linkedin QR
#pip install pyqrcode
#pip install pypng

import pyqrcode
import png
link="https://www.linkedin.com/in/deepika-barnikala-ab5a4b301/?trk=opento_sprofile_topcard"
qr=pyqrcode.create(link)
#print(qr)
qr.png("My_linkedIn.png",scale=10)
