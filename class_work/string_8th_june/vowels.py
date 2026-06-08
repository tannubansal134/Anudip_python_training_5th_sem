# Program to count the frequency of vowels in a sentence
# ignoring the case (uppercase and lowercase)

# Take a sentence as input from the user
sentence = input("Enter a sentence: ")

# Initialize counters for each vowel
a = 0
e = 0
i = 0
o = 0
u = 0

# Traverse each character in the sentence
for ch in sentence:

    # Check which vowel is present and increase its count
    if ch == 'a' or  ch == 'A':
        a += 1
    elif ch == 'e' or  ch == 'E':
        e += 1
    elif ch == 'i' or ch == 'I':
        i += 1
    elif ch == 'o' or ch == 'O':
        o += 1
    elif ch == 'u' or ch == 'U':
        u += 1

# Display the frequency of each vowel
print("Frequency of vowels:")
if a > 0:
    print("a :", a)
if e > 0:
    print("e :", e)
if i > 0:
    print("i :", i)
if o > 0:
    print("o :", o)
if u > 0:
    print("u :", u)