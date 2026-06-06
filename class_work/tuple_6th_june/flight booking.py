#Program to do flight reservation using python
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

#Task 1:Display all passengers whose booking status is confirmed
print("Confirmed Passengers")
for passenger in bookings:
    if passenger[2]=="Confirmed":
        print("Passenger ID :", passenger[0])
        print("Destination :", passenger[1])
        print("Status :", passenger[2])

#Task 2:Count the number of passengers travelling to delhi
delhi_count=0
for passenger in bookings:
    if passenger[1]=="Delhi":
        delhi_count+=1

print("Passengers travelling to Delhi :", delhi_count)

#Task 3:Count Confirmed,Waiting,Cancelled bookings
confirmed_count=0
waiting_count=0
cancelled_count=0
for passenger in bookings:
    if passenger[2]=="Confirmed":
        confirmed_count+=1
    elif passenger[2]=="Waiting":
        waiting_count+=1
    elif passenger[2]=="Cancelled":
        cancelled_count+=1

print("Confirmed :",confirmed_count)
print("Waiting :",waiting_count)
print("Cancelled :",cancelled_count)

#Task 4:Create a List Containing passengers with Waiting status
waiting_status=[]
for passenger in bookings:
    if passenger[2]=="Waiting":
        waiting_status.append(passenger[0])

print("Passengers with Waiting Status")
print(waiting_status)

#Task 5:Count the destination with highest number of bookings
delhi_booking=0
mumbai_booking=0
chennai_booking=0
for passenger in bookings:
    if passenger[1]=="Delhi":
        delhi_booking+=1
    elif passenger[1]=="Mumbai":
        mumbai_booking+=1
    elif passenger[1]=="Chennai":
        chennai_booking+=1

print("Delhi :", delhi_booking)
print("Mumbai :", mumbai_booking)
print("Chennai :", chennai_booking)

if delhi_booking>mumbai_booking and delhi_booking>chennai_booking:
    print("Highest bookings destination is Delhi")
elif mumbai_booking>delhi_booking and mumbai_booking>chennai_booking:
    print("Highest bookings destination is Mumbai")
else:
    print("Highest bookings destination is Chennai")