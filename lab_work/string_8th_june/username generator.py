"""
Program: Username Generator

Tasks:
1. Remove spaces from student name.
2. Convert name to lowercase.
3. Append current year (2026).
4. If username length exceeds 12 characters,keep only first 12 characters before appending year.
5. Count vowels in generated username.
6. Count consonants in generated username.
7. Display username statistics.
"""

# Input student name
name = input("Enter Student Name: ")

#--------------------------------------------------
# Remove spaces
username = name.replace(" ", "")

#--------------------------------------------------
# Convert to lowercase
username = username.lower()

#--------------------------------------------------
# Keep only first 12 characters if length exceeds 12
if len(username) > 12:
    username = username[:12]

#--------------------------------------------------
# Append current year
username = username + "2026"

#--------------------------------------------------
# Count vowels and consonants
vowels = 0
consonants = 0

for ch in username:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
            
#--------------------------------------------------
# Display results
print("\nOriginal Name:", name)
print("Generated Username:", username)
print("Username Length:", len(username))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Status: Username Generated Successfully")