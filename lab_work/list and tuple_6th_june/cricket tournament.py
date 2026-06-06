"""
Program: Batsman's Score Analysis

This program performs the following tasks:
1. Count half-centuries and centuries.
2. Find the highest score.
3. Display all scores below 20.
4. Calculate the average score.
"""

scores = [45, 78, 12, 100, 67, 8, 90, 55]

# --------------------------------------------------
# Task 1: Count half-centuries and centuries-

half_centuries = 0
centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Number of Half-Centuries :", half_centuries)
print("Number of Centuries :", centuries)

# --------------------------------------------------
# Task 2: Find the highest score-

highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print("\nHighest Score :", highest_score)

# --------------------------------------------------
# Task 3: Display all scores below 20

print("\nScores Below 20")

for score in scores:
    if score < 20:
        print(score)

# --------------------------------------------------
# Task 4: Calculate the average score

total_score = 0

for score in scores:
    total_score += score

average_score = total_score / len(scores)

print("\nTotal Score :", total_score)
print("Average Score :", average_score)