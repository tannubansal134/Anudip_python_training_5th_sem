'''Problem Statement
Sensor readings are stored in telemetry.txt.
101 
98 
105 
110 
112 
95 
90 
88 
120 
102
Tasks
1.Read all sensor readings.
2.Display abnormal readings (< 90 or > 110).
3.Calculate average sensor value.
4.Count normal and abnormal readings.
5.Store abnormal readings in alerts.txt.
'''

# Create telemetry.txt file and store sensor readings
#-------------------------------------------------
file = open("telemetry.txt", "w")
file.write("101 98 105 110 112 95 90 88 120 102")
file.close()

# Read all sensor readings from the file
#-------------------------------------------------
file = open("telemetry.txt", "r")
data = file.read()
file.close()
readings = list(map(int, data.split()))

# Find abnormal readings (< 90 or > 110)
#-------------------------------------------------
abnormal = []

for value in readings:
    if value < 90 or value > 110:
        abnormal.append(value)

print("Abnormal Sensor Readings:")
for value in abnormal:
    print(value, end=" ")

# Calculate average sensor value
#-------------------------------------------------
average = sum(readings) / len(readings)

print("\n\nAverage Sensor Value:", round(average, 1))

# Count normal and abnormal readings
#-------------------------------------------------
normal_count = 0
abnormal_count = 0

for value in readings:
    if value < 90 or value > 110:
        abnormal_count += 1
    else:
        normal_count += 1

print("Normal Readings:", normal_count)
print("Abnormal Readings:", abnormal_count)

# Store abnormal readings in alerts.txt
#-------------------------------------------------
file = open("alerts.txt", "w")

for value in abnormal:
    file.write(str(value) + "\n")

file.close()

print("Alert File Generated Successfully.")