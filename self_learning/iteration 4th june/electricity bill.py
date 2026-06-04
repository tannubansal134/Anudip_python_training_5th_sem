# Read the number of units consumed
units = int(input("Enter electricity units consumed: "))

# Calculate bill based on slab rates
if units <= 100:
    bill = units * 5

elif units <= 200:
    # First 100 units at ₹5/unit
    # Remaining units at ₹7/unit
    bill = (100 * 5) + ((units - 100) * 7)

else:
    # First 100 units at ₹5/unit
    # Next 100 units at ₹7/unit
    # Remaining units at ₹10/unit
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Add 10% surcharge if bill exceeds ₹5000
if bill > 5000:
    surcharge = bill * 0.10
    bill = bill + surcharge

# Display final payable amount
print("Final Payable Amount = ₹", bill)