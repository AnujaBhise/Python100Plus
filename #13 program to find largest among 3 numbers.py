#13 program to find largest among 3 numbers
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 > num2 and num1>num3:
    print(num1,"is largest number ")
elif num2 > num1 and num2 > num3:
    print(num2,"is largest number ")
else: 
    print(num3,"is largest number ")
