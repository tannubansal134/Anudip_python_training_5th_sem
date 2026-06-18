'''Problem 19: Word Frequency Analyzer
Problem Statement
A text file contains the following paragraph.
Sample Input/Data (article.txt)
Python is easy to learn.
Python is powerful. 
Python supports multiple programming paradigms. 
Programming with Python is enjoyable.
Tasks
1.Count the total number of words.
2.Count the frequency of each word.
3.Find the most frequently occurring word.
4.Display words appearing only once.
5.Display all unique words.
'''

# Open and read file
#-------------------------------------------------------
file = open("article.txt", "r")
text = file.read()
file.close()

# Convert to lowercase and remove punctuation
#-------------------------------------------------------
text = text.lower()
text = text.replace(".", "")
text = text.replace(",", "")
words = text.split()

# 1. Count total number of words
#-------------------------------------------------------
total_words = len(words)
print("Total Words:", total_words)

# 2. Count frequency of each word
#-------------------------------------------------------
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\nWord Frequencies:")
for word in freq:
    print(word, ":", freq[word])

# 3. Find most frequently occurring word
#-------------------------------------------------------
max_word = ""
max_count = 0

for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        max_word = word

print("\nMost Frequent Word:", max_word, "(", max_count, "times )")

# 4. Display words appearing only once
#-------------------------------------------------------
print("\nWords Appearing Once:")
for word in freq:
    if freq[word] == 1:
        print(word, end=" ")

# 5. Display all unique words
#-------------------------------------------------------
print("\n\nUnique Words:")
for word in freq:
    print(word, end=" ")

print("\n\nUnique Words Count:", len(freq))

