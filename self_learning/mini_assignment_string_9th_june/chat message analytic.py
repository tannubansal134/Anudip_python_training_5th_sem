'''Problem Statement
A messaging application wants to analyze chat messages.
Store at least 20 chat messages in a list.
Requirements
For each message:
1.Count total words.
2.Count total characters.
3.Count vowels and consonants.
4.Find longest word.
5.Find shortest word.
6.Count occurrence of each word.
7.Display repeated words.
8.Display words starting with vowels.
9.Display words longer than 5 characters.
10.Create a dictionary containing word frequencies.
Challenge
Generate a report showing:
Most Frequently Used Word 
Longest Message 
Shortest Message 
Average Words Per Message
'''

# Store 20 messages in a single string
#------------------------------------------------------
messages = input("Enter Messages Separated By | : ")

# Split messages
#----------------------------------------------------------
msg_list = messages.split("|")

total_words_all = 0
longest_message = ""
shortest_message = msg_list[0]

for msg in msg_list:

    print("\nMessage :", msg)

# Count words
#--------------------------------------------------------
    words = msg.split()
    print("Total Words :", len(words))

# Count characters
#--------------------------------------------------------
    print("Total Characters :", len(msg))

# Count vowels and consonants
#--------------------------------------------------------
    vowels = 0
    consonants = 0

    for ch in msg.lower():

        if ch.isalpha():

            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels :", vowels)
    print("Consonants :", consonants)

# Longest and shortest word
#--------------------------------------------------------
    longest_word = ""
    shortest_word = words[0]

    for word in words:

        if len(word) > len(longest_word):
            longest_word = word

        if len(word) < len(shortest_word):
            shortest_word = word

    print("Longest Word :", longest_word)
    print("Shortest Word :", shortest_word)

# Words starting with vowels
#--------------------------------------------------------
    print("Words Starting With Vowel")

    for word in words:

        if word[0].lower() in "aeiou":
            print(word)

# Words longer than 5 characters
#--------------------------------------------------------
    print("Words Longer Than 5 Characters")

    for word in words:

        if len(word) > 5:
            print(word)

    total_words_all += len(words)

    if len(msg) > len(longest_message):
        longest_message = msg

    if len(msg) < len(shortest_message):
        shortest_message = msg

print("\nAverage Words Per Message :", total_words_all/len(msg_list))
print("Longest Message :", longest_message)
print("Shortest Message :", shortest_message)