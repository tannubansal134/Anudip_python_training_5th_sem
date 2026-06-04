 Program to check whether three sides can form a triangle or not

a = float(input("Enter first side: "))
if(a<=0):
    exit("side greater than zero")

#______________

b = float(input("Enter second side: "))
if(b<=0):
    exit("side greater than zero")

#________________

c = float(input("Enter third side: "))
if(c<=0):
    exit("side greater than zero")

#_______________


# Triangle condition
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle can be formed")
    if (a == b == c):
        print("It is an Equilateral Triangle")

    elif( a == b or b == c or a == c):
        print("It is an Isosceles Triangle")

    else:
        print("It is a Scalene Triangle")
else:
    print("Triangle cannot be formed")