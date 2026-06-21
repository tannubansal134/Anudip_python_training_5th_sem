# Write a program to accept names from the user until they enter "STOP" using a while loop, store them in a list, and display them in alphabetical order.

# Create an empty list to store names
#-----------------------------------------
names = []

# Accept names using a while loop
#-----------------------------------------------------
while True:
    name = input("Enter a name (or STOP to finish): ")

    if name.upper() == "STOP":
        break
    names.append(name)

names.sort()

# Display the sorted names
#---------------------------------------------------
print("\nNames in Alphabetical Order:")
for name in names:
    print(name)