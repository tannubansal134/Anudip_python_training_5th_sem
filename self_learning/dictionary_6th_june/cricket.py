"""
Program: Cricket Scoreboard Analysis

This program performs the following tasks:
1. Displays players who scored 50 or more runs.
2. Counts the number of centuries.
3. Finds the player with the highest score.
4. Creates a list of players scoring below 30 runs.
5. Determines how many players scored between 50 and 99.
"""

# Dictionary containing player names and scores
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

#-----------------------------------------------
# Display players who scored 50 or more runs

print("Players who scored 50 or more runs:")

for player, score in scores.items():
    if score >= 50:
        print(player, ":", score)

#----------------------------------------
# Count the number of centuries
# (Century means score of 100 or more

centuries = 0

for score in scores.values():
    if score >= 100:
        centuries += 1

print("\nNumber of centuries:", centuries)

#---------------------------------------------
# Find the player with the highest score

highest_player = max(scores, key=scores.get)

print("\nPlayer with the highest score:")
print(highest_player, ":", scores[highest_player])

#-----------------------------------------------
# create a list of players scoring below 30 runs

low_scorers = []

for player, score in scores.items():
    if score < 30:
        low_scorers.append(player)

print("\nPlayers scoring below 30 runs:")
print(low_scorers)

#-------------------------------------------
# Determine how many players scored
# between 50 and 99 runs

count = 0

for score in scores.values():
    if 50 <= score <= 99:
        count += 1

print("\nPlayers scoring between 50 and 99 runs:", count)