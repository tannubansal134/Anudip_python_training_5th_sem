#program to converttime into corresponding hour , minutes, second
#input of time in seconds
second = int(input("enter time in second :"))
#check second is negative
if( second < 0):
    exit("time cannot be negative...... exited")
#-------------------------------------------------
print("----------------------------")
hour = 0
minute = 0
#converting number of second into hours
if(second >= 3600):
    hour = second // 3600
    second = second % 3600
#-------------------------------------------------
#converting into minute
if(second >= 60):
    minute = second // 60
    second = second % 60
#----------------------------------------------------
print("----------------------------------")
print("equivalent time : ",hour,"hour",minute,"minute",second,"second")