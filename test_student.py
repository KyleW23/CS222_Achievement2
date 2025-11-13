import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student()

    def test_calcPercentage(self):
        assignments = 100
        projects = 93
        achievements = 100
        finalExam = 85
        self.student.calcPercentage(assignments, projects, achievements, finalExam)
        self.assertEqual(self.student.getPercentage(), 95.05)

    def test_calcLetterGrade(self):
        percentage = 73
        self.student.calcLetterGrade(percentage)
        self.assertEqual(self.student.getLetterGrade(), "C")

if __name__ == '__main__':
    unittest.main()