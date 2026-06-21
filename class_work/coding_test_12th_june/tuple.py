# Store city names in a tuple and display them using a while loop without converting the tuple into a list.

# Create a tuple of city names
#------------------------------------------------
cities = ("Delhi", "Mumbai", "Chennai", "Kolkata", "Bengaluru")

# Initialize index variable
#------------------------------------------
i = 0

# Display city names using a while loop
#---------------------------------------------------
while i < len(cities):
    print(cities[i])
    i += 1