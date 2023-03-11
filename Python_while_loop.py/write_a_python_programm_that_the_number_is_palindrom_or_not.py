num=int(input("Enter a number: "))
rev=0
temp=num
while (num>0):
    rev=(rev*10)+num%10
    num=num//10
if (rev==num):
    print("Its a Palindrom number.")
else:
    print("Not a Palindrom.")
