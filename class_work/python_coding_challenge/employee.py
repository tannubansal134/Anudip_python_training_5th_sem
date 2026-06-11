'''Employee attendance records are stored in attendance.txt. 
Sample Input/Data (attendance.txt) 
EMP101,P EMP102,A 
EMP103,P 
EMP104,P 
EMP105,A 
EMP106,P 
EMP107,P EMP108,A 
EMP109,P 
EMP110,P 
Tasks 
1.	Count present and absent employees.  
2.	Display absent employee IDs.  
3.	Calculate attendance percentage.  
4.	Generate an absentee report in absent_report.txt.  
5.	Display employees eligible for attendance awards (100% attendance).  
'''
# Employee Attendance Tracker

filev = open("attendance.txt", "r")

absent_file = open("absent_report.txt", "w")

line = filev.readline()

present = 0
absent = 0

absent_ids = []

while line:

    data = line.strip().split(",")

    emp_id = data[0]
    status = data[1]

    if status == "P":
        present += 1

    else:
        absent += 1

        absent_ids.append(emp_id)

        absent_file.write(emp_id + "\n")

    line = filev.readline()

filev.close()
absent_file.close()

# --------------------------------
# Display Present and Absent Count
# --------------------------------

print("Present Employees:", present)

print("\nAbsent Employees:", absent)

# --------------------------------
# Display Absent Employee IDs
# --------------------------------

print("\nAbsent Employee IDs:")

for emp in absent_ids:
    print(emp)

# --------------------------------
# Attendance Percentage
# --------------------------------

total = present + absent

percentage = (present / total) * 100

print("\nAttendance Percentage:", percentage, "%")

# --------------------------------
# Report Generation
# --------------------------------

print("\nAbsentee Report Generated Successfully.")

# --------------------------------
# Attendance Award
# --------------------------------

if absent == 0:
    print("\nAttendance Award Eligibility: Applicable")

else:
    print("\nAttendance Award Eligibility: Not Applicable")

'''Sample Output 
Present Employees: 7 
 
Absent Employees: 3 
 
Absent Employee IDs: 
EMP102 
EMP105 
EMP108 
 
Attendance Percentage: 70.0% 
 
Absentee Report Generated Successfully. 
 
Attendance Award Eligibility: Not Applicable 
'''