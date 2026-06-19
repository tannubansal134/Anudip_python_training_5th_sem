'''Problem Statement
Patients arriving at the emergency ward are categorized as:
patients = [ 
("P101", "Critical"), 
("P102", "Stable"), 
("P103", "Critical"), 
("P104", "Moderate"), 
("P105", "Stable"), 
("P106", "Critical"),
("P107", "Moderate"),
("P108", "Stable"), 
("P109", "Critical"), 
("P110", "Moderate") 
]
Tasks
1.Count patients in each category.
2.Display IDs of critical patients.
3.Create separate lists for Critical, Moderate, and Stable patients.
4.Determine which category requires maximum attention.
5.Save critical patient IDs to critical_patients.txt.
'''

# Patient data
#--------------------------------------------------------
patients = [
    ("P101", "Critical"),
    ("P102", "Stable"),
    ("P103", "Critical"),
    ("P104", "Moderate"),
    ("P105", "Stable"),
    ("P106", "Critical"),
    ("P107", "Moderate"),
    ("P108", "Stable"),
    ("P109", "Critical"),
    ("P110", "Moderate")
]

critical = []
moderate = []
stable = []

# Categorize patients
#--------------------------------------------------------
for pid, status in patients:
    if status == "Critical":
        critical.append(pid)
    elif status == "Moderate":
        moderate.append(pid)
    else:
        stable.append(pid)

# Display counts
#--------------------------------------------------------
print("Patient Count by Category:")
print("Critical :", len(critical))
print("Moderate :", len(moderate))
print("Stable :", len(stable))

# Display critical patients
#--------------------------------------------------------
print("\nCritical Patients:")
for pid in critical:
    print(pid, end=" ")

# Display lists
#--------------------------------------------------------
print("\n\nCritical Patients List:", critical)
print("Moderate Patients List:", moderate)
print("Stable Patients List:", stable)

# Maximum attention category
#--------------------------------------------------------
counts = {
    "Critical": len(critical),
    "Moderate": len(moderate),
    "Stable": len(stable)
}

attention = max(counts, key=counts.get)

print("\nCategory Requiring Maximum Attention:", attention)

# Save critical patients to file
#--------------------------------------------------------
file = open("critical_patients.txt", "w")

for pid in critical:
    file.write(pid + "\n")

file.close()

print("Critical Patient Report Generated Successfully.")