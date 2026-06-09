"""
Program: String-Based Attendance Tracker

Attendance Record:
P = Present
A = Absent

Tasks:
1. Count Present and Absent days.
2. Calculate attendance percentage.
3. Find longest consecutive Presence streak.
4. Find longest consecutive Absence streak.
5. Check whether attendance is below 75%.
"""

# Attendance string
attendance = "PPAPPPAAPPPPAPP"

#--------------------------------------------
# Count Present and Absent days
present_days = attendance.count("P")
absent_days = attendance.count("A")

#--------------------------------------------
# Total days
total_days = len(attendance)

#--------------------------------------------
# Attendance percentage
percentage = (present_days / total_days) * 100

#--------------------------------------------
# Find longest Presence streak
max_present = 0
current_present = 0

for ch in attendance:
    if ch == "P":
        current_present += 1
        if current_present > max_present:
            max_present = current_present
    else:
        current_present = 0

#--------------------------------------------
# Find longest Absence streak
max_absent = 0
current_absent = 0

for ch in attendance:
    if ch == "A":
        current_absent += 1
        if current_absent > max_absent:
            max_absent = current_absent
    else:
        current_absent = 0

#--------------------------------------------
# Display results
print("Attendance Record:", attendance)
print("Present Days:", present_days)
print("Absent Days:", absent_days)
print("Attendance Percentage:", round(percentage, 2), "%")
print("Longest Presence Streak:", max_present)
print("Longest Absence Streak:", max_absent)

#--------------------------------------------
# Check attendance status
if percentage < 75:
    print("Status: Attendance Below 75%")
else:
    print("Status: Attendance Satisfactory")