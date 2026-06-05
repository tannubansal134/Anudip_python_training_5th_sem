#given a list of inventory stock and display the following 
stock=[25, 5, 0, 12, 3, 18, 0, 30]

#Display products that are out of stock
for s in stock:
    if s==0:
        print("The item is out of stock",s)

#Display products that need restocking(quantity less than 10)
for s in stock:
    if s<10:
        print("the product needs restocking",s)

#Count available products
available_count=0
for s in stock:
    if s>0:
        available_count+=1

print("The available count is",available_count)

#Creating new list containing stock greater than 15
healthy_stock=[]

for quantity in stock:
    if quantity >= 15:
        healthy_stock.append(quantity)

print("Products with stock >= 15:", healthy_stock)
  