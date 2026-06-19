'''Problem Statement
Two research abstracts are provided as strings.
abstract1 = "Artificial intelligence is transforming education and healthcare."
abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence."
Tasks
1.Convert both abstracts into sets of words.
2.Identify common words.
3.Identify unique words in each abstract.
4.Calculate the percentage similarity.
5.Display whether plagiarism review is required (similarity > 50%).
'''

# Abstracts
#-------------------------------------------------------------------------
abstract1 = "Artificial intelligence is transforming education and healthcare."
abstract2 = "Healthcare and education are rapidly transforming through artificial intelligence."

# 1. Convert both abstracts into sets of words
#------------------------------------------------------------------------
words1 = set(abstract1.lower().replace(".", "").split())
words2 = set(abstract2.lower().replace(".", "").split())

print("Abstract 1 Words:")
print(words1)

print("\nAbstract 2 Words:")
print(words2)

# 2. Identify common words
#------------------------------------------------------------------------
common_words = words1.intersection(words2)

print("\nCommon Words:")
print(common_words)

# 3. Identify unique words in each abstract
#------------------------------------------------------------------------
unique1 = words1 - words2
unique2 = words2 - words1

print("\nUnique Words in Abstract 1:")
print(unique1)

print("\nUnique Words in Abstract 2:")
print(unique2)

# 4. Calculate percentage similarity
#------------------------------------------------------------------------
similarity = (len(common_words) / len(words1.union(words2))) * 100

print("\nSimilarity Percentage:", round(similarity, 1), "%")

# 5. Check whether plagiarism review is 
#------------------------------------------------------------------------
print("\nPlagiarism Review Required:")

if similarity > 50:
    print("Yes")
else:
    print("No")