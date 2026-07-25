'''
Matplotlib:
-----------
Matplotlib library is an pyhton library that provides functionality to charts, graphs,
bar and data visualization.

line plot:
-----------

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,15,30,5]
plt.plot(x,y)
plt.title('Sample plot')
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()

import matplotlib.pyplot as plt
x=[2026,2025,2024,2023,2022]
y=[120,150,135,95,80]
plt.plot(x,y)
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number Of Cars')
plt.show()

#bar plot:
-----------
import matplotlib.pyplot as plt
x=[2026,2025,2024,2023,2022]
y=[120,150,135,95,80]
plt.bar(x,y, color='violet', edgecolor='black')
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number Of Cars')
plt.show()

import matplotlib.pyplot as plt
x=['BMW','BENZ','AUDI','KIA','HONDA']
y=[120,150,135,95,183]
plt.bar(x,y, color='yellow', edgecolor='black')
plt.title('Car Sales')
plt.xlabel('CAr Brand')
plt.ylabel('Number Of Cars')
plt.show()

import matplotlib.pyplot as plt
subjects_=['Python','java','C','MySQL','C++']
student_=[60,58,82,80,70]
plt.pie(student_, labels=subjects_, colors=['red','purple','green','blue','yellow'], autopct='%1.1f%%')
plt.legend(subjects_)
plt.title('Courses')
plt.show()


import matplotlib.pyplot as plt
x=['BMW','BENZ','AUDI','KIA','HONDA']
y=[120,150,135,95,183]
plt.scatter(x,y, color='black')
plt.title('Car Sales')
plt.xlabel('CAr Brand')
plt.ylabel('Number Of Cars')
plt.show()'''

import matplotlib.pyplot as plt
y=[10,20,30,40,50,60,70,80,90,100]
plt.hist(y,bins=30)
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Num of Cars")
plt.show()

































