# Read the number as a string
num = input("Enter a number: ")

# Check if the number has an even number of digits
if len(num) % 2 == 0:

    # Find the middle position
    mid = len(num) // 2

    # Split into left half and right half
    left_half = num[:mid]
    right_half = num[mid:]

    # Compare both halves
    if left_half == right_half:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")

else:
    # Odd-length numbers cannot have equal halves
    print("Not a Mirror Number")