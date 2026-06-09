"""
      STUDENT PERFORMANCE ANALYTICS SYSTEM

This program performs the following tasks:

1. Display all student records
2. Search a student using Student ID
3. Add a new student
4. Update marks of an existing student
5. Delete a student
6. Find topper and lowest scorer
7. Calculate class average
8. Count pass and fail students
9. Generate grades
        o A (90+)
        o B (75-89) 
        o C (50-74) 
        o F (<50)
10. Display students scoring above average
11. Display top 5 performers
12. Create a separate dictionary for scholarship students (marks > 85)

expected learning
- Nested Dictionary
- Dictionary Traversal
- Searching
- Aggregation
- Report Generation
"""

# ------------------------------------------------------
# Dictionary containing details of 30 students

students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 91},
    "S104": {"name": "Aman", "marks": 48},
    "S105": {"name": "Neha", "marks": 67},
    "S106": {"name": "Riya", "marks": 95},
    "S107": {"name": "Karan", "marks": 55},
    "S108": {"name": "Megha", "marks": 88},
    "S109": {"name": "Arjun", "marks": 76},
    "S110": {"name": "Simran", "marks": 62},
    "S111": {"name": "Rohit", "marks": 44},
    "S112": {"name": "Pooja", "marks": 79},
    "S113": {"name": "Deepak", "marks": 93},
    "S114": {"name": "Nisha", "marks": 58},
    "S115": {"name": "Vikas", "marks": 81},
    "S116": {"name": "Komal", "marks": 69},
    "S117": {"name": "Sahil", "marks": 97},
    "S118": {"name": "Tina", "marks": 73},
    "S119": {"name": "Yash", "marks": 51},
    "S120": {"name": "Muskan", "marks": 89},
    "S121": {"name": "Aditya", "marks": 64},
    "S122": {"name": "Kriti", "marks": 92},
    "S123": {"name": "Manish", "marks": 47},
    "S124": {"name": "Payal", "marks": 84},
    "S125": {"name": "Nitin", "marks": 78},
    "S126": {"name": "Shreya", "marks": 96},
    "S127": {"name": "Mohit", "marks": 53},
    "S128": {"name": "Isha", "marks": 87},
    "S129": {"name": "Harsh", "marks": 61},
    "S130": {"name": "Sneha", "marks": 90}
}

# ------------------------------------------------------
# Function to display all student records

def display_students():
    print("\n----- STUDENT RECORDS -----")
    for sid, details in students.items():
        print(sid, ":", details)

# ------------------------------------------------------
# Function to search student by ID

def search_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        print("Record Found:")
        print(students[sid])
    else:
        print("Student Not Found")

# ------------------------------------------------------
# Function to add new student

def add_student():
    sid = input("Enter New Student ID: ")

    if sid in students:
        print("Student ID already exists")
    else:
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students[sid] = {"name": name, "marks": marks}

        print("Student Added Successfully")

# ------------------------------------------------------
# Function to update marks

def update_marks():
    sid = input("Enter Student ID: ")

    if sid in students:
        new_marks = float(input("Enter New Marks: "))
        students[sid]["marks"] = new_marks

        print("Marks Updated Successfully")
    else:
        print("Student Not Found")

# ------------------------------------------------------
# Function to delete student

def delete_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        del students[sid]
        print("Student Deleted Successfully")
    else:
        print("Student Not Found")

# ------------------------------------------------------
# Function to find topper and lowest scorer

def topper_lowest():
    topper = max(students, key=lambda x: students[x]["marks"])
    lowest = min(students, key=lambda x: students[x]["marks"])

    print("\nTopper:")
    print(topper, students[topper])

    print("\nLowest Scorer:")
    print(lowest, students[lowest])

# ------------------------------------------------------
# Function to calculate class average

def class_average():
    total = 0

    for details in students.values():
        total += details["marks"]

    avg = total / len(students)

    print("Class Average =", round(avg, 2))

    return avg

# ------------------------------------------------------
# Function to count pass and fail students
# Passing Marks = 50

def pass_fail_count():
    passed = 0
    failed = 0

    for details in students.values():

        if details["marks"] >= 50:
            passed += 1
        else:
            failed += 1

    print("Passed Students =", passed)
    print("Failed Students =", failed)

# ------------------------------------------------------
# Function to generate grades

def generate_grades():

    print("\n----- STUDENT GRADES -----")

    for sid, details in students.items():

        marks = details["marks"]

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 50:
            grade = "C"

        else:
            grade = "F"

        print(sid, "-", details["name"], "=", grade)

# ------------------------------------------------------
# Function to display students above average

def above_average_students():

    avg = class_average()

    print("\nStudents Scoring Above Average")

    for sid, details in students.items():

        if details["marks"] > avg:
            print(sid, details)

# ------------------------------------------------------
# Function to display top 5 performers

def top_five_students():

    sorted_students = sorted(
        students.items(),
        key=lambda x: x[1]["marks"],
        reverse=True
    )

    print("\n----- TOP 5 PERFORMERS -----")

    for sid, details in sorted_students[:5]:
        print(sid, details)

# ------------------------------------------------------
# Function to create scholarship dictionary
# Scholarship Criteria : Marks > 85

def scholarship_students():

    scholarship = {}

    for sid, details in students.items():

        if details["marks"] > 85:
            scholarship[sid] = details

    print("\nScholarship Students Dictionary")

    for sid, details in scholarship.items():
        print(sid, details)

# ------------------------------------------------------
# Main Menu

while True:

    print("\n")
    print("===== STUDENT PERFORMANCE ANALYTICS SYSTEM =====")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper and Lowest Scorer")
    print("7. Calculate Class Average")
    print("8. Count Pass and Fail Students")
    print("9. Generate Grades")
    print("10. Students Above Average")
    print("11. Top 5 Performers")
    print("12. Scholarship Students")
    print("13. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        display_students()

    elif choice == 2:
        search_student()

    elif choice == 3:
        add_student()

    elif choice == 4:
        update_marks()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        topper_lowest()

    elif choice == 7:
        class_average()

    elif choice == 8:
        pass_fail_count()

    elif choice == 9:
        generate_grades()

    elif choice == 10:
        above_average_students()

    elif choice == 11:
        top_five_students()

    elif choice == 12:
        scholarship_students()

    elif choice == 13:
        print("Thank You! Program Ended.")
        break

    else:
        print("Invalid Choice")