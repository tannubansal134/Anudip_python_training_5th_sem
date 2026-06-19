'''Problem Statement
Vehicle counts recorded at a junction every 15 minutes are stored as follows:
traffic = [120, 95, 140, 180, 75, 60, 200, 160, 110, 85]
Tasks
1.Classify traffic conditions:
o Low (< 80 vehicles)
o Moderate (80-150 vehicles)
o High (> 150 vehicles)
2.Count occurrences of each traffic condition.
3.Find the peak traffic interval.
4.Create separate lists for each traffic category.
5.Recommend whether manual traffic control is required (more than 3 High traffic intervals
'''

# Traffic data
#--------------------------------------------------------
traffic = [120, 95, 140, 180, 75, 60, 200, 160, 110, 85]
low = []
moderate = []
high = []

print("Traffic Conditions:")

# Classify traffic
#--------------------------------------------------------
for count in traffic:

    if count < 80:
        print(count, "-> Low")
        low.append(count)

    elif count <= 150:
        print(count, "-> Moderate")
        moderate.append(count)

    else:
        print(count, "-> High")
        high.append(count)

# Count intervals
#--------------------------------------------------------
print("\nLow Traffic Intervals:", len(low))
print("Moderate Traffic Intervals:", len(moderate))
print("High Traffic Intervals:", len(high))

# Peak traffic
#--------------------------------------------------------
peak = max(traffic)

print("\nPeak Traffic Count:", peak, "vehicles")

# Lists
#--------------------------------------------------------
print("Low Traffic List:", low)
print("Moderate Traffic List:", moderate)
print("High Traffic List:", high)

# Manual traffic control recommendation
#--------------------------------------------------------
if len(high) > 3:
    print("\nManual Traffic Control Required: Yes")
else:
    print("\nManual Traffic Control Required: No")