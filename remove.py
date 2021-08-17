

# This method is used to remove first occurence of given element from the exisisting array
from array import*
stu_roll=array("i",[18,28,292,277,282,18]) # first occurence element delet
n=len(stu_roll)

i=0
while(i<n):
    print(stu_roll[i])
    i+=1

print("array after remove")
stu_roll.remove(292)
n=len(stu_roll)

i=0
while(i<n):
    print(stu_roll[i])
    i+=1