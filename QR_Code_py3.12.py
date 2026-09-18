import pyqrcode
import png

#create a QRCode by giving link
link="https://www.linkedin.com/in/deepika-barnikala-ab5a4b301/?trk=opento_sprofile_topcard"
qr=pyqrcode.create(link)
#print(qr)
qr.png("myqr.png",scale=10)

#personal businessCard-->name,PhnNo,emailId,website etc
