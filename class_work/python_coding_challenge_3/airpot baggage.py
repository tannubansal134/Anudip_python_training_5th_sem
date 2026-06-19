'''Passenger baggage weights (in kg) are stored as tuples: 
baggage = ( 
    ("P101", 18), 
    ("P102", 32), 
    ("P103", 24), 
    ("P104", 36), 
    ("P105", 28), 
    ("P106", 20), 
    ("P107", 41), 
    ("P108", 26), 
    ("P109", 19), 
    ("P110", 34) 
) 
Tasks 
1.	Display passengers carrying baggage above 30 kg.  
2.	Count passengers within and exceeding limits.  
3.	Calculate excess baggage charges (₹500 per kg above 30 kg).  
4.	Create a list of passengers requiring manual inspection.  
5.	Find the passenger carrying the heaviest baggage.  
'''
'''Airport Baggage Screening System
Problem Statement
Passenger baggage weights (in kg) are stored as tuples:

Tasks
1. Display passengers carrying baggage above 30 kg.
2. Count passengers within and exceeding limits.
3. Calculate excess baggage charges (₹500 per kg above 30 kg).
4. Create a list of passengers requiring manual inspection.
5. Find the passenger carrying the heaviest baggage.
Sample Output
Passengers Exceeding 30 kg Limit:
P102
P104
P107
P110
Passengers Within Limit: 6
Passengers Exceeding Limit: 4
Excess Baggage Charges:
P102 : ₹1000
P104 : ₹3000
P107 : ₹5500
P110 : ₹2000
Passenger with Heaviest Baggage:
P107 (41 kg)
Passengers Requiring Manual Inspection:
['P102', 'P104', 'P107', 'P110']'''

#---------------------------------------------------------------------------------
#creating a tuple 
baggage = (
 ("P101", 18),
 ("P102", 32),
 ("P103", 24),
 ("P104", 36),
 ("P105", 28),
 ("P106", 20),
 ("P107", 41),
 ("P108", 26),
 ("P109", 19),
 ("P110", 34)
)
# to display paseengers above 30 kg
print("passengers carrying baggage above 30 kg : ")
for passenger in baggage:
    if passenger[1]>30:
        print(passenger[0])
#---------------------------------------------------------------------------
# to count passengers within and exceeding limits
within_limits = 0
exceeding_limits = 0
for passengers in baggage:
    if passengers[1] <= 30:
        within_limits += 1
    else:
        exceeding_limits += 1
print("passengers within limit: ",within_limits)
print("passengers exceeding limit: ",exceeding_limits)
#-----------------------------------------------------------------------------
# to calculate excess baggage charges 
print("excess baggage charges: ")
for passenger in baggage:
    if passenger[1] > 30:
        excess_weight = passenger[1] - 30
        charges = excess_weight * 500
        print(passenger[0],": ₹",charges)
#-------------------------------------------------------------------------
# to create a list of passengers  
list_inspection = []
for passenger in baggage:
    if passenger[1] > 30:
        list_inspection.append(passenger[0])
print("passengers requiring manual inspection: ")
print(list_inspection)
#----------------------------------------------------------------------
# to find the passenger carrying the heaviest load
heaviest_passenger = baggage[0][0]
heaviest_weight = baggage[0][1]
for passenger in baggage:
    if passenger[1] > heaviest_weight:
        heaviest_passenger = passenger[0]
        heaviest_weight = passenger[1]
print("the heaviest loader : " , heaviest_passenger )
print("the heaviest weight : " , heaviest_weight )
