'''to ask the user the input number of rows and then display pattern
i.e , n=5
*
**
***
****
*****
--------------------------------------------------------------
'''
rows = int(input("enter the numner of rows:"))
if(rows<0):
    exit("number of rows are invalid")
# to display pattern
for i in range(1,rows+1):
    print("*" *i)