'''Problem Statement
Employee performance scores are stored below.
Sample Data
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
Tasks
1.Display employees scoring above 80.
2.Count employees needing improvement (score < 60).
3.Find the top performer.
4.Calculate average performance score.
5.Categorize employees:
o Excellent (≥ 90)
o Good (75-89)
o Average (60-74)
o Poor (< 60)
'''

# Dictionary storing employee performance scores
#---------------------------------------------------------
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

# 1. Display employees scoring above 80
#---------------------------------------------------------
print("Employees Scoring Above 80:")
for emp in performance:
    if performance[emp] > 80:
        print(emp, end=" ")

# 2. Count employees needing improvement (score < 60)
#----------------------------------------------------------
improvement = 0
for emp in performance:
    if performance[emp] < 60:
        improvement += 1

print("\n\nEmployees Needing Improvement:", improvement)

# 3. Find the top performer
#------------------------------------------------------
top_emp = ""
top_score = 0

for emp in performance:
    if performance[emp] > top_score:
        top_score = performance[emp]
        top_emp = emp

print("Top Performer:", top_emp, "(", top_score, ")", sep="")

# 4. Calculate average performance score
#----------------------------------------------------------
total = 0
for score in performance.values():
    total += score

average = total / len(performance)

print("Average Score:", round(average, 1))

# 5. Categorize employees
#------------------------------------------------------
excellent = []
good = []
average_emp = []
poor = []

for emp in performance:
    score = performance[emp]

    if score >= 90:
        excellent.append(emp)
    elif score >= 75:
        good.append(emp)
    elif score >= 60:
        average_emp.append(emp)
    else:
        poor.append(emp)

print("Excellent:", excellent)
print("Good:", good)
print("Average:", average_emp)
print("Poor:", poor)