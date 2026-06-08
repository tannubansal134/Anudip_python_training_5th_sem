"""
Program: Cricket Tournament Statistics

This program performs the following tasks:
1. Display players scoring more than 500 runs.
2. Find the Orange Cap winner.
3. Find the lowest scorer.
4. Calculate total runs scored.
5. Create a list of players scoring below 400.
6. Count players scoring between 400 and 600 runs.
"""

# Dictionary containing runs scored by players
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

#-------------------------------------------------
# Display players scoring more than 500 runs

print("Players Scoring More Than 500 Runs:")

for player, score in runs.items():
    if score > 500:
        print(player, end=" ")
print()

#-------------------------------------------------
# Find the Orange Cap winner

orange_cap = max(runs, key=runs.get)

print(
    "\nOrange Cap Winner:",
    orange_cap,
    f"({runs[orange_cap]})"
)

#-------------------------------------------------
# Find the lowest scorer

lowest_scorer = min(runs, key=runs.get)

print(
    "Lowest Scorer:",
    lowest_scorer,
    f"({runs[lowest_scorer]})"
)

#-------------------------------------------------
# Calculate total runs scored

total_runs = sum(runs.values())

print("Total Tournament Runs:", total_runs)

#-------------------------------------------------
# Create a list of players scoring below 400

below_400 = []

for player, score in runs.items():
    if score < 400:
        below_400.append(player)

print("Players Scoring Below 400:", below_400)

#-------------------------------------------------
# Count players scoring between 400 and 600 runs
# (Including 400 and 600)

count = 0

for score in runs.values():
    if 400 <= score <= 600:
        count += 1

print("Players Between 400 and 600 Runs:", count)