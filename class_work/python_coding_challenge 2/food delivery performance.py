'''Problem Statement 
Delivery times (in minutes) for different orders are recorded below: Sample Data 
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Tasks 
1.	Find the fastest delivery time.  
2.	Find the slowest delivery time.  
3.	Calculate the average delivery time.  
4.	Display delayed orders (>45 minutes).  
5.	Categorize deliveries:  
o 	Fast (≤30 minutes)  o 	Normal (31–45 minutes)  o 	Delayed (>45 minutes)  
'''
#-------------------------------------------------------------
# ==========================================================
# Delivery Performance Tracker
# ==========================================================

delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Find the fastest delivery time
#----------------------------------------------------------
fastest_delivery = min(delivery_times)
print("Fastest Delivery:", fastest_delivery, "minutes")

# 2. Find the slowest delivery time
#----------------------------------------------------------

slowest_delivery = max(delivery_times)
print("\nSlowest Delivery:", slowest_delivery, "minutes")

# 3. Calculate the average delivery time
#-------------------------------------------------------------
average_delivery = sum(delivery_times) / len(delivery_times)
print("\nAverage Delivery Time:", round(average_delivery, 1), "minutes")

# 4. Display delayed orders (>45 minutes)
#------------------------------------------------------------
delayed_orders = []

for time in delivery_times:
    if time > 45:
        delayed_orders.append(time)

print("\nDelayed Orders:")
print(delayed_orders)

# 5. Categorize deliveries
#-------------------------------------------------------------
fast_count = 0
normal_count = 0
delayed_count = 0

for time in delivery_times:
    if time <= 30:
        fast_count += 1
    elif 31 <= time <= 45:
        normal_count += 1
    else:
        delayed_count += 1

print("\nFast Deliveries:", fast_count)
print("Normal Deliveries:", normal_count)
print("Delayed Deliveries:", delayed_count)



'''Sample Output 
Fastest Delivery: 18 minutes 
 
Slowest Delivery: 80 minutes 
 
Average Delivery Time: 40.8 minutes 
 
Delayed Orders: 
[60, 80, 55] 
 
Fast Deliveries: 4 
Normal Deliveries: 3 
Delayed Deliveries: 3 
'''