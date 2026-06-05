# program to remove duplicate enteries of given number
# creating blank list to store numbers
numbers = []
print("enter any 20 numbers:")
for x in range(20):
    num = int(input("Enter a number: "))
    # append into list
    numbers.append(num)
print("-----------------------------------------")
elemet = int(input("enter any number to remove its duplicate: "))
#--------------------------------------------------------------
# finding the frequency of given number
frequency = numbers.count(element)
if frequency == 0:
    print("element not found")
elif frequency == 1:
    print("no duplicate found")
else:                        
     # reversing the list
     numbers.reverse()
     for i in range (1,frequency):
         # removing element
        numbers.remove(element)
    # reversing the list again
     numbers.reverse()
     print("after removing duplicates")
     print(numbers)

         
