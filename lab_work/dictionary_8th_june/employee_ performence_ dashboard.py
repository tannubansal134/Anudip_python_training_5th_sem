"""
Program: Employee Performance Dashboard

This program performs the following tasks:
1. Display employees scoring above 80.
2. Count employees needing improvement (score < 60).
3. Find the top performer.
4. Calculate average performance score.
5. Create separate lists:
   - Excellent (>= 90)
   - Good (75 - 89)
   - Average (60 - 74)
   - Poor (< 60)
"""

# Dictionary containing employee performance scores
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

#--------------------------------------------
# Display employees scoring above 80

print("Employees Scoring Above 80:")

for emp_id, score in performance.items():
    if score > 80:
        print(emp_id, end=" ")
print()

#--------------------------------------------
# Count employees needing improvement
# Employees with score less than 60

improvement_count = 0

for score in performance.values():
    if score < 60:
        improvement_count += 1

print("Employees Needing Improvement:", improvement_count)

#--------------------------------------------
# Find the top performer

top_employee = max(performance, key=performance.get)

print(
    "Top Performer:",
    top_employee,
    f"({performance[top_employee]})"
)

#--------------------------------------------
# Calculate average performance score

total_score = sum(performance.values())
average_score = total_score / len(performance)

print("Average Score:", round(average_score, 1))

#--------------------------------------------
# Create separate lists based on performance categories

excellent = []
good = []
average = []
poor = []

for emp_id, score in performance.items():

    if score >= 90:
        excellent.append(emp_id)

    elif 75 <= score <= 89:
        good.append(emp_id)

    elif 60 <= score <= 74:
        average.append(emp_id)

    else:
        poor.append(emp_id)

print("Excellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)