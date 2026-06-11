'''Problem Statement
A company stores employee details in a text file named employees.txt.
File Format
EMP101,Anuj,45000 
EMP102,Rahul,52000
EMP103,Priya,38000
EMP104,Neha,61000
EMP105,Amit,29000 
EMP106,Sneha,55000 
EMP107,Karan,47000 
EMP108,Pooja,72000 
EMP109,Rohit,33000
EMP110,Anjali,68000
Requirements
Create a menu-driven program to:
1.Display all employee records.
2.Search employee details using Employee ID.
3.Calculate the average salary.
4.Find the highest-paid and lowest-paid employee.
5.Display employees earning above ₹50,000.
6.Add a new employee record to the file.
7.Generate salary categories:
      o High (₹60,000 and above)
      o Medium (₹40,000-₹59,999)
      o Low (Below ₹40,000)
'''

#------------------------------------------------------------------------
# Function to read employee records from file
def read_employee():
    emp_list = []

    file = open("employees.txt", "r")
    data = file.readlines()

    for line in data:
        line = line.strip()
        record = line.split(",")
        record[2] = int(record[2])
        emp_list.append(record)

    file.close()
    return emp_list

#------------------------------------------------------------------------
# Function to display all employee records
def display_employee():
    emp_list = read_employee()

    print("\nEmployee Records")
    print("--------------------------------")

    for emp in emp_list:
        print(emp[0], emp[1], emp[2])

#------------------------------------------------------------------------
# Function to search employee by ID
def search_employee():
    emp_list = read_employee()

    emp_id = input("Enter Employee ID : ")

    found = False

    for emp in emp_list:
        if emp[0] == emp_id:
            print("\nEmployee Found")
            print("ID :", emp[0])
            print("Name :", emp[1])
            print("Salary :", emp[2])
            found = True

    if found == False:
        print("Employee Not Found")

#------------------------------------------------------------------------
# Function to calculate average salary
def average_salary():
    emp_list = read_employee()

    total = 0

    for emp in emp_list:
        total = total + emp[2]

    average = total / len(emp_list)

    print("Average Salary =", average)

#------------------------------------------------------------------------
# Function to find highest and lowest salary
def highest_lowest():
    emp_list = read_employee()

    high = emp_list[0]
    low = emp_list[0]

    for emp in emp_list:

        if emp[2] > high[2]:
            high = emp

        if emp[2] < low[2]:
            low = emp

    print("\nHighest Paid Employee")
    print(high[0], high[1], high[2])

    print("\nLowest Paid Employee")
    print(low[0], low[1], low[2])

#------------------------------------------------------------------------
# Function to display employees earning above 50000
def above_50000():
    emp_list = read_employee()

    print("\nEmployees Earning Above 50000")

    for emp in emp_list:
        if emp[2] > 50000:
            print(emp[0], emp[1], emp[2])

#------------------------------------------------------------------------
# Function to add new employee
def add_employee():

    file = open("employees.txt", "a")

    emp_id = input("Enter Employee ID : ")
    name = input("Enter Employee Name : ")
    salary = input("Enter Employee Salary : ")

    file.write("\n" + emp_id + "," + name + "," + salary)

    file.close()

    print("Employee Record Added Successfully")

#------------------------------------------------------------------------
# Function to generate salary category
def salary_category():

    emp_list = read_employee()

    print("\nSalary Categories")

    for emp in emp_list:

        if emp[2] >= 60000:
            category = "High"

        elif emp[2] >= 40000:
            category = "Medium"

        else:
            category = "Low"

        print(emp[0], emp[1], emp[2], "-", category)


# ===============================
# Main Menu Driven Program
# ===============================

while True:

    print("\n====== Employee Payroll Management System ======")
    print("1. Display All Employees")
    print("2. Search Employee")
    print("3. Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Employees Earning Above 50000")
    print("6. Add New Employee")
    print("7. Salary Category")
    print("8. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        display_employee()

    elif choice == 2:
        search_employee()

    elif choice == 3:
        average_salary()

    elif choice == 4:
        highest_lowest()

    elif choice == 5:
        above_50000()

    elif choice == 6:
        add_employee()

    elif choice == 7:
        salary_category()

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

