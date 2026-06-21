# Create a function that accepts a sentence and returns the longest word present in the string.

def longest_word(sentence):
    words = sentence.split()

    longest = words[0]

    # Check each word in the list
    #-------------------------------------------
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

text = input("Enter a sentence: ")

# Call the function and display the result
#-----------------------------------------------------
result = longest_word(text)

print("Longest word:", result)