class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores = scores

    def calculate(self):
        grade = 0

        for num in scores:
            grade += num

        scoreNum = int(len(scores))
        grade /= scoreNum

        if 100 >= grade >= 90:
            return 'O'
        elif 90 > grade >= 80:
            return 'E'
        elif 80 > grade >= 70:
            return 'A'
        elif 70 > grade >= 55:
            return 'P'
        elif 55 > grade >= 40:
            return 'D'
        elif grade < 40:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())