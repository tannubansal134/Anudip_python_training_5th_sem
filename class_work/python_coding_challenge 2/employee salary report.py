'''Problem Statement
Employee details are stored in a text file named employees.txt.
Sample Input/Data (employees.txt)
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
Tasks
1.Display employees earning more than ₹50,000.
2.Find the highest-paid employee.
3.Find the lowest-paid employee.
4.Calculate the average salary.
5.Generate salary categories:
o High (≥ ₹60,000)
o Medium (₹40,000 - ₹59,999)
o Low (< ₹40,000)
'''

# Open the file and read all employee records
#-------------------------------------------------------
file = open("employees.txt", "r")

employees_above_50000 = []

high_salary = []
medium_salary = []
low_salary = []

highest_salary = 0
highest_employee = ""

lowest_salary = 999999
lowest_employee = ""

total_salary = 0
count = 0

for line in file:
    
    line = line.strip()
    
    data = line.split(",")
    
    emp_id = data[0]
    name = data[1]
    salary = int(data[2])

    total_salary += salary
    count += 1

# Employees earning more than 50000
#-------------------------------------------------------
    if salary > 50000:
        employees_above_50000.append(name)

 # Find highest paid employee
 #-------------------------------------------------------
    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name

# Find lowest paid employee
#-------------------------------------------------------
    if salary < lowest_salary:
        lowest_salary = salary
        lowest_employee = name

 # Salary categories
 #-------------------------------------------------------
    if salary >= 60000:
        high_salary.append(name)
    elif salary >= 40000:
        medium_salary.append(name)
    else:
        low_salary.append(name)

file.close()

# Calculate average salary
#-------------------------------------------------------
average_salary = total_salary / count

# Display report
#-------------------------------------------------------
print("Employees Earning Above ₹50,000:")
for name in employees_above_50000:
    print(name)

print("\nHighest Paid Employee:", highest_employee, "(₹" + str(highest_salary) + ")")
print("Lowest Paid Employee:", lowest_employee, "(₹" + str(lowest_salary) + ")")
print("Average Salary: ₹", average_salary)

print("\nHigh Salary:", high_salary)
print("Medium Salary:", medium_salary)
print("Low Salary:", low_salary)