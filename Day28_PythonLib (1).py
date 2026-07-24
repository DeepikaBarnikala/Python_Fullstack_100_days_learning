'''

                        DAY 28 - PYTHON CONCEPTS
                        -------------------------
datetime:
----------
%d -> day in the month
%m -> month in the year
%Y -> year
%H -> hour
%M -> minute
%S -> second
%I -> 12 hour clock
%p -> AM or PM

ex:
---
from datetime import datetime
current = datetime.now()
print(current)
print(current.strftime('%Y'))
print(current.strftime('%m'))
print(current.strftime('%d'))
print(current.strftime('%d/%m/%Y %H:%M:%S'))
print(current.strftime('%d/%m/%Y %H:%M:%S %p'))

import calendar
print(calendar.calendar(2026))
print(calendar.month(2026,7))
print(calendar.weekday(2026,7,24))
print(calendar.isleap(2026))

Data Analysis
-------------
Data Analysis is the process of inspecting, cleaning, transform and modeling data to discover useful insights, support decision-making, and identify patterns.
It is widely used in industries such as finance, healthcare, marketing and technology.

Types of Data Analysis:
-----------------------
1. Descriptive Analysis - Summarizing data
Ex: Avg saler for month
2. Diagnostic Analysis - Understanding causes
Ex: Why sales dropped
3. Predictive Analysis - Forecasting future Outcomes
Ex: Predicting customer churn
4. Prescriptive Analysis - Suggesting actions based on data
Ex: Best marketing strategies

Numpy
-----
--> Numpy is a library in python which is known as numerical python
--> This Numpy have different dimensional arrays such as 1D,2D,3D
--> To used the Numpy we have to import library as import numpy as np
ex:
---
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)

Indexing in array
------------------
-> As we used indexing in the list or tuple , here the way it works
-> By calling index position from array, we will the get the value
-> And Negative indexing also willl work

ex -> Negative Indexing
------------------------
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)
print(arr_1[-1])

ex -> Normal Indexing
----------------------
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)
print(arr_1[1])

ex:
---
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1)
print(arr_1[:2])

print(arr_1.sum())
print(arr_1.mean())
print(arr_1.max())
print(arr_1.min())

import numpy as np
arr_1 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(arr_1)
print(arr_1.reshape(4,3))

Pandas:
-------
-> pandas is an powerful python library and this is built on the top numpy
-> By uased pandas data manipulation will be done....
-> Pandas have data structers like series and dataframes
-> to use this we have import library pandas  

Series:
-------
ex:
---
import pandas as pd
data = pd.Series(
    [2000,4000,7000],
    index=['Earphone','Charger','MObile']
    )
print(data)

DataFrame:
----------
ex:
---
import pandas as pd
df = {
    'products' : ['Laptop','Charger','Mobile'],
    'brand' : ['Mac','Realme','Iphone'],
    'price' : [5700,1500,2500],
    'stocks' : [5,15,9],
    'sales' : ['Amazon','Offline','Flipcart']
    }

data = pd.DataFrame(df)
print(data)
'''



