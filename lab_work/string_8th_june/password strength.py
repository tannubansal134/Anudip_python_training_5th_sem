"""
Program: Password Strength Checker
Rules:
• Minimum length 8
• Contains at least:
       o 1 uppercase letter
       o 1 lowercase letter
       o 1 digit
       o 1 special character

This program performs the following tasks:
1. Counts uppercase letters
2. Counts lowercase letters
3. Counts digits
4. Counts special characters
5. Displays all digits separately
6. Displays all special characters separately
7. Determines whether the password is Strong, Medium, or Weak
"""

# Input password from user
password = input("Enter Password: ")

#--------------------------------------------
# Initialize counters and lists
# for storing different types
# of characters.

upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

digit_list = []
special_list = []

#--------------------------------------------
# Traverse each character of the password and classify it.

for ch in password:

    if ch.isupper():
        upper_count += 1

    elif ch.islower():
        lower_count += 1

    elif ch.isdigit():
        digit_count += 1
        digit_list.append(ch)

    else:
        special_count += 1
        special_list.append(ch)

#--------------------------------------------
# Check password strength.

# Strong:
# Length >= 8 and contains uppercase, lowercase, digit and special character.

# Medium:
# Length >= 8 and contains any three conditions.

# Weak:
# Otherwise.

strength = "Weak"

conditions = 0

if upper_count >= 1:
    conditions += 1

if lower_count >= 1:
    conditions += 1

if digit_count >= 1:
    conditions += 1

if special_count >= 1:
    conditions += 1

if len(password) >= 8 and conditions == 4:
    strength = "Strong"

elif len(password) >= 8 and conditions >= 3:
    strength = "Medium"

else:
    strength = "Weak"

#--------------------------------------------
# Display results

print("\nPassword:", password)
print("Uppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)
print("Digits Found:", digit_list)
print("Special Characters Found:", special_list)
print("Password Strength:", strength)