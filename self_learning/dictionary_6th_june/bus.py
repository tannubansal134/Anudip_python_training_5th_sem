"""
Program: Bus Route Passenger Analysis

This program performs the following tasks:
1. Displays stops having more than 20 passengers.
2. Counts stops with fewer than 10 passengers.
3. Finds the busiest stop.
4. Creates a list of stops requiring an extra bus.
5. Calculates the average number of passengers.
"""

# Dictionary containing bus stops and passenger counts
passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

#----------------------------------------------- 
# display stops having more than 20 passengers

print("Stops having more than 20 passengers:")

for stop, count in passengers.items():
    if count > 20:
        print(stop, ":", count)

#------------------------------------------------
# Count stops with fewer than 10 passengers

low_count = 0

for count in passengers.values():
    if count < 10:
        low_count += 1

print("\nStops with fewer than 10 passengers:", low_count)

#-----------------------------------------------
# Find the busiest stop

busiest_stop = max(passengers, key=passengers.get)

print("\nBusiest Stop:")
print(busiest_stop, ":", passengers[busiest_stop])

#----------------------------------------------------
# Create a list of stops requiring an extra bus
# (passengers greater than 25)

extra_bus = []

for stop, count in passengers.items():
    if count > 25:
        extra_bus.append(stop)

print("\nStops requiring an extra bus:")
print(extra_bus)

#-----------------------------------------------------
# Calculate the average number of passengers

average_passengers = sum(passengers.values()) / len(passengers)

print("\nAverage Number of Passengers:", average_passengers)