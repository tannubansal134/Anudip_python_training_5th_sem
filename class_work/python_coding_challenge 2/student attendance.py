'''Problem Statement
The attendance status of a student for 15 days is represented as follows:
Sample Data
attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P')
Tasks
1.Count present days.
2.Count absent days.
3.Calculate attendance percentage.
4.Determine whether attendance is below 75%.
5.Display the attendance status.
'''

# Tuple containing attendance status
#-------------------------------------------------------
attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A', 'P', 'P', 'P', 'P', 'A', 'P', 'P')

# Count present days
#-------------------------------------------------------
present_days = attendance.count('P')

# Count absent days
#-------------------------------------------------------
absent_days = attendance.count('A')

# Calculate attendance percentage
#-------------------------------------------------------
total_days = len(attendance)
attendance_percentage = (present_days / total_days) * 100

# Determine attendance status
#-------------------------------------------------------
if attendance_percentage < 75:
    status = "Below 75%"
else:
    status = "75% or Above"

# Display results
#-------------------------------------------------------
print("Present Days:", present_days)
print("Absent Days:", absent_days)
print("Attendance Percentage:", round(attendance_percentage, 2), "%")
print("Attendance Status:", status)