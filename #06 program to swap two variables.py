#6 program to swap two variables
#solution 1 : using 3rd varible

x = 10
y =20
print("THe initial value of  x is",x)
print("THe initial value of  y is",y)
temp =x
print("THe value of  temporary variable is ",temp)
x=y
print("THe value of  x is",x)
y=temp
print("THe value of  y is",y)

#solution 2 : using without 3rd varible 
x =23
y =12

print("THe initial value of  x is",x)
print("THe initial value of  y is",y)

x,y =y,x
print("THe swapped value of  x is",x)
print("THe swapped value of  y is",y)