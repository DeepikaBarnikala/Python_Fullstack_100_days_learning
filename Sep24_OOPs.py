'''
OOP -->Encapsualtion,Inheritance,Polymorphism,Abstraction

#Abstraction -->It is the process of hiding necessary details and display/acces
#relevant information only --> abc module
#Instagram --> Photo,Video,Reel

import abc
#print(dir(abc)) #returns the available methods,classes...
from abc import ABC,abstractmethod

#Now we will create some base classes to have abstraction applied for all classes
class Content(ABC):
    @abstractmethod
    def upload(self):
        #self.number = 34
        pass
class Photo(Content):
    """This derived class will have upload features"""
    def upload(self):
        print("Photo is Uploaded Successfully")
        print("Photo is compressed and edited as per filters choosen")
        print("Photo is Posted")
class Video(Content):
    """This derived class will have video upload features"""
    def upload(self):
        print("Encoding the video")
        print("Compressed and filters are added")
        print("Edited video is published successfully")
class Reel(Content):
    """This derived class will have reel uploading features"""
    def upload(self):
        print("Timing and content is chosen")
        print("Reel content is mapped with time and audience")
        print("Reel is edited and uploaded successfully")

contents = [Photo(),Video(),Reel()]
print(contents)
for content in contents:
    content.upload()


#Projects -->OOP -->Monday before class




















