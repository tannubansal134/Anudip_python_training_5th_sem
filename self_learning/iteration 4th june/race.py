# Read number of racers
N = int(input("Enter number of racers: "))

# Read lap time of first racer
time = float(input("Enter lap time of racer 1: "))

# Initialize fastest and slowest values
fastest_time = time
slowest_time = time

# Store positions of fastest and slowest racers
fastest_pos = 1
slowest_pos = 1

# Read remaining racers' lap times
for i in range(2, N + 1):
    time = float(input(f"Enter lap time of racer {i}: "))

    # Check for fastest racer (minimum lap time)
    if time < fastest_time:
        fastest_time = time
        fastest_pos = i

    # Check for slowest racer (maximum lap time)
    if time > slowest_time:
        slowest_time = time
        slowest_pos = i

# Calculate difference between fastest and slowest lap times
difference = slowest_time - fastest_time

# Display results
print("Fastest Racer Position =", fastest_pos)
print("Slowest Racer Position =", slowest_pos)
print("Difference =", difference)