#12 program to check leap year 
#year =365 days
#leap year =366 days : once in 4 yrs
#condtion 1 :year %400 == 0 And year %100 ==0  eg.2000
#condition2 : year %4 == 0 ANd year %100 != 0 eg. 1996 ,2008 
#and :use logical operators

year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(year,"is a leap year")

elif (year % 4 ==0 )and (year % 100 != 0):
    print(year,"is a leap year")

else:
    print(year,"is not a leap year")

