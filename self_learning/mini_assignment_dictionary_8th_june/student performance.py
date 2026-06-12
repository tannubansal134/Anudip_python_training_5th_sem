'''Problem Statement
A coaching institute wants to analyze student performance.
Store details of at least 30 students in a dictionary.
Example Structure
students = { 
"S101": {"name": "Anuj", "marks": 85}, 
"S102": {"name": "Rahul", "marks": 72} 
}
Requirements
1.Display all student records.
2.Search a student using Student ID.
3.Add a new student.
4.Update marks of an existing student.
5.Delete a student.
6.Find topper and lowest scorer.
7.Calculate class average.
8.Count pass and fail students.
9.Generate grades:
o A (90+)
o B (75-89)
o C (50-74)
o F (<50)
10. Display students scoring above average.
11. Display top 5 performers.
12. Create a separate dictionary for scholarship students (marks > 85).
Expected Learning
• Nested Dictionaries
• Dictionary Traversal
• Searching
• Aggregation
• Report Generation
'''
# Student Performance Analytics System

# Dictionary containing details of 30 students
students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 96},
    "S104": {"name": "Neha", "marks": 68},
    "S105": {"name": "Amit", "marks": 39},
    "S106": {"name": "Sneha", "marks": 54},
    "S107": {"name": "Karan", "marks": 91},
    "S108": {"name": "Pooja", "marks": 78},
    "S109": {"name": "Rohit", "marks": 47},
    "S110": {"name": "Anjali", "marks": 88},
    "S111": {"name": "Vikas", "marks": 65},
    "S112": {"name": "Riya", "marks": 92},
    "S113": {"name": "Manish", "marks": 58},
    "S114": {"name": "Kavita", "marks": 74},
    "S115": {"name": "Deepak", "marks": 81},
    "S116": {"name": "Nisha", "marks": 49},
    "S117": {"name": "Arjun", "marks": 95},
    "S118": {"name": "Meena", "marks": 67},
    "S119": {"name": "Yash", "marks": 83},
    "S120": {"name": "Simran", "marks": 77},
    "S121": {"name": "Tarun", "marks": 62},
    "S122": {"name": "Ayesha", "marks": 89},
    "S123": {"name": "Harsh", "marks": 45},
    "S124": {"name": "Komal", "marks": 93},
    "S125": {"name": "Rakesh", "marks": 71},
    "S126": {"name": "Shweta", "marks": 56},
    "S127": {"name": "Nitin", "marks": 98},
    "S128": {"name": "Preeti", "marks": 60},
    "S129": {"name": "Saurabh", "marks": 87},
    "S130": {"name": "Muskan", "marks": 52}
}

# Menu-driven loop
while True:

    # Display menu options
    print("\n===== STUDENT PERFORMANCE ANALYTICS SYSTEM =====")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper and Lowest Scorer")
    print("7. Calculate Class Average")
    print("8. Count Pass and Fail Students")
    print("9. Generate Grades")
    print("10. Display Students Above Average")
    print("11. Display Top 5 Performers")
    print("12. Scholarship Students")
    print("13. Exit")

    # Accept user choice
    choice = int(input("Enter Choice: "))

# Display all student records
#-----------------------------------------
    if choice == 1:

        print("\nStudent Records")
        print("-" * 40)

        for sid in students:
            print(sid,
                  students[sid]["name"],
                  students[sid]["marks"])

# Search student by ID
#--------------------------------------------------
    elif choice == 2:

        sid = input("Enter Student ID: ")

        if sid in students:
            print("Name :", students[sid]["name"])
            print("Marks:", students[sid]["marks"])
        else:
            print("Student Not Found")

# Add new student
#---------------------------------------------------
    elif choice == 3:

        sid = input("Enter Student ID: ")

        if sid in students:
            print("Student ID Already Exists")
        else:
            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))

            students[sid] = {
                "name": name,
                "marks": marks
            }

            print("Student Added Successfully")

# Update marks of existing student
#--------------------------------------------------------
    elif choice == 4:

        sid = input("Enter Student ID: ")

        if sid in students:
            marks = int(input("Enter New Marks: "))
            students[sid]["marks"] = marks
            print("Marks Updated Successfully")
        else:
            print("Student Not Found")

 # Delete student record
 #-------------------------------------------------------
    elif choice == 5:

        sid = input("Enter Student ID: ")

        if sid in students:
            del students[sid]
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")

# Find topper and lowest scorer
#-------------------------------------------------------
    elif choice == 6:

        max_marks = -1
        min_marks = 101

        for sid in students:

            if students[sid]["marks"] > max_marks:
                max_marks = students[sid]["marks"]
                topper = sid

            if students[sid]["marks"] < min_marks:
                min_marks = students[sid]["marks"]
                lowest = sid

        print("\nTopper")
        print(topper,
              students[topper]["name"],
              max_marks)

        print("\nLowest Scorer")
        print(lowest,
              students[lowest]["name"],
              min_marks)

# Calculate class average
#-------------------------------------------------------
    elif choice == 7:

        total = 0

        for sid in students:
            total += students[sid]["marks"]

        average = total / len(students)

        print("Class Average =", round(average, 2))

# Count pass and fail students
#-------------------------------------------------------
    elif choice == 8:

        passed = 0
        failed = 0

        for sid in students:

            if students[sid]["marks"] >= 50:
                passed += 1
            else:
                failed += 1

        print("Passed Students =", passed)
        print("Failed Students =", failed)

# Generate grades
#-------------------------------------------------------
    elif choice == 9:

        print("\nGrades Report")
        print("-" * 40)

        for sid in students:

            marks = students[sid]["marks"]

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 50:
                grade = "C"
            else:
                grade = "F"

            print(sid,
                  students[sid]["name"],
                  marks,
                  grade)

# Display students scoring above average
#-------------------------------------------------------
    elif choice == 10:

        total = 0

        for sid in students:
            total += students[sid]["marks"]

        average = total / len(students)

        print("\nStudents Above Average")

        for sid in students:

            if students[sid]["marks"] > average:
                print(sid,
                      students[sid]["name"],
                      students[sid]["marks"])

 # Display top 5 performers 
 #-------------------------------------------------------
    elif choice == 11:

        temp = {}

        # Create a copy of dictionary
        for sid in students:
            temp[sid] = students[sid]

        print("\nTop 5 Performers")

        count = 0

        while count < 5:

            max_marks = -1

            for sid in temp:

                if temp[sid]["marks"] > max_marks:
                    max_marks = temp[sid]["marks"]
                    top_sid = sid

            print(top_sid,
                  temp[top_sid]["name"],
                  temp[top_sid]["marks"])

            # Remove selected topper
            del temp[top_sid]

            count += 1

    # Create scholarship dictionary
    elif choice == 12:

        scholarship = {}

# Store students with marks greater than 85
#-------------------------------------------------------
        for sid in students:

            if students[sid]["marks"] > 85:
                scholarship[sid] = students[sid]

        print("\nScholarship Students")
        print("-" * 40)

        for sid in scholarship:
            print(sid,
                  scholarship[sid]["name"],
                  scholarship[sid]["marks"])

    # Exit program
    elif choice == 13:

        print("Program Ended Successfully")
        break

    # Invalid choice
    else:

        print("Invalid Choice")