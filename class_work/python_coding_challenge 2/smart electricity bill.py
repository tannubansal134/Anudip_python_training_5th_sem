'''Problem Statement 
Monthly electricity consumption (units) of different houses in a residential society is stored as follows: Sample Data 
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
Tasks 
1.	Display houses consuming more than 400 units.  
2.	Find the highest-consuming house.  
3.	Find the lowest-consuming house.  
4.	Calculate the total units consumed.  
5.	Create separate lists for:  
o 	Low Consumption (< 200)  o 	Medium Consumption (200–400)  o 	High Consumption (> 400)  
6.	Count houses eligible for an energy-saving campaign (consumption > 300).  
'''
# Sample Data
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
# 1. Display houses consuming more than 400 units.
print("Houses consuming more than 400 units:")
for house, consumption in units.items():
    if consumption > 400:
        print(house)
#2. Find the highest-consuming house.
#--------------------------------------------------------
print("------------------------------------------------")
highest_consuming_house = max(units, key=units.get)
print("Hightest Consumption:\n",highest_consuming_house,"(", units[highest_consuming_house], "units)") 
#--------------------------------------------------------
print("------------------------------------------------")     
#3. Find the lowest-consuming house.
lowest_consuming_house = min(units, key=units.get)  
print("Lowest Consumption:\n",lowest_consuming_house,"(", units[lowest_consuming_house], "units)") 
#--------------------------------------------------------
print("------------------------------------------------")  
#4. Calculate the total units consumed.
total_units = sum(units.values())
print("Total Units Consumed:",total_units)
#--------------------------------------------------------
print("------------------------------------------------")  
#5. Create separate lists for:
# Low Consumption (< 200)
low_consumption = []
for house, consumption in units.items():
    if consumption < 200:
        low_consumption.append(house)
print("Low Consumption Houses:\n",low_consumption)
#--------------------------------------------------------
print("------------------------------------------------")  
#Medium Consumption (200–400)  
medium_consumption = []
for house, consumption in units.items():
    if 200 <= consumption <= 400:
        medium_consumption.append(house)    
print("Medium Consumption Houses:\n",medium_consumption)
#--------------------------------------------------------
print("------------------------------------------------")  
#High Consumption (> 400)   
high_consumption = []
for house, consumption in units.items():
    if consumption > 400:
        high_consumption.append(house)
print("High Consumption Houses:\n",high_consumption)
#--------------------------------------------------------
print("------------------------------------------------")  
#6. Count houses eligible for an energy-saving campaign (consumption > 300).
count = 0
for house, consumption in units.items():
    if consumption > 300:
        count += 1
print("Houses eligible for energy-saving campaign:", count)
#--------------------------------------------------------
print("------------------------------------------------")  

'''Sample Output 
Houses Consuming More Than 400 Units: 
House103 
House106 
House110 
 
Highest Consumption: 
House110 (600 units) 
 
Lowest Consumption: 
House109 (145 units) 
 
Total Units Consumed: 3220 
 
Low Consumption: 
['House102', 'House105', 'House109'] 
 
Medium Consumption: 
['House101', 'House104', 'House107', 'House108'] 
 
High Consumption: 
['House103', 'House106', 'House110'] 
 
Eligible for Energy-Saving Campaign: 5 
'''