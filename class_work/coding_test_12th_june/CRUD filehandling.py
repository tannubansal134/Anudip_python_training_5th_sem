# Create a menu-driven program using selection statements to perform CRUD operations using file handling on student records.

# File name to store student records
#------------------------------------------------
file_name = "students.txt"

while True:
    print("\n===== STUDENT RECORD MANAGEMENT =====")
    print("1. Create Student Record")
    print("2. Read Student Records")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Exit")

    
    choice = input("Enter your choice (1-5): ")

# CREATE Operation
#---------------------------------------------------
    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        with open(file_name, "a") as file:
            file.write(roll_no + "," + name + "," + marks + "\n")

        print("Student record added successfully!")

# READ Operation
#--------------------------------------------------------
    elif choice == "2":
        try:
            
            with open(file_name, "r") as file:
                records = file.readlines()

                if len(records) == 0:
                    print("No records found.")
                else:
                    print("\nStudent Records:")
                    print("Roll No\tName\tMarks")
                    print("-" * 30)

                    for record in records:
                        data = record.strip().split(",")
                        print(data[0], "\t", data[1], "\t", data[2])

        except FileNotFoundError:
            print("File does not exist.")

# UPDATE Operation
#-----------------------------------------------------
    elif choice == "3":
        roll_no = input("Enter Roll Number to Update: ")

        try:
            with open(file_name, "r") as file:
                records = file.readlines()

            found = False
            with open(file_name, "w") as file:
                for record in records:
                    data = record.strip().split(",")

                    if data[0] == roll_no:
                        found = True

                        new_name = input("Enter New Name: ")
                        new_marks = input("Enter New Marks: ")

                        file.write(roll_no + "," + new_name + "," + new_marks + "\n")
                    else:
                        file.write(record)

            if found:
                print("Record updated successfully!")
            else:
                print("Student record not found.")

        except FileNotFoundError:
            print("File does not exist.")

 # DELETE Operation
 #-----------------------------------------------------
    elif choice == "4":
        roll_no = input("Enter Roll Number to Delete: ")

        try:
            with open(file_name, "r") as file:
                records = file.readlines()

            found = False

            with open(file_name, "w") as file:
                for record in records:
                    data = record.strip().split(",")

                    if data[0] == roll_no:
                        found = True
                    else:
                        file.write(record)

            if found:
                print("Record deleted successfully!")
            else:
                print("Student record not found.")

        except FileNotFoundError:
            print("File does not exist.")

# EXIT Program
#---------------------------------------------------
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")