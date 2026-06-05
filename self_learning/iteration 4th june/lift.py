# Lift starts at floor 0
current_floor = 0

# Variable to store total floors travelled
total_travelled = 0

# Repeatedly take destination floor input
while True:
    destination = int(input("Enter Destination (-1 to stop): "))

    # Stop the program if user enters -1
    if destination == -1:
        break

    # Calculate floors travelled in this trip
    travelled = abs(destination - current_floor)

    # Display floors travelled
    print("Travelled:", travelled, "floors")

    # Add to total travelled floors
    total_travelled += travelled

    # Update current floor
    current_floor = destination

# Display total floors travelled
print("Total Travelled:", total_travelled, "floors")