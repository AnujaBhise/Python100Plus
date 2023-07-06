#14 program to check prime number

num =int(input("Enter a number : "))
if num==1:
    print("The number is neither prime nor composite")
if num>1:
    for  i in range(2,num):
        if num % i == 0:
            print("The number is not prime ")
            break
    else:
        print("The number is a prime")