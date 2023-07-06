#18 program to check armstrong number
# Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits
#eg 153 = (1+125+27) = 153,407,1634

#take user input
num =int(input("Enter the number"))
sum =0 
order=len(str(num)) #calculate length of number
temp = num
while temp > 0: 
    digit = temp % 10 #for ontain last digit :153
    cube= digit**order
    sum =sum +cube
    temp =temp //10 #for removing last digit from temp now  :15

if sum == num:
    print("It is an Armstrong number")
else:
    print("It is not Armstrong number")
