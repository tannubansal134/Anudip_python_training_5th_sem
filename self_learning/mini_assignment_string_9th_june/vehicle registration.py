'''Problem Statement
A transport department wants to verify vehicle registration numbers.
Store at least 20 vehicle numbers.
Example
MH12AB4589 
DL05XY9988 
KA03PQ1234
Requirements
For each registration number:
1.Extract state code.
2.Extract district code.
3.Extract series.
4.Extract vehicle number.
5.Count letters and digits.
6.Validate format:
o First 2 characters = Alphabets
o Next 2 characters = Digits
o Next 2 characters = Alphabets
o Last 4 characters = Digits
7.Display invalid registrations.
8.Count vehicles state-wise.
Challenge
Generate a state-wise report:
MH -> 6 Vehicles 
DL -> 4 Vehicles 
KA -> 5 Vehicles 
UP -> 5 Vehicles
'''
# Input 20 vehicle numbers separated by space
#------------------------------------------------------
vehicles = input("Enter Vehicle Numbers : ")

vehicle_list = vehicles.split()

mh = 0
dl = 0
ka = 0
up = 0

for num in vehicle_list:

    print("\nVehicle :", num)

# Extract parts
#------------------------------------------------------
    state = num[:2]
    district = num[2:4]
    series = num[4:6]
    vehicle_no = num[6:]

    print("State :", state)
    print("District :", district)
    print("Series :", series)
    print("Vehicle Number :", vehicle_no)

    letters = 0
    digits = 0

    for ch in num:

        if ch.isalpha():
            letters += 1

        if ch.isdigit():
            digits += 1

    print("Letters :", letters)
    print("Digits :", digits)

 # Validation
 #------------------------------------------------------
    if len(num) == 10 and \
       num[:2].isalpha() and \
       num[2:4].isdigit() and \
       num[4:6].isalpha() and \
       num[6:].isdigit():

        print("Valid Registration")

    else:
        print("Invalid Registration")

# State count
#------------------------------------------------------
    if state == "MH":
        mh += 1

    elif state == "DL":
        dl += 1

    elif state == "KA":
        ka += 1

    elif state == "UP":
        up += 1

print("\nState Wise Report")
print("MH ->", mh, "Vehicles")
print("DL ->", dl, "Vehicles")
print("KA ->", ka, "Vehicles")
print("UP ->", up, "Vehicles")