'''Problem Statement
Student marks are stored in results.txt.
File Format
S101,Anuj,85
S102,Rahul,72 
S103,Priya,96 
S104,Neha,68 
S105,Amit,39 
S106,Sneha,54 
S107,Karan,91 
S108,Pooja,78 
S109,Rohit,47 
S110,Anjali,88
Requirements
Write a program to:
1. Display all student records.
2. Search a student using Student ID.
3. Find topper and lowest scorer.
4. Calculate class average.
5. Count pass and fail students.
6. Generate grades:
       o  A (90+)
       o  B (75-89)
       o  c(40-74)
       o  F(<40)
7. Write grade reports into a new file named grades.txt
'''

# -----------------------------------------------------
# Function to load student records from results.txt
# -----------------------------------------------------
def load_students():

    students = []

    file = open("results.txt", "r")

    for line in file:

        line = line.strip()

        if line != "":

            sid, name, marks = line.split(",")

            students.append({
                "id": sid,
                "name": name,
                "marks": int(marks)
            })

    file.close()

    return students


# -----------------------------------------------------
# Function to display all student records
# -----------------------------------------------------
def display_students():

    students = load_students()

    print("\n===== STUDENT RECORDS =====")

    for student in students:

        print(
            student["id"],
            student["name"],
            student["marks"]
        )


# -----------------------------------------------------
# Function to search a student
# -----------------------------------------------------
def search_student():

    students = load_students()

    sid = input("Enter Student ID : ")

    found = False

    for student in students:

        if student["id"] == sid:

            print("\nStudent Found")
            print("ID    :", student["id"])
            print("Name  :", student["name"])
            print("Marks :", student["marks"])

            found = True
            break

    if found == False:
        print("Student not found")


# -----------------------------------------------------
# Function to find topper and lowest scorer
# -----------------------------------------------------
def topper_lowest():

    students = load_students()

    topper = students[0]
    lowest = students[0]

    for student in students:

        if student["marks"] > topper["marks"]:
            topper = student

        if student["marks"] < lowest["marks"]:
            lowest = student

    print("\nTopper")
    print(topper["id"], topper["name"], topper["marks"])

    print("\nLowest Scorer")
    print(lowest["id"], lowest["name"], lowest["marks"])


# -----------------------------------------------------
# Function to calculate class average
# -----------------------------------------------------
def class_average():

    students = load_students()

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("\nClass Average =", round(average, 2))


# -----------------------------------------------------
# Function to count pass and fail students
# -----------------------------------------------------
def pass_fail():

    students = load_students()

    passed = 0
    failed = 0

    for student in students:

        if student["marks"] >= 40:
            passed += 1
        else:
            failed += 1

    print("\nPassed Students :", passed)
    print("Failed Students :", failed)


# -----------------------------------------------------
# Function to assign grade
# -----------------------------------------------------
def get_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 40:
        return "C"

    else:
        return "F"


# -----------------------------------------------------
# Function to generate grades
# -----------------------------------------------------
def generate_grades():

    students = load_students()

    print("\n===== GRADE REPORT =====")

    for student in students:

        grade = get_grade(student["marks"])

        print(
            student["id"],
            student["name"],
            student["marks"],
            grade
        )


# -----------------------------------------------------
# Function to write grade report in grades.txt
# -----------------------------------------------------
def write_grades():

    students = load_students()

    file = open("grades.txt", "w")

    file.write("ID,Name,Marks,Grade\n")

    for student in students:

        grade = get_grade(student["marks"])

        file.write(
            f"{student['id']},{student['name']},{student['marks']},{grade}\n"
        )

    file.close()

    print("Grade report saved in grades.txt")


# -----------------------------------------------------
# Main Menu
# -----------------------------------------------------
while True:

    print("\n")
    print("=================================")
    print(" Student Result Management System")
    print("=================================")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Find Topper & Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass & Fail Students")
    print("6. Generate Grades")
    print("7. Write Grades Report")
    print("8. Exit")
    print("=================================")

    choice = input("Enter Choice : ")

    if choice == "1":
        display_students()

    elif choice == "2":
        search_student()

    elif choice == "3":
        topper_lowest()

    elif choice == "4":
        class_average()

    elif choice == "5":
        pass_fail()

    elif choice == "6":
        generate_grades()

    elif choice == "7":
        write_grades()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")