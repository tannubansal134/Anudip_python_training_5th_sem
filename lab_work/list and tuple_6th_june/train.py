"""
Program: Passenger Ticket Status Analysis

This program performs the following tasks:
1. Display all waiting-list passengers.
2. Count confirmed and waiting passengers.
3. Find whether a specific passenger has a confirmed ticket.
4. Create separate lists for confirmed and waiting passengers.
"""

passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# --------------------------------------------------
# Task 1 & Task 2 & Task 4 initialization

confirmed_count = 0
waiting_count = 0

confirmed_list = []
waiting_list = []

# --------------------------------------------------
# Task 1: Display waiting-list passengers

print("Waiting List Passengers:")

for person in passengers:
    name = person[0]
    status = person[1]

    if status == "Waiting":
        print(name)

    # --------------------------------------------------
    # Task 2: Count confirmed and waiting passengers

    if status == "Confirmed":
        confirmed_count += 1
        confirmed_list.append(name)
    else:
        waiting_count += 1
        waiting_list.append(name)

# --------------------------------------------------
# Task 3: Check specific passenger status

search_name = "Rahul"
found = False

for person in passengers:
    if person[0] == search_name:
        found = True
        if person[1] == "Confirmed":
            print("\nRahul has a Confirmed ticket")
        else:
            print("\nRahul is on Waiting list")
        break

if not found:
    print("\nPassenger not found")

# --------------------------------------------------
# Results

print("\nConfirmed Passengers :", confirmed_count)
print("Waiting Passengers :", waiting_count)

# --------------------------------------------------
# Task 4: Separate lists already created

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)