# Attendance Tracker for 30 Students using Dictionary

# Create an empty dictionary to store attendance
attendance = {}

# Input attendance for 30 students
for i in range(30):
    roll_no = input("Enter Roll Number: ")
    status = input("Enter Attendance (Present/Absent): ")

    # Store roll number as key and attendance status as value
    attendance[roll_no] = status

# Display roll numbers of students who are Present
print("\nStudents who are Present:")

for roll_no, status in attendance.items():
    if status.lower() == "present":
        print(roll_no)