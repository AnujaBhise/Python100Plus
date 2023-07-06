#15 program to print all prime numbers in interval

lower = int(input("Enter range of numbers\nEnter lower range : "))
upper = int(input("\nEnter upper range:  "))

for num in range(lower,upper +1):
    if num>1:
        for i in range(2,num):
            if num %i ==0:
                break
        else:
            print(num) 
                