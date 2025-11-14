class Student:
    def __init__(self):
        self.percentage = 0
        self.letterGrade = ""

    def getPercentage(self):
        return self.percentage

    def setPercentage(self, percentage: float):
        self.percentage = percentage

    def getLetterGrade(self):
        return self.letterGrade
    
    def setLetterGrade(self, letterGrade):
        self.letterGrade = letterGrade

    def calcPercentage(self, assignments: float, projects: float, achievements: float, finalExam: float) -> float:
        assignmentsWeighted = assignments * .3
        projectsWeighted = projects * .6
        achievementsWeighted = achievements * .05
        finalExamWeighted = finalExam * .05

        self.setPercentage((assignmentsWeighted + projectsWeighted + achievementsWeighted + finalExamWeighted))
    
    def calcLetterGrade(self,) -> float:
        if self.getPercentage() >= 93:
            self.setLetterGrade("A")
        elif self.getPercentage() >= 90:
            self.setLetterGrade("A-")
        elif self.getPercentage() >= 87:
            self.setLetterGrade("B+")
        elif self.getPercentage() >= 83:
            self.setLetterGrade("B")
        elif self.getPercentage() >= 80:
            self.setLetterGrade("B-")
        elif self.getPercentage() >= 77:
            self.setLetterGrade("C+")
        elif self.getPercentage() >= 73:
            self.setLetterGrade("C")
        elif self.getPercentage() >= 70:
            self.setLetterGrade("C-")
        elif self.getPercentage() >= 67:
            self.setLetterGrade("D+")
        elif self.getPercentage() >= 63:
            self.setLetterGrade("D")
        elif self.getPercentage() >= 60:
            self.setLetterGrade("D-")
        else:
            self.setLetterGrade("F")