marks=[78,45,92,35,88,40,99,56]
#Display passed students
print("Passed Students")
for mark in marks:
    if mark>=40:
        print(mark)

#Count failed students
fail_count = 0
for mark in marks:
    if mark < 40:
        fail_count += 1

#Find highest and Lowest marks
highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

print("Highest marks:", highest)
print("Lowest marks:", lowest)

#List containing marks above 75
above_75=[]
for mark in marks:
    if mark > 75:
        above_75.append(mark)
print("Marks above 75:", above_75)
        
