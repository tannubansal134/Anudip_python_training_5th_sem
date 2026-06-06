"""
Program: Passenger Count Analysis

This program performs the following tasks:
1. Find the busiest stop.
2. Display stops with fewer than 10 passengers.
3. Calculate average passengers.
4. Determine whether any stop exceeded 25 passengers.
"""

passengers = [12, 18, 25, 30, 28, 15, 8]

# --------------------------------------------------
# Task 1: Find the busiest stop

busiest = passengers[0]
busiest_stop = 0

for i in range(len(passengers)):
    if passengers[i] > busiest:
        busiest = passengers[i]
        busiest_stop = i

print("Busiest Stop : Stop", busiest_stop + 1)
print("Passengers :", busiest)

# --------------------------------------------------
# Task 2: Stops with fewer than 10 passengers

print("\nStops with Fewer Than 10 Passengers")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1, "-", passengers[i], "passengers")

# --------------------------------------------------
# Task 3: Calculate average passengers

total = 0

for p in passengers:
    total += p

average = total / len(passengers)

print("\nAverage Passengers :", average)

# --------------------------------------------------
# Task 4: Check if any stop exceeded 25 passengers

exceeded = False

for p in passengers:
    if p > 25:
        exceeded = True
        break

if exceeded:
    print("\nYes, at least one stop exceeded 25 passengers")
else:
    print("\nNo stop exceeded 25 passengers")