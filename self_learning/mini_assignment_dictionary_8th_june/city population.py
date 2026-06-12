'''Problem Statement
The government wants to analyze city data.
Store details of at least 30 cities.
Example Structure
cities = { 
"Delhi": { 
"population": 32000000, 
"area": 1484, 
"literacy": 89 
} 
}
Requirements
1.Display all city details.
2.Find the most populated city.
3.Find the least populated city.
4.Calculate average population.
5.Display cities with literacy rate above 90%.
6.Display cities with literacy below average.
7.Calculate population density.
8.Find city with highest density.
9.Categorize cities:
o Small
o Medium
o Large
10. Create a development-priority list.
11.Generate separate dictionaries for:
o High Literacy Cities
o Low Literacy Cities
12. Generate a national summary report.
Challenge
Rank all cities based on population density.
'''
# City Data
#----------------------------------------------------------

cities = {
    "Delhi":{"population":32000000,"area":1484,"literacy":89},
    "Mumbai":{"population":21000000,"area":603,"literacy":91},
    "Kolkata":{"population":15000000,"area":206,"literacy":88},
    "Chennai":{"population":11000000,"area":426,"literacy":92},
    "Bengaluru":{"population":14000000,"area":741,"literacy":90},
    "Hyderabad":{"population":12000000,"area":650,"literacy":87},
    "Pune":{"population":8000000,"area":516,"literacy":91},
    "Ahmedabad":{"population":9000000,"area":505,"literacy":86},
    "Jaipur":{"population":4500000,"area":467,"literacy":84},
    "Lucknow":{"population":4000000,"area":631,"literacy":82},
    "Kanpur":{"population":3200000,"area":403,"literacy":81},
    "Nagpur":{"population":3100000,"area":227,"literacy":89},
    "Indore":{"population":3500000,"area":530,"literacy":87},
    "Bhopal":{"population":2500000,"area":463,"literacy":88},
    "Patna":{"population":2800000,"area":250,"literacy":80},
    "Surat":{"population":7000000,"area":461,"literacy":89},
    "Vadodara":{"population":2500000,"area":235,"literacy":88},
    "Agra":{"population":2200000,"area":188,"literacy":78},
    "Meerut":{"population":1800000,"area":141,"literacy":77},
    "Varanasi":{"population":1700000,"area":112,"literacy":81},
    "Ranchi":{"population":1600000,"area":175,"literacy":85},
    "Raipur":{"population":1500000,"area":226,"literacy":86},
    "Jodhpur":{"population":1400000,"area":233,"literacy":83},
    "Amritsar":{"population":1300000,"area":139,"literacy":87},
    "Gwalior":{"population":1200000,"area":289,"literacy":84},
    "Udaipur":{"population":900000,"area":64,"literacy":90},
    "Mysuru":{"population":1100000,"area":128,"literacy":92},
    "Coimbatore":{"population":2200000,"area":246,"literacy":91},
    "Dehradun":{"population":1000000,"area":300,"literacy":93},
    "Shimla":{"population":200000,"area":35,"literacy":94}
}
while True:

    # Menu
    print("\n===== CITY POPULATION & DEVELOPMENT DASHBOARD =====")
    print("1. Display All City Details")
    print("2. Most Populated City")
    print("3. Least Populated City")
    print("4. Average Population")
    print("5. Cities With Literacy Above 90%")
    print("6. Cities With Literacy Below Average")
    print("7. Calculate Population Density")
    print("8. City With Highest Density")
    print("9. Categorize Cities")
    print("10. Development Priority List")
    print("11. High & Low Literacy Dictionaries")
    print("12. National Summary Report")
    print("13. Rank Cities By Density")
    print("14. Exit")

    choice = int(input("Enter Choice : "))

 # 1. Display all cities
 #-------------------------------------------------------  
    if choice == 1:

        print("\nCITY DETAILS")

        for city in cities:

            print(city,
                  cities[city]["population"],
                  cities[city]["area"],
                  cities[city]["literacy"])

# 2. Most populated city
#-------------------------------------------------------
    elif choice == 2:

        max_pop = -1

        for city in cities:

            if cities[city]["population"] > max_pop:

                max_pop = cities[city]["population"]
                top_city = city

        print("\nMost Populated City")
        print(top_city, max_pop)

# 3. Least populated city
#-------------------------------------------------------
    elif choice == 3:

        min_pop = 999999999

        for city in cities:

            if cities[city]["population"] < min_pop:

                min_pop = cities[city]["population"]
                low_city = city

        print("\nLeast Populated City")
        print(low_city, min_pop)

# 4. Average population
#-------------------------------------------------------
    elif choice == 4:

        total_population = 0

        for city in cities:

            total_population += cities[city]["population"]

        average = total_population / len(cities)

        print("Average Population =", round(average, 2))

# 5. Literacy above 90%
#-------------------------------------------------------
    elif choice == 5:

        print("\nCities With Literacy Above 90%")

        for city in cities:

            if cities[city]["literacy"] > 90:

                print(city,
                      cities[city]["literacy"])

# 6. Literacy below average
#-------------------------------------------------------
    elif choice == 6:

        total_literacy = 0

        for city in cities:
            total_literacy += cities[city]["literacy"]

        avg_literacy = total_literacy / len(cities)

        print("Average Literacy =", round(avg_literacy, 2))

        print("\nCities Below Average Literacy")

        for city in cities:

            if cities[city]["literacy"] < avg_literacy:

                print(city,
                      cities[city]["literacy"])

# 7. Population Density
#-------------------------------------------------------
    elif choice == 7:

        print("\nPopulation Density")

        for city in cities:

            density = cities[city]["population"] / cities[city]["area"]

            print(city,
                  round(density, 2))

# 8. Highest Density City
#-------------------------------------------------------
    elif choice == 8:

        max_density = -1

        for city in cities:

            density = cities[city]["population"] / cities[city]["area"]

            if density > max_density:

                max_density = density
                dense_city = city

        print("\nHighest Density City")
        print(dense_city,
              round(max_density, 2))

# 9. Categorize Cities
#-------------------------------------------------------
    elif choice == 9:

        print("\nCITY CATEGORIES")

        for city in cities:

            pop = cities[city]["population"]

            if pop < 2000000:
                category = "Small"

            elif pop < 10000000:
                category = "Medium"

            else:
                category = "Large"

            print(city, "-", category)

# 10. Development Priority List
#-------------------------------------------------------
    elif choice == 10:

        print("\nDevelopment Priority Cities")

        for city in cities:

            if cities[city]["literacy"] < 85:

                print(city,
                      cities[city]["literacy"])

# 11. High Literacy & Low Literacy Dictionaries
#-------------------------------------------------------
    elif choice == 11:

        high_literacy = {}
        low_literacy = {}

        for city in cities:

            if cities[city]["literacy"] >= 90:

                high_literacy[city] = cities[city]

            else:

                low_literacy[city] = cities[city]

        print("\nHigh Literacy Cities")

        for city in high_literacy:
            print(city)

        print("\nLow Literacy Cities")

        for city in low_literacy:
            print(city)

# 12. National Summary Report
#-------------------------------------------------------
    elif choice == 12:

        total_population = 0
        total_literacy = 0

        max_pop = -1
        min_pop = 999999999

        for city in cities:

            total_population += cities[city]["population"]
            total_literacy += cities[city]["literacy"]

            if cities[city]["population"] > max_pop:

                max_pop = cities[city]["population"]
                top_city = city

            if cities[city]["population"] < min_pop:

                min_pop = cities[city]["population"]
                low_city = city

        avg_population = total_population / len(cities)
        avg_literacy = total_literacy / len(cities)

        print("\n===== NATIONAL SUMMARY REPORT =====")

        print("Total Cities :", len(cities))
        print("Average Population :", round(avg_population, 2))
        print("Average Literacy :", round(avg_literacy, 2))

        print("Most Populated City :", top_city)
        print("Least Populated City :", low_city)

# 13. Rank Cities By Density
#-------------------------------------------------------
    elif choice == 13:

        temp = {}

 # Create temporary dictionary
#-------------------------------------------------------
        for city in cities:
            temp[city] = cities[city]

        rank = 1

        print("\nCITY DENSITY RANKING")

        while len(temp) > 0:

            max_density = -1

            for city in temp:

                density = temp[city]["population"] / temp[city]["area"]

                if density > max_density:

                    max_density = density
                    best_city = city

            print(rank,
                  best_city,
                  round(max_density, 2))

            del temp[best_city]

            rank += 1

# 14. Exit
    elif choice == 14:

        print("Program Ended Successfully")
        break

    else:

        print("Invalid Choice")