#given a list which contains bus seats marks and 1(booked) and 0(unbooked) and display following
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0] 
#Count booked and available seats
available_count=0
booked_count=0

for s in seats:
    if s==1:
        booked_count+=1
    else:
        available_count+=1

print("Booked Count is",booked_count)
print("Available Count is",available_count)

#Find first available seat and stop searching immediately
for s in seats:
    if s==0:
        print("This is the first available seat")
        break

#Create List of all available seat numbers
available_seats=[]

for s in seats:
    if s==0:
        available_seats.append(s)

print("Available_Seats",available_seats)

#Determine whether bus is more than 70% occupied
occupied_percentage=(booked_count/len(seats))*100

if occupied_percentage>70:
    print("Bus is more than 70% occupied")
else:
    print("Bus is not more than 70% occupied")