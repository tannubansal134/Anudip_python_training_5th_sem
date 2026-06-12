'''Problem Statement
Store statistics of at least 30 cricket players.
Example Structure
players = { 
"Virat": { 
"runs": 645, 
"matches": 12, 
"wickets": 0 
} 
}
Requirements
1.Display all player statistics.
2.Find highest run scorer.
3.Find lowest run scorer.
4.Calculate average runs.
5.Find player with maximum wickets.
6.Find all-rounders (runs > 300 and wickets > 5).
7.Display players scoring above average.
8.Create categories:
o Star Performer
o Good Performer
o Average Performer
o Poor Performer
9. Generate team statistics.
10. Display top 5 batsmen.
11. Display top 5 bowlers.
12. Create a separate dictionary for award winners.
Challenge
Generate a tournament report.
'''
# Cricket Players Statistics
#----------------------------------------------------------

players = {
    "Virat":{"runs":645,"matches":12,"wickets":0},
    "Rohit":{"runs":590,"matches":12,"wickets":1},
    "Gill":{"runs":520,"matches":11,"wickets":0},
    "KL Rahul":{"runs":430,"matches":10,"wickets":0},
    "Iyer":{"runs":410,"matches":11,"wickets":1},
    "Hardik":{"runs":350,"matches":9,"wickets":8},
    "Jadeja":{"runs":320,"matches":12,"wickets":14},
    "Ashwin":{"runs":210,"matches":10,"wickets":18},
    "Bumrah":{"runs":60,"matches":12,"wickets":22},
    "Shami":{"runs":40,"matches":11,"wickets":24},
    "Siraj":{"runs":35,"matches":12,"wickets":18},
    "Kuldeep":{"runs":75,"matches":10,"wickets":20},
    "Axar":{"runs":180,"matches":9,"wickets":11},
    "Pant":{"runs":470,"matches":10,"wickets":0},
    "Samson":{"runs":390,"matches":9,"wickets":0},
    "Surya":{"runs":510,"matches":11,"wickets":1},
    "Rinku":{"runs":280,"matches":8,"wickets":0},
    "Tilak":{"runs":300,"matches":9,"wickets":2},
    "Chahal":{"runs":50,"matches":8,"wickets":15},
    "Arshdeep":{"runs":20,"matches":10,"wickets":17},
    "Ishan":{"runs":330,"matches":8,"wickets":0},
    "Washington":{"runs":220,"matches":8,"wickets":10},
    "Prasidh":{"runs":25,"matches":7,"wickets":12},
    "Mukesh":{"runs":15,"matches":7,"wickets":9},
    "Avesh":{"runs":40,"matches":8,"wickets":13},
    "Dhruv":{"runs":260,"matches":7,"wickets":0},
    "Jitesh":{"runs":190,"matches":6,"wickets":0},
    "Sai Sudharsan":{"runs":410,"matches":9,"wickets":0},
    "Nitish":{"runs":340,"matches":8,"wickets":6},
    "Abhishek":{"runs":450,"matches":10,"wickets":7}
}
while True:

    # Menu
    print("\n===== CRICKET TOURNAMENT ANALYTICS SYSTEM =====")
    print("1. Display All Player Statistics")
    print("2. Highest Run Scorer")
    print("3. Lowest Run Scorer")
    print("4. Average Runs")
    print("5. Maximum Wicket Taker")
    print("6. Display All-Rounders")
    print("7. Players Above Average Runs")
    print("8. Categorize Players")
    print("9. Team Statistics")
    print("10. Top 5 Batsmen")
    print("11. Top 5 Bowlers")
    print("12. Award Winners Dictionary")
    print("13. Tournament Report")
    print("14. Exit")

    choice = int(input("Enter Choice : "))

 # 1. Display all player statistics
 #-------------------------------------------------------
    if choice == 1:

        print("\nPLAYER STATISTICS")

        for player in players:

            print(player,
                  players[player]["runs"],
                  players[player]["matches"],
                  players[player]["wickets"])

 # 2. Highest run scorer
 #-------------------------------------------------------
    elif choice == 2:

        max_runs = -1

        for player in players:

            if players[player]["runs"] > max_runs:

                max_runs = players[player]["runs"]
                top_batsman = player

        print("\nHighest Run Scorer")
        print(top_batsman, max_runs)

 # 3. Lowest run scorer
 #-------------------------------------------------------
    elif choice == 3:

        min_runs = 999999

        for player in players:

            if players[player]["runs"] < min_runs:

                min_runs = players[player]["runs"]
                low_batsman = player

        print("\nLowest Run Scorer")
        print(low_batsman, min_runs)

# 4. Calculate average runs
#-------------------------------------------------------
    elif choice == 4:

        total_runs = 0

        for player in players:

            total_runs += players[player]["runs"]

        avg_runs = total_runs / len(players)

        print("Average Runs =", round(avg_runs, 2))

 # 5. Maximum wicket taker
 #-------------------------------------------------------
    elif choice == 5:

        max_wickets = -1

        for player in players:

            if players[player]["wickets"] > max_wickets:

                max_wickets = players[player]["wickets"]
                best_bowler = player

        print("\nMaximum Wicket Taker")
        print(best_bowler, max_wickets)

# 6. Display all-rounders
#-------------------------------------------------------
    elif choice == 6:

        print("\nALL-ROUNDERS")

        for player in players:

            if players[player]["runs"] > 300 and players[player]["wickets"] > 5:

                print(player,
                      players[player]["runs"],
                      players[player]["wickets"])

# 7. Players above average runs
#-------------------------------------------------------
    elif choice == 7:

        total_runs = 0

        for player in players:
            total_runs += players[player]["runs"]

        avg_runs = total_runs / len(players)

        print("\nPlayers Above Average Runs")

        for player in players:

            if players[player]["runs"] > avg_runs:

                print(player,
                      players[player]["runs"])

# 8. Categorize Players
#-------------------------------------------------------
    elif choice == 8:

        print("\nPLAYER CATEGORIES")

        for player in players:

            runs = players[player]["runs"]

            if runs >= 500:
                category = "Star Performer"

            elif runs >= 350:
                category = "Good Performer"

            elif runs >= 200:
                category = "Average Performer"

            else:
                category = "Poor Performer"

            print(player, "-", category)

 # 9. Team Statistics
 #-------------------------------------------------------
    elif choice == 9:

        total_runs = 0
        total_wickets = 0
        total_matches = 0

        for player in players:

            total_runs += players[player]["runs"]
            total_wickets += players[player]["wickets"]
            total_matches += players[player]["matches"]

        print("\nTEAM STATISTICS")
        print("Total Runs :", total_runs)
        print("Total Wickets :", total_wickets)
        print("Total Matches :", total_matches)

# 10. Top 5 Batsmen
#-------------------------------------------------------
    elif choice == 10:

        temp = {}

        for player in players:
            temp[player] = players[player]

        print("\nTOP 5 BATSMEN")

        count = 0

        while count < 5:

            max_runs = -1

            for player in temp:

                if temp[player]["runs"] > max_runs:

                    max_runs = temp[player]["runs"]
                    best = player

            print(best, max_runs)

            del temp[best]

            count += 1

# 11. Top 5 Bowlers
#-------------------------------------------------------
    elif choice == 11:

        temp = {}

        for player in players:
            temp[player] = players[player]

        print("\nTOP 5 BOWLERS")

        count = 0

        while count < 5:

            max_wickets = -1

            for player in temp:

                if temp[player]["wickets"] > max_wickets:

                    max_wickets = temp[player]["wickets"]
                    best = player

            print(best, max_wickets)

            del temp[best]

            count += 1

# 12. Award Winners Dictionary
#-------------------------------------------------------
    elif choice == 12:

        awards = {}

        for player in players:

            if players[player]["runs"] > 500 or players[player]["wickets"] > 15:

                awards[player] = players[player]

        print("\nAWARD WINNERS")

        for player in awards:

            print(player,
                  awards[player]["runs"],
                  awards[player]["wickets"])

 # 13. Tournament Report
 #-------------------------------------------------------
    elif choice == 13:

        total_runs = 0
        total_wickets = 0

        max_runs = -1
        max_wickets = -1

        for player in players:

            total_runs += players[player]["runs"]
            total_wickets += players[player]["wickets"]

            if players[player]["runs"] > max_runs:

                max_runs = players[player]["runs"]
                top_batsman = player

            if players[player]["wickets"] > max_wickets:

                max_wickets = players[player]["wickets"]
                top_bowler = player

        print("\n===== TOURNAMENT REPORT =====")

        print("Total Players :", len(players))
        print("Total Runs :", total_runs)
        print("Total Wickets :", total_wickets)

        print("\nTop Batsman")
        print(top_batsman, max_runs)

        print("\nTop Bowler")
        print(top_bowler, max_wickets)

    # 14. Exit
    elif choice == 14:

        print("Program Ended Successfully")
        break

    else:

        print("Invalid Choice")