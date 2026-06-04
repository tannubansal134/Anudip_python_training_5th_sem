# Simple Interest using in condition

p = int(input("Enter Principal Amount: "))
r = int(input("Enter Rate of Interest: "))
t = int(input("Enter Time (in years): "))
if p > 0 and r > 0 and t > 0:
    simple_interest = (p*r*t) / 100
    print("Simple Interest =", simple_interest)
else:
    print("Please enter valid positive values.")