#17 program to display multiplication for a table
#solution 1: Using for loop
num = int(input("Enter a number to dsiplay its table"))
for  i in range(1,11):
    print(num,"x",i,"=",num*i)

#solution 2: Using while loop
i=1
print("Using while loop")
while(i<= 10):
    print(num,"x",i,"=",num*i)
    i+=1