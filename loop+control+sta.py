# while loop
''' a=1
while a<=10:
    print(a)
    a+=1
print("rest of the code")

a=int(input("ENTER A NUMBER LESS THEN 10: "))
while a<=100:
    print(a)
    a+=1
print("rest of the code")

# WHILE LOOP WITH ELSE

a=1
while a<=5:
    print(a)
    a+=1
else:
    print("this is while loop")

print("reset of the code")

# INFINITE WHILE LOOP

a=0
while True:
    a+=1
    print(a)
    if (a==3):
        break
print("rest of the code") '''

# NESTED WHILE LOOP

a=1
while a<=3:
    print("outer loop",a)
    a+=1

    j=1
    while j<=5:
        print(" inner loop",j)
        j+=1
        
print("rest of the code")
