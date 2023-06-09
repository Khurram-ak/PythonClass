class Person:
    def __init__(self,_fName,_lName):
        self.fName=_fName
        self.lName=_lName

    def fullName(self):
        return self.fName + " " + self.lName

class Student(Person):
    def __init__(self, _fName, _lName,_grade):
        self.grade=_grade
        super().__init__(_fName, _lName)

    def yourGrade(self):
        return self.grade

# class Student(Person):
#     grade=""
#     def yourGrade(self):
#         return self.grade

class Teacher(Person):
    subject=""
    pass


std1=Student("Khurram","amir")
teacher1=Teacher("faraz","zaki")
std1.grade=5
gradeStd=std1.yourGrade()
print(gradeStd)

teacher1.subject="maths"
# print(teacher1.subject)

# print(std1.yourGrade())
# print(std1.grade)
# print(std1.fName)
# print(std1.lName)
# print(teacher1.fullName())


# class Student(Person):
#     def __init__(self, _fName, _lName,_grade):
#         self.grade=_grade
#         super().__init__(_fName, _lName)

#     def yourGrade(self):
#         return self.grade
