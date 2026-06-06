"""
Program: Employee Salary Analysis

This program performs the following tasks:
1. Display employees earning above ₹50,000.
2. Find the highest-paid employee.
3. Calculate the total salary expenditure.
4. Count employees earning below ₹40,000.
"""

employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# --------------------------------------------------
# Task 1: Display employees earning above ₹50,000

print("Employees Earning Above ₹50,000")

for employee in employees:
    name = employee[0]
    salary = employee[1]

    if salary > 50000:
        print(name, "-", salary)

# --------------------------------------------------
# Task 2: Find the highest-paid employee

highest_paid = employees[0]

for employee in employees:
    if employee[1] > highest_paid[1]:
        highest_paid = employee

print("\nHighest-Paid Employee :", highest_paid[0])
print("Salary :", highest_paid[1])

# --------------------------------------------------
# Task 3: Calculate the total salary expenditure

total_salary = 0

for employee in employees:
    total_salary += employee[1]

print("\nTotal Salary Expenditure :", total_salary)

# --------------------------------------------------
# Task 4: Count employees earning below ₹40,000

count_below_40000 = 0

for employee in employees:
    if employee[1] < 40000:
        count_below_40000 += 1

print("\nNumber of Employees Earning Below ₹40,000 :",
      count_below_40000)