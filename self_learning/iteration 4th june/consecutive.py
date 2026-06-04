# Accept a number from the user
num = int(input("Enter a number: "))

# Store the original number for display if needed
temp = num

# Assume the number is consecutive until proven otherwise
is_consecutive = True

# Check digits from right to left
while num >= 10:
    last_digit = num % 10          # Current digit
    previous_digit = (num // 10) % 10  # Digit before it

    # Check if current digit is exactly 1 greater than previous digit
    if last_digit != previous_digit + 1:
        is_consecutive = False
        break

    # Remove the last digit
    num = num // 10

# Display the result
if is_consecutive:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")