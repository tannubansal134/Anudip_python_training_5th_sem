'''Problem Statement
The prices of products purchased by a customer are stored in a tuple.
Sample Data
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200)
Tasks
1.Calculate the total bill amount.
2.Find the most expensive product.
3.Find the least expensive product.
4.Count products costing more than ₹1,000.
5.Create a list of products eligible for discount (price > ₹800).
'''

# Tuple of product prices
#---------------------------------------------------------
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200)

# 1. Calculate total bill amount
#----------------------------------------------------------
total_bill = sum(prices)

# 2. Find the most expensive product
#--------------------------------------------------------
most_expensive = max(prices)

# 3. Find the least expensive product
#--------------------------------------------------------
least_expensive = min(prices)

# 4. Count products costing more than ₹1000
#-----------------------------------------------------------
count_above_1000 = 0
for price in prices:
    if price > 1000:
        count_above_1000 += 1

# 5. Create a list of products eligible for discount (price > ₹800)
#-----------------------------------------------------------
discount_products = []
for price in prices:
    if price > 800:
        discount_products.append(price)

# Display results
#-----------------------------------------------------------
print("Total Bill Amount: ₹", total_bill)
print("Most Expensive Product: ₹", most_expensive)
print("Least Expensive Product: ₹", least_expensive)
print("Products Costing More Than ₹1000:", count_above_1000)
print("Discount Eligible Products:", discount_products)