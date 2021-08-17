


# this method is used to remove last element in the exsisting array

'''from array import*
stu_roll=array("i",[17,93,29,28,73])
n=len(stu_roll)

i=0
while (i<n):
    print(stu_roll[i])
    i+=1

print("array after pop")
stu_roll.pop()
n=len(stu_roll)

i=0
while (i<n):
    print(stu_roll[i])
    i+=1 '''

# Other type pop(n)
# this method is used remove an element specified by position number from the exsisting array and it is return remove
 # element pop(position_number)

from array import*
stu_roll=array("i",[17,93,29,28,73])
n=len(stu_roll)

i=0
while (i<n):
    print(stu_roll[i])
    i+=1

print("array after pop")
s=stu_roll.pop(3)
n=len(stu_roll)

i=0
while (i<n):
    print(stu_roll[i])
    i+=1
print("removed element:",s)