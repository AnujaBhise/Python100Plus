#3 program to find Square Root
#Solution 1:Using Exponentiation

num = 64
num1 = int(input("Enter the number"))
sr = num**(1/2) #Reduce the power to Half 
sr = num1**(1/2)
print("The squareRoot of given number is : ",sr)

#Solution 2: USing MATH  module

import math
num = int(input("Enter the number : "))
sr = math.sqrt(num)
print("The SquareRoot of given number is ",sr)