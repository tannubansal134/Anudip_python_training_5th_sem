'''Problem Statement
Crop moisture levels (%) are stored as follows:
moisture = { 
"Field1": 55, 
"Field2": 30, 
"Field3": 72, 
"Field4": 28, 
"Field5": 64, 
"Field6": 35, 
"Field7": 80, 
"Field8": 42, 
"Field9": 25, 
"Field10": 68 
}
Tasks
1.Identify fields requiring irrigation (< 40%).
2.Classify fields into Low, Moderate, and High moisture categories.
3.Count fields in each category.
4.Find fields with the highest and lowest moisture levels.
5.Generate an irrigation priority list.
'''

# Moisture data
#--------------------------------------------------------
moisture = {
    "Field1": 55,
    "Field2": 30,
    "Field3": 72,
    "Field4": 28,
    "Field5": 64,
    "Field6": 35,
    "Field7": 80,
    "Field8": 42,
    "Field9": 25,
    "Field10": 68
}
low = []
moderate = []
high = []

# Fields requiring irrigation
#--------------------------------------------------------
print("Fields Requiring Irrigation:")

for field, value in moisture.items():
    if value < 40:
        print(field, end=" ")
        low.append(field)
    elif value <= 65:
        moderate.append(field)
    else:
        high.append(field)

# Display categories
#--------------------------------------------------------
print("\n\nLow Moisture Fields:", low)
print("Moderate Moisture Fields:", moderate)
print("High Moisture Fields:", high)

# Count fields in each category
#--------------------------------------------------------
print("\nLow Moisture Count:", len(low))
print("Moderate Moisture Count:", len(moderate))
print("High Moisture Count:", len(high))

# Highest and lowest moisture
#--------------------------------------------------------
highest = max(moisture, key=moisture.get)
lowest = min(moisture, key=moisture.get)

print("\nField with Highest Moisture:")
print(highest, "(" + str(moisture[highest]) + "%)")

print("Field with Lowest Moisture:")
print(lowest, "(" + str(moisture[lowest]) + "%)")

# Irrigation priority list
#--------------------------------------------------------
priority = sorted(low, key=lambda x: moisture[x])

print("Irrigation Priority List:", priority)