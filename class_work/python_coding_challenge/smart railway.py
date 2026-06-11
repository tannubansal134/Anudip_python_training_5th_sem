'''A railway reservation system stores the booking status of seats in a train coach. Sample Data 
seats = {     1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 
Tasks 
1.	Display all available seat numbers.  
2.	Count booked and available seats.  
3.	Reserve the first available seat.  
4.	Cancel booking for a given seat number.  
5.	Store the updated reservation status in reservations.txt.  
6.	Display occupancy percentage
'''
# Railway Reservation System

#---------------------------------------------------
# Smart Railway Reservation System

seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}

# --------------------------------------------------
# Available Seats
# --------------------------------------------------

print("Available Seats:")

for seat_no, status in seats.items():

    if status == "Available":
        print(seat_no, end=" ")

print("\n")

# --------------------------------------------------
# Count Seats
# --------------------------------------------------

booked = 0
available = 0

for status in seats.values():

    if status == "Booked":
        booked += 1
    else:
        available += 1

print("Booked Seats:", booked)
print("Available Seats:", available)
print()

# --------------------------------------------------
# Reserve First Available Seat
# --------------------------------------------------

for seat_no, status in seats.items():

    if status == "Available":

        seats[seat_no] = "Booked"

        print(f"Seat {seat_no} Reserved Successfully.")
        break

print()

# --------------------------------------------------
# Occupancy Percentage
# --------------------------------------------------

booked = 0

for status in seats.values():

    if status == "Booked":
        booked += 1

occupancy = (booked / len(seats)) * 100

print(f"Occupancy Percentage: {occupancy:.1f}%")
print()

# --------------------------------------------------
# Save Reservation Status
# --------------------------------------------------

filev = open("reservations.txt", "w")

for seat_no, status in seats.items():

    filev.write(f"{seat_no},{status}\n")

filev.close()

print("Reservation Details Saved Successfully.")
'''Sample Output 
Available Seats: 
2 4 7 9 
 
Booked Seats: 6 
Available Seats: 4 
 
Seat 2 Reserved Successfully. 
 
Occupancy Percentage: 70.0% 
 
Reservation Details Saved Successfully. 
'''