# WAP to input a sentence from user and count the number of special characters present in the sentence

# Take a sentence as input from the user
sentence = input("Enter a sentence: ")

# Initialize a counter variable
count = 0

# Loop through each character in the sentence
for ch in sentence:

    # Check if the character is not a letter, digit, or space
    if not ch.isalnum() and ch != " ":
        count += 1

# Display the total number of special characters
print("Number of special characters =", count)