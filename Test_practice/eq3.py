#the number is prime or not;
#logic; diivisible by given number or 1;
num = int(input("Enter a number: "))
if (num>1):
    for i in range(2,num):
        if(num%i==0):
            print("Its not a prime number.")
            break
    else:
        print("Its a prime number.")
else:
    print(num,"Its not a prime number.")