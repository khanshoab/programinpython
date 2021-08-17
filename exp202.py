''' implementing of function in python '''

def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

def fibo(num):
    a=0
    b=1
    c=a+b
    print('fabinacci series upto ',num,'is',a,'\t',end='')
    res=[0,1]
   while c<=num:  
       print(c,'\t',end='')
       a=b
       b=c
       c=a+b
       print()

def fibo1( num):
    a=0
    b=1
    c=a+b
    res=[0,1]
    while c<=num:
        res.append(c)
        a=b
        b=c
        c=a+b
    return res


def main():
    while(True):
        n=int(input('enter any number:'))
        print('factorial number of ',n,'is',fact(n))
        ch=input('\tDo u want to continue (Y\N)?')
        if (ch=='N', or ch=='n'):
            break
''''
if__name__=='__main__':
    main()
    '''