"""
Program: Employee Salary Processing

This program performs the following tasks:
1. Displays employees earning above ₹60,000.
2. Counts employees earning below ₹40,000.
3. Finds the highest-paid employee.
4. Creates a list of employees eligible for a bonus(salary > ₹50,000)
5. Calculates the average salary.
"""

# Dictionary containing employee IDs and salaries
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

#--------------------------------------------
# Display employees earning above ₹60,000

print("Employees earning above ₹60,000:")

for emp, sal in salary.items():
    if sal > 60000:
        print(emp, ":", sal)

#----------------------------------------
# count employees earning below ₹40,000

count = 0

for sal in salary.values():
    if sal < 40000:
        count += 1

print("\nEmployees earning below ₹40,000:", count)

#----------------------------------------------------
# Find the highest-paid employee

highest_employee = max(salary, key=salary.get)

print("\nHighest Paid Employee:")
print(highest_employee, ":", salary[highest_employee])

#---------------------------------------------------
# Create a list of employees eligible for bonus
#(Salary greater than ₹50,000)

bonus_list = []

for emp, sal in salary.items():
    if sal > 50000:
        bonus_list.append(emp)

print("\nEmployees eligible for bonus:")
print(bonus_list)

#--------------------------------------------------
# Calculate average salary

average_salary = sum(salary.values()) / len(salary)

print("\nAverage Salary: ₹", average_salary)