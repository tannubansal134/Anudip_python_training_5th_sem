# Read the 6-digit secret code as a string
code = input("Enter a 6-digit code: ")

# Check if the code contains exactly 6 digits
if len(code) == 6 and code.isdigit():

    # Calculate sum of first 3 digits
    first_sum = int(code[0]) + int(code[1]) + int(code[2])

    # Calculate sum of last 3 digits
    last_sum = int(code[3]) + int(code[4]) + int(code[5])

    # Check if both sums are equal
    if first_sum == last_sum:
        print("Valid Code")
    else:
        print("Invalid Code")

else:
    # Code is not exactly 6 digits
    print("Invalid Code")