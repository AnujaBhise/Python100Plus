#20 program to find sum of natural numbers (1,2,3,4......)

#take userinput
num = int(input("Enter a number here"))

if num < 0:
    print("Enter positive number")
    num = int(input("Enter a number here"))
#check if number is always positive
if num > 0:
    sum =0
#calculate sum of nautral numbers
    for i  in range(1,num+1):
        sum = sum+i #add each number to sum

print("Sum of ",num,"natural numbers is ",sum)