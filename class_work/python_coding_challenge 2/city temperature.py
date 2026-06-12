'''Problem Statement 
Daily temperatures of different cities are stored below. Sample Data 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1.	Display cities with temperature above 40°C.  
2.	Find the hottest city.  
3.	Find the coolest city.  
4.	Calculate average temperature.  
5.	Create a list of pleasant cities (<35°C).  
'''
# ==========================================================
# City Temperature Monitoring System
# ==========================================================

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Display cities with temperature above 40°C
print("Cities Above 40°C:")

for city in temperature:
    if temperature[city] > 40:
        print(city)

# 2. Find the hottest city
hottest_city = ""
highest_temp = 0

for city in temperature:
    if temperature[city] > highest_temp:
        highest_temp = temperature[city]
        hottest_city = city

print("\nHottest City:")
print(hottest_city, "(", highest_temp, "°C )")

# 3. Find the coolest city
coolest_city = ""
lowest_temp = 999

for city in temperature:
    if temperature[city] < lowest_temp:
        lowest_temp = temperature[city]
        coolest_city = city

print("\nCoolest City:")
print(coolest_city, "(", lowest_temp, "°C )")

# 4. Calculate average temperature
total_temp = 0

for city in temperature:
    total_temp = total_temp + temperature[city]

average_temp = total_temp / len(temperature)

print("\nAverage Temperature:", round(average_temp, 1), "°C")

# 5. Create a list of pleasant cities (<35°C)
pleasant_cities = []

for city in temperature:
    if temperature[city] < 35:
        pleasant_cities.append(city)

print("\nPleasant Cities:")
print(pleasant_cities)
'''Sample Output 
Cities Above 40°C: 
Delhi 
Jaipur 
Ahmedabad 
 
Hottest City: 
Ahmedabad (43°C) 
 
Coolest City: 
Bengaluru (28°C) 
 
Average Temperature: 36.8°C 
 
Pleasant Cities: 
['Mumbai', 'Bengaluru', 'Pune'] 
'''