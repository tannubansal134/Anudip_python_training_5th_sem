'''Problem Statement
An organization has collected 20 email addresses from users.
Create a program to analyze these email addresses.
Requirements
For each email:
1.Extract username.
2.Extract domain.
3.Extract extension.
4.Count digits in username.
5.Count special characters.
6.Check if email is valid:
o Exactly one '@'
o Contains '.'
o No spaces
7.Display invalid emails.
8.Count emails belonging to each domain.
Sample Input
rahul123@gmail.com 
priya@outlook.com 
anuj@company.in
Challenge
Generate a domain report:
gmail.com -> 8 users 
outlook.com -> 5 users 
yahoo.com -> 3 users 
company.in -> 4 users
'''
# Email Validation & Domain Analytics System
#-------------------------------------------------
emails = ""

# Input 20 emails
#-----------------------------------------------------
for i in range(20):
    email = input("Enter Email : ")
    emails = emails + email + ","

print("\nEMAIL ANALYSIS REPORT")

temp = ""
for ch in emails:

    if ch != ",":
        temp = temp + ch

    else:
        email = temp
        temp = ""

        print("\nEmail :", email)

# Validate email
#--------------------------------------------------------------------
        if email.count("@") == 1 and "." in email and " " not in email:

            at = email.find("@")

 # Extract username
 #--------------------------------------------------------------------
            username = email[:at]

 # Extract domain
 #--------------------------------------------------------------------
            domain = email[at+1:]

 # Extract extension
 #-------------------------------------------------------------------
            dot = domain.rfind(".")
            extension = domain[dot+1:]

            digits = 0
            special = 0

 # Count digits and special characters
 #-------------------------------------------------------------------
            for c in username:

                if c.isdigit():
                    digits += 1

                elif not c.isalpha():
                    special += 1

            print("Username :", username)
            print("Domain :", domain)
            print("Extension :", extension)
            print("Digits :", digits)
            print("Special Characters :", special)

        else:
            print("Invalid Email")

print("\nDOMAIN REPORT")

checked = ""
temp = ""

for ch in emails:

    if ch != ",":
        temp = temp + ch

    else:
        email = temp
        temp = ""

        if email.count("@") == 1 and "." in email and " " not in email:

            domain = email[email.find("@")+1:]

            if domain not in checked:

                count = 0
                temp2 = ""

                for x in emails:

                    if x != ",":
                        temp2 = temp2 + x

                    else:
                        e = temp2
                        temp2 = ""

                        if e.count("@") == 1 and "." in e and " " not in e:

                            d = e[e.find("@")+1:]

                            if d == domain:
                                count += 1

                print(domain, "->", count, "users")
                checked = checked + domain + " "

print("\nINVALID EMAILS")

temp = ""

for ch in emails:

    if ch != ",":
        temp = temp + ch

    else:
        email = temp
        temp = ""

        if not (email.count("@") == 1 and "." in email and " " not in email):
            print(email)