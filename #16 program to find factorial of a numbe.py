#16 program to find factorial of a number
#5!= 5*4*3*2*1
#solution 1 : Using for loop
num = int(input("Enter a number :"))
fact=1
if num < 0:
    print("factorial of number does not exist")
if num == 0:
    print("factorial of 0 does not exist")
if num > 0:
    for i in range(1,num+1):
        fact = fact * i
    print("factorial of a ",num," is: ",fact)
#solution 2 : Using Recursion
def fact(num):
    if num == 0:
        return 1
    else:
        return (num * fact(num-1))
result = fact(num)
print("Factorial by Recursion : ",result)