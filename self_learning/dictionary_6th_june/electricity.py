"""
Program: Electricity Consumption Analysis

This program performs the following tasks:
1. Displays houses consuming more than 300 units.
2. Counts houses consuming less than 200 units.
3. Finds the house with the highest consumption.
4. Creates a list of houses eligible for an
   energy-saving awareness campaign.
5. Categorizes houses as Low, Medium, or High
   based on electricity consumption.
"""

# Dictionary containing house numbers and electricity units consumed
units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

#------------------------------------------------ 
# Display houses consuming more than 300 units

print("Houses consuming more than 300 units:")

for house, consumption in units.items():
    if consumption > 300:
        print(house, ":", consumption)

#------------------------------------------------ 
# Count houses consuming less than 200 units

count = 0

for consumption in units.values():
    if consumption < 200:
        count += 1

print("\nNumber of houses consuming less than 200 units:", count)

#------------------------------------------------ 
# Find the house with the highest consumption

highest_house = max(units, key=units.get)

print("\nHouse with the highest consumption:")
print(highest_house, ":", units[highest_house])

#------------------------------------------------ 
# Create a list of houses eligible for
# an energy-saving awareness campaign
# (consumption greater than 400 units)

campaign_list = []

for house, consumption in units.items():
    if consumption > 400:
        campaign_list.append(house)

print("\nHouses eligible for awareness campaign:")
print(campaign_list)

#------------------------------------------------ 
# Categorize houses based on electricity consumption

# Low    : Less than 200 units
# Medium : 200 to 350 units
# High   : More than 350 units

print("\nHouse Categories:")

for house, consumption in units.items():

    if consumption < 200:
        category = "Low"

    elif 200 <= consumption <= 350:
        category = "Medium"

    else:
        category = "High"

    print(house, ":", consumption, "units ->", category)