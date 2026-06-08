"""
Program: Employee ID Validation and Analysis System

Employee ID Format Example:
EMP2026ANUJ458

Tasks Performed:
1.Count the number of uppercase letters.
2.Count the number of digits.
3.Extract the joining year.
4.Extract the employee name.
5.Check whether the ID follows these rules:
    o Starts with "EMP"
    o Contains exactly 4 digits for the year
    o Ends with exactly 3 digits
     
6.Create a list containing all digits present in the ID.
7.Find the sum of all digits present in the ID.
8.Display whether the ID is valid or invalid
"""

# Input Employee ID from user
emp_id = input("Enter Employee ID: ")

#---------------------------------------
# Count the number of uppercase letters
# using a loop and isupper() function

uppercase_count = 0

for ch in emp_id:
    if ch.isupper():
        uppercase_count += 1

#---------------------------------------
# Count the number of digits
# present in the employee ID

digit_count = 0

for ch in emp_id:
    if ch.isdigit():
        digit_count += 1

#---------------------------------------
# Extract joining year.
# Year starts after EMP and
# contains 4 digits.

joining_year = emp_id[3:7]

#---------------------------------------
# Extract employee name.
# Name is present between
# the year and last 3 digits.

employee_name = emp_id[7:-3]

#---------------------------------------
# Create a list containing
# all digits present in the ID.

digit_list = []

for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))

#---------------------------------------
# Calculate the sum of all digits.

sum_digits = sum(digit_list)

#---------------------------------------
# Validate Employee ID according
# to the given rules:

# 1. Starts with EMP
# 2. Contains exactly 4 digits for year
# 3. Ends with exactly 3 digits
# 4. Name part contains only uppercase letters

is_valid = False

if (emp_id.startswith("EMP") and
    joining_year.isdigit() and
    len(joining_year) == 4 and
    employee_name.isalpha() and
    employee_name.isupper() and
    emp_id[-3:].isdigit()):
    
    is_valid = True

#---------------------------------------
# Display all results

print("\nEmployee ID:", emp_id)
print("Uppercase Letters:", uppercase_count)
print("Digits:", digit_count)
print("Joining Year:", joining_year)
print("Employee Name:", employee_name)
print("Digit List:", digit_list)
print("Sum of Digits:", sum_digits)

if is_valid:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")