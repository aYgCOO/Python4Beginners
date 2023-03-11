year = int(input("Enter a year: "))
if (year%400==0) and (year%100==0):
    print(year,"the year is a leap year.")
elif (year%4==0) and (year%100!=0):
    print(year,"the year is a leap year.")
else:
    print(year,"the year is not a leap year.")
    