'''Dictionary: It is a key:value pair and separated by : ,
keys are unique ie no duplicates and values can be duplicated.
--> represented by using {} and dict is ordered
--> dict is mutable because we can update key values
methods:
keys()--> used to get all keys from the dict
syntax: var_name.keys()
values()--> used to get all the values from the dict
syntax: var_name.values()
items()---> we'll get both keys and values
clear()--> used to remove all the key:val from dict--> result is empty dict
get()--> returns specific key value and if key isnot present in dict it will returns None.
pop()-->removes a spe ific key
'''
ICIC_details_ = {"name": "Deepika",
                 "mobile":1234567890,
                 "Adhar":"123456787654",
                 "AC num": 987652,
                 "ATM PIN":"7789",
                 "age": 22,
                 "Gender":"F"}
print(ICIC_details_)
print(type(ICIC_details_))
# dict methods
print(ICIC_details_.keys())
print(ICIC_details_.get("AC num"))
print(ICIC_details_.values())
print(ICIC_details_.items())
print(ICIC_details_ ["name"])# accessing values with keys
ICIC_details_.pop("age")
print(ICIC_details_)

#clearing a dict using clear() method
details_={
    "name":"Sumanth",
    "Age":25,
    "Gender": "M"}
print(details_)
#updating a dict
details_.update({"Name":"Rishikesh"})
details_.update({"Age":27})
details_.update({"mob":9347808977})
print(details_)
details_.clear()
print(details_) 
