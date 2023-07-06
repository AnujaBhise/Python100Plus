#5 program to solve quadratic equations

#quadratic equation ax**2  + bx + c = 0 
#condition1 : a,b,c are real numbers
#condition2 : a! = 0

#cmath module :complex math module
#used for solving complex maths operations

import cmath 
a = int(input("Enter number(a!=0) :" ))
b = int(input("Enter number b:" ))
c = int(input("Enter number c:" ))

#formula for discriminant
d = ( b**2) - (4*a*c)

root1 = (-b - cmath.sqrt(d)) / (2*a)
root2 = (-b + cmath.sqrt(d)) / (2*a)

print("THe Roots are ",root1,root2)
