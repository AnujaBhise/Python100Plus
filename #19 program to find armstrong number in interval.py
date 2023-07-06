#19 program to find armstrong number in interval

lower =int(input("Enter lower limit"))
upper =int(input("Enter upper limit"))

for num in range(lower,upper+1):
# Convert the number to a string to count the digits
    order = len(str(num))
    temp=num
    sum =0

# Calculate the sum of digits raised to the power of the number of digits
    while temp >0:
        digit = temp%10
        cube = digit ** order
        sum = sum + cube
        temp = temp //10

# Check if the sum is equal to the original number
    if sum == num:
        print(num)
