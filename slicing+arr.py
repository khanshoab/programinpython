

# Slicing on array can be used to retrieve a piece  of the array that contains a group of element .
# Slicing is useful to retrieve a range of element.
#new_array_name  = array_name[start:stop:stepsize]

''' from array import*
stu_roll = array("i",[101,102,103,104,105,106,107])
print("original array")
n = len(stu_roll)

for i in range(n):
    print(i,"=",stu_roll[i])

print("*************")
a = stu_roll[1:5]
a = stu_roll[0:]
a = stu_roll[-4:]
a = stu_roll[-5:-3]  # =-5-(-3)=-2=2=103,104
a = stu_roll[0:7:3]
for i in a:
    print(i)     '''

from array import*
stu_roll = array("i",[101,102,103,104,105])  # It is another way to used slicing
for i in stu_roll[1:5]:
    print(i)