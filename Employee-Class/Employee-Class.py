class Employee:
    # name = "moti"  
    salary = 3000 # class variable
    # __new__ is called first
    # __init__ is called after

    def __init__(self, name, age):
        self.age = age  # object variable
        self.name = name 

emp1 = Employee("motasem", 22)
emp2 = Employee("ali", 50)

# Employee.salary = Employee.salary * 3  # global change
emp1.salary = 7000  # only for this object
print(emp1.name, emp1.age, emp1.salary)
print(emp2.name, emp2.age, emp2.salary)
