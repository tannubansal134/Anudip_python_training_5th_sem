"""
Program: Character Frequency and Compression Analyzer

Tasks:
1. Count occurrences of each character.
2. Create a dictionary of character frequencies.
3. Display unique characters.
4. Find the most frequent character.
5. Create compressed output.
       A3B3C3D3A3
6. Calculate compression ratio.
"""

# Original text
text = "AAABBBCCCDDDAAA"

#----------------------------------------------------
# Create frequency dictionary
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

#----------------------------------------------------
# Display character frequencies
print("Original Text:", text)
print("\nCharacter Frequencies:")

for key, value in freq.items():
    print(key, "->", value)

#----------------------------------------------------
# Display unique characters
unique_chars = list(freq.keys())
print("\nUnique Characters:", unique_chars)

#----------------------------------------------------
# Find most frequent character
most_frequent = max(freq, key=freq.get)

print("Most Frequent Character:", most_frequent)

#----------------------------------------------------
# Create compressed output
compressed = ""
count = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

#----------------------------------------------------
# Add last character group
compressed += text[-1] + str(count)

print("Compressed Output:", compressed)

#----------------------------------------------------
# Length calculations
original_length = len(text)
compressed_length = len(compressed)

#----------------------------------------------------
# Compression ratio
compression_ratio = round(compressed_length / original_length, 2)

print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", compression_ratio)