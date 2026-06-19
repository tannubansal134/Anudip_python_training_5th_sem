'''Problem 4: Disaster Relief Resource Allocation
Problem Statement
Relief materials available at different warehouses are stored as dictionaries.
resources = { 
"Warehouse1": ["Food", "Medicine", "Blankets"],
"Warehouse2": ["Water", "Food", "Tents"], 
"Warehouse3": ["Medicine", "Tents", "Clothes"], 
"Warehouse4": ["Food", "Water", "Medicine"] 
}
Tasks
1.Display all unique relief items.
2.Find warehouses containing medicines.
3.Count how many warehouses stock each resource.
4.Identify the most widely available resource.
5.Display resources available in all warehouses.
'''

# Dictionary containing warehouse resources
#-------------------------------------------------------
resources = {
    "Warehouse1": ["Food", "Medicine", "Blankets"],
    "Warehouse2": ["Water", "Food", "Tents"],
    "Warehouse3": ["Medicine", "Tents", "Clothes"],
    "Warehouse4": ["Food", "Water", "Medicine"]
}

# 1. Display all unique relief items
#-------------------------------------------------------
unique_resources = set()

for items in resources.values():
    unique_resources.update(items)

print("Unique Resources:", unique_resources)

# 2. Find warehouses containing medicines
#-------------------------------------------------------
print("\nWarehouses with Medicines:")

for warehouse, items in resources.items():
    if "Medicine" in items:
        print(warehouse)

# 3. Count how many warehouses stock each resource
#-------------------------------------------------------
resource_count = {}

for items in resources.values():
    for item in items:
        if item in resource_count:
            resource_count[item] += 1
        else:
            resource_count[item] = 1

print("\nResource Availability:")

for item, count in resource_count.items():
    print(item, ":", count)

# 4. Identify the most widely available resource(s)
#-------------------------------------------------------
max_count = max(resource_count.values())

print("\nMost Widely Available Resources:")

for item, count in resource_count.items():
    if count == max_count:
        print(item)

# 5. Display resources available in all warehouses
#-------------------------------------------------------
common_resources = set(resources["Warehouse1"])

for items in resources.values():
    common_resources = common_resources.intersection(set(items))

print("\nResources Available in All Warehouses:")

if len(common_resources) > 0:
    print(common_resources)
else:
    print("None")