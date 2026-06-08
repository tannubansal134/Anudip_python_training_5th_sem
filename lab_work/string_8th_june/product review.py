"""
Program: Product Review Analyzer

Tasks:
1. Count total words
2. Create a dictionary containing word frequencies
3. Find the most frequently used word
4. Find all words appearing only once
5. Count words having more than 5 characters
6. Display words in reverse order
7. Create a list of unique words
"""

# Input Review
review = "This product is excellent excellent excellent and very useful"

#-------------------------------------------------------------
# Convert into list of words
words = review.split()

#-------------------------------------------------------------
# Count total words
total_words = len(words)

#-------------------------------------------------------------
# Create frequency dictionary
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

#-------------------------------------------------------------
# Find most frequently word
most_frequent = max(frequency, key=frequency.get)

#-------------------------------------------------------------
# Find words appearing only once
single_words = []

for word, count in frequency.items():
    if count == 1:
        single_words.append(word)

#-------------------------------------------------------------
# Count words having more than 5 characters
count_long = 0

for word in words:
    if len(word) > 5:
        count_long += 1

#-------------------------------------------------------------
# Reverse order of words
reverse_words = words[::-1]

#-------------------------------------------------------------
# Unique words list
unique_words = list(frequency.keys())

#-------------------------------------------------------------
# Display Result
print("Total Words:", total_words)

print("\nWord Frequencies:")
for word, count in frequency.items():
    print(word, "->", count)

print("\nMost Frequent Word:", most_frequent)

print("Words Appearing Only Once:", single_words)

print("Words Having More Than 5 Characters:", count_long)

print("Words In Reverse Order:")
print(reverse_words)

print("Unique Words:")
print(unique_words)