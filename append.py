

#   appen()  this method is used to add an element at the end of the existing of the  array

from array import*
cus_id=array("i",[872,2098,2087,826,38756,8786,2938])
n=len(cus_id)
i=0
while (i<n):
    print(cus_id[i])
    i+=1

print("array after append")
cus_id.append(1077)
n=len(cus_id)
i=0
while (i<n):
    print(cus_id[i])
    i+=1
