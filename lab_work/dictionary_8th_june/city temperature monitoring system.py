"""
Program: City Temperature Monitoring System

This program performs the following tasks:
1. Display cities having temperature above 40°C.
2. Find the hottest city.
3. Find the coolest city.
4. Calculate average temperature.
5. Create a list of pleasant cities (temperature < 35°C).
6. Count cities with temperature between 35°C and 40°C.
"""

# Dictionary containing city temperatures
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

#-------------------------------------------------
# Display cities having temperature above 40°C

print("Cities Above 40°C:")

for city, temp in temperature.items():
    if temp > 40:
        print(city, end=" ")
print()

#-------------------------------------------------
# Find the hottest city

hottest_city = max(temperature, key=temperature.get)

print(
    "\nHottest City:",
    hottest_city,
    f"({temperature[hottest_city]}°C)"
)

#-------------------------------------------------
# Find the coolest city

coolest_city = min(temperature, key=temperature.get)

print(
    "Coolest City:",
    coolest_city,
    f"({temperature[coolest_city]}°C)"
)

#-------------------------------------------------
# Calculate average temperature

total_temperature = sum(temperature.values())
average_temperature = total_temperature / len(temperature)

print(
    "Average Temperature:",
    round(average_temperature, 1),
    "°C"
)

#-------------------------------------------------
# Create a list of pleasant cities
# Temperature less than 35°C

pleasant_cities = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print("Pleasant Cities:", pleasant_cities)

"""
Task 6:
Count cities with temperature between
35°C and 40°C (inclusive)
"""
count = 0

for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1

print("Cities Between 35°C and 40°C:", count)