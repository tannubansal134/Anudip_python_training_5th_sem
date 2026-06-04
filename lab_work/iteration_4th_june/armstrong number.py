# Program to check whether a number is an Armstrong Number

# Accept a number from the user
num = int(input("Enter a number: "))

# Store the original number
original_num = num

# Find the number of digits
digits = len(str(num))

# Variable to store the sum
sum = 0

# Calculate the sum of each digit raised to the power of number of digits
while num > 0:
    digit = num % 10          # Extract last digit
    sum = sum + digit ** digits
    num = num // 10           # Remove last digit

# Check whether the number is Armstrong or not
if sum == original_num:
    print(original_num, "is an Armstrong Number")
else:
    print(original_num, "is not an Armstrong Number")