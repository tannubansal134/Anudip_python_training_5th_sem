"""
Program: Vehicle Number Plate Analyzer

Tasks:
1. Extract State Code
2. Extract District Code
3. Extract Vehicle Series
4. Extract Vehicle Number
5. Count Letters and Digits separately
6. Verify 
        o First 2 characters must be alphabets.
        o Next 2 must be digits.
        o Next 2 must be alphabets.
        o Last 4 must be digits.
7. Display whether the number plate is valid
"""

# Input vehicle number
vehicle = input("Enter Vehicle Number Plate: ")

#--------------------------------------------------------
# Extract parts
state_code = vehicle[:2]
district_code = vehicle[2:4]
series = vehicle[4:6]
vehicle_number = vehicle[6:]

#--------------------------------------------------------
# Count letters and digits
letters = 0
digits = 0

for ch in vehicle:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

#--------------------------------------------------------
# Validation
valid = True

if not state_code.isalpha():
    valid = False

if not district_code.isdigit():
    valid = False

if not series.isalpha():
    valid = False

if not (vehicle_number.isdigit() and len(vehicle_number) == 4):
    valid = False
    
#--------------------------------------------------------
# Display Result
print("\nVehicle Number:", vehicle)
print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)
print("Total Letters:", letters)
print("Total Digits:", digits)

if valid:
    print("Vehicle Number Status: Valid")
else:
    print("Vehicle Number Status: Invalid")