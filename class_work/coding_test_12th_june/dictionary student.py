#  Write a program to maintain a dictionary of student marks. Allow the user to add, update, and delete records using selection statements.

# Create an empty dictionary
#------------------------------------------------
student_marks = {}

while True:
    print("\n===== STUDENT MARKS MANAGEMENT =====")
    print("1. Add Record")
    print("2. Update Record")
    print("3. Delete Record")
    print("4. Display Records")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    # Add a new student record
    #----------------------------------------------------------
    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        student_marks[name] = marks
        print("Record added successfully!")
    elif choice == 2:
        name = input("Enter student name to update: ")

        if name in student_marks:
            marks = int(input("Enter new marks: "))
            student_marks[name] = marks
            print("Record updated successfully!")
        else:
            print("Student not found!")
    elif choice == 3:
        name = input("Enter student name to delete: ")

        if name in student_marks:
            del student_marks[name]
            print("Record deleted successfully!")
        else:
            print("Student not found!")

# Display all records
#--------------------------------------------------
    elif choice == 4:
        if len(student_marks) == 0:
            print("No records available.")
        else:
            print("\nStudent Records:")
            for name, marks in student_marks.items():
                print(name, ":", marks)

 # Exit the program
 #----------------------------------------------
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")