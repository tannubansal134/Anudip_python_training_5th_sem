# Write a function to check whether a given string is a palindrome using a while loop.

# Function to check whether a string is a palindrome
#----------------------------------------------------
def check_palindrome(text):
    text = text.lower()
    left = 0
    right = len(text) - 1

    while left < right:

 # If characters do not match, it is not a palindrome
 #---------------------------------------------------
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


# Input string from the user
#------------------------------------------------
string = input("Enter a string: ")

# Check and display the result
#-----------------------------------------------------
if check_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")