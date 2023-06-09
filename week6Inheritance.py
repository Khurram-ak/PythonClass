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
        return "Your Grade is " + self.grade

class Teacher(Person):
    subject=""
    def getSubject(self):
        return self.subject
    pass

std1=Student("khurram","amir",10)

print(std1.fName)
print(std1.lName)
print(std1.grade)


# teacher1=Teacher("faraz","zaki")
# gradeStd=std1.yourGrade()
# teacher1.subject="maths"
# print(std1.yourGrade())
# print(teacher1.fullName())


