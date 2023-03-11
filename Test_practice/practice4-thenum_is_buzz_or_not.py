#Practice4;
#buzz: Its divisible by 7 or its end with 7 ;
a = int(input("Enter a number: "))
if (a%7==0):
    print(a,"This is a buzz number.")
elif (a%10==7):
    print(a,"this is a buzz number.")
else:
    print("This is not a buzz number.")