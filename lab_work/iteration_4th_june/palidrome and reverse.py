# Program to find reverse of a number and check palindrome 

# Input from user
num = int(input("Enter a number: "))

original = num
reverse = 0

# Reverse the number
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Display reverse number
print("Reverse:", reverse)

# Check palindrome condition
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")