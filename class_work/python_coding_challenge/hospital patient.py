'''A hospital maintains patient details in a file named patients.txt. 
Sample Input/Data (patients.txt) 
P101,Anuj,Normal 
P102,Rahul,Critical 
P103,Priya,Stable 
P104,Neha,Critical 
P105,Amit,Stable 
P106,Sneha,Normal 
P107,Karan,Critical 
P108,Pooja,Stable 
P109,Rohit,Normal 
P110,Anjali,Stable 
Tasks 
1.	Display all patient records.  
2.	Display critical patients.  
3.	Count patients under each status.  
4.	Search patient details using Patient ID.  
5.	Save critical patient records to critical_patients.txt.  
'''
# Hospital Patient Record Management System

# --------------------------------------------
# Display All Patient Records
# --------------------------------------------

filev = open("patients.txt", "r")

print("Patient Records:\n")

line = filev.readline()

while line:
    print(line.strip())
    line = filev.readline()

filev.close()

# --------------------------------------------
# Display Critical Patients
# --------------------------------------------

filev = open("patients.txt", "r")

print("\nCritical Patients:")

line = filev.readline()

while line:

    data = line.strip().split(",")

    if data[2] == "Critical":
        print(data[1])

    line = filev.readline()

filev.close()

# --------------------------------------------
# Count Patient Status
# --------------------------------------------

normal = 0
stable = 0
critical = 0

filev = open("patients.txt", "r")

line = filev.readline()

while line:

    data = line.strip().split(",")

    if data[2] == "Normal":
        normal += 1

    elif data[2] == "Stable":
        stable += 1

    else:
        critical += 1

    line = filev.readline()

filev.close()

print("\nPatient Count:")
print("Normal :", normal)
print("Stable :", stable)
print("Critical :", critical)

# --------------------------------------------
# Search Patient
# --------------------------------------------

patient_id = input("\nEnter Patient ID : ")

filev = open("patients.txt", "r")

found = False

line = filev.readline()

while line:

    data = line.strip().split(",")

    if data[0] == patient_id:

        print("\nPatient Found:")
        print(line.strip())

        found = True
        break

    line = filev.readline()

if found == False:
    print("Patient Not Found")

filev.close()

# --------------------------------------------
# Save Critical Patients
# --------------------------------------------

filev = open("patients.txt", "r")
report = open("critical_patients.txt", "w")

line = filev.readline()

while line:

    data = line.strip().split(",")

    if data[2] == "Critical":
        report.write(line)

    line = filev.readline()

filev.close()
report.close()

print("\nCritical Patient Report Generated Successfully.")


'''Sample Output 
Critical Patients: 
Rahul 
Neha 
Karan 
 
Patient Count: 
Normal : 3 
Stable : 4 
Critical : 3 
 
Patient Found: 
P104,Neha,Critical 
 
Critical Patient Report Generated Successfully. 
'''