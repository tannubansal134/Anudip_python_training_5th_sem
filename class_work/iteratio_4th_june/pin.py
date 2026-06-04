# progrm to displaying the pin
pin = ""
while pin != "1234":
    pin = input("Enter PIN: ")

    if pin != "1234":
        print("Incorrect PIN. Try Again.")
#--------------------------------------------------

print("Access Granted.")