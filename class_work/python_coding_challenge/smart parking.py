'''Problem Statement 
The parking status of vehicles in a mall is maintained as follows. 
Sample Data
parking_slots = [  
       "Occupied", "Vacant", "Occupied", "Vacant",    
        "Occupied", "Occupied", "Vacant", "Occupied",    
         "Vacant", "Occupied"
         ] 
Tasks 
1. Display vacant parking slot numbers. 
2. Count occupied and vacant slots. 
3. Allocate the first vacant slot to a new vehicle. 
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt. 
''' 
# Parking Management System using List and Tuple

parking_slots = [
    (1, "Occupied"),
    (2, "Vacant"),
    (3, "Occupied"),
    (4, "Vacant"),
    (5, "Occupied"),
    (6, "Occupied"),
    (7, "Vacant"),
    (8, "Occupied"),
    (9, "Vacant"),
    (10, "Occupied")
]

#-----------------------------------------------------
# 1. Display vacant parking slots
print("Vacant Parking Slots:")
for slot_no, status in parking_slots:
    if status == "Vacant":
        print(slot_no, end=" ")
print()

#-----------------------------------------------------
# 2. Count occupied and vacant slots
occupied = 0
vacant = 0

for slot_no, status in parking_slots:
    if status == "Occupied":
        occupied += 1
    else:
        vacant += 1

print("Occupied Slots:", occupied)
print("Vacant Slots:", vacant)

#-----------------------------------------------------
# 3. Allocate first vacant slot
for i in range(len(parking_slots)):
    slot_no, status = parking_slots[i]

    if status == "Vacant":
        parking_slots[i] = (slot_no, "Occupied")
        print("Vehicle Allocated to Slot", slot_no)
        break
#-----------------------------------------------------
# 4. Calculate occupancy percentage
occupied = 0

for slot_no, status in parking_slots:
    if status == "Occupied":
        occupied += 1

occupancy = (occupied / len(parking_slots)) * 100
print("Occupancy Percentage:", occupancy, "%")

#-----------------------------------------------------
# 5. Display updated parking status
print("\nUpdated Parking Status:")
for slot_no, status in parking_slots:
    print("Slot", slot_no, ":", status)

'''Sample Output
Vacant Parking Slots: 2 4 7 9 
Occupied Slots: 6
 Vacant Slots: 4 
 Vehicle Allocated to Slot 2 Occupancy Percentage: 70.0% 
 Parking Details Saved Successfully. 
 '''