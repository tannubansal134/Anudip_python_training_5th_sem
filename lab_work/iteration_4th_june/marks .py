# Program to calculate total marks, percentage, grade and failed subjects 

# Input marks for 5 subjects
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

# Calculate total marks
total = m1 + m2 + m3 + m4 + m5

# Calculate percentage (assuming each subject is out of 100)
percentage = (total / 500) * 100

# Count failed subjects (marks < 40)
fail_count = 0

if m1 < 40:
    fail_count += 1
if m2 < 40:
    fail_count += 1
if m3 < 40:
    fail_count += 1
if m4 < 40:
    fail_count += 1
if m5 < 40:
    fail_count += 1

# Determine grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Display results
print("\n--- Result ---")
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Number of subjects failed:", fail_count)