a=int(input("Enter a number: "))
rev=0
while (a>0):
    reminder = a%10
    rev = (rev*10) + reminder
    a=a//10
    print("Reverse=",rev)