'''The prices of products added to a shopping cart are stored below. Sample Data 
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 
1.	Calculate the total cart value.  
2.	Find the most expensive and cheapest products.  
3.	Count products eligible for premium shipping (price > ₹1000).  
4.	Generate a discount list (products above ₹1500).  
5.	Calculate the average product price.  
'''
# Smart Shopping Cart Analyzer

cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

# ------------------------------------
# Total Cart Value
# ------------------------------------

total = sum(cart)

print("Total Cart Value: ₹", total)

# ------------------------------------
# Most Expensive Product
# ------------------------------------

most_expensive = max(cart)

print("\nMost Expensive Product: ₹", most_expensive)

# ------------------------------------
# Cheapest Product
# ------------------------------------

cheapest = min(cart)

print("\nCheapest Product: ₹", cheapest)

# ------------------------------------
# Premium Shipping Products
# ------------------------------------

premium_count = 0

for price in cart:

    if price > 1000:
        premium_count += 1

print("\nPremium Shipping Eligible Products:", premium_count)

# ------------------------------------
# Discount Eligible Products
# ------------------------------------

discount_products = []

for price in cart:

    if price > 1500:
        discount_products.append(price)

print("\nDiscount Eligible Products:")
print(discount_products)

# ------------------------------------
# Average Product Price
# ------------------------------------

average = total / len(cart)

print("\nAverage Product Price: ₹", average)
 
'''Sample Output 
Total Cart Value: ₹11,097 
 
Most Expensive Product: ₹2,500 
 
Cheapest Product: ₹300 
 
Premium Shipping Eligible Products: 4 
 
Discount Eligible Products: 
[2500, 1800] 
 
Average Product Price: ₹1,109.7 
'''