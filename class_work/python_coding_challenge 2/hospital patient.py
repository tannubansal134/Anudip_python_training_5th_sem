'''Problem Statement 
Patient heart rates are recorded below. Sample Data 
heart_rate = {     "P101": 72, 
    "P102": 105, 
    "P103": 88, 
    "P104": 120, 
    "P105": 65, 
    "P106": 98, 
    "P107": 110, 
    "P108": 70, 
    "P109": 85, 
    "P110": 130 
} 
Tasks 
1.	Display critical patients (heart rate >100).  
2.	Find highest and lowest heart rate.  
3.	Calculate average heart rate.  
4.	Count stable patients (60–100 bpm).  
'''
# ==========================================================
# Hospital Patient Monitoring System
# ==========================================================

heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70,
    "P109": 85,
    "P110": 130
}

# 1. Display critical patients (heart rate > 100)
print("Critical Patients:")

for patient in heart_rate:
    if heart_rate[patient] > 100:
        print(patient)

# 2. Find highest heart rate
highest_patient = ""
highest_rate = 0

for patient in heart_rate:
    if heart_rate[patient] > highest_rate:
        highest_rate = heart_rate[patient]
        highest_patient = patient

print("\nHighest Heart Rate:")
print(highest_patient, "(", highest_rate, "bpm )")

# 3. Find lowest heart rate
lowest_patient = ""
lowest_rate = 999

for patient in heart_rate:
    if heart_rate[patient] < lowest_rate:
        lowest_rate = heart_rate[patient]
        lowest_patient = patient

print("\nLowest Heart Rate:")
print(lowest_patient, "(", lowest_rate, "bpm )")

# 4. Calculate average heart rate
total_rate = 0

for patient in heart_rate:
    total_rate = total_rate + heart_rate[patient]

average_rate = total_rate / len(heart_rate)

print("\nAverage Heart Rate:", round(average_rate, 1), "bpm")

# 5. Count stable patients (60–100 bpm)
stable_patients = 0

for patient in heart_rate:
    if heart_rate[patient] >= 60 and heart_rate[patient] <= 100:
        stable_patients += 1

print("\nStable Patients:", stable_patients)
'''Sample Output 
Critical Patients: 
P102 
P104 
P107 
P110 
 
Highest Heart Rate:
P110 (130 bpm) 
 
Lowest Heart Rate: 
P105 (65 bpm) 
 
Average Heart Rate: 94.3 bpm 
 
Stable Patients: 6 
'''