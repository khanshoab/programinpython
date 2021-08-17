

# this is method is used to insert an element in a particular position of the existing array.

#insert
from array import*
stu_roll=array("i",[17,93,29,28,73])
n=len(stu_roll)

i=0
while (i<n):
    print(stu_roll[i])
    i+=1

print("array after insert")
stu_roll.insert(1,103)
stu_roll.insert (3,882)
n=len(stu_roll)

i=0
while (i<n):
    print(stu_roll[i])
    i+=1


