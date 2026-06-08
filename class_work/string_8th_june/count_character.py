# Program to count the number of characters in a string
# without using the len() function

# Take a string input from the user
sentence = input("Enter a sentence: ")

# Initialize a counter variable
count = 0

# Traverse each character in the string
for ch in sentence:
    count += 1

# Display the total number of characters
print("Total number of characters =", count)