'''Problem Statement
Daily temperatures recorded in Celsius are given below.
Sample Data
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31]
Tasks
Create functions to:
1.Convert Celsius to Fahrenheit.
2.Display all temperatures in Fahrenheit.
3.Find the highest Fahrenheit temperature.
4.Find the lowest Fahrenheit temperature.
5.Calculate the average Fahrenheit temperature.
'''

# List of temperatures in Celsius
#-------------------------------------------------------
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31]

# convert Celsius to Fahrenheit
#-------------------------------------------------------
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# display all temperatures in Fahrenheit
#-------------------------------------------------------
def display_fahrenheit(temp_list):
    fahrenheit_list = []
    
    for temp in temp_list:
        fahrenheit_list.append(celsius_to_fahrenheit(temp))
    
    print("Temperatures in Fahrenheit:")
    for temp in fahrenheit_list:
        print(temp, end=" ")
    print()
    
    return fahrenheit_list

# find highest Fahrenheit temperature
#-------------------------------------------------------
def highest_temperature(fahrenheit_list):
    return max(fahrenheit_list)

# find lowest Fahrenheit temperature
#-------------------------------------------------------
def lowest_temperature(fahrenheit_list):
    return min(fahrenheit_list)

# calculate average Fahrenheit temperature
#-------------------------------------------------------
def average_temperature(fahrenheit_list):
    return sum(fahrenheit_list) / len(fahrenheit_list)
fahrenheit_temps = display_fahrenheit(temperatures)

print("Highest Temperature:", highest_temperature(fahrenheit_temps), "°F")
print("Lowest Temperature:", lowest_temperature(fahrenheit_temps), "°F")
print("Average Temperature:", round(average_temperature(fahrenheit_temps), 2), "°F")