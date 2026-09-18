'''
scenario to understand(*args,**kwargs)
Modules--> some intresting cases --> projects(virtual assistance, emial automation)
00p--> github(branch)


def employees(*names,**settings):
    """ Employee details along with their settings"""
    print("Employee Names")
    for employee in names:
        print("-------------")
        print('-',employee)
    for key,value in settings.items():
        print("Key is",key)
        print("value is",value)
employees("Deepika","Divya","Srinivas",
          department="Operations",
          experience_letter=True,
          salary=True)

Package
   |
Module-->A module is a simple python file(reusable,organized code etc)

Module
import keyword

   |
organization--> Class
   |
Employeees-->Function
Performance Metrics-->Function
Increment-->Function
   |
Emp1,Emp2,Emp3....-->Objects
'''
#Employee details

def employees(*names,**settings):
    """ Employee details along with their settings"""
    print("Employee Names")
    for employee in names:
        print("-------------")
        print('-',employee)
    for key,value in settings.items():
        print("Key is",key)
        print("value is",value)
employees("Deepika","Divya","Srinivas",
          department="Operations",
          experience_letter=True,
          salary=True)
#if __name__="__main__":

details={'Organization':'Codegnan',
         'Year':2018,
         'Branches':['Vijayawada','Hyderabad','Visakhapatnam']}
print(__name__) #Dunder methods--> Magic Methods























