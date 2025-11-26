from student import Student


def main():
    student = Student()

    choice(student)

    student.calcLetterGrade()

    print(f"\nGrade Percentage: {student.getPercentage():.2f}%")
    print(f"Final Letter Grade: {student.getLetterGrade()}")

def choice(student):
    while(True):
        choice = input("Do you need your percentage calculated? (y/n) ").lower()
        if choice == 'y':
            print("Please Enter Your Grade For Each Category (ex. 73.48): ")
            assignments = float(input("Assignments: "))
            projects = float(input("Projects: "))
            achievements = float(input("Achievements: "))
            finalExam = float(input("Final Exam: "))
            student.calcPercentage(assignments, projects, achievements, finalExam)
            break
        elif choice == 'n':
            percentage = float(input("Please Enter Your Grade Percentage (ex. 73.48): "))
            student.setPercentage(percentage)
            break
        else:
            print("Please Give A Valid Answer!\n")

main()