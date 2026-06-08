"""
Program: Chat Message Analysis System

Message:
Python is awesome and Python is easy to learn

Tasks Performed:
1. Count total characters
2. Count total words
3. Find the longest word
4. Find the shortest word
5. Count how many times the word "Python" appears.
6. Create a list of words having more than 4 characters
7. Display all words starting with a vowel
8. Count the number of vowels and consonants
"""

# Input message from user
message = input("Enter Message: ")

#------------------------------------------
# Count total characters using len() function.
total_characters = len(message)

#------------------------------------------
# Convert the message into a list of words.
words = message.split()

#------------------------------------------
# Count total number of words.
total_words = len(words)

#------------------------------------------
# Find the longest word.

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

#------------------------------------------
# Find the shortest word.

shortest_word = words[0]

for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

#------------------------------------------
# Count how many times the word 'Python' appears.

python_count = 0

for word in words:
    if word == "Python":
        python_count += 1

#------------------------------------------
# Create a list of words having more than 4 characters.

long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

#------------------------------------------
# Create a list of words starting with a vowel.

vowel_words = []

for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

#------------------------------------------
# Count vowels and consonants. Spaces are ignored.

vowel_count = 0
consonant_count = 0

for ch in message:
    
    if ch.isalpha():
        
        if ch.lower() in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

#------------------------------------------
# Display all results.

print("\nMessage:", message)
print("Total Characters:", total_characters)
print("Total Words:", total_words)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Occurrences of Python:", python_count)
print("Words Longer Than 4 Characters:", long_words)
print("Words Starting With Vowel:", vowel_words)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)