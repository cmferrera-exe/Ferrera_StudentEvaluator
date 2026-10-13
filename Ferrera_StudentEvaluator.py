

def display_header():
    print("=========================")
    print("STUDENT EVALUATOR")
    print("=========================")

def get_student_info():
    return student_name, assessment_1, assessment_2, assessment_3

def evaluate_performance(assessment_1, assessment_2, assessment_3, average, performance):
    return average, performance

def display_report(student_name, assessment_1, assessment_2, assessment_3, average, performance):
    #local variables
    print("STUDENT PERFORMANCE REPORT")
    print(f"Student Name: {student_name}")
    print(f"Assessment scores: {assessment_1}, {assessment_2}, {assessment_3}")
    print(f"Average score: {average: .2f}")
    print(f"Performance Level: {performance}")

display_header()

#Global variables
student_name = input("Enter student name: ")
assessment_1 = int(input("Enter assessment 1: "))
assessment_2 = int(input("Enter assessment 2: "))
assessment_3 = int(input("Enter assessment 3: "))

get_student_info()

#global variables
average = (assessment_1 + assessment_2 + assessment_3)/3

performance = ""

if performance == "":
    if 90 >= average >= 100:
        performance = "Outstanding"
    elif 85 >= average >= 90:
        performance = "Very Satisfactory"
    elif 80 >= average >= 85:
        performance = "Satisfactory"
    elif 75 >= average >= 80:
        performance = "Fairly Satisfactory"
    elif average < 75:
        performance = "Needs improvement"

evaluate_performance(assessment_1, assessment_2, assessment_3, average, performance)
display_report(student_name, assessment_1, assessment_2, assessment_3, average, performance)














