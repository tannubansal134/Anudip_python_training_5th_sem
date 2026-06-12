'''Problem Statement 
The marks obtained by students in the final examination are stored as follows: Sample Data marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 
Tasks 
1.	Display students scoring above 85 marks.  
2.	Find the topper.  
3.	Find the student with the lowest marks.  
4.	Calculate class average marks.  
5.	Generate grades:  
o 	A (90+)  o 	B (75–89)  o 	C (50–74)  o 	F (<50)  
6.	Create a list of scholarship students (marks ≥ 90).  
'''
#-------------------------------------------------------------
# Sample Data
marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}
# 1.  Task to Display students scoring above 85 marks.
print("Students Scoring Above 85:")
for student, mark in marks.items():
    if mark > 85:
        print(student)
#--------------------------------------------------------
print("--------------------------------------------------")
# 2. Task to Find the topper.  
topper = max(marks, key=marks.get)
print("Topper:")
print(topper, "(", marks[topper], ")")
#--------------------------------------------------------
print("--------------------------------------------------")
#3. Task to Find the student with the lowest marks.
lowest_scorer = min(marks, key=marks.get)
print("Lowest Scorer:")
print(lowest_scorer, "(", marks[lowest_scorer], ")")
#--------------------------------------------------------
print("--------------------------------------------------")
#4. Task to Calculate class average marks.
average_marks = sum(marks.values()) / len(marks)
print("Average Marks:", average_marks)  
#--------------------------------------------------------
print("--------------------------------------------------")
#5. Task to Generate grades.
grades = {}
for student, mark in marks.items():
    if mark >= 90:
        grades[student] = 'A'
    elif 75 <= mark < 90:
        grades[student] = 'B'
    elif 50 <= mark < 75:
        grades[student] = 'C'
    else:
        grades[student] = 'F'
print("Grades:")
for student, grade in grades.items():
    print(student, ":", grade)  
#--------------------------------------------------------
print("--------------------------------------------------") 
#6. Task to Create a list of scholarship students (marks ≥ 90).
scholarship_students = []
for student, mark in marks.items():
    if mark >= 90:
        scholarship_students.append(student)
print("Scholarship Students:\n", scholarship_students)

'''Sample Output 
Students Scoring Above 85: 
Anuj 
Priya 
Sneha 
Anjali 
 
Topper: 
Sneha (95) 
 
Lowest Scorer: 
Rohit (47) 
 
Average Marks: 76.4 
 
Scholarship Students: 
['Anuj', 'Sneha', 'Anjali'] 
'''