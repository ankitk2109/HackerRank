#Problem Statement at: https://www.hackerrank.com/challenges/30-inheritance/

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores): #Using parents init method to initialize these variables.
        Person.__init__(self,firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        sum_ = 0
        for i in range(len(self.scores)):
            sum_ += scores[i]
        grade = sum_/len(self.scores)
        if(grade<40):
            return 'T'
        elif(grade>=40 and grade<55):
            return 'D'
        elif(grade>=55 and grade<70):
            return 'P'
        elif(grade>=70 and grade<80):
            return 'A'
        elif(grade>=80 and grade<90):
            return 'E'
        elif(grade>=90 and grade<=100):
            return 'O'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())