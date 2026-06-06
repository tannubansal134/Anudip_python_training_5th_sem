"""
Program: Student Attendance Analysis

This program performs the following tasks:
1. Count present and absent days.
2. Calculate attendance percentage.
3. Determine eligibility (minimum 75% attendance).
4. Display positions where the student was absent.
"""

attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# --------------------------------------------------
# Task 1: Count present and absent days

present = 0
absent = 0

for day in attendance:
    if day == 'P':
        present += 1
    else:
        absent += 1

print("Total Present Days :", present)
print("Total Absent Days :", absent)

# --------------------------------------------------
# Task 2: Calculate attendance percentage

total_days = len(attendance)
percentage = (present / total_days) * 100

print("\nAttendance Percentage :", percentage)

# --------------------------------------------------
# Task 3: Determine eligibility (minimum 75%)

if percentage >= 75:
    print("\nStudent is Eligible")
else:
    print("\nStudent is Not Eligible")

# --------------------------------------------------
# Task 4: Display positions where student was absent

print("\nAbsent Positions (Index Values)")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i)