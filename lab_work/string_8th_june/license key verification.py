"""
Program: Software License Key Validator

Tasks:
1. Verify there are exactly 4 groups.
2. Verify each group contains exactly 4 characters.
3. Count total letters.
4. Count vowels.
5. Remove hyphens and display merged key.
6. Create a list containing all groups.
7. Display whether the key format is valid.
"""

# Input license key
license_key = input("Enter License Key: ")

#------------------------------------------------------
# Split key into groups
groups = license_key.split("-")

#------------------------------------------------------
# Check number of groups
valid_groups = len(groups) == 4

#------------------------------------------------------
# Check each group contains exactly 4 characters
valid_length = True

for group in groups:
    if len(group) != 4:
        valid_length = False
        break

#------------------------------------------------------
# Determine overall validity
if valid_groups and valid_length:
    status = "Valid"
else:
    status = "Invalid"
    
#------------------------------------------------------
# Remove hyphens
merged_key = license_key.replace("-", "")

#------------------------------------------------------
# Count total letters
total_letters = 0

for ch in merged_key:
    if ch.isalpha():
        total_letters += 1

#------------------------------------------------------
# Count vowels
vowels = 0

for ch in merged_key.upper():
    if ch in "AEIOU":
        vowels += 1

#------------------------------------------------------
# Display results
print("\nLicense Key:", license_key)
print("Groups:", groups)
print("Number of Groups:", len(groups))
print("Total Letters:", total_letters)
print("Total Vowels:", vowels)
print("Merged Key:", merged_key)
print("License Key Status:", status)