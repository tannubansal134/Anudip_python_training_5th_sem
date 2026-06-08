"""
Program: Email Analyzer System

Tasks:
1. Extract Username
2. Extract Domain Name
3. Extract Extension
4. Count Digits present in Username
5. Count Special Characters
6. check whether:
        o Exactly one '@' exists.
        o At least one '.' exists after '@'.
7. Display valid Email or invalid email
"""

# Input Email
email = input("Enter Email Address: ")

#---------------------------------------
# Extract Username
username = email.split("@")[0]

#---------------------------------------
# Extract Domain and Extension
domain_part = email.split("@")[1]

domain = domain_part.split(".")[0]
extension = domain_part.split(".")[-1]

#---------------------------------------
# Count Digits in Username
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

#---------------------------------------
# Count Special Characters in Email
special_count = 0

for ch in email:
    if not ch.isalnum():
        special_count += 1

#---------------------------------------
# Email Validation
valid = True

#---------------------------------------
# Exactly one @
if email.count("@") != 1:
    valid = False

#---------------------------------------
# At least one . after @
at_pos = email.find("@")

if "." not in email[at_pos:]:
    valid = False
    
#---------------------------------------
# Display Result
print("\nEmail:", email)
print("Username:", username)
print("Domain:", domain)
print("Extension:", extension)
print("Digits Found:", digit_count)
print("Special Characters Found:", special_count)

if valid:
    print("Email Status: Valid")
else:
    print("Email Status: Invalid")