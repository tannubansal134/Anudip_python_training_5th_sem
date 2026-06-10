''' To read the data from file and display the following:
1. No. of Vowels in file.
2. No. of characters into the file.
3. No. of lines into the file.'''
# ==========================================================
# File Handling Program
# 1. Create a file
# 2. Count vowels
# 3. Count characters
# 4. Count lines
# ==========================================================

# Create file and write data
file = open("sample.txt", "w")

file.write("Python is easy to learn.\n")
file.write("File handling is important.\n")
file.write("Practice daily for coding skills.")

file.close()

# Open file in read mode
file = open("sample.txt", "r")

data = file.read()

file.close()

# ----------------------------------------------------------
# Count vowels

vowel_count = 0

for ch in data:

    if ch.lower() in "aeiou":
        vowel_count += 1

# ----------------------------------------------------------
# Count characters

character_count = len(data)

# ----------------------------------------------------------
# Count lines

file = open("sample.txt", "r")

line_count = 0

for line in file:
    line_count += 1

file.close()

# ----------------------------------------------------------
# Display Result

print("Number of Vowels :", vowel_count)
print("Number of Characters :", character_count)
print("Number of Lines :", line_count)