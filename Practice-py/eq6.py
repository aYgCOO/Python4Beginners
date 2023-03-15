#Write a python programm to check the given number is divisible by 3 or 5;
num = int(input("Enter a number: "))
while(num>0):
    if (num%3==0):
        print(num,"is divisible by 3")
    elif (num%5==0):
        print(num,"is divisible by 5")
    else:
        print(num,"is not divisible by 3,5")
    num-=1

   

    