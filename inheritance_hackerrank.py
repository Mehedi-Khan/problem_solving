"""
This is an example of inheriting methods and properties
from the super class to sub class.
Here, Person is the superclass and student is the
sub class.

"""



class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = round(sum(self.scores) / len(self.scores))
        p = None
        if 90 <= avg <= 100:
            p = "O"
        elif 80 <= avg <= 90:
            p = "E"
        elif 70 <= avg <= 80:
            p = "A"
        elif 55 <= avg <= 70:
            p = "P"
        elif 40 <= avg <= 55:
            p = "D"
        else:
            p = "T"
        return p


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())