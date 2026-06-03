# program to calculate area and perimeter of triangle
# input of three sides
side1 = int(input("enter first side(in cm):"))
side2 = int(input("enter second side(in cm):"))
side3 = int(input("enter third side(in cm):"))
print("---------------------------------------")
print("first side:",side,"cm")
print("second side:",side,"cm")
print("third  side:",side,"cm")
# to calculate perimeter
perimeter = side1+side2+side3
#-------------------------------
s = perimeter/2
# displaying area
print("Area:",(s*(s-side1)*(s-side2)*(s-side3))**0.5,"sq.cm")
# displaying perimeter
print("perimeter:",perimeter,"cm")
      
      