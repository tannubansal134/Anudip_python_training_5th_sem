# Accept a number from the user
num = input("Enter a number: ")

# A mountain number must have at least 3 digits
if len(num) < 3:
    print("Not a Mountain Number")
else:
    i = 1

    # Check the increasing part
    while i < len(num) and num[i] > num[i - 1]:
        i += 1

    # Peak cannot be the first or last digit
    if i == 1 or i == len(num):
        print("Not a Mountain Number")
    else:
        # Check the decreasing part
        while i < len(num) and num[i] < num[i - 1]:
            i += 1

        # If all digits are checked successfully
        if i == len(num):
            print("Mountain Number")
        else:
            print("Not a Mountain Number")