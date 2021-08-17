''' write python program to implement list,tuple ,dictionry and arry
theory 
@auther :khan shoab akhtar vakil ahmad khan (19co33)
'''
# List Theory
l=[46,84,63,96,63,74,'khan',64,'shoab',5.7]
print("printing orginal list",l) #printing the list
print("printing the last element of list",l[-1])
print("printing the first three element of the list",l[1:3])
print("printing the first three element of the list",l[1:3]*3)
print("---------------list function----------------")
l1=list(range(1,8)) # creating list range 
print("list of range 1 to 7",l1)
l1.append(9) #append 9
print("append 9: ",l1)
l1.sort(reverse=True)
print("ascending sort:",l1)
l1.sort()
l1.reverse
print("reverse:",l1)
print("remove 9:")

#Tuple
''' Tuple theory'''
tpl=(-5,834,83,73,92,'khan','shoab',82,83,83,36) # creating tuple
print("created tuple is",tpl)
print("tuple element 0 to 2 is",tpl[0:2])

''''Tuple Function '''
print("-----------TUPLE FUNCTION--------")
tpl2=(10,754,73,985,93,90)
print("created tpl2 is ",tpl2 )
print("length:",len(tpl2))
print("min:",min(tpl2))
print("max,",max(tpl2))
print("count no of 83's:",tpl2.count(83))
print("reverse sort :",sorted(tpl2,reverse=True))
print("")

# SET
''' SET THEORY '''
print("---------SET theory------------")
s1={29,36,84,93,73,85,934,63}
s2=set()
s3={83,93,62,83,'khan',834}
print(s1,s2,s3)
s1.add(90)
print(s1,s2.issuperset(s2))
print(s1.union(s3))

# DICTIONARY
'''dictionry theory'''
d1={'khan':"shoab",'gsh':74,'asas':90,'bhai':65} # creating a dictionary 
print("print dictionary:",d1)
print()
print("-->keys:",d1.keys())
print("-->values:",d1.values())
print("-->keys and values:",d1.items())
d1.update({'khan':"khana shahab"})
print("-->print update dictionary:",d1)

#Array
''' array theory'''
print("-----print array----")
print()
arr=array('i',[10,47,83,832,762,82]) # creating array with integer values
print("the array element are")
for i in arr: # i is element and arr in array name
    print(i) # requries indentation
print("length of array is ",len(arr))
arr1=array('u',['hs','jdhj','ks','ksj']) # creating array with character values 
print("the character array element are ")
for i in arr1: #i is element and arr in array name 
    print(i)# requires indentation 
