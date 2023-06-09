class Person:
    def __init__(self,_fName,_lName):
        self.fName=_fName
        self.lName=_lName

    def fullName(self):
        return self.fName + " " + self.lName



p1=Person("khurram","ak")

print(p1.fullName())

# print(p1.fName + " " + p1.lName)
