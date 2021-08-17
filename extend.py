

# This method is used to append another array on itereable object at end of the array
from array import* 
stu_roll=array("i",[27,29,47])  # two array merge 
arr=array("i",[373,498,293])
n=len(stu_roll)

i=0
while (i<n):
    print(stu_roll[i])
    i+=1

print("after apend element:")
stu_roll.extend(arr)
n=len(stu_roll)

i=0
while (i<n):
    print(stu_roll[i])
    i+=1