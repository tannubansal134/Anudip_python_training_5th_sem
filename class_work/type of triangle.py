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
#--------------------------------------------
#verifying triangle formation
if(angle1+angle2+angle3 ==180):
   # triangle is formed
   # actue angled triangle
   if(angle1 < 90 and angle2 < 90 and angle3 < 90):
      print("above angles form actue angled triangle")
   elif(angle1 == 90 or angle2 == 90 or angle3 == 90):
      print("above angles from right angled triangle")
   else:
      print("above angles form obtuse angled triangle ")
else:
   print("above angles do not form any triangle")
      
      