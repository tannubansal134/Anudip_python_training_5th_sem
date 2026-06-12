'''Problem Statement 
Daily mobile screen time (in minutes) of a student is recorded for 10 days. Sample Data screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260] 
Tasks 
1.	Calculate average screen time.  
2.	Find the highest and lowest screen time.  
3.	Count days exceeding 200 minutes.  
4.	Display days with healthy usage (<180 minutes).  
5.	Categorize usage:  
o 	Healthy (<180)  o 	Moderate (180–240)  o 	Excessive (>240)  
'''
# ==========================================================
# Mobile Screen Time Analysis System
# ==========================================================

screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]

# 1. Calculate average screen time
#--------------------------------------------------------
total = 0

for time in screen_time:
    total = total + time

average = total / len(screen_time)

print("Average Screen Time:", average, "minutes")

# 2. Find highest and lowest screen time
#--------------------------------------------------------
highest = screen_time[0]
lowest = screen_time[0]

for time in screen_time:
    if time > highest:
        highest = time

    if time < lowest:
        lowest = time

print("\nHighest Screen Time:", highest, "minutes")
print("\nLowest Screen Time:", lowest, "minutes")

# 3. Count days exceeding 200 minutes
#---------------------------------------------------------
count = 0

for time in screen_time:
    if time > 200:
        count += 1

print("\nDays Exceeding 200 Minutes:", count)

# 4. Display healthy usage days (<180)
#---------------------------------------------------------
print("\nHealthy Usage Days:")

for i in range(len(screen_time)):
    if screen_time[i] < 180:
        print("Day", i + 1)

# 5. Categorize usage
#------------------------------------------
healthy = 0
moderate = 0
excessive = 0

for time in screen_time:
    if time < 180:
        healthy += 1
    elif time <= 240:
        moderate += 1
    else:
        excessive += 1

print("\nHealthy:", healthy)
print("Moderate:", moderate)
print("Excessive:", excessive)

'''Sample Output 
Average Screen Time: 205.5 minutes 
 
Highest Screen Time: 300 minutes 
 
Lowest Screen Time: 120 minutes 
 
Days Exceeding 200 Minutes: 5 
 
Healthy Usage Days: 
Day 3 
Day 5 
Day 9 
 
Healthy: 3 
Moderate: 4 
Excessive: 3 
'''


















   