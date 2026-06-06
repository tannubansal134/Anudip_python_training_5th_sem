#program to display employee performance managememt using tuples
employees = (    
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76), 
    ("E103", "Priya", 58), 
    ("E104", "Neha", 88), 
    ("E105", "Amit", 45) 
    ) 

# Task 1: Display details of employees scoring 80 or above

print("Employees Scoring 80 or Above")
for emp in employees:
    if emp[2] >= 80:
        print("Employee ID:", emp[0])
        print("Name:", emp[1])
        print("Score:", emp[2])

# Task 2: Count employees who need improvement (score below 60)

count=0
for emp in employees:
    if emp[2] < 60:
        count += 1

print("Employees who needs improvement are:", count)

# Task 3: Find employee with the highest score

highest=employees[0]
for emp in employees:
    if emp[2]>highest[2]:
        highest = emp

print("Employee with Highest Score")
print("Employee ID:", highest[0])
print("Name:", highest[1])
print("Score:", highest[2])

# Task 4: Create a list of employee names scoring above 75

high_performers=[]
for emp in employees:
    if emp[2]>75:
        high_performers.append(emp[1])

print("Employees Scoring Above 75")
print(high_performers)

# Task 5: Display performance category for each employee

print("Employee Performance Categories")
for emp in employees:
    if emp[2]>=90:
        category="Excellent"
    elif emp[2]>=75:
        category="Good"
    elif emp[2]>=60:
        category="Average"
    else:
        category="Needs Improvement"

    print("Name :", emp[1])
    print("Category :", category)