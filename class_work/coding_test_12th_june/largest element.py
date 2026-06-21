#  Write a program to input 10 numbers into a list and find the second largest element using iteration statements.

# Create an empty list
#--------------------------------------------
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Assume first element as largest and second largest
#-------------------------------------------------------------
largest = numbers[0]
second_largest = numbers[0]

# Find the largest element
#----------------------------------------------------
for num in numbers:
    if num > largest:
        largest = num

# Find the second largest element
#-----------------------------------------------------
for num in numbers:
    if num > second_largest and num != largest:
        second_largest = num

# Display the list and second largest element
#---------------------------------------------------------
print("\nList of Numbers:", numbers)
print("Second Largest Element:", second_largest)