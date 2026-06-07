"""
Program: Student Marks Analysis

This program performs the following tasks:
1. Displays students scoring 80 or above.
2. Counts the number of students who failed (marks < 40).
3. Finds the highest scorer.
4. Creates a list of students scoring between 60 and 75.
5. Assigns grades to all students based on their marks.

Grade Criteria:
A : Marks >= 90
B : Marks between 75 and 89
C : Marks between 50 and 74
F : Marks below 50
"""

# Dictionary containing student names and marks
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

#---------------------------------------------
#Display students who scored 80 or above

print("Students scoring 80 or above:")
for student, score in marks.items():
    if score >= 80:
        print(student, ":", score)

#-------------------------------------------
# Count the number of students who failed
#(Failure means marks less than 40)
failed_count = 0

for score in marks.values():
    if score < 40:
        failed_count += 1

print("\nNumber of students who failed:", failed_count)

#--------------------------------------------------
#Find the highest scorer in the class

highest_scorer = max(marks, key=marks.get)
highest_marks = marks[highest_scorer]

print("\nHighest Scorer:")
print(highest_scorer, ":", highest_marks)

#------------------------------------------
#Create a list of students scoring
#between 60 and 75 (inclusive)

students_60_75 = []

for student, score in marks.items():
    if 60 <= score <= 75:
        students_60_75.append(student)

print("\nStudents scoring between 60 and 75:")
print(students_60_75)

#-----------------------------------------------

#Assign grades according to the given criteria
# and display the result

print("\nStudent Grades:")

for student, score in marks.items():

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(student, ":", score, "-> Grade", grade)