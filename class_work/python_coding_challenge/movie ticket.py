'''Seat booking status in a cinema hall is stored as follows. Sample Data 
tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
} 
Tasks 
1.	Display available seats.  
2.	Count booked and available seats.  
3.	Reserve the first available seat.  
4.	Save updated booking details to tickets.txt.  
5.	Calculate hall occupancy percentage.
'''
# Cinema Hall Ticket Booking System

tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}

# ----------------------------------
# Display Available Seats
# ----------------------------------

print("Available Seats:")

for seat, status in tickets.items():

    if status == "Available":
        print(seat)

# ----------------------------------
# Count Seats
# ----------------------------------

booked = 0
available = 0

for status in tickets.values():

    if status == "Booked":
        booked += 1
    else:
        available += 1

print("\nBooked Seats:", booked)
print("Available Seats:", available)

# ----------------------------------
# Reserve First Available Seat
# ----------------------------------

for seat, status in tickets.items():

    if status == "Available":

        tickets[seat] = "Booked"

        print(f"\nSeat {seat} Reserved Successfully.")

        break

# ----------------------------------
# Hall Occupancy Percentage
# ----------------------------------

booked = 0

for status in tickets.values():

    if status == "Booked":
        booked += 1

percentage = (booked / len(tickets)) * 100

print(f"\nHall Occupancy Percentage: {percentage:.1f}%")

# ----------------------------------
# Save Booking Details
# ----------------------------------

filev = open("tickets.txt", "w")

for seat, status in tickets.items():

    filev.write(seat + "," + status + "\n")

filev.close()

print("\nBooking Details Saved Successfully.")

'''Sample Output 
Available Seats: 
A2 
A4 
B2 
B4 
C2 
 
Booked Seats: 5 
Available Seats: 5 
 
Seat A2 Reserved Successfully. 
 
Hall Occupancy Percentage: 60.0% 
 
Booking Details Saved Successfully. 
'''