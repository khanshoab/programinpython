

#This method is used to reverse the order of given array element .
from array import*
stu_roll=array('i',[23,29,28,27,47,17])
n=len(stu_roll)

i=0
while (i<n):
    print(stu_roll[i])
    i+=1

print("array after reverse")
stu_roll.reverse()
n=len(stu_roll)

i=0
while (i<n):
    print(stu_roll[i])
    i+=1