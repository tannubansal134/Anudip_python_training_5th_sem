'''Problem Statement
A news agency wants to analyze the content of an article.
Use a paragraph containing at least 300 words.
Requirements
1.Count total characters.
2.Count total words.
3.Count total sentences.
4.Count vowels and consonants.
5.Find longest word.
6.Find shortest word.
7.Find the most frequent word.
8.Create a dictionary of word frequencies.
9.Display words appearing only once.
10.Display words appearing more than 5 times.
11.Count words starting with each alphabet.
12.Display all unique words.
Challenge
Generate a complete text summary:
Total Words 
Total Sentences 
Average Word Length 
Most Frequent Word 
Vocabulary Size'''
# Input article paragraph
#------------------------------------------------------
article = input("Enter Article : ")

# Total characters
#------------------------------------------------------
print("Total Characters :", len(article))

# Total words
#------------------------------------------------------
words = article.split()
print("Total Words :", len(words))

# Total sentences
#------------------------------------------------------
sentences = article.count(".") + article.count("?") + article.count("!")
print("Total Sentences :", sentences)

# Count vowels and consonants
#------------------------------------------------------
vowels = 0
consonants = 0

for ch in article.lower():

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels :", vowels)
print("Consonants :", consonants)

# Longest and shortest word
#------------------------------------------------------
longest = ""
shortest = words[0]

for word in words:

    word = word.replace(".", "")

    if len(word) > len(longest):
        longest = word

    if len(word) < len(shortest):
        shortest = word

print("Longest Word :", longest)
print("Shortest Word :", shortest)

# Display unique words
#------------------------------------------------------
print("\nUnique Words")

unique = ""

for word in words:

    word = word.lower()

    if word not in unique:
        print(word)
        unique += word + " "

# Average word length
#------------------------------------------------------
total_length = 0

for word in words:
    total_length += len(word)

print("Average Word Length :", total_length/len(words))
print("Vocabulary Size :", len(unique.split()))