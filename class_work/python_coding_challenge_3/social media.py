'''Problem Statement
Trending hashtags collected during an event are stored in a file named hashtags.txt.
#AI 
#Python 
#AI 
#MachineLearning 
#DataScience 
#Python 
#AI 
#Coding 
#DataScience 
#Python
Tasks
1.Count occurrences of each hashtag.
2.Display the top trending hashtag.
3.Create a set of unique hashtags.
4.Identify hashtags used more than twice.
5.Generate a trend report file.
'''

# Create hashtags file
#-------------------------------------------------
file = open("hashtags.txt", "w")
file.write("#AI #Python #AI #MachineLearning #DataScience #Python #AI #Coding #DataScience #Python")
file.close()
file = open("hashtags.txt", "r")
data = file.read()
file.close()

hashtags = data.split()

# Count frequencies
#-------------------------------------------------
frequency = {}

for tag in hashtags:
    if tag in frequency:
        frequency[tag] += 1
    else:
        frequency[tag] = 1

print("Hashtag Frequency:")

for tag, count in frequency.items():
    print(tag, ":", count)

# Top trending hashtags
#-------------------------------------------------
max_count = max(frequency.values())

print("\nTop Trending Hashtags:")

for tag, count in frequency.items():
    if count == max_count:
        print(tag)

# Unique hashtags
#-------------------------------------------------
unique_tags = set(hashtags)

print("\nUnique Hashtags:")
print(unique_tags)

# Hashtags used more than twice
#-------------------------------------------------
print("\nHashtags Used More Than Twice:")

for tag, count in frequency.items():
    if count > 2:
        print(tag)

# Generate report file
#-------------------------------------------------
file = open("trend_report.txt", "w")

for tag, count in frequency.items():
    file.write(tag + " : " + str(count) + "\n")

file.close()

print("\nTrend Report Generated Successfully.")