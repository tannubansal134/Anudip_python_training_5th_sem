# to create a dictionary to store student's data
students = {'std101':"Akash",'std102':"Abhinav",'std103':"Anil",'std104':"rahul"}
# to display the data
print("student details:")
print(students)
print("------------------------------")
# to update record of student whose roll number is std103
students['std103'] = 'rohit'
# to update record of student whose roll number is std105
students['std105'] = 'rakesh'
print("students details :")
print(students)
print("-----------------------------------------------------------")
for x in students:
    print(x,'->', students[x])