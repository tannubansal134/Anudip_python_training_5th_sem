# Create a function that accepts a string and returns the count of vowels and consonants using iteration statements.
# Function to count vowels and consonants in a string
def count_vowels_consonants(text):
    vowels = 0       # Variable to store vowel count
    consonants = 0   # Variable to store consonant count
    for ch in text.lower():

        if ch.isalpha():

            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


# Take input from the user
#------------------------------------------
s = input("Enter a string: ")

# Call the function
#-------------------------------------------------------
vowel_count, consonant_count = count_vowels_consonants(s)

# Display the results
#-----------------------------------------------------
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)