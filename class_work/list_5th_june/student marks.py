# List of student marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# List to store passed students
passed_students = []

# Counter for failed students
failed_count = 0

# Initialize highest and lowest marks
highest = marks[0]
lowest = marks[0]

# List to store marks above 75 (Merit List)
merit_list = []

# Traverse the list
for mark in marks:

    # Check for pass/fail
    if mark >= 40:
        passed_students.append(mark)
    else:
        failed_count += 1

    # Find highest mark
    if mark > highest:
        highest = mark

    # Find lowest mark
    if mark < lowest:
        lowest = mark

    # Create merit list
    if mark > 75:
        merit_list.append(mark)

# Display results
print("Passed Students:", passed_students)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)