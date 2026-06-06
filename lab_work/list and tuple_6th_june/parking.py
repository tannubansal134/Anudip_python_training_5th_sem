"""
Program: Parking Slot Analysis

This program performs the following tasks:
1. Count occupied and available slots.
2. Find the first available slot.
3. Display all available slot numbers.
4. Check whether parking occupancy exceeds 75%.
"""

slots = [1, 0, 1, 1, 0, 0, 1, 0]

# --------------------------------------------------
# Task 1: Count occupied and available slots

occupied_count = 0
available_count = 0

for slot in slots:
    if slot == 1:
        occupied_count += 1
    else:
        available_count += 1

print("Occupied Slots :", occupied_count)
print("Available Slots :", available_count)

# --------------------------------------------------
# Task 2: Find the first available slot

first_available = -1

for i in range(len(slots)):
    if slots[i] == 0:
        first_available = i + 1
        break

print("\nFirst Available Slot :", first_available)

# --------------------------------------------------
# Task 3: Display all available slot numbers

print("\nAvailable Slot Numbers")

for i in range(len(slots)):
    if slots[i] == 0:
        print("Slot Number :", i + 1)

# --------------------------------------------------
# Task 4: Check whether parking occupancy exceeds 75%

total_slots = len(slots)
occupancy_percentage = (occupied_count / total_slots) * 100

print("\nOccupancy Percentage :", occupancy_percentage, "%")

if occupancy_percentage > 75:
    print("Parking Occupancy Exceeds 75%")
else:
    print("Parking Occupancy Does Not Exceed 75%")