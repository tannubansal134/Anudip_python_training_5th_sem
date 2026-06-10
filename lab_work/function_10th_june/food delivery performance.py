''' Problem Statement
Delivery times (in minutes) for different orders are given below:
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

Requirements
Create the following functions:
1. fastest_delivery(times)
Returns the shortest delivery time.
2. delayed_orders(times)
Returns a list of orders taking more than 45 minutes.
3. average_delivery_time(times)
Returns the average delivery time.
4. delivery_category(times)
Displays order categories:
      • Fast → ≤ 30 minutes
      • Normal → 31-45 minutes
      • Delayed → > 45 minutes
'''

# -------------------------------------------------------
# List containing delivery times (in minutes)

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# -------------------------------------------------------
# Function to find the fastest delivery

def fastest_delivery(times):
 minimum = times[0]
 for time in times:

        if time < minimum:
            minimum = time
        return minimum


# -------------------------------------------------------
# Function to find delayed orders
# Orders taking more than 45 minutes

def delayed_orders(times):
    delayed = []
    for time in times:

        if time > 45:
            delayed.append(time)
    return delayed


# -------------------------------------------------------
# Function to calculate average delivery time

def average_delivery_time(times):
    total = 0
    for time in times:
        total += time
    average = total / len(times)
    return average

# -------------------------------------------------------
# Function to display delivery categories

def delivery_category(times):

    print("\nDelivery Categories")
    for time in times:

        if time <= 30:
            print(time, "-> Fast")

        elif time <= 45:
            print(time, "-> Normal")

        else:
            print(time, "-> Delayed")


# -------------------------------------------------------
# Main Program

# Calling fastest_delivery function
fastest = fastest_delivery(delivery_time)

print("Fastest Delivery :", fastest, "minutes")

# Calling delayed_orders function
delayed = delayed_orders(delivery_time)

print("Delayed order :", delayed)

# Calling average_delivery_time function
average = average_delivery_time(delivery_time)

print("Average Delivery Time :", round(average, 1), "minutes")

# Calling delivery_category function
delivery_category(delivery_time)