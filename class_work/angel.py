angle1 = float(input("enter first angle:"))
# validate angle1
if(angle1 <=0):
    exit("angle must be positive")
#---------------------------------------
angle2 = float(input("enter second angle:"))
#validate angle2
if(angle2 <= 0):
    exit("angle must be positive")
#---------------------------------------
angle3 = float(input("enter the third angle"))
#validate angle3
if(angle3 <= 0):
    exit("angle must be positive")
#verifying triangle formation
if(angle1+angle2+angle3==180):
    print("above angles from a triangle")
else:
    print("above angles do not form a triangle")
