

# implicit type of conversion ( it convert automatically)
a = 2
b = 5
valu = a/b
print(valu)
print(type(valu))

j = 'how are you  '
k = 'my friend'
p = j+k
print(p)
print(type(p))

'''r = 18
p = '78'
g = r+p
print(g)               it gives error

m=20
n='how are you'
l=m+n
print(l)       unsupported oprend type  '''

#  EXPLICIT TYPE CONVERSION     .programmer can convert one data type into another data type.

a=5
b=2
valu=a/b          # here is data loss 0.5
print(type(valu))
int_value=int(valu)
print(int_value)
print(type(int_value))



q=20
u='40'
print(type(u))
r=q+ int (u)
print(r)


'''w=20
u='hello my friend'    
print(type(u))
z=w+ int (u)
print(z) '''



# float to integer
n=100.739
va=int (n)
print(va)
print(type(n))

# integer to float
b=75
bs=float (b)
print(bs)
print(type(bs))

# integer to copmlex
g=73
bd = complex (g)
print(bd)

# integer to string
gj=794
hg= str (gj)
print(hg)

# string to tuple
n="khan shoab"
nn= tuple (n)
print(nn)
print(type(nn))

# string to list
n="khan shoab"
nn= list (n)
print(nn)
print(type(nn))

# tuple to list
s = ('khan','bhai','ahmad','nasim','book')
ss=list (s)
print(ss)

#  list to tuple
s = ['khan','bhai','ahmad','nasim','book']
ss=tuple (s)
print(ss)

#decimal to binary
s=10
ss= bin (s)
print(ss)

# shortcut
s=76
print(bin(s))