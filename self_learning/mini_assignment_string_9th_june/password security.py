'''Problem Statement
A cybersecurity company wants to analyze user passwords before allowing account creation.
The system should accept at least 15 passwords and generate a security report.
Requirements
For each password:
1.Count uppercase letters.
2.Count lowercase letters.
3.Count digits.
4.Count special characters.
5.Check minimum length (8 characters).
6.Check if spaces exist.
7.Determine password strength:
oStrong
oMedium
oWeak
8.Display repeated characters.
9.Count vowels and consonants.
10.Identify the most frequently occurring character
'''

# Password Security Analyzer
#-----------------------------------------------------

total_passwords = 15
strong_count = 0
medium_count = 0
weak_count = 0

for i in range(total_passwords):
    print("\nPassword", i + 1)
    password = input("Enter Password: ")

    upper = 0
    lower = 0
    digits = 0
    special = 0
    vowels = 0
    consonants = 0

    freq = {}

    for ch in password:
 # Frequency Count
 #-----------------------------------------------------

        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

 # Uppercase
 #----------------------------------------------------
        if ch.isupper():
            upper += 1

# Lowercase
#-----------------------------------------------------
        elif ch.islower():
            lower += 1

 # Digit
 #-----------------------------------------------------
        elif ch.isdigit():
            digits += 1

# Special Character
#---------------------------------------------------------
        else:
            special += 1

 # Vowels and Consonants
 #---------------------------------------------------------
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
 # Length Check
 #----------------------------------------------------
    if len(password) >= 8:
        length_check = "Yes"
    else:
        length_check = "No"

# Space Check
#-----------------------------------------------------
    if " " in password:
        space_check = "Yes"
    else:
        space_check = "No"
# Password Strength
#------------------------------------------------------
    if len(password) >= 8 and upper > 0 and lower > 0 and digits > 0 and special > 0 and space_check == "No":
        strength = "Strong"
        strong_count += 1
    elif len(password) >= 8 and ((upper > 0 and lower > 0) or digits > 0):
        strength = "Medium"
        medium_count += 1
    else:
        strength = "Weak"
        weak_count += 1

# Repeated Characters
#------------------------------------------------------
    repeated = ""
    for key in freq:
        if freq[key] > 1:
            repeated += key + " "

    if repeated == "":
        repeated = "None"

 # Most Frequent Character
 #--------------------------------------------------------
    max_char = ""
    max_count = 0

    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            max_char = key

 # Report for Current Password
 #------------------------------------------------------
    print("\n----- Password Report -----")
    print("Password:", password)
    print("Uppercase Letters :", upper)
    print("Lowercase Letters :", lower)
    print("Digits            :", digits)
    print("Special Characters:", special)
    print("Minimum Length 8? :", length_check)
    print("Contains Spaces?  :", space_check)
    print("Strength          :", strength)
    print("Repeated Chars    :", repeated)
    print("Vowels            :", vowels)
    print("Consonants        :", consonants)
    print("Most Frequent Char:", max_char, "(", max_count, "times )")

# Final Summary Report
#------------------------------------------------------
print("\n========== SECURITY REPORT ==========")
print("Total Passwords Analyzed :", total_passwords)
print("Strong Passwords         :", strong_count)
print("Medium Passwords         :", medium_count)
print("Weak Passwords           :", weak_count)