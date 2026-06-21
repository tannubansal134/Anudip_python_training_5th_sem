# Write a program to count the frequency of each character in a given string and store the result in a dictionary.

# Input string from the user
#-----------------------------------------------------
text = input("Enter a string: ")

char_freq = {}

# Traverse each character in the string
#-----------------------------------------------------
for ch in text:
    
    if ch in char_freq:
        char_freq[ch] += 1      
    else:
        char_freq[ch] = 1      

# Display character frequencies
#-------------------------------------------------
print("\nCharacter Frequency:")
for key, value in char_freq.items():
    print(key, ":", value)