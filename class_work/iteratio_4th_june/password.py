# program to displaying the password
password = ""
while password != "admin123":
    password = input("Enter Password: ")

    if password != "admin123":
        print("Invalid Password.")
#---------------------------------------------

print("Login Successful.")