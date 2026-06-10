'''Problem Statement         
A railway coach has seats represented as follows:
seats = [
 "Booked", "Available", "Booked", "Booked", 
 "Available", "Available", "Booked", "Available", 
 "Booked", "Booked", "Available", "Booked" 
 ]

Requirements
Create the following functions:
1. count_seats(seats)
Returns the number of booked and available seats.
2. first_available(seats)
Returns the seat number of the first available seat.
3. occupancy_percentage(seats)
Returns the percentage of occupied seats.
4. display_available_seats(seats)
Displays all available seat numbers.
'''
 # -------------------------------------------------------
# List containing seat status

seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# -------------------------------------------------------
# Function to count booked and available seats

def count_seats(seats):
    booked_seats = 0
    available_seats = 0
    for seat in seats:

        if seat == "Booked":
            booked_seats += 1
        else:
            available_seats += 1
    return booked_seats, available_seats


# -------------------------------------------------------
# Function to find first available seat

def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
          return i + 1
    return "NO Available seat"

# -------------------------------------------------------
# Function to calculate occupancy percentage
def occupancy_percentage(seats):
    occupied_seats = 0
    for seat in seats:

        if seat == "Booked":
            occupied_seats+= 1
    percentage = (occupied_seats / len(seats)) * 100
    return percentage

# -------------------------------------------------------
# Function to display all available seat numbers

def display_available_seats(seats):

    print("Available Seat Numbers:", end=" ")

    for index in range(len(seats)):

        if seats[index] == "Available":
            print(index + 1, end=" ")

    print()
# -------------------------------------------------------
# Main Program

# Calling count_seats function
booked, available = count_seats(seats)

print("Booked Seats    :", booked)
print("Available Seats :", available)

# Calling first_available function
seat_no = first_available(seats)

print("\nFirst Available Seat :", seat_no)

# Calling occupancy_percentage function
percent = occupancy_percentage(seats)

print("\nOccupancy Percentage :", round(percent, 2), "%")

# Calling display_available_seats function
display_available_seats(seats)