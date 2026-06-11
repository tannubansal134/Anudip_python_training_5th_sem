'''The amount of waste collected (in kilograms) from different sectors of a city is stored below. Sample Data waste = { 
    "Sector1": 320, 
    "Sector2": 180, 
    "Sector3": 510, 
    "Sector4": 275, 
    "Sector5": 150, 
    "Sector6": 430, 
    "Sector7": 220, 
    "Sector8": 390, 
    "Sector9": 145, 
    "Sector10": 600 
} 
Tasks 
1.	Display sectors generating more than 400 kg of waste.  
2.	Find the sector generating maximum waste.  
3.	Find the sector generating minimum waste.  
4.	Calculate the total waste collected.  
5.	Categorize sectors:  
o 	Low Waste (<200 kg)  o 	Medium Waste (200–400 kg)  o 	High Waste (>400 kg)  
6.	Count sectors requiring awareness campaigns (waste generation >300 kg).  
7.	Save the awareness campaign list to campaign_sectors.txt.  
'''
# Smart City Waste Collection Management System

waste = {
    "Sector1": 320,
    "Sector2": 180,
    "Sector3": 510,
    "Sector4": 275,
    "Sector5": 150,
    "Sector6": 430,
    "Sector7": 220,
    "Sector8": 390,
    "Sector9": 145,
    "Sector10": 600
}

# -----------------------------------
# Sectors Generating More Than 400 kg
# -----------------------------------

print("Sectors Generating More Than 400 kg Waste:")

for sector, amount in waste.items():

    if amount > 400:
        print(sector)

# -----------------------------------
# Maximum and Minimum Waste
# -----------------------------------

max_sector = max(waste, key=waste.get)
min_sector = min(waste, key=waste.get)

print("\nMaximum Waste Generation:")
print(max_sector, f"({waste[max_sector]} kg)")

print("\nMinimum Waste Generation:")
print(min_sector, f"({waste[min_sector]} kg)")

# -----------------------------------
# Total Waste Collected
# -----------------------------------

total = sum(waste.values())

print("\nTotal Waste Collected:", total, "kg")

# -----------------------------------
# Waste Categories
# -----------------------------------

low = []
medium = []
high = []

for sector, amount in waste.items():

    if amount < 200:
        low.append(sector)

    elif amount <= 400:
        medium.append(sector)

    else:
        high.append(sector)

print("\nLow Waste:")
print(low)

print("\nMedium Waste:")
print(medium)

print("\nHigh Waste:")
print(high)

# -----------------------------------
# Awareness Campaign Sectors
# -----------------------------------

campaign_file = open("campaign_sectors.txt", "w")

print("\nSectors Requiring Awareness Campaign:")

for sector, amount in waste.items():

    if amount > 300:

        print(sector)

        campaign_file.write(sector + "\n")

campaign_file.close()

print("\nCampaign Report Generated Successfully.")
'''Sample Output 
Sectors Generating More Than 400 kg Waste: 
Sector3 
Sector6 
Sector10 
 
Maximum Waste Generation: 
Sector10 (600 kg) 
 
Minimum Waste Generation: 
Sector9 (145 kg) 
 
Total Waste Collected: 3220 kg 
 
Low Waste: 
['Sector2', 'Sector5', 'Sector9'] 
 
Medium Waste: 
['Sector1', 'Sector4', 'Sector7', 'Sector8'] 
 
High Waste: 
['Sector3', 'Sector6', 'Sector10'] 
 
Sectors Requiring Awareness Campaign: 
Sector1 
Sector3 
Sector6 
Sector8 
Sector10 
 
Campaign Report Generated Successfully. 
'''