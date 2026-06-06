
#Program to create a dictionary of 10 employees.
#Employee ID is used as the key and Salary is used as the value.

# Find the total number of employees having salary greater than 30000.
# Display the list of employees whose salary is below 20000.


# Create an empty dictionary
employees = {}

# Input details of 10 employees
for i in range(10):
    emp_id = input("Enter Employee ID: ")
    salary = int(input("Enter Salary: "))

    # Store employee ID and salary in dictionary
    employees[emp_id] = salary

#----------------------------------------------------
#Count employees whose salary is greater than 30000
count = 0

for salary in employees.values():
    if salary > 30000:
        count += 1

print("\nTotal employees having salary greater than 30000 =", count)

#---------------------------------------------------
# Display employee IDs whose salary is below 20000

print("\nEmployees having salary below 20000:")

for emp_id, salary in employees.items():
    if salary < 20000:
        print(emp_id)