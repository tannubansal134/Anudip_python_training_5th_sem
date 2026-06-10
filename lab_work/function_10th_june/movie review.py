'''Problem Statement
Movie reviews are stored as follows:
reviews = [ 
"excellent movie", 
"average story", 
"excellent acting", 
"poor direction", 
"excellent visuals", 
"poor screenplay", 
"good music", 
"excellent climax", 
"average performance", 
"good cinematography"
 ]
Requirements
Create the following functions:
1. count_sentiments(reviews)
Counts:
 • Excellent
 • Good
 • Average
 • Poor reviews
2. most_common_word(reviews)
Returns the most frequently occurring word.
3. longest_review(reviews)
Returns the review containing the maximum number of characters.
4. reviews_with_keyword(reviews, keyword)
Displays all reviews containing a given keyword.
'''
# ----------------------------------------------------------
# List of movie reviews

reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# ----------------------------------------------------------
# Function to count different sentiments

def count_sentiments(review_list):
    excellent = 0
    good = 0
    average = 0
    poor = 0
    for review in review_list:

        if review.startswith("excellent"):
            excellent += 1

        elif review.startswith("good"):
            good += 1

        elif review.startswith("average"):
            average += 1

        elif review.startswith("poor"):
            poor += 1

    # Display result
    print("Excellent Reviews :", excellent)
    print("Good Reviews      :", good)
    print("Average Reviews   :", average)
    print("Poor Reviews      :", poor)


# ----------------------------------------------------------
# Function to find the most common word
def most_common_word(review_list):
    frequency = {}
    for review in review_list:
        words = review.split()

        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

    # Find word with maximum frequency
    max_word = ""
    max_count = 0

    for word in frequency:

        if frequency[word] > max_count:
            max_count = frequency[word]
            max_word = word

    return max_word


# ----------------------------------------------------------
# Function to find the longest review

def longest_review(review_list):

    # Assume first review is longest
    longest = review_list[0]

    # Compare lengths
    for review in review_list:

        if len(review) > len(longest):
            longest = review

    return longest


# ----------------------------------------------------------
# Function to display reviews containing a keyword

def reviews_with_keyword(review_list, keyword):

    print("\nReviews containing '{}' :".format(keyword))

    found = False

    for review in review_list:

        if keyword.lower() in review.lower():
            print(review)
            found = True

    if found == False:
        print("No matching reviews found.")


# ----------------------------------------------------------
# Main Program-

print("MOVIE REVIEW ANALYSIS")
print("-" * 40)

# Count sentiments
count_sentiments(reviews)

# Find most common word
print("\nMost Common Word :", most_common_word(reviews))

# Find longest review
print("Longest Review   :", longest_review(reviews))

# Display reviews containing a keyword
reviews_with_keyword(reviews, "excellent")