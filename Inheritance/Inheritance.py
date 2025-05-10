# Person
class Person:
    def __init__(self,first_name,last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def Fullname(self):
        return f"{self.first_name} {self.last_name}"



#Employee
class Employee(Person):
    salary = 5000

    def __init__(self,first_name,last_name,position):
        # self.first_name = first_name  # beja nevaestan in 2 ta va bara erthbari az super estefadeh mikonim
        # self.last_name = last_name    # beja nevaestan in 2 ta va bara erthbari az super estefadeh mikonim
        # Person.__init__(self,first_name,last_name)
        super().__init__(first_name,last_name)
        self.position = position

    def job(self):
        return f"i am {self.first_name} {self.last_name} {self.position}"

class Manager:
    def authority(self):
        return "can fire"

# CTO
class CTO(Employee,Manager):
    salary = 10000

    def job(self):
        return f"i am {self.first_name} {self.last_name} CTO in company"

# Intern
class Intern(Employee):
    salary = 1000

    def job(self):
        return f"i am {self.first_name} {self.last_name} new learning"

emp1 = Employee("Motasem","Akbari","backend")
print(emp1.job())
print(emp1.salary)
emo2 = CTO("Motasem","Akbari","backend")
print(emo2.job())
print(emo2.salary)
print(emo2.authority())
emo3 = Intern("Motasem","Akbari","backend")
print(emo3.job())
print(emo3.salary)