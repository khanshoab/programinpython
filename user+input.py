

# getting user input by using for loop
'''
from array import*
stu_roll=array("i",[])
n=int(input("enter no of element:"))

for i in range(n):
    stu_roll.append(int(input("enter element:")))

for i in range(len(stu_roll)):
    print(stu_roll[i])

'''
# getting input from user using while

from array import*
stu_id=array("i",[])
a=int(input("enter no of element:"))

i=0
j=0
while (i<a):
    stu_id.append(int(input("enter element:")))
    i+=1

while (j<len(stu_id)):
    print(stu_id[j])
    j+=1    


