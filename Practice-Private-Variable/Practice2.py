class Student():
    def __init__(self, name, grade) -> None:
        self.name = name
        self.__grade = grade

    def review(self):
        if self.__grade >= 10:
            return f"grade: {self.__grade} ,passed"
        else:
            return f"grade: {self.__grade} ,failed"

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if 0 <= new_grade <= 20:
            self.__grade = new_grade
        else:
            raise ValueError("Grade must be between 0 and 20.")

stu1 = Student("Motasem",19)
stu2 = Student("Ali",7)

print(stu1.review())
print(stu2.review())

print(stu1.get_grade())
print(stu2.get_grade())

stu1.set_grade(10)
stu2.set_grade(15)

print(stu1.review())
print(stu2.review())