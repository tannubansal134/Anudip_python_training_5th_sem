"""
Program: Smart Electricity Billing System

This program performs the following tasks:
1. Display houses consuming more than 400 units.
2. Find the highest-consuming house.
3. Find the lowest-consuming house.
4. Calculate total units consumed.
5. Create lists:
   - Low Consumption (< 200)
   - Medium Consumption (200–400)
   - High Consumption (> 400)
6. Count houses eligible for an energy-saving campaign
   (consumption > 300).
"""

# Dictionary containing monthly electricity consumption
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

#---------------------------------------------- 
# Display houses consuming more than 400 units

print("Houses Consuming More Than 400 Units:")

for house, consumption in units.items():
    if consumption > 400:
        print(house, end=" ")
print()

#---------------------------------------------- 
# Find the highest-consuming house

highest_house = max(units, key=units.get)

print(
    "\nHighest Consumption:",
    highest_house,
    f"({units[highest_house]} units)"
)

#---------------------------------------------- 
# Find the lowest-consuming house

lowest_house = min(units, key=units.get)

print(
    "Lowest Consumption:",
    lowest_house,
    f"({units[lowest_house]} units)"
)

#---------------------------------------------- 
# Calculate total units consumed

total_units = sum(units.values())

print("Total Units Consumed:", total_units)

#---------------------------------------------- 
# Create separate consumption lists

low_consumption = []
medium_consumption = []
high_consumption = []

for house, consumption in units.items():

    if consumption < 200:
        low_consumption.append(house)

    elif 200 <= consumption <= 400:
        medium_consumption.append(house)

    else:
        high_consumption.append(house)

print("Low Consumption:", low_consumption)
print("Medium Consumption:", medium_consumption)
print("High Consumption:", high_consumption)

#---------------------------------------------- 
# Count houses eligible for an energy-saving campaign
# Consumption greater than 300 units

eligible_count = 0

for consumption in units.values():
    if consumption > 300:
        eligible_count += 1

print("Eligible for Energy-Saving Campaign:", eligible_count)