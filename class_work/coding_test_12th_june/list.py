# Write a program to input 8 numbers into a list, convert them into a set, and display the unique elements in ascending order.

# Create an empty list
#-----------------------------------------------------
numbers = []

# Input 8 numbers from the user
#-------------------------------------------------------
for i in range(8):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Convert the list into a set to remove duplicates
#------------------------------------------------------
unique_numbers = set(numbers)

# Convert the set into a sorted list
#-----------------------------------------------------
sorted_numbers = sorted(unique_numbers)

# Display the unique elements in ascending order
#--------------------------------------------------------
print("\nUnique elements in ascending order:")
print(sorted_numbers)