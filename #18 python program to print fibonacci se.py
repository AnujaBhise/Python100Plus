#18 python program to print fibonacci series

n1 =0 
n2 =1
nterm = int(input("Enter the number to obtain fibonacci seq"))
if nterm==1:
    print(n1,n2)
else:
    print(n1)
    print(n2)
    for i in range(2,nterm):
        fib = n1 +n2
        n1= n2
        n2 = fib
        print(fib)