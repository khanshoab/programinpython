no_rows = int(input("enter the number of row :"))

for row in range (1,no_rows+1):
    for column in range(1,row+1):
        print("*",end="")
    print()