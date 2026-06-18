'''Problem Statement
A training institute collects feedback from students after completing a Python course. The feedback comments are stored in a text file named feedback.txt.
Sample Input/Data (feedback.txt)
The sessions were very interactive and informative.
Excellent teaching methodology and practical examples. 
The pace of the course was appropriate. 
More real-world projects should be included. 
The trainer explained concepts very clearly.
Tasks
1.Count the total number of lines.
2.Count the total number of words.
3.Count the total number of characters.
4.Find the longest feedback comment.
5.Find the shortest feedback comment.
6.Count the total number of vowels present in the file.
'''


# Open the file in read mode
#-------------------------------------------------------
file = open("feedback.txt", "r")

lines = file.readlines()
file.close()

# Count total lines
#-------------------------------------------------------
total_lines = len(lines)

# Initialize variables
#-------------------------------------------------------
total_words = 0
total_characters = 0
total_vowels = 0

# Assume first line as longest and shortest initially
#-------------------------------------------------------
longest_feedback = lines[0].strip()
shortest_feedback = lines[0].strip()

for line in lines:

    words = line.split()
    total_words += len(words)

    total_characters += len(line.strip())

# Find longest feedback comment
#-------------------------------------------------------
    if len(line.strip()) > len(longest_feedback):
        longest_feedback = line.strip()

# Find shortest feedback comment
#-------------------------------------------------------
    if len(line.strip()) < len(shortest_feedback):
        shortest_feedback = line.strip()

# Count vowels
#-------------------------------------------------------
    for ch in line.lower():
        if ch in "aeiou":
            total_vowels += 1

# Display results
#-------------------------------------------------------
print("Total Lines:", total_lines)
print("Total Words:", total_words)
print("Total Characters:", total_characters)
print("Longest Feedback:", longest_feedback)
print("Shortest Feedback:", shortest_feedback)
print("Total Vowels:", total_vowels)