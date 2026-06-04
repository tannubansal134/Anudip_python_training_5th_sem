# Program to calculate electricity bill based on slab rates

# input units consumed
units = int(input("Enter Units Consumed: "))

bill = 0  
# calculate bill based on slab rates
if units <= 100:
    bill = units * 5
    category = "Low Consumption"

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    category = "Medium Consumption"

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    category = "High Consumption"

# display results
print("Units Consumed:", units)
print("Total Bill: ₹", bill)
print("Category:", category)