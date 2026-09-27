
# EMPLOYEE MANAGEMENT SYSTEM

#EMPLOYEE CLASS

class Employee:
    #Class variable
    employee_count = 0

    def __init__(self, name, salary):

        # Encapsulation
        # Private attribute
        self.__name = name
        self.salary = salary

        # Increase employee count
        Employee.employee_count += 1

    # Public method to access private name
    def display(self):

        print("Name:", self.__name)

    # General details method
    def details(self):

        print("Employee Details")
        print("Name:", self.__name)
        print("Salary:", self.salary)

    # STATIC METHOD
    @staticmethod
    def get_employee_count():

        return Employee.employee_count

    # CLASS METHOD

    @classmethod
    def get_employee_count_classmethod(cls):

        return cls.employee_count

    # OPERATOR OVERLOADING
    # print(employee)
    def __str__(self):

        return self.__name + " - " + str(self.salary)

    # employee1 == employee2
    def __eq__(self, other):

        return self.salary == other.salary

    # employee1 < employee2
    def __lt__(self, other):

        return self.salary < other.salary

    # employee1 > employee2
    def __gt__(self, other):

        return self.salary > other.salary

# MANAGER CLASS

class Manager(Employee):

    def __init__(self, name, salary, team_size):

        # Call Employee constructor
        super().__init__(name, salary)

        self.team_size = team_size

    # Polymorphism
    # Overriding details()
    def details(self):

        print("\nManager Details")

        self.display()

        print("Salary:", self.salary)
        print("Team Size:", self.team_size)


# DEVELOPER CLASS

class Developer(Employee):

    def __init__(
        self,
        name,
        salary,
        programming_language
    ):

        # Call Employee constructor
        super().__init__(name, salary)

        self.programming_language = programming_language

    # Polymorphism
    # Overriding details()
    def details(self):

        print("\nDeveloper Details")

        self.display()

        print("Salary:", self.salary)
        print(
            "Programming Language:",
            self.programming_language
        )

# CREATING OBJECTS

manager = Manager("Deepika",80000,10)

developer1 = Developer("Priya",60000,"Python")

developer2 = Developer("Arjun",60000,"Java")


# POLYMORPHISM

manager.details()

developer1.details()

developer2.details()


# STATIC METHOD
print("\nTotal Employees using Static Method:")

print(Employee.get_employee_count())


# CLASS METHOD

print("\nTotal Employees using Class Method:")

print(Employee.get_employee_count_classmethod())


# OPERATOR OVERLOADING

# __str__
print("\nEmployee using __str__:")

print(manager)


# __eq__
print("\nAre developer1 and developer2 equal?")

print(developer1 == developer2)


# __lt__
print("\nIs developer1 salary less than manager salary?")

print(developer1 < manager)


# __gt__
print("\nIs manager salary greater than developer1 salary?")

print(manager > developer1)
