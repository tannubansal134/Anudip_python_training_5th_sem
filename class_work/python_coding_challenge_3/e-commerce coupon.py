'''Problem Statement
A file named coupons.txt contains coupon usage records.
SAVE50 
WELCOME20 
SAVE50 
WELCOME20 
FESTIVE10 
SAVE50 
WELCOME20 
NEWUSER 
FESTIVE10 
SAVE50 
NEWUSER
Tasks
1.Count the usage frequency of each coupon.
2.Identify coupons used more than 3 times.
3.Create a set of unique coupons.
4.Display the most frequently used coupon.
5.Save suspicious coupon records into fraud_report.txt.
'''

# Create coupons.txt file
#-------------------------------------------------
file = open("coupons.txt", "w")
file.write("SAVE50 WELCOME20 SAVE50 FESTIVE10 SAVE50 WELCOME20 NEWUSER FESTIVE10 SAVE50 NEWUSER")
file.close()

# Read data from file
#-------------------------------------------------------
file = open("coupons.txt", "r")
data = file.read()
file.close()

# Convert data into list of coupons
#-------------------------------------------------------
coupons = data.split()

# Count frequency of each coupon
#-------------------------------------------------------
frequency = {}

for coupon in coupons:
    if coupon in frequency:
        frequency[coupon] += 1
    else:
        frequency[coupon] = 1

print("Coupon Usage Frequency:")
for coupon, count in frequency.items():
    print(coupon, ":", count)

# Find suspicious coupons (used more than 3 times)
#-------------------------------------------------------
suspicious = []

for coupon, count in frequency.items():
    if count > 3:
        suspicious.append(coupon)

print("\nSuspicious Coupons:")
for coupon in suspicious:
    print(coupon)

# Create set of unique coupons
#-------------------------------------------------------

unique_coupons = set(coupons)

print("\nUnique Coupons:")
print(unique_coupons)

# Find most frequently used coupon
#-------------------------------------------------------
max_coupon = ""
max_count = 0

for coupon, count in frequency.items():
    if count > max_count:
        max_count = count
        max_coupon = coupon

print("\nMost Frequently Used Coupon:", max_coupon)

# Save suspicious coupons to fraud_report.txt
#-------------------------------------------------------
file = open("fraud_report.txt", "w")

for coupon in suspicious:
    file.write(coupon + "\n")

file.close()

print("\nFraud Report Generated Successfully.")