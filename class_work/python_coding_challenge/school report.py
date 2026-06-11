''''Problem Statement Student marks are stored in marks.txt.
 Sample Input/Data (marks.txt)
 S101,Anuj,92 
 S102,Rahul,76
 S103,Priya,88 
 S104,Neha,45 
 S105,Amit,58 
 S106,Sneha,95 
 S107,Karan,81 
 S108,Pooja,73 
 S109,Rohit,39 
 S110,Anjali,90
 Tasks 
 1. Calculate grades for all students. 
 2. Generate a report card file report_card.txt. 
 3. Display topper details.
 4. Count pass and fail students. 
 5. Display students eligible for merit certificates (marks ≥ 90).  
'''
#--------------------------------------------------------
# Student Result Management System

students = [
    ("S101", "Anuj", 92),
    ("S102", "Rahul", 76),
    ("S103", "Priya", 88),
    ("S104", "Neha", 45),
    ("S105", "Amit", 58),
    ("S106", "Sneha", 95),
    ("S107", "Karan", 81),
    ("S108", "Pooja", 73),
    ("S109", "Rohit", 39),
    ("S110", "Anjali", 90)
]

#-------------------------------------------------
# Function to calculate grade
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"
#------------------------------------------
# Display Report Cards
print("REPORT CARDS")
print("-" * 40)

pass_count = 0
fail_count = 0

for sid, name, marks in students:
    grade = get_grade(marks)

    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1

    print("ID:", sid,
          "Name:", name,
          "Marks:", marks,
          "Grade:", grade)
    
#-----------------------------------------------
# Topper Details
topper = students[0]

for student in students:
    if student[2] > topper[2]:
        topper = student

print("\nTopper:", topper[1], "(", topper[2], ")", sep="")

#---------------------------------------------------
# Pass and Fail Count
print("\nPassed Students:", pass_count)
print("Failed Students:", fail_count)

#------------------------------------------------------
# Merit Certificate Holders
print("\nMerit Certificate Holders:")

for sid, name, marks in students:
    if marks >= 90:
        print(name, end=" ")

print()
'''Sample Output
Topper: 
Sneha (95) 
Passed Students: 9
Failed Students: 1
 Merit Certificate Holders: 
 Anuj Sneha Anjali  
 Report Cards Generated Successfully. 
 '''