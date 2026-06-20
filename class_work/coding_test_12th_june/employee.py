# Develop a program to read employee details from a file and display employees whose salary is greater than ₹30,000 using if statements.

# Open the file in read mode
#------------------------------------------
file = open("employees 1.txt", "r")
lines = file.readlines()
print("Employees with salary greater than ₹30,000:\n")

# Process each line in the file
#--------------------------------------------------
for line in lines:

       line = line.strip()

 # Split the line into employee details
 #-----------------------------------------------
emp_id, name, salary = line.split(",")
salary = int(salary)

 # Check if salary is greater than 30000
 #------------------------------------------------
if salary > 30000:
        print("Employee ID:", emp_id)
        print("Name:", name)
        print("Salary: ₹", salary)
        print()

# Close the file
file.close()
